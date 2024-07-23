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

    int display() {
        Node* q = this;

        if (q == nullptr) {
            cout << "Queue IS EMPTY!!" << endl;
        } else {
            cout << "Queue Values:" << endl;
            while (q != nullptr) {
                cout << "Value is: " << q->data << endl;
                q = q->next;
            }
        }
        return 0;
    }

    Node* queueInsertion() {
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


    Node* queueDeletion() {
        Node* head = this;
        Node* p = nullptr;

         if(head == nullptr) {
            cout << "Queue IS EMPTY!!" << endl;
        } else {
            p = head;
            head = p->next;
            cout << p->data << ": is deleted" << endl;

            free(p);
        }

        return head;
    }
};

int main() {
    Node* head = nullptr; 
    int choice;

    do {
        cout << endl;
        cout << "1.Insert" << endl;
        cout << "2.Delete" << endl;
        cout << "3.Display" << endl;
        cout << "4.Exit" << endl;

        cout << endl << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: head = head->queueInsertion(); break;
            case 2: head = head->queueDeletion(); break;
            case 3: head->display(); break;
            case 4: exit(0); break;

            default: cout << endl<< "ENTER VALID CHOICE" << endl; break;
        }
    } while(choice != 4);
    

    delete head;
    
    return 0;
}
