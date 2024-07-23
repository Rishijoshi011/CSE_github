#include <iostream>

using namespace std; 

class Node {

private:
    int data;
    Node* next;
    Node* previous;

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
        Node *head = nullptr, *p = nullptr, *q = nullptr;
        int size;

        cout << "Enter the number of nodes you want to create: ";
        cin >> size;

        head = new Node();
        p = head;
        q = head;
        p->next = nullptr;
        p->previous = nullptr;

        cout << "Enter value: " << endl;
        cin >> head->data;
        p->data = head->data;

        for (int i = 1; i < size; i++) {
            p->next = new Node();
            q = p->next;
            q->previous = p;
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

    int reverseDisplay() {
        Node* head = this;
        Node* p = head;

        if (head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            for (p = head; p->next; p = p->next) {}
            cout << "Linked List Values:" << endl;
            while (p->previous != nullptr) {
                cout << "Value is: " << p->data << endl;
                p = p->previous;
            }
            cout << "Value is: " << p->data << endl;
        }
        
        return 0;
    }

    Node* insertAtFirst() {
        Node* head = this;
        Node* p = new Node();

        cout << "Enter value: " << endl;
        cin >> p->data;
        p->next = nullptr;
        p->previous = nullptr;

        if(head == nullptr) { 
            head = p; 
        } else {
            p->next = head;
            head->previous = p;
            head = p;   
        }

        return head;
   }
    
    Node* insertAtLast() {
        Node* head = this;
        Node* p = new Node();
        Node* q = nullptr;

        cout << "Enter value: " << endl;
        cin >> p->data;
        p->next = nullptr;
        p->previous = nullptr;

        if (head == nullptr) {
            head = p;
        } else {
            for (q = head; q->next != nullptr; q = q->next) {}
            q->next = p;
            p->previous = q;
        }
        
        return head;
    }

    Node* insertAtSpecifiedLocation() {
        Node* head = this;
        Node* p = new Node();
        Node* q = nullptr;
        int location, i = 1;

        cout << "Enter value: " << endl;
        cin >> p->data;
        p->next = nullptr;
        p->previous = nullptr;

        if(head == nullptr) {
            cout << "Inserting at first place beacuse linked list is empty" << endl;
            head = p;
        } else {
            cout << "Enter location: " << endl;
            cin >> location;

            if(location <= 0) { cout << "ENTER POSITIVE LOCATION!!" << endl; return head;} 

            if(location == 1) {
                p->next = head;
                head->previous = p;
                head = p;
            } else {
                for (q = head; (q->next != nullptr) && (i < location - 1); q = q->next, i++) {}
                p->next = q->next;
                q->next = p;
                p->previous = q;
            }
            return head;
        }


        return head;
    }

    Node* deleteAtFirst() {
        Node* head = this;
        Node*p = nullptr;

        if (head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            p = head;
            head = p->next;
            cout << p->data << ": is deleted" << endl;

            free(p);
        }

        return head;
    }

    Node* deleteAtLast() {
        Node* head = this;
        Node* p = nullptr;
        Node* q = nullptr;

        if (head == nullptr) {
            cout << "LINKED LIST IS EMPTY!!" << endl;
        } else {
            if(head->next == nullptr){
                p = head;
                head = nullptr;
                cout << p->data << ": is deleted" << endl;

                free(p);
            } else {
                for (q = head; q->next->next != nullptr; q = q->next) {}
                p = q->next;
                q->next = nullptr;
                cout << p->data << ": is deleted" << endl;

                free(p);
            }
        }
        
        return head;
    }

    Node *deleteAtSpecifiedLocation() {
        Node *head = this;
        Node *p = nullptr;
        Node *q = nullptr;
        int location, i = 1;

        if (head == nullptr) {
            cout << "LINKEDLIST IS EMPTY!!" << endl;
        } else {
            cout << "Enter location: " << endl;
            cin >> location;

            if(location <= 0) { cout << "ENTER POSITIVE LOCATION!!" << endl; return head;} 

            if (head->next == nullptr || location == 1) {
                p = head;
                head = nullptr;
                cout << p->data << ": is deleted" << endl;
                free(p);

            } else {
                for (q = head; (q->next != nullptr) && (i < location - 1); q = q->next, i++) {}
                if ((q->next == nullptr) && (i < location)) {
                    cout << "INVALID LOCATION!!" << endl;
                } else {
                    p = q->next;
                    q->next = p->next;
                    p->next->previous = q;

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
        cout << "3.Reverse display" << endl;
        cout << "4.Exit" << endl;
        cout << "5.Insert at First" << endl;
        cout << "6.Insert at Last" << endl;
        cout << "7.Insert at Specified Location" << endl;
        cout << "8.Delete at First" << endl;
        cout << "9.Delete at Last" << endl;
        cout << "10.Delete at Specified loaction" << endl;

        cout << endl << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: head = Node::createLinkedList(); break;
            case 2: head->display(); break;
            case 3: head->reverseDisplay(); break;
            case 4: exit(0); break;
            case 5: head = head->insertAtFirst(); break;
            case 6: head = head->insertAtLast(); break;
            case 7: head = head->insertAtSpecifiedLocation(); break;
            case 8: head = head->deleteAtFirst(); break;
            case 9: head = head->deleteAtLast(); break;
            case 10: head = head->deleteAtSpecifiedLocation(); break;

            default: cout << endl<< "ENTER VALID CHOICE" << endl; break;
        }
    } while(choice != 4);
    

    delete head;
    
    return 0;
}
