import os
import re

try:
    currunt_dir = os.path.dirname(__file__)
    file_path = os.path.join(currunt_dir, "Text_files", "25_data.txt")

    with open(file_path, "r") as file_obj:
        data = file_obj.read()
        numbers = re.findall(r'\d+\.?\d*', data)
        print(f"These are the numbers: {numbers}")
        
    file_obj.close()
    
except FileNotFoundError:
    print("File not Found")