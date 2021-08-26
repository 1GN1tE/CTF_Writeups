#include <stdio.h>
#include <stdlib.h>
char data[] = {0x36, 0x65, 0x31, 0xe3, 0xb6, 0xaa, 0x22, 0xae, 0x89, 0x7b, 0x8b, 0x7a, 0x21, 0xaf, 0xa7, 0x3a, 0x88, 0x3a, 0x0f, 0x7b, 0x8a, 0x6e, 0x8a, 0x2e, 0x0b, 0x7a, 0x88, 0xbb, 0xa3, 0x2e, 0x8f, 0x7b, 0x27, 0xfb, 0x0a, 0xbb, 0x89, 0x3b, 0x2b, 0x74, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37, 0x13, 0x37};

void sub_5C75C6()
{
    char v0; // al
    char v1; // al
    char v2; // al
    char v3; // al
    char v4; // al
    char v5; // [rsp+0h] [rbp-Ah]
    char v6; // [rsp+1h] [rbp-9h]
    char v7; // [rsp+1h] [rbp-9h]
    int i; // [rsp+6h] [rbp-4h]

    for ( i = 0; i < 100; i += 2 )
    {
        for(int a = 0; a <= 128; a++)
        {
            for(int b = 0; b <= 128; b++)
            {
                v6 = (a >> 4) | (b << 4);
                v5 = (b >> 4) | (a << 4);
                if ( v6 >= 0 )
                    v0 = 2 * v6;
                else
                    v0 = (2 * v6) | 1;
                if ( v0 >= 0 )
                    v1 = 2 * v0;
                else
                    v1 = (2 * v0) | 1;
                if ( v1 >= 0 )
                    v2 = 2 * v1;
                else
                    v2 = (2 * v1) | 1;
                v7 = v2;
                if ( v5 >= 0 )
                    v3 = 2 * v5;
                else
                    v3 = (2 * v5) | 1;
                if ( v3 >= 0 )
                    v4 = 2 * v3;
                else
                    v4 = (2 * v3) | 1;

                char c = v7 ^ 0x13;
                char d = v4 ^ 0x37;

                if ((c == data[i]) && (d == data[i+1])) {
                    printf("%c%c",a,b);
                    break;
                }
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    sub_5C75C6();
    return 0;
}
// IJCTF{fb1551bdd947185c4c5027da19c82205}