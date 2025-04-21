#include <iostream>
#include <cstring>
#include <iomanip>
#include <sstream>

typedef unsigned int uint32;

class MD5 {
public:
    MD5() { reset(); }

    std::string digest(const std::string& str) {
        reset();
        update((const unsigned char*)str.c_str(), str.length());
        finalize();
        return toHex();
    }

private:
    uint32 a, b, c, d;
    uint32 msgLenLow, msgLenHigh;
    unsigned char buffer[64];
    uint32 block[16];
    bool finalized;

    void reset() {
        finalized = false;
        msgLenLow = msgLenHigh = 0;
        a = 0x67452301;
        b = 0xefcdab89;
        c = 0x98badcfe;
        d = 0x10325476;
    }

    static uint32 F(uint32 x, uint32 y, uint32 z) { return (x & y) | (~x & z); }
    static uint32 G(uint32 x, uint32 y, uint32 z) { return (x & z) | (y & ~z); }
    static uint32 H(uint32 x, uint32 y, uint32 z) { return x ^ y ^ z; }
    static uint32 I(uint32 x, uint32 y, uint32 z) { return y ^ (x | ~z); }

    static uint32 rotateLeft(uint32 x, int n) { return (x << n) | (x >> (32 - n)); }

    void step(uint32& w, uint32 x, uint32 y, uint32 z, uint32 data, uint32 s, uint32 ac, uint32 (*func)(uint32, uint32, uint32)) {
        w = w + func(x, y, z) + data + ac;
        w = rotateLeft(w, s) + x;
    }

    void transform(const unsigned char block[64]) {
        for (int i = 0; i < 16; ++i)
            this->block[i] = ((uint32)block[i * 4]) | ((uint32)block[i * 4 + 1] << 8) |
                             ((uint32)block[i * 4 + 2] << 16) | ((uint32)block[i * 4 + 3] << 24);

        uint32 A = a, B = b, C = c, D = d;

        // Round 1
        step(A, B, C, D, this->block[0], 7, 0xd76aa478, F);
        step(D, A, B, C, this->block[1], 12, 0xe8c7b756, F);
        step(C, D, A, B, this->block[2], 17, 0x242070db, F);
        step(B, C, D, A, this->block[3], 22, 0xc1bdceee, F);
        step(A, B, C, D, this->block[4], 7, 0xf57c0faf, F);
        step(D, A, B, C, this->block[5], 12, 0x4787c62a, F);
        step(C, D, A, B, this->block[6], 17, 0xa8304613, F);
        step(B, C, D, A, this->block[7], 22, 0xfd469501, F);
        step(A, B, C, D, this->block[8], 7, 0x698098d8, F);
        step(D, A, B, C, this->block[9], 12, 0x8b44f7af, F);
        step(C, D, A, B, this->block[10], 17, 0xffff5bb1, F);
        step(B, C, D, A, this->block[11], 22, 0x895cd7be, F);
        step(A, B, C, D, this->block[12], 7, 0x6b901122, F);
        step(D, A, B, C, this->block[13], 12, 0xfd987193, F);
        step(C, D, A, B, this->block[14], 17, 0xa679438e, F);
        step(B, C, D, A, this->block[15], 22, 0x49b40821, F);

        a += A; b += B; c += C; d += D;
    }

    void update(const unsigned char* input, size_t length) {
        size_t index = (msgLenLow >> 3) & 0x3F;
        if ((msgLenLow += (uint32)(length << 3)) < (length << 3))
            msgLenHigh++;
        msgLenHigh += (uint32)(length >> 29);

        size_t partLen = 64 - index;
        size_t i = 0;

        if (length >= partLen) {
            memcpy(&buffer[index], input, partLen);
            transform(buffer);

            for (i = partLen; i + 63 < length; i += 64)
                transform(&input[i]);

            index = 0;
        }

        memcpy(&buffer[index], &input[i], length - i);
    }

    void finalize() {
        static unsigned char PADDING[64] = { 0x80 };
        if (finalized) return;

        unsigned char bits[8];
        for (int i = 0; i < 4; ++i) {
            bits[i] = (unsigned char)(msgLenLow >> (i * 8));
            bits[i + 4] = (unsigned char)(msgLenHigh >> (i * 8));
        }

        size_t index = (msgLenLow >> 3) & 0x3f;
        size_t padLen = (index < 56) ? (56 - index) : (120 - index);
        update(PADDING, padLen);
        update(bits, 8);

        finalized = true;
    }

    std::string toHex() const {
        std::ostringstream os;
        uint32 vals[4] = { a, b, c, d };
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                os << std::hex << std::setw(2) << std::setfill('0') << ((vals[i] >> (j * 8)) & 0xff);
        return os.str();
    }
};

int main() {
    MD5 md5;
    std::string input;
    std::cout << "Enter a message: ";
    std::getline(std::cin, input);

    std::string hash = md5.digest(input);
    std::cout << "MD5 Hash: " << hash << std::endl;

    return 0;
}
