#include <iostream>
#include <string>

using namespace std;

unsigned char rol(unsigned char v, int s)
{
	int b = s % 8;
	return (unsigned char)(v << b | v >> (8 - b));
}

unsigned char ror(unsigned char v, int s)
{
	int b = s % 8;
	return (unsigned char)(v >> b | v << (8 - b));
}

int main(int argc, char const *argv[])
{
    unsigned char vals[] = {113, 3, 47, 134, 147, 48, 211, 195, 255, 199, 147, 173, 122, 83, 127, 147, 147, 127, 56, 195, 237, 112, 147, 238, 7, 67, 100, 135, 22, 127, 116, 82, 0, 182, 195, 43, 147, 3, 47, 103, 147, 48, 12, 195, 255, 41, 147, 173, 125, 83, 127, 144, 147, 127, 215, 195, 237, 77, 147, 238, 5, 67, 100, 110, 22, 127, 156, 82, 0};
    string key = "c4t3rp1114rz_s3cr3t1y_ru13_7h3_w0r1d";

    string flag;

    for(int i = 0; i < 69; i++) {
        unsigned char x = vals[i];
        x = ror(x , 6);
        x += 127;
        x ^= key[i % key.length()];
        x -= 222;
        x = ror(x , 114);
        flag.insert(0 , 1, (char)x);
    }

    cout << flag << endl;

    return 0;
}
