#include <iostream>
#include <string>

using namespace std;


int main() {

    string str;
    int assci_val[30];
    int var_xor = 0, var_and = 0, var_or = 0;

    cout << "Enter String: " << endl;
    getline(cin, str);

    // cout  << "Enter XOR, AND, OR values: " << endl;
    // cin >> var_xor >> var_and >> var_or;

    cout << "--------------Question-A--------------------" << endl;
    for(int i = 0; i < str.length(); i++) {
        assci_val[i] = str[i];
        // cout << assci_val[i] << " ";
    }

    for (int i = 0; i < str.length(); i++) {
        cout << str[i] << " bit "<< assci_val[i] << " xor by " << var_xor  << ": "<< (assci_val[i] ^ var_xor) << endl; // ! XOR
        cout << str[i] << " bit "<< assci_val[i] << " AND by " << var_and  << ": "<< (assci_val[i] & var_and) << endl; // ! AND
        cout << str[i] << " bit "<< assci_val[i] << " OR by " << var_or  << ": "<< (assci_val[i] | var_or) << endl; // ! OR
        cout << endl;
    }
    cout << "---------------Question-B--------------------" << endl;
    cout << "Operations are performed with the 127" << endl;
    var_xor = 127, var_and = 127, var_or = 127;
    
    for (int i = 0; i < str.length(); i++) {
        cout << str[i] << " bit "<< assci_val[i] << " xor by " << var_xor  << ": "<< (assci_val[i] ^ var_xor) << endl; // ! XOR
        cout << str[i] << " bit "<< assci_val[i] << " AND by " << var_and  << ": "<< (assci_val[i] & var_and) << endl; // ! AND
        cout << str[i] << " bit "<< assci_val[i] << " OR by " << var_or  << ": "<< (assci_val[i] | var_or) << endl; // ! OR
        cout << endl;
    }
    
    cout << "----------------Question-C-------------------" << endl;
    for (int i = 0; i < str.length(); i++) {
        cout << str[i] << " bit "<< assci_val[i] << " OR by " << var_or  << ": "<< (assci_val[i] | var_or) << endl; // ! OR
        cout << str[i] << " bit "<< assci_val[i] << " left shift by " << 1  << ": "<< (assci_val[i] << 1) << endl; // ! left shift
        cout << str[i] << " bit "<< assci_val[i] << " right shift by " << 1  << ": "<< (assci_val[i] >> 1) << endl; // ! right shift
        cout << endl;
    }
    
    return 0;
}

// int result_xor, result_and, result_or, result_lshift, result_rshift;

    // for (int i = 0; i < str.length(); i++) {
        //     result_xor = (assci_val[i] ^ var_xor);  // ! XOR
    //     result_and = (assci_val[i] & var_and);  // ! AND
    //     result_or = (assci_val[i] | var_or);    // ! OR
    //     result_lshift = (assci_val[i] << 1);    // ! left shift
    //     result_rshift = (assci_val[i] >> 1);    // ! right shift
    // }


    // for (int i = 0; i < str.length(); i++) {
    //     cout << str[i] << " bit "<< assci_val[i] << " xor by " << var_xor  << ": "<< (assci_val[i] ^ var_xor) << endl; // ! XOR
    //     cout << str[i] << " bit "<< assci_val[i] << " AND by " << var_and  << ": "<< (assci_val[i] & var_and) << endl; // ! AND
    //     cout << str[i] << " bit "<< assci_val[i] << " OR by " << var_or  << ": "<< (assci_val[i] | var_or) << endl; // ! OR
    //     cout << str[i] << " bit "<< assci_val[i] << " left shift by " << 1  << ": "<< (assci_val[i] << 1) << endl; // ! left shift
    //     cout << str[i] << " bit "<< assci_val[i] << " right shift by " << 1  << ": "<< (assci_val[i] >> 1) << endl; // ! right shift
    //     cout << endl;