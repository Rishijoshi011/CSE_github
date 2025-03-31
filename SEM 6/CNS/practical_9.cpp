#include <iostream>
#include <string>
#include <cmath>

using namespace std;

long long modExp(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod; 
    while (exp > 0) {
        if (exp % 2 == 1) { 
            result = (result * base) % mod;
        }
        exp = exp >> 1; 
        base = (base * base) % mod; 
    }
    return result;
}

long long simpleHash(const string& message, long long n) {
    long long hash = 0;
    for (char c : message) {
        hash = (hash * 31 + c) % n;
    }
    return hash;
}

long long gcdExtended(long long a, long long b, long long* x, long long* y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }
    long long x1, y1;
    long long gcd = gcdExtended(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return gcd;
}

long long modInverse(long long e, long long phi) {
    long long x, y;
    long long g = gcdExtended(e, phi, &x, &y);
    if (g != 1) {
        cerr << "Modular inverse doesn't exist";
        exit(EXIT_FAILURE);
    }
    return (x % phi + phi) % phi;
}


void generateKeys(long long& e, long long& d, long long& n) {
    long long p = 1009; 
    long long q = 1013; 
    n = p * q;
    long long phi = (p - 1) * (q - 1);

    e = 65537; 
    d = modInverse(e, phi);
}

long long signMessage(long long hash, long long d, long long n) {
    return modExp(hash, d, n);
}

bool verifySignature(long long hash, long long signature, long long e, long long n) {
    long long decryptedHash = modExp(signature, e, n);
    return hash == decryptedHash;
}

int main() {
    string message;
    cout << "Enter message: ";
    getline(cin, message);

    long long e, d, n;
    generateKeys(e, d, n);

    long long hashValue = simpleHash(message, n);

    long long signature = signMessage(hashValue, d, n);

    cout << "Original Hash: " << hashValue << endl;
    cout << "Signature: " << signature << endl;

    if (verifySignature(hashValue, signature, e, n)) {
        cout << "Signature verified successfully!" << endl;
    } else {
        cout << "Signature verification failed!" << endl;
    }

    return 0;
}
