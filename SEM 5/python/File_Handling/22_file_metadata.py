try:
    file_path = "Text_files/22_Data.txt"  # Relative path to the file
    file_obj = open(file_path, "r")
    text = file_obj.read()
    print(text)
    
except FileNotFoundError:
    print("File is not found")
finally:
    # Ensure file is closed if it was successfully opened
    try:
        file_obj.close()
    except NameError:
        pass  # file_obj was not defined because the file could not be opened
