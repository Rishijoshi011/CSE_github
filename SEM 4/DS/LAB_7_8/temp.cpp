#include <iostream>

using namespace std; 

class Node {

private:
    int data;
    Node* next;

public:

    ~Node() {
        Node* head = this;
        while (head != nullptr) {
            Node* next = head->next;
            delete head;
            head = next;
        }
    }

    static Node* createLinkedList() {
        Node *head = nullptr, *p = nullptr;
        int size;

        cout << "Enter the number of nodes you want to create: ";
        cin >> size;
 
        head = new Node();
        p = head;
        head->next = nullptr;

        cout << "Enter value: " << endl;
        cin >> p->data;

        for (int i = 1; i < size; i++) {
            p->next = new Node();
            p = p->next;

            cout << "Enter values: " << endl;
            cin >> p->data;
        }
        p->next = nullptr;

        return head;
    }


    int display() {
        Node* q = this;

        if (q == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            cout << "Linked List Values:" << endl;
            while (q != nullptr) {
                cout << "Value is: " << q->data << endl;
                q = q->next;
            }
        }
        return 0;
    }

    Node* insertAtFirst() {
        Node* head = this;
        Node* p = new Node();

        cout << "Enter value: " << endl;
        cin >> p->data;
        
        p->next = head;
        head = p;
        
        return head;
    }

    Node* insertAtLast() {
        Node* head = this;
        Node* p = new Node();
        Node* q = nullptr;
        int value;

        cout << "Enter value: " << endl;
        cin >> value;
        p->data = value;
        p->next = nullptr;

        if(head == nullptr) {
            head = p;
        } else {
            for (q = head; q->next != nullptr; q = q->next) {}
            q->next = p;
        }

        return head;
    }

   
    Node* insertSortedNodes() {
        Node* head = this;
        Node* p = new Node();
        Node* q = nullptr;
        int value;

        cout << "Enter element to insert: ";
        cin >> value;
        p->data = value;
        p->next = nullptr;

        if (head == nullptr) {
            cout << "Inserting at first place because there no node present in linked list" << endl;
            head = p;
        } else {
            if (p->data < head->data) { 
                p->next = head; 
                head = p;
            } else {
                for ( q = head; (q->next != nullptr) && (value > q->next->data); q = q->next){}
                p->next = q->next;
                q->next = p;
            }
        }

        return head;
    }

    Node* deleteAtFirst() {
        Node* head = this;
        Node* p = nullptr;

         if(head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            p = head;
            head = p->next;
            cout << p->data << ": is deleted" << endl;

            free(p);
        }

        return head;
    }

    Node* deleteAtSpecifiedlocation_after() {
        Node* head = this;
        Node* p = nullptr;
        Node* q = nullptr;
        int location, i = 1;

        if (head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            cout << "Enter location of Node to delete that Node" << endl;
            cin >> location;

            if(location <= 0) { cout << "ENTER POSITIVE LOCATION!!" << endl; return head; } 

            if(head->next == nullptr || location == 1) {
                p = head;
                head = p->next;
                cout << p->data << ": is deleted" << endl;
                
                free(p);
            } else {
                for (q = head; q->next->next != nullptr && i < location; q = q->next, i++) {}
                if ((q->next == nullptr) && (i < location)) {
                    cout << "INVALID LOCATION!!" << endl;
                } else {
                    p = q->next;
                    q->next = p->next;
                    cout << p->data << ": is deleted" << endl;

                    free(p);
                }
            } 
        }

        return head;
    }

    Node* deleteAtSpecifiedlocation_before() {
        Node* head = this;
        Node* p = nullptr;
        Node* q = nullptr;
        int location, i = 1;

        if (head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            cout << "Enter location of Node to delete that Node" << endl;
            cin >> location;

            if(location <= 0) { cout << "ENTER POSITIVE LOCATION!!" << endl; return head;} 

            if(head->next == nullptr || location == 1) {
                p = head;
                head = p->next;
                cout << p->data << ": is deleted" << endl;
                
                free(p);
            } else {
                for (q = head; q->next->next != nullptr && i < location - 2 ; q = q->next, i++) {}
                if ((q->next == nullptr) && (i < location)) {
                    cout << "INVALID LOCATION!!" << endl;
                } else {
                    p = q->next;
                    q->next = p->next;
                    cout << p->data << ": is deleted" << endl;

                    free(p);
                }
            } 
        }
        return head;
    }
};

int main() {
    Node* head = nullptr; 
    int choice;

    do {
        cout << endl;
        cout << "1.Create" << endl;
        cout << "2.Display" << endl;
        cout << "3.Exit" << endl;
        cout << "4.Insert at First" << endl;
        cout << "5.Insert at Last" << endl;
        cout << "6.Insert value by number at sorted postion" << endl;
        cout << "7.Delete at First" << endl;
        cout << "8.Delete after Specified loaction" << endl;
        cout << "9.Delete before Specified loaction" << endl;

        cout << endl << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: head = Node::createLinkedList(); break;
            case 2: head->display(); break;
            case 3: exit(0); break;
            case 4: head = head->insertAtFirst(); break;
            case 5: head = head->insertAtLast(); break;
            case 6: head = head->insertSortedNodes(); break;
            case 7: head = head->deleteAtFirst(); break;
            case 8: head = head->deleteAtSpecifiedlocation_after(); break;
            case 9: head = head->deleteAtSpecifiedlocation_before(); break;

            default: cout << endl<< "ENTER VALID CHOICE" << endl; break;
        }
    } while(choice != 3);
    

    delete head;
    
    return 0;
}
