#include <iostream>
#include <cstring>

using namespace std;

void generateKey(const char* text, const char* key, char* newKey) {
    int textLen = strlen(text), keyLen = strlen(key);
    for (int i = 0, j = 0; i < textLen; i++, j++) {
        if (j == keyLen) {
            j = 0;
        }
        newKey[i] = key[j];
    }
    newKey[textLen] = '\0';
}

void encrypt_text(const char* text, const char* key, char* encryptedText) {
    int len = strlen(text);
    for (int i = 0; i < len; i++) {
        encryptedText[i] = ((text[i] + key[i]) % 26) + 'A';
    }
    encryptedText[len] = '\0';
}

void decrypt_cipher(const char* encryptedText, const char* key, char* decryptedText) {
    int len = strlen(encryptedText);
    for (int i = 0; i < len; i++) {
        decryptedText[i] = (((encryptedText[i] - key[i]) + 26) % 26) + 'A';
    }
    decryptedText[len] = '\0';
}

int main() {
    char text[100], key[100], newKey[100], encryptedText[100], decryptedText[100];

    cout << "Enter text (uppercase letters only): ";
    cin >> text;
    
    cout << "Enter key (uppercase letters only): ";
    cin >> key;

    generateKey(text, key, newKey);
    encrypt_text(text, newKey, encryptedText);
    decrypt_cipher(encryptedText, newKey, decryptedText);

    cout << "Encrypted Text: " << encryptedText << endl;
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
