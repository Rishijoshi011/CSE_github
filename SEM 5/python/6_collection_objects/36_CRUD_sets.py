def creation():
    sets_ = set()
    size = int(input("Enter Size: "))
    print("Enter Elements: ")
    for i in range(size):
        x = int(input())
        sets_.add(x)
        
    return sets_

def update(sets_):
    element = int(input("Enter the element to update: "))
    
    if element in sets_:
        sets_.remove(element)
        new_value = int(input("Enter new value: "))
        sets_.add(new_value)
        
        print(f"Updated set: {sets_}")
        
    else:
        print("Element not found in set")

def append_ele(sets_):
    element = int(input("Enter element to append: "))
    sets_.add(element)
    
    print(f"set after appending: {sets_}")

def deletion(sets_, element):
    if element in sets_:
        sets_.remove(element)
        print(f"Element {element} deleted")
        
    else:
        print(f"Element {element} not found in set")
        
    return sets_

def delete_all(sets_):
    return {}

def sort_set(sets_):
    sorted_set = sorted(sets_)
    print(f"Sorted set: {sorted_set}")

def menu():
    print("\n1. Create")
    print("2. Update Element")
    print("3. Delete Whole set")
    print("4. Delete Element")
    print("5. Append Element to set")
    print("6. Sort set")
    print("7. Length")
    print("8. Exit")

sets_ = {}

while True:
    menu()
    choice = int(input("\nEnter Choice: "))
    
    if choice == 1:
        sets_ = creation()
        print(sets_)

    elif choice == 2:
        if sets_:
            update(sets_)
        else:
            print("set is empty. Create a set first.")

    elif choice == 3:
        sets_ = delete_all(sets_)
        print("set has been deleted")

    elif choice == 4:
        if sets_:
            element = int(input("Enter element to delete: "))
            sets_ = deletion(sets_, element)
            
            print(sets_)
        else:
            print("set is empty. Create a set first.")

    elif choice == 5:
        if sets_:
            append_ele(sets_)
        else:
            print("set is empty. Create a set first.")

    elif choice == 6:
        if sets_:
            sort_set(sets_)
        else:
            print("set is empty. Create a set first.")

    elif choice == 7:
        if sets_:
            print(f"Length of the set: {len(sets_)}")
        else:
            print("set is empty. Create a set first.")

    elif choice == 8:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
