#include <iostream>
#include <string>

using namespace std;

int generateHash(string message) {
    int hash = 0;
    for (char ch : message) {
        hash += (int)ch;
    }
    return hash % 1009; 
}

int signHash(int hash, int privateKey) {
    return (hash * privateKey) % 1009; 
}

int main() {
    string message;
    int privateKey = 17; 

    cout << "Enter the message to sign: ";
    getline(cin, message);

    int hash = generateHash(message);
    int digitalSignature = signHash(hash, privateKey);

    cout << "\nOriginal Message: " << message << endl;
    cout << "Hash Value: " << hash << endl;
    cout << "Digital Signature (Simulated): " << digitalSignature << endl;

    return 0;
}
