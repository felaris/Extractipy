import os
import re
import json

folder_path = ""  # Replace with the  folder path
extensions = [".py", ".jsx", ".html", ".js", ".css", ".php", ".java", ".cpp", ".txt", ".csv", ".xml", ".json", ".md", ".rb"]
excluded_chars = [",", ".","/","_",""]

word_dict = {}

# Traverse through the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(tuple(extensions)):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                words = re.findall(r"\b(?<![A-Z])(?<![a-z])(?![A-Z])(?![a-z])(?!\d)\w+\b", content)
                
                
                # Add words to the dictionary
                for word in words:
                    if word not in excluded_chars:
                        if word not in word_dict:
                            word_dict[word] = word.capitalize()

# Write the output to a JSON file
output_file = "output.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(word_dict, f, indent=4)

print(f"Output written to {output_file}")
