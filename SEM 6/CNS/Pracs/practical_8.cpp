#include <iostream>
#include <string>

using namespace std;

int P10[] = {3, 5, 2, 7, 4, 10, 1, 9, 8, 6};
int P8[] = {6, 3, 7, 4, 8, 5, 10, 9};
int IP[] = {2, 6, 3, 1, 4, 8, 5, 7};
int IP_inv[] = {4, 1, 3, 5, 7, 2, 8, 6};
int EP[] = {4, 1, 2, 3, 2, 3, 4, 1};
int P4[] = {2, 4, 3, 1};

int S0[4][4] = {
    {1, 0, 3, 2}, {3, 2, 1, 0}, {0, 2, 1, 3}, {3, 1, 3, 2}};
int S1[4][4] = {
    {0, 1, 2, 3}, {2, 0, 1, 3}, {3, 0, 1, 0}, {2, 1, 0, 3}};

string permute(string input, int* table, int size) {
    string output = "";
    for (int i = 0; i < size; i++) {
        output += input[table[i] - 1];
    }
    return output;
}

string leftShift(string key, int shifts) {
    return key.substr(shifts) + key.substr(0, shifts);
}

string generateKey(string key, bool first) {
    key = permute(key, P10, 10);
    key = leftShift(key.substr(0, 5), first ? 1 : 2) + leftShift(key.substr(5, 5), first ? 1 : 2);
    return permute(key, P8, 8);
}

string xorOperation(string a, string b) {
    string result = "";
    for (size_t i = 0; i < a.length(); i++) {
        result += (a[i] == b[i]) ? '0' : '1';
    }
    return result;
}

string sBox(string input, int S[4][4]) {
    int row = (input[0] - '0') * 2 + (input[3] - '0');
    int col = (input[1] - '0') * 2 + (input[2] - '0');
    int val = S[row][col];
    return string(1, '0' + (val / 2)) + string(1, '0' + (val % 2));
}

string fk(string input, string key) {
    string left = input.substr(0, 4);
    string right = input.substr(4, 4);
    string expandedRight = permute(right, EP, 8);
    string xored = xorOperation(expandedRight, key);
    string sboxOut = sBox(xored.substr(0, 4), S0) + sBox(xored.substr(4, 4), S1);
    string permuted = permute(sboxOut, P4, 4);
    return xorOperation(left, permuted) + right;
}

string swapHalves(string input) {
    return input.substr(4, 4) + input.substr(0, 4);
}

string encrypt(string plaintext, string key) {
    string K1 = generateKey(key, true);
    string K2 = generateKey(key, false);
    string permutedText = permute(plaintext, IP, 8);
    string firstRound = fk(permutedText, K1);
    string swapped = swapHalves(firstRound);
    string secondRound = fk(swapped, K2);
    return permute(secondRound, IP_inv, 8);
}

string decrypt(string ciphertext, string key) {
    string K1 = generateKey(key, true);
    string K2 = generateKey(key, false);
    string permutedText = permute(ciphertext, IP, 8);
    string firstRound = fk(permutedText, K2);
    string swapped = swapHalves(firstRound);
    string secondRound = fk(swapped, K1);
    return permute(secondRound, IP_inv, 8);
}

int main() {
    string key, plaintext;
    cout << "Enter 10-bit key: ";
    cin >> key;
    cout << "Enter 8-bit plaintext: ";
    cin >> plaintext;
    
    string ciphertext = encrypt(plaintext, key);
    cout << "Encrypted Text: " << ciphertext << endl;
    
    string decryptedText = decrypt(ciphertext, key);
    cout << "Decrypted Text: " << decryptedText << endl;
    
    return 0;
}


// Enter 10-bit key: 1010000010
// Enter 8-bit plaintext: 11010101
// Encrypted Text: 11100011
// Decrypted Text: 11010101