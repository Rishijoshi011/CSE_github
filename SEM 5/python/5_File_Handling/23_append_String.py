import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "23_append.txt")

    with open(file_path, "a") as file_obj:
        text = input("Enter String: ")
        file_obj.write(text)
        file_obj.write("\n")
    
    file_obj.close()
    
except FileNotFoundError:
    print("File not found")