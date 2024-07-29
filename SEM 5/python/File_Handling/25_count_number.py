from curses.ascii import isdigit
import os

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "25_data.txt")

    with open(file_path, "r") as file_obj:
        data = file_obj.read()
        # split_data = data.split()
        
        number_count = isdigit(data)
        print(number_count)
        
    file_obj.close()
    
except FileNotFoundError:
    print("File not Found")