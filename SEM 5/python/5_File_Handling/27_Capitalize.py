import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "27_capitalize.txt")
    
    with open(file_path, "r+") as file_obj:
        data = file_obj.read()
        
        file_obj.seek(0) # * placing cursor to start of file to delete all data 
        file_obj.truncate() 
        
        data = data.title() # * it will capitalize all first letter of word
        file_obj.write(data)

    file_obj.close()
    
except FileNotFoundError:
    print("File not Found")
    