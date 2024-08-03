def creation():
    dict_ = {}
    size = int(input("Enter Size: "))
    print("Enter Elements (key and value): ")
    for i in range(size):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value {i+1}: ")
        dict_[key] = value
        
    return dict_

def update(dict_):
    key = input("Enter the key to update: ")
    
    if key in dict_:
        new_value = input("Enter new value: ")
        dict_[key] = new_value
        
        print(f"Updated dictionary: {dict_}")
        
    else:
        print("Key not found in dictionary")

def append_ele(dict_):
    key = input("Enter key to append: ")
    value = input("Enter value to append: ")
    dict_[key] = value
    
    print(f"Dictionary after appending: {dict_}")

def deletion(dict_, key):
    if key in dict_:
        del dict_[key]
        print(f"Key {key} deleted")
        
    else:
        print(f"Key {key} not found in dictionary")
        
    return dict_

def delete_all(dict_):
    return {}

def sort_dictionary(dict_):
    sorted_dict = dict(sorted(dict_.items()))
    print(f"Sorted dictionary: {sorted_dict}")

def menu():
    print("\n1. Create")
    print("2. Update Element")
    print("3. Delete Whole dictionary")
    print("4. Delete Element")
    print("5. Append Element to dictionary")
    print("6. Sort dictionary")
    print("7. Length")
    print("8. Exit")

dict_ = {}

while True:
    menu()
    choice = int(input("\nEnter Choice: "))
    
    if choice == 1:
        dict_ = creation()
        print(dict_)

    elif choice == 2:
        if dict_:
            update(dict_)
        else:
            print("Dictionary is empty. Create a dictionary first.")

    elif choice == 3:
        dict_ = delete_all(dict_)
        print("Dictionary has been deleted")

    elif choice == 4:
        if dict_:
            key = input("Enter key to delete: ")
            dict_ = deletion(dict_, key)
            
            print(dict_)
        else:
            print("Dictionary is empty. Create a dictionary first.")

    elif choice == 5:
        if dict_:
            append_ele(dict_)
        else:
            print("Dictionary is empty. Create a dictionary first.")

    elif choice == 6:
        if dict_:
            sort_dictionary(dict_)
        else:
            print("Dictionary is empty. Create a dictionary first.")

    elif choice == 7:
        if dict_:
            print(f"Length of the dictionary: {len(dict_)}")
        else:
            print("Dictionary is empty. Create a dictionary first.")

    elif choice == 8:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
