#include <iostream>
#include <cstring>

using namespace std;

const int SIZE = 3;

void multiplyMatrix(int key[SIZE][SIZE], int text[SIZE], int result[SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        result[i] = 0;
        for (int j = 0; j < SIZE; j++) {
            result[i] += key[i][j] * text[j];
        }
        result[i] = (result[i] % 26 + 26) % 26;
    }
}

int modInverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) {
            return x;
        }
    }
    return -1;
}

void findInverseMatrix(int key[SIZE][SIZE], int inverseKey[SIZE][SIZE]) {
    int determinant = key[0][0] * (key[1][1] * key[2][2] - key[1][2] * key[2][1]) - 
                      key[0][1] * (key[1][0] * key[2][2] - key[1][2] * key[2][0]) + 
                      key[0][2] * (key[1][0] * key[2][1] - key[1][1] * key[2][0]);

    determinant = (determinant % 26 + 26) % 26;
    int determinantInverse = modInverse(determinant, 26);

    if (determinantInverse == -1) {
        cout << "Key matrix is not invertible.\n";
        return;
    }

    int adjoint[SIZE][SIZE] = {
        {(key[1][1] * key[2][2] - key[1][2] * key[2][1]), -(key[0][1] * key[2][2] - key[0][2] * key[2][1]), (key[0][1] * key[1][2] - key[0][2] * key[1][1])},
        {-(key[1][0] * key[2][2] - key[1][2] * key[2][0]), (key[0][0] * key[2][2] - key[0][2] * key[2][0]), -(key[0][0] * key[1][2] - key[0][2] * key[1][0])},
        {(key[1][0] * key[2][1] - key[1][1] * key[2][0]), -(key[0][0] * key[2][1] - key[0][1] * key[2][0]), (key[0][0] * key[1][1] - key[0][1] * key[1][0])}
    };

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            inverseKey[i][j] = (adjoint[i][j] * determinantInverse) % 26;
            if (inverseKey[i][j] < 0) {
                inverseKey[i][j] += 26;
            }
        }
    }
}

void encrypt_text(char plaintext[], char ciphertext[]) {
    int key[SIZE][SIZE] = {{6, 24, 1}, {13, 16, 10}, {20, 17, 15}};
    int textBlock[SIZE], encryptedBlock[SIZE];

    int len = strlen(plaintext);
    while (len % SIZE != 0) {
        plaintext[len] = 'X';
        len++;
        plaintext[len] = '\0';
    }

    cout << "Encrypted Text: ";
    for (int i = 0; i < len; i += SIZE) {
        for (int j = 0; j < SIZE; j++) {
            textBlock[j] = plaintext[i + j] - 'A';
        }

        multiplyMatrix(key, textBlock, encryptedBlock);

        for (int j = 0; j < SIZE; j++) {
            ciphertext[i + j] = (char)(encryptedBlock[j] + 'A');
            cout << ciphertext[i + j];
        }
    }
    ciphertext[len] = '\0'; // Null terminate the ciphertext
    cout << endl;
}

void decrypt_cipher(char ciphertext[]) {
    int key[SIZE][SIZE] = {{6, 24, 1}, {13, 16, 10}, {20, 17, 15}};
    int inverseKey[SIZE][SIZE];
    findInverseMatrix(key, inverseKey);

    int textBlock[SIZE], decryptedBlock[SIZE];
    int len = strlen(ciphertext);

    cout << "Decrypted Text: ";
    for (int i = 0; i < len; i += SIZE) {
        for (int j = 0; j < SIZE; j++) {
            textBlock[j] = ciphertext[i + j] - 'A';
        }

        multiplyMatrix(inverseKey, textBlock, decryptedBlock);

        for (int j = 0; j < SIZE; j++) {
            cout << (char)(decryptedBlock[j] + 'A');
        }
    }
    cout << endl;
}

int main() {
    char plaintext[100], ciphertext[100];

    cout << "Enter plaintext (uppercase letters only): ";
    cin >> plaintext;

    // Encrypt and store the ciphertext
    encrypt_text(plaintext, ciphertext);

    // Auto decrypt the ciphertext
    decrypt_cipher(ciphertext);

    return 0;
}
