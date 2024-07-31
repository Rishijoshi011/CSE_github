import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "26_source.txt")
    
    with open(file_path, "r") as file_obj:
        data = file_obj.read()
        
    file_obj.close()
    
    
except FileNotFoundError:
    print("File not Found")

try:
    file_path = os.path.join(currunt_dir, "Text_files", "26_destination.txt")
    
    with open(file_path, "a") as file_obj:
        file_obj.write(data)
        file_obj.write("\n")
        
    file_obj.close()
    
except FileNotFoundError:
    print("File not Found")
    