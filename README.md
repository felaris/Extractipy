# Extractipy


This code is designed to traverse through a specified folder and its subfolders, 
search for files with certain extensions, and extract words from those files. 
The extracted words are then processed to create a dictionary of unique words with their capitalized forms. 
Finally, the dictionary is written to a JSON file.

## Prerequisites

This code requires the following:

- Python (version 3 or above) installed on your system.
- The `os`, `re`, and `json` modules, which are part of the Python standard library.

## Usage

1. Set the value of the `folder_path` variable to the path of the folder you want to traverse. This folder should contain the files you want to analyze.
2. Optionally, modify the `extensions` list to include or exclude file extensions according to your requirements.
3. Optionally, modify the `excluded_chars` list to include any characters that should be excluded from the word dictionary.
4. Run the code.

## How it works

1. The code starts by initializing an empty dictionary called `word_dict` to store the words and their capitalized forms.
2. It uses the `os.walk()` function to traverse through the specified folder and its subfolders.
3. For each file encountered, the code checks if it has one of the allowed extensions. If it does, the file is opened and its content is read.
4. The `re.findall()` function is then used to extract words from the file's content. The regular expression pattern `\b(?<![A-Z])(?<![a-z])(?![A-Z])(?![a-z])(?!\d)\w+\b` is used to match words. This pattern ensures that the words are not preceded or followed by any letters (uppercase or lowercase) or digits, and they are not part of any larger word. This helps in extracting individual words without including other elements like function names, variable names, or numbers.
5. Each extracted word is checked against the `excluded_chars` list. If it is not present in the list, it is added to the `word_dict` dictionary with its capitalized form as the value. If the word is already present in the dictionary, it is skipped to avoid duplicates.
6. After processing all the files, the `word_dict` dictionary is written to a JSON file named `output.json`. The `json.dump()` function is used to convert the dictionary into a JSON string and write it to the file.
7. The code prints a message indicating the location where the output file has been written.

## Output

The output of the code is a JSON file named `output.json`. The file contains a dictionary where each key represents a unique word extracted from the specified files, and the corresponding value is its capitalized form.

## Notes

- Ensure that the specified `folder_path` exists and contains the files you want to analyze.
- Make sure the necessary permissions are granted to read the files and write the output file in the specified location.
- The code assumes that the files in the specified folder are encoded using UTF-8. If your files are encoded differently, you may need to modify the encoding in the `open()` function calls.
- The code does not perform any error handling or validation, so it is recommended to provide valid inputs and handle exceptions as per your requirements.


