#include <iostream>
#include <string>

using namespace std;

const int SIZE = 5;

void generateKeyMatrix(const string& key, char keyMatrix[SIZE][SIZE]) {
    bool used[26] = {false};
    string refinedKey = "";

    for (char ch : key) {
        if (ch >= 'a' && ch <= 'z') ch -= 32;
        if (ch == 'J') ch = 'I';
        if (ch >= 'A' && ch <= 'Z' && !used[ch - 'A']) {
            refinedKey += ch;
            used[ch - 'A'] = true;
        }
    }

    for (char ch = 'A'; ch <= 'Z'; ++ch) {
        if (ch == 'J') continue;
        if (!used[ch - 'A']) {
            refinedKey += ch;
            used[ch - 'A'] = true;
        }
    }

    int index = 0;
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            keyMatrix[i][j] = refinedKey[index++];
        }
    }
}

void findPosition(char keyMatrix[SIZE][SIZE], char ch, int &row, int &col) {
    if (ch == 'J') ch = 'I';
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            if (keyMatrix[i][j] == ch) {
                row = i;
                col = j;
                return;
            }
        }
    }
}

string prepareText(const string& text) {
    string result = "";
    for (char ch : text) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            if (ch >= 'a' && ch <= 'z') ch -= 32;
            result += ch;
        }
    }

    string processed = "";
    for (size_t i = 0; i < result.length(); ++i) {
        processed += result[i];
        if (i + 1 < result.length() && result[i] == result[i + 1]) {
            processed += 'X';
        }
    }

    if (processed.length() % 2 != 0) {
        processed += 'X';
    }

    return processed;
}

string encrypt(const string& text, char keyMatrix[SIZE][SIZE]) {
    string preparedText = prepareText(text);
    string encryptedText = "";

    for (size_t i = 0; i < preparedText.length(); i += 2) {
        char first = preparedText[i];
        char second = preparedText[i + 1];
        int row1, col1, row2, col2;
        findPosition(keyMatrix, first, row1, col1);
        findPosition(keyMatrix, second, row2, col2);

        if (row1 == row2) {
            encryptedText += keyMatrix[row1][(col1 + 1) % SIZE];
            encryptedText += keyMatrix[row2][(col2 + 1) % SIZE];
        } else if (col1 == col2) {
            encryptedText += keyMatrix[(row1 + 1) % SIZE][col1];
            encryptedText += keyMatrix[(row2 + 1) % SIZE][col2];
        } else {
            encryptedText += keyMatrix[row1][col2];
            encryptedText += keyMatrix[row2][col1];
        }
    }
    return encryptedText;
}

string decrypt(const string& text, char keyMatrix[SIZE][SIZE]) {
    string decryptedText = "";

    for (size_t i = 0; i < text.length(); i += 2) {
        char first = text[i];
        char second = text[i + 1];
        int row1, col1, row2, col2;
        findPosition(keyMatrix, first, row1, col1);
        findPosition(keyMatrix, second, row2, col2);

        if (row1 == row2) {
            decryptedText += keyMatrix[row1][(col1 - 1 + SIZE) % SIZE];
            decryptedText += keyMatrix[row2][(col2 - 1 + SIZE) % SIZE];
        } else if (col1 == col2) {
            decryptedText += keyMatrix[(row1 - 1 + SIZE) % SIZE][col1];
            decryptedText += keyMatrix[(row2 - 1 + SIZE) % SIZE][col2];
        } else {
            decryptedText += keyMatrix[row1][col2];
            decryptedText += keyMatrix[row2][col1];
        }
    }
    return decryptedText;
}

int main() {
    string key, text;
    char keyMatrix[SIZE][SIZE];

    cout << "Enter key: ";
    cin >> key;
    generateKeyMatrix(key, keyMatrix);

    cout << "Enter text to encrypt: ";
    cin >> text;

    string encryptedText = encrypt(text, keyMatrix);
    cout << "Encrypted Text: " << encryptedText << endl;

    string decryptedText = decrypt(encryptedText, keyMatrix);
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
