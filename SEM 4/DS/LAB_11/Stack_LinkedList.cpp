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
            cout << "STACK IS EMPTY!!" << endl;
        } else {
            cout << "STACK Values:" << endl;
            while (q != nullptr) {
                cout << "Value is: " << q->data << endl;
                q = q->next;
            }
        }
        return 0;
    }

    Node* PUSH() {
        Node* head = this;
        Node* p = new Node();

        cout << "Enter value: " << endl;
        cin >> p->data;
        
        p->next = head;
        head = p;
        
        return head;
    }

    

    Node* POP() {
        Node* head = this;
        Node* p = nullptr;

         if(head == nullptr) {
            cout << "STACK IS EMPTY!!" << endl;
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
        cout << "1.PUSH" << endl;
        cout << "2.POP" << endl;
        cout << "3.Display" << endl;
        cout << "4.Exit" << endl;

        cout << endl << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: head = head->PUSH(); break;
            case 2: head = head->POP(); break;
            case 3: head->display(); break;
            case 4: exit(0); break;

            default: cout << endl<< "ENTER VALID CHOICE" << endl; break;
        }
    } while(choice != 4);
    

    delete head;
    
    return 0;
}
