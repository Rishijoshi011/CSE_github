import os

def occurrences(data_file, char_to_find):
    return data_file.count(char_to_find)

try:
    current_dir = os.path.dirname(__file__)    
    file_path = os.path.join(current_dir, "Text_files", "22_Data.txt")

    with open(file_path, "r") as file_obj:
        data = file_obj.read()  # * data will contains all data
        words = len(data.split()) 
        lines = len(data.splitlines())
        
        print(f"Word Count: {words}")
        print(f"Lines Count: {lines}")
        print(f"Word Occured: {occurrences(data, "dolor")}")
        print(f"Char Occured: {occurrences(data, "e")}")
        print(f"Blank Spaces: {occurrences(data, " ")}")

except FileNotFoundError:
    print("File is not found")
