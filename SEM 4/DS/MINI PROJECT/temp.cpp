#include <iostream>
#include <string>

using namespace std;

// Define the structure of a todo item
struct TodoItem {
    string task;
    TodoItem* next;
};

// Define the TodoList class
class TodoList {
private:
    TodoItem* head;

public:
    TodoList() {
        head = nullptr;
    }

    // Function to add a new task to the todo list
    void addTask(string task) {
        TodoItem* newItem = new TodoItem;
        newItem->task = task;
        newItem->next = head;
        head = newItem;
        cout << "Task '" << task << "' added to the todo list." << endl;
    }

    // Function to display all tasks in the todo list
    void displayTasks() {
        if (head == nullptr) {
            cout << "No tasks in the todo list." << endl;
            return;
        }
        TodoItem* current = head;
        int taskNumber = 1;
        cout << "Todo List:" << endl;
        while (current != nullptr) {
            cout << taskNumber << ". " << current->task << endl;
            current = current->next;
            taskNumber++;
        }
    }

    // Function to remove a task from the todo list by its number
    void removeTask(int taskNumber) {
        TodoItem* current = head;
        TodoItem* prev = nullptr;
        int currentNumber = 1;
        while (current != nullptr && currentNumber != taskNumber) {
            prev = current;
            current = current->next;
            currentNumber++;
        }
        if (current != nullptr) {
            if (prev != nullptr) {
                prev->next = current->next;
            } else {
                head = current->next;
            }
            cout << "Task '" << current->task << "' removed from the todo list." << endl;
            delete current;
        } else {
            cout << "Task number " << taskNumber << " not found in the todo list." << endl;
        }
    }

    // Function to mark a task as complete by its number
    void markTaskAsComplete(int taskNumber) {
        TodoItem* current = head;
        int currentNumber = 1;
        while (current != nullptr && currentNumber != taskNumber) {
            current = current->next;
            currentNumber++;
        }
        if (current != nullptr) {
            current->task += " [Completed]";
            cout << "Task '" << current->task << "' marked as complete." << endl;
        } else {
            cout << "Task number " << taskNumber << " not found in the todo list." << endl;
        }
    }

    // Function to check if the todo list is empty
    bool isEmpty() {
        return head == nullptr;
    }

    // Function to clear all tasks from the todo list
    void clearTasks() {
        TodoItem* current = head;
        while (current != nullptr) {
            TodoItem* temp = current;
            current = current->next;
            delete temp;
        }
        head = nullptr;
        cout << "All tasks cleared from the todo list." << endl;
    }

    // Destructor to free memory
    ~TodoList() {
        clearTasks();
    }
};

int main() {
    TodoList todoList;
    int choice;
    string task;
    int taskNumber;

    do {
        cout << "\nTodo List Menu:" << endl;
        cout << "1. Add Task" << endl;
        cout << "2. Display Tasks" << endl;
        cout << "3. Remove Task" << endl;
        cout << "4. Mark Task as Complete" << endl;
        cout << "5. Clear All Tasks" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore(); // clear input buffer

        switch (choice) {
            case 1:
                cout << "Enter task to add: ";
                getline(cin, task);
                todoList.addTask(task);
                break;
            case 2:
                todoList.displayTasks();
                break;
            case 3:
                if (todoList.isEmpty()) {
                    cout << "No tasks to remove." << endl;
                    break;
                }
                cout << "Enter task number to remove: ";
                cin >> taskNumber;
                todoList.removeTask(taskNumber);
                break;
            case 4:
                if (todoList.isEmpty()) {
                    cout << "No tasks to mark as complete." << endl;
                    break;
                }
                cout << "Enter task number to mark as complete: ";
                cin >> taskNumber;
                todoList.markTaskAsComplete(taskNumber);
                break;
            case 5:
                if (todoList.isEmpty()) {
                    cout << "No tasks to clear." << endl;
                    break;
                }
                todoList.clearTasks();
                break;
            case 6:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 6);

    return 0;
}