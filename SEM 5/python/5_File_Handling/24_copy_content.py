import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "24_sourceFile.txt")
    
    with open(file_path, "r") as file_obj:
        data = file_obj.read()

    file_obj.close() 
except FileNotFoundError:
    print("File not Found")
    
try:
    file_path = os.path.join(currunt_dir, "Text_files", "24_destinationFile.txt")
    
    with open(file_path, "w") as file_obj:
        file_obj.write(data)
    
    file_obj.close()
except FileNotFoundError: 
    print("File not found")