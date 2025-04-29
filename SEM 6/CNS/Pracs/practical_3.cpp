#include <iostream>
#include <string>

using namespace std;

string encrypt_text(string plaintext, string key) {
    string normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string ciphertext = "";

    for (int i = 0; i < plaintext.length(); i++) {
        char ch = plaintext[i];

        if (ch >= 'A' && ch <= 'Z') {
            int index = ch - 'A';
            ciphertext += key[index];
        }
        else if (ch >= 'a' && ch <= 'z') {
            int index = ch - 'a';
            ciphertext += tolower(key[index]);
        }
        else {
            ciphertext += ch; 
        }
    }
    return ciphertext;
}

string decrypt_cipher(string ciphertext, string key) {
    string normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string plaintext = "";

    for (int i = 0; i < ciphertext.length(); i++) {
        char ch = ciphertext[i];

        
        if (ch >= 'A' && ch <= 'Z') {
            int index = key.find(ch); 
            plaintext += normal[index];
        }
        
        else if (ch >= 'a' && ch <= 'z') {
            int index = key.find(toupper(ch)); 
            plaintext += tolower(normal[index]);
        }
        else {
            plaintext += ch; 
        }
    }
    return plaintext;
}

int main() {
    string key = "QWERTYUIOPLKJHGFDSAZXCVBNM"; 

    string message;
    cout << "Enter the message: ";
    getline(cin, message);

    // Encrypt and Decrypt
    string encryptedText = encrypt_text(message, key);
    string decryptedText = decrypt_cipher(encryptedText, key);

    // Display results
    cout << "Encrypted Text: " << encryptedText << endl;
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
