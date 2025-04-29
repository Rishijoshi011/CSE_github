#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <vector>

typedef unsigned int uint32;

class SHA1 {
public:
    SHA1() { reset(); }

    std::string digest(const std::string &message) {
        reset();
        update((const unsigned char*)message.c_str(), message.length());
        finalize();
        return toHex();
    }

private:
    uint32 h0, h1, h2, h3, h4;
    std::vector<unsigned char> buffer;
    uint64_t messageLength;

    void reset() {
        h0 = 0x67452301;
        h1 = 0xEFCDAB89;
        h2 = 0x98BADCFE;
        h3 = 0x10325476;
        h4 = 0xC3D2E1F0;
        buffer.clear();
        messageLength = 0;
    }

    static uint32 rotateLeft(uint32 value, uint32 bits) {
        return (value << bits) | (value >> (32 - bits));
    }

    void processBlock(const unsigned char block[64]) {
        uint32 w[80];
        for (int i = 0; i < 16; ++i)
            w[i] = (block[i * 4] << 24) |
                   (block[i * 4 + 1] << 16) |
                   (block[i * 4 + 2] << 8) |
                   (block[i * 4 + 3]);

        for (int i = 16; i < 80; ++i)
            w[i] = rotateLeft(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1);

        uint32 a = h0, b = h1, c = h2, d = h3, e = h4;

        for (int i = 0; i < 80; ++i) {
            uint32 f, k;
            if (i < 20) {
                f = (b & c) | (~b & d);
                k = 0x5A827999;
            } else if (i < 40) {
                f = b ^ c ^ d;
                k = 0x6ED9EBA1;
            } else if (i < 60) {
                f = (b & c) | (b & d) | (c & d);
                k = 0x8F1BBCDC;
            } else {
                f = b ^ c ^ d;
                k = 0xCA62C1D6;
            }

            uint32 temp = rotateLeft(a, 5) + f + e + k + w[i];
            e = d;
            d = c;
            c = rotateLeft(b, 30);
            b = a;
            a = temp;
        }

        h0 += a;
        h1 += b;
        h2 += c;
        h3 += d;
        h4 += e;
    }

    void update(const unsigned char *data, size_t length) {
        messageLength += length * 8;
        buffer.insert(buffer.end(), data, data + length);

        while (buffer.size() >= 64) {
            processBlock(&buffer[0]);
            buffer.erase(buffer.begin(), buffer.begin() + 64);
        }
    }

    void finalize() {
        buffer.push_back(0x80);
        while ((buffer.size() + 8) % 64 != 0)
            buffer.push_back(0x00);

        for (int i = 7; i >= 0; --i)
            buffer.push_back((messageLength >> (i * 8)) & 0xFF);

        for (size_t i = 0; i < buffer.size(); i += 64)
            processBlock(&buffer[i]);
    }

    std::string toHex() const {
        std::ostringstream result;
        uint32 words[5] = { h0, h1, h2, h3, h4 };
        for (int i = 0; i < 5; ++i)
            result << std::hex << std::setw(8) << std::setfill('0') << words[i];
        return result.str();
    }
};

int main() {
    SHA1 sha1;
    std::string input;
    std::cout << "Enter a message: ";
    std::getline(std::cin, input);

    std::string hash = sha1.digest(input);
    std::cout << "SHA-1 Hash: " << hash << std::endl;

    return 0;
}
