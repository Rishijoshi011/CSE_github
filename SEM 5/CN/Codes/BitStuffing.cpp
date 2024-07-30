#include <iostream>
#include <string>
#define PATTERN "11111"

using namespace std;

void bitStuffing(string user_bits) {
    cout << "Passed bits are: " << user_bits << endl;
    size_t pos = 0;
    int indexes[10] = {-1};  

    for (int i = 0; i < 10; i++) {
        pos = user_bits.find(PATTERN, pos);
        if (pos != std::string::npos) {
            indexes[i] = pos;
            pos += 1;  
        } else {
            break;  
        }
    }

    for (int i = 0; i < 10 && indexes[i] != -1; i++) {
        cout << "Position of pattern: " << indexes[i] << endl;
    }
}

int main() {
    cout << "Enter the bits: ";
    string user_bits;
    cin >> user_bits;

    bitStuffing(user_bits);

    return 0;
}
