#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getOrder(string key) {
    vector<pair<char, int>> keyMap;
    for (int i = 0; i < key.length(); ++i)
        keyMap.emplace_back(key[i], i);

    sort(keyMap.begin(), keyMap.end());

    vector<int> order(key.length());
    for (int i = 0; i < key.length(); ++i)
        order[keyMap[i].second] = i;

    return order;
}

string encrypt(string message, string key) {
    int cols = key.length();
    vector<int> order = getOrder(key);
    int rows = (message.length() + cols - 1) / cols;

    vector<vector<char>> grid(rows, vector<char>(cols, 'X')); 

    int k = 0;
    for (int i = 0; i < rows && k < message.length(); ++i)
        for (int j = 0; j < cols && k < message.length(); ++j)
            grid[i][j] = message[k++];

    string ciphertext = "";
    for (int o = 0; o < cols; ++o) {
        for (int j = 0; j < cols; ++j) {
            if (order[j] == o) {
                for (int i = 0; i < rows; ++i)
                    ciphertext += grid[i][j];
                break;
            }
        }
    }

    return ciphertext;
}

int main() {
    string message, key;

    cout << "Enter the plaintext message (no spaces): ";
    cin >> message;

    cout << "Enter the key (e.g., word or numbers): ";
    cin >> key;

    string encrypted = encrypt(message, key);
    cout << "Encrypted message: " << encrypted << endl;

    return 0;
}
