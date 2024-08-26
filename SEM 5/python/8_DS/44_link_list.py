from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional['Node'] = None 

class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None  

    def insert(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data: int):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            print(f"{data} deleted from the Linked List")
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(f"{data} not found in the Linked List")
        else:
            current.next = current.next.next
            print(f"{data} deleted from the Linked List")

if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter element to insert: "))
            linked_list.insert(data)
        elif choice == 2:
            linked_list.display()
        elif choice == 3:
            data = int(input("Enter element to delete: "))
            linked_list.delete(data)
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")


# ** caution: chatgpt genererated code