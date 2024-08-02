def creation():
    list_ = []
    size = int(input("Enter Size: "))
    print("Enter Elements: ")
    for i in range(size):
        list_.append(int(input()))
        
    return list_

def update(list_):
    index = int(input("Enter index to update: "))
    
    if 0 <= index < len(list_):
        new_value = int(input("Enter new value: "))
        list_[index] = new_value
        
        print(f"Updated list: {list_}")
        
    else:
        print("Invalid index")

def append_ele(list_):
    element = int(input("Enter element to append: "))
    list_.append(element)
    
    print(f"List after appending: {list_}")

def deletion(list_, element):
    if element in list_:
        list_.remove(element)
        print(f"Element {element} deleted")
        
    else:
        print(f"Element {element} not found in list")
        
    return list_

def delete_all(list_):
    return []

def sort_list(list_):
    list_.sort()
    print(f"Sorted list: {list_}")    

def menu():
    print("\n1. Create")
    print("2. Update Element")
    print("3. Delete Whole List")
    print("4. Delete Element")
    print("5. Append Element to List")
    print("6. Sort List")
    print("7. Length")
    print("8. Exit")

list_ = []

while True:
    menu()
    choice = int(input("\nEnter Choice: "))
    
    if choice == 1:
        list_ = creation()
        print(list_)

    elif choice == 2:
        if list_:
            update(list_)
        else:
            print("List is empty. Create a list first.")

    elif choice == 3:
        list_ = delete_all(list_)
        print("List has been deleted")

    elif choice == 4:
        if list_:
            element = int(input("Enter element to delete: "))
            list_ = deletion(list_, element)
            
            print(list_)
        else:
            print("List is empty. Create a list first.")

    elif choice == 5:
        if list_:
            append_ele(list_)
        else:
            print("List is empty. Create a list first.")

    elif choice == 6:
        if list_:
            sort_list(list_)
        else:
            print("List is empty. Create a list first.")

    elif choice == 7:
        if list_:
            print(f"Length of the list: {len(list_)}")
        else:
            print("List is empty. Create a list first.")

    elif choice == 8:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
