#include <iostream>
#include <string>

using namespace std;

string encryption(string str, int key) {
    string encrypted_str = "";
    for (int i = 0; i < str.length(); i++) {
        char c = str.at(i);
        if(c == ' ') {
        } else {
            if (isalpha(c)) {
                if (islower(c)) {
                    c = (c - 'a' + key) % 26 + 'a';
                } else if (isupper(c)) {
                    c = (c - 'A' + key) % 26 + 'A';
                }
            } else {
                int temp = (int) c;
                temp += key;
                c = (char) temp;
            }
        }
            encrypted_str += c;
    }
    return encrypted_str;
}

string description(string encrypted_str, int key) {
    string str = "";
    for (int i = 0; i < encrypted_str.length(); i++) {
        char c = encrypted_str.at(i);
        if(c == ' ') {

        } else {
            if (isalpha(c)) {
                if (islower(c)) {
                    c = (c - 'a' - key + 26) % 26 + 'a';
                } else if (isupper(c)) {
                    c = (c - 'A' - key + 26) % 26 + 'A';
                }
            } else {
                int temp = (int) c;
                temp -= key;
                c = (char) temp;
            }
        }
            str += c;
    }
    return str;
}

int main() {

    string str = "hello world";
    unsigned int key = 5;

    cout << "Enter any text" << endl;
    getline(cin, str);

    cout << "Enter key" << endl;
    cin >> key;

    string encrypted_str = encryption(str, key);
    string description_str = description(encrypted_str, key);

    cout << "text: " << str << endl;
    cout << "Encrypted text: " << encrypted_str << endl;
    cout << "descripted text: " << description_str << endl;

    return 0;
}
