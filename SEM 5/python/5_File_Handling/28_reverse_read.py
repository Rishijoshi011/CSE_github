import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "28_source.txt")
    
    with open(file_path, "r+") as file_obj:
        file_obj.seek(0, 2)
        position = file_obj.tell()
        
        line = ""
        while position >= 0:
            file_obj.seek(position)
            char = file_obj.read(1)
            
            if char == "\n":
                print(line[::-1])
                line = ""
            else:
                line += char
            position -= 1
            
    if line:
        print(line[::-1])
        
    file_obj.close()
     
except FileNotFoundError:
    print("File not Found")