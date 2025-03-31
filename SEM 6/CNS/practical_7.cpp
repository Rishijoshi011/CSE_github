#include <iostream>
#include <cstring>

using namespace std;

string railFenceEncrypt(string text, int key) {
    char rail[key][text.length()];
    memset(rail, ' ', sizeof(rail));

    int row = 0, direction = 1;
    for (int i = 0; i < text.length(); i++) {
        rail[row][i] = text[i];
        row += direction;
        if (row == key - 1 || row == 0) direction *= -1;
    }

    string encryptedText = "";
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < text.length(); j++) {
            if (rail[i][j] != ' ') encryptedText += rail[i][j];
        }
    }
    return encryptedText;
}

string railFenceDecrypt(string cipher, int key) {
    char rail[key][cipher.length()];
    memset(rail, ' ', sizeof(rail));

    int row = 0, direction = 1;
    for (int i = 0; i < cipher.length(); i++) {
        rail[row][i] = '*';
        row += direction;
        if (row == key - 1 || row == 0) direction *= -1;
    }

    int index = 0;
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < cipher.length(); j++) {
            if (rail[i][j] == '*' && index < cipher.length()) {
                rail[i][j] = cipher[index++];
            }
        }
    }

    string decryptedText = "";
    row = 0, direction = 1;
    for (int i = 0; i < cipher.length(); i++) {
        decryptedText += rail[row][i];
        row += direction;
        if (row == key - 1 || row == 0) direction *= -1;
    }
    return decryptedText;
}

void sortKey(string key, int keyOrder[]) {
    int len = key.length();
    char tempKey[len];
    for (int i = 0; i < len; i++) tempKey[i] = key[i];

    for (int i = 0; i < len; i++) {
        int minIdx = i;
        for (int j = i + 1; j < len; j++) {
            if (tempKey[j] < tempKey[minIdx]) {
                minIdx = j;
            }
        }
        swap(tempKey[i], tempKey[minIdx]);
        swap(keyOrder[i], keyOrder[minIdx]);
    }
}

string columnarEncrypt(string text, string key) {
    int keyLen = key.length();
    int textLen = text.length();
    int numRows = (textLen + keyLen - 1) / keyLen;
    char grid[numRows][keyLen];

    int index = 0;
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < keyLen; j++) {
            grid[i][j] = (index < textLen) ? text[index++] : 'X';
        }
    }

    int keyOrder[keyLen];
    for (int i = 0; i < keyLen; i++) keyOrder[i] = i;
    sortKey(key, keyOrder);

    string encryptedText = "";
    for (int i = 0; i < keyLen; i++) {
        int col = keyOrder[i];
        for (int j = 0; j < numRows; j++) {
            encryptedText += grid[j][col];
        }
    }
    return encryptedText;
}

string columnarDecrypt(string cipher, string key) {
    int keyLen = key.length();
    int cipherLen = cipher.length();
    int numRows = (cipherLen + keyLen - 1) / keyLen;
    char grid[numRows][keyLen];

    int keyOrder[keyLen];
    for (int i = 0; i < keyLen; i++) keyOrder[i] = i;
    sortKey(key, keyOrder);

    int index = 0;
    for (int i = 0; i < keyLen; i++) {
        int col = keyOrder[i];
        for (int j = 0; j < numRows; j++) {
            grid[j][col] = cipher[index++];
        }
    }

    string decryptedText = "";
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < keyLen; j++) {
            decryptedText += grid[i][j];
        }
    }
    return decryptedText;
}

int main() {
    string text, key;
    int railKey;

    cout << "Enter text to encrypt: ";
    cin >> text;

    cout << "Enter Rail-Fence key: ";
    cin >> railKey;

    string railCipher = railFenceEncrypt(text, railKey);
    cout << "Rail-Fence Encrypted Text: " << railCipher << endl;

    string railDecrypted = railFenceDecrypt(railCipher, railKey);
    cout << "Rail-Fence Decrypted Text: " << railDecrypted << endl;

    cout << "Enter Columnar Transposition key (word): ";
    cin >> key;

    string columnCipher = columnarEncrypt(text, key);
    cout << "Columnar Encrypted Text: " << columnCipher << endl;

    string columnDecrypted = columnarDecrypt(columnCipher, key);
    cout << "Columnar Decrypted Text: " << columnDecrypted << endl;

    return 0;
}
