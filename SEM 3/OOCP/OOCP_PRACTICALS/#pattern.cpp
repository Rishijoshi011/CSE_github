// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

// ! left, middle and right triangle pattern is dependent on the space given in ""
// * left triangle space = "" 0
// * middle triangle space = " " 1
// * right triangle space = "  " 2
    
int main() {

    int k = 5;
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            if (j >= k) { cout << "* "; }
            else { cout << ""; }

        }
        cout << endl;
        k--;
    }

    k = 1;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            if (j >= k) { 
                cout << "* "; 
            } else { 
                cout << ""; 
            }
        }
        cout << endl;
        k++;
    }

    return 0;
}