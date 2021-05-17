//
//  serpent.c
//  Serpent
//

#include "serpent.h"
#include "s-boxes.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <inttypes.h>

// IMPORTANT: ONLY CONVERTS A BIG ENDIAN HEX STRING
void hexConvert(const char *s, unsigned char* b) {
    const char* a = "0123456789abcdef";
    // find
    for(int i = 0; i < 32; i+=2) {
        unsigned char e = 0;
        for(int j = 0; j < 16; ++j) {
            if(s[i] == a[j]){
                e |= j << 4;
                break;
            }
        }
        for(int j = 0; j < 16; ++j) {
            if(s[i+1] == a[j]){
                e |= j << 0;
                break;
            }
        }
        b[15-(i/2)] = e;
    }
}

void printHex(const unsigned char *s, int bytelength, const char * message) {
    const char* a = "0123456789abcdef";
    // printf("%s\n", message);
    // printf("(little endian)\n");
    // for(int i = 0; i < bytelength; ++i){
    //     printf("%c", a[(s[i] >> 0) & 0xF]);
    //     printf("%c", a[(s[i] >> 4) & 0xF]);
    // }
    // printf("\n(big endian)\n");
    // for(int i = bytelength-1; i >= 0; --i){
    //     printf("%c", a[(s[i] >> 4) & 0xF]);
    //     printf("%c", a[(s[i] >> 0) & 0xF]);
    // }
    // printf("\n");
}

uint32_t rotl (WORD x, int p) {
    return ((x << p) | (x >> (BITS_PER_WORD-p))) & 0xffffffff;
}

void InitialPermutation(const uint *input, uint *result) {
    // copy end bits
    result[0] |= ((input[0] >> 0 ) & 0x1) << 0 ;
    result[3] |= ((input[3] >> 31) & 0x1) << 31;
    // transform bits
    // THIS SHOULD BE CORRECT
    for(int i = 1; i < 127; ++i) {
        uint replacer = ((i*32)%127);
        uint currentBlockPosition = i/32;
        uint currentBlockReplacer = replacer/32;
        result[currentBlockPosition] |= ((input[currentBlockReplacer] >> (replacer%32)) & 1) << (i % 32);
    }
}

void FinalPermutation(const uint *input, uint *result) {
    // copy end bits
    result[0] |= ((input[0] >> 0 ) & 0x1) << 0 ;
    result[3] |= ((input[3] >> 31) & 0x1) << 31;
    // transform bits
    for(int i = 1; i < 127; ++i) {
        uint replacer = ((i*4)%127);
        uint currentBlockPosition = i/32;
        uint currentBlockReplacer = replacer/32;
        result[currentBlockPosition] |= ((input[currentBlockReplacer] >> (replacer%32)) & 1) << (i % 32);
    }
}

void InverseInitialPermutation(const uint *input, uint *result) {
    // copy end bits
    result[0] |= ((input[0] >> 0 ) & 0x1) << 0 ;
    result[3] |= ((input[3] >> 31) & 0x1) << 31;
    for(int i = 0; i < 127; ++i) {
        uint position = ((32*i)%127);
        uint currentBlockPosition = position/32;
        uint currentBlockReplacer = i/32;
        result[currentBlockPosition] |= ((input[currentBlockReplacer] >> (i%32)) & 1) << (position % 32);
    }
}

void InverseFinalPermutation(const uint *input, uint *result) {
    // copy end bits
    result[0] |= ((input[0] >> 0 ) & 0x1) << 0 ;
    result[3] |= ((input[3] >> 31) & 0x1) << 31;
    for(int i = 0; i < 127; ++i) {
        uint position = ((4*i)%127);
        uint currentBlockPosition = position/32;
        uint currentBlockReplacer = i/32;
        result[currentBlockPosition] |= ((input[currentBlockReplacer] >> (i%32)) & 1) << (position % 32);
    }
}

// IMPORTED FUNCTION
void setBit(uint *x, int p, BIT v) {
    /* Set the bit at position 'p' of little-endian word array 'x' to 'v'. */
    
    if (v) {
        x[p/BITS_PER_WORD] |= ((WORD) 0x1 << p%BITS_PER_WORD);
    } else {
        x[p/BITS_PER_WORD] &= ~((WORD) 0x1 << p%BITS_PER_WORD);
    }
}
// IMPORTED FUNCTION
BIT getBit(WORD x[], int p) {
    /* Return the value of the bit at position 'p' in little-endian word
     array 'x'. */
    
    return (BIT) ((x[p/BITS_PER_WORD]
                   & ((WORD) 0x1 << p%BITS_PER_WORD)) >> p%BITS_PER_WORD);
}

void key_generation_standard(uint subkeysHat[33][4],
                             const uchar *key,
                             uchar *output,
                             uint kBytes) {
    
    // 33 subkeys * 32bits * 4 blocks
    uint subkeys[33][4]= {0};
    uint keysplit[8]   = {0};
    uint interkey[140] = {0};
    
    // memory precheck
    if(output == NULL) {
        fprintf(stderr, "Given output char pointer not initialized/allocated.\n");
        exit(EXIT_FAILURE);
    }
    
    /* BIT EXTEND KEY */
    
    // check if key needs to be padded then
    // split original key into 8 32bit prekeys
    if(kBytes < 32){
        unsigned char tempkey[32] = {0};
        // if shorter than 32 bytes, pad key with 0b1
        ulong kl = kBytes;
        for(int i = 0; i < kl; ++i) {
            tempkey[i] = key[i];
        }
        tempkey[kl] = 0b00000001;
        for(int i = 0; i < 8; ++i) {
            keysplit[i] = *(((uint*)tempkey)+i);
        }
        printHex(tempkey, 32, "Key:");
    }
    else if(kBytes == 32) {
        for(int i = 0; i < 8; ++i) {
            keysplit[i] = *(((uint*)key)+i);
        }
        printHex(key, 32, "Key:");
    }
    else {
        printf("Key Length Error\n");
        exit(EXIT_FAILURE);
    }
    
    // load keysplit into interkey
    for(int i = 0; i < 8; ++i){
        interkey[i] = keysplit[i];
    }
    
    /* GENERATE PREKEYS */
    
    for(int i = 8; i < 140; ++i) {
        interkey[i] = rotl((interkey[i-8] ^ interkey[i-5] ^ interkey[i-3] ^ interkey[i-1] ^ phi ^ (i-8)), 11);
    }
    
    /* GENERATE SUBKEYS */
    
    // generate keys from s-boxes
    // holds keys
    for(int i = 0; i < 33; ++i) {
        // descending selector starting at 3
        int currentBox = (32 + 3 - i) % 32;
        char sboxOut= 0;
        for(int j = 0; j < 32; ++j) {
            sboxOut = SBox[currentBox%8][((interkey[8+0+(4*i)]>>j)&1) <<0 |
                                         ((interkey[8+1+(4*i)]>>j)&1) <<1 |
                                         ((interkey[8+2+(4*i)]>>j)&1) <<2 |
                                         ((interkey[8+3+(4*i)]>>j)&1) <<3 ];
            for(int l = 0; l < 4; ++l) {
                subkeys[i][l] |= ((sboxOut >> l)&1)<<j;
            }
        }
    }
    
    // PERMUTATE THE KEYS
    for(int i = 0; i < 33; ++i) {
        InitialPermutation(subkeys[i], subkeysHat[i]);
    }
}

void key_generation_bitslice(uint subkeys[33][4],
                             const uchar *key,
                             uchar *output,
                             uint kBytes) {
    
    // 33 subkeys * 32bits * 4 blocks
    uint keysplit[8]   = {0};
    uint interkey[140] = {0};
    
    // memory precheck
    if(output == NULL) {
        fprintf(stderr, "Given output char pointer not initialized/allocated.\n");
        exit(EXIT_FAILURE);
    }
    
    /* BIT EXTEND KEY */
    
    // check if key needs to be padded then
    // split original key into 8 32bit prekeys
    if(kBytes < 32){
        unsigned char tempkey[32] = {0};
        // if shorter than 32 bytes, pad key with 0b1
        ulong kl = kBytes;
        for(int i = 0; i < kl; ++i) {
            tempkey[i] = key[i];
        }
        tempkey[kl] = 0b00000001;
        for(int i = 0; i < 8; ++i) {
            keysplit[i] = *(((uint*)tempkey)+i);
        }
        printHex(tempkey, 32, "Key:");
    }
    else if(kBytes == 32) {
        for(int i = 0; i < 8; ++i) {
            keysplit[i] = *(((uint*)key)+i);
        }
        printHex(key, 32, "Key:");
    }
    else {
        printf("Key Length Error\n");
        exit(EXIT_FAILURE);
    }
    
    // load keysplit into interkey
    for(int i = 0; i < 8; ++i){
        interkey[i] = keysplit[i];
    }
    
    /* GENERATE PREKEYS */
    
    for(int i = 8; i < 140; ++i) {
        interkey[i] = rotl((interkey[i-8] ^ interkey[i-5] ^ interkey[i-3] ^ interkey[i-1] ^ phi ^ (i-8)), 11);
    }
    
    /* GENERATE SUBKEYS */
    
    // generate keys from s-boxes
    // holds keys
    for(int i = 0; i < 33; ++i) {
        // descending selector starting at 3
        int currentBox = (32 + 3 - i) % 32;
        char sboxOut= 0;
        for(int j = 0; j < 32; ++j) {
            sboxOut = SBox[currentBox%8][((interkey[8+0+(4*i)]>>j)&1) <<0 |
                                         ((interkey[8+1+(4*i)]>>j)&1) <<1 |
                                         ((interkey[8+2+(4*i)]>>j)&1) <<2 |
                                         ((interkey[8+3+(4*i)]>>j)&1) <<3 ];
            for(int l = 0; l < 4; ++l) {
                subkeys[i][l] |= ((sboxOut >> l)&1)<<j;
            }
        }
    }
}

void serpent_encrypt_standard(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes) {
    
    // 33 subkeys * 32bits * 4 blocks
    uint subkeysHat[33][4]= {0};
    
    printHex(plaintext, 16, "Plaintext:");
    key_generation_standard(subkeysHat, key, output, kBytes);
    
    /*  Start plaintext processing  */
    
    /* INITIAL PERMUTATION */
    
    // ignore bit[0] and bit[127]
    // replace bit[1..126] with bit[(i*32)%127]
    const uint *charpToInt = (const uint*)plaintext;
    uint result[4] = {0};
    InitialPermutation(charpToInt, result);
    
    // result == Bi
    
    /* LINEAR TRANSFORMATION */
    
    // 32 rounds
    uint X[4] = {0};
    for(int i = 0; i < 32; ++i) {
        for (int j = 0; j < 4; ++j) {
            X[j] = result[j] ^ subkeysHat[i][j];
        }
        for(int j = 0; j < 4; ++j) {
            X[j] =  (SBox[i%8][(X[j] >> 0 ) & 0xF]) << 0 |
                    (SBox[i%8][(X[j] >> 4 ) & 0xF]) << 4 |
                    (SBox[i%8][(X[j] >> 8 ) & 0xF]) << 8 |
                    (SBox[i%8][(X[j] >> 12) & 0xF]) << 12|
                    (SBox[i%8][(X[j] >> 16) & 0xF]) << 16|
                    (SBox[i%8][(X[j] >> 20) & 0xF]) << 20|
                    (SBox[i%8][(X[j] >> 24) & 0xF]) << 24|
                    (SBox[i%8][(X[j] >> 28) & 0xF]) << 28;
        }
        if(i < 31){            
            for(int a = 0; a < 128; ++a) {
                char b = 0;
                int  j = 0;
                while (LTTable[a][j] != MARKER) {
                    b ^= getBit(X, LTTable[a][j]);
                    ++j;
                }
                setBit(result, a, b);
            }
        }
        else{
            // In the last round, the transformation is replaced by an additional key mixing
            result[0] = X[0] ^ subkeysHat[32][0];
            result[1] = X[1] ^ subkeysHat[32][1];
            result[2] = X[2] ^ subkeysHat[32][2];
            result[3] = X[3] ^ subkeysHat[32][3];
        }
    }
    
    /* FINAL PERMUTATION */
    uint finalResult[4] = {0};
    FinalPermutation(result, finalResult);
    
    // copy 128 bits to output string
    memcpy(output, finalResult, 16);
}
void serpent_encrypt_bitslice(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes) {
    
    uint subkeys[33][4] = {0};
    
    printHex(plaintext, 16, "Plaintext:");
    
    key_generation_bitslice(subkeys, key, output, kBytes);
    
    /*  Start plaintext processing  */
    
    // Adapt char pointer to 32bit pointer
    uint *X = (uint*)plaintext;
    
    /* LINEAR TRANSFORMATION */
    // 32 rounds
    uint uX[4] = {0};
    for(int i = 0; i < 32; ++i) {
        for (int j = 0; j < 4; ++j) {
            uX[j] = X[j] ^ subkeys[i][j];
            X[j] =  0;
        }
        for(int j = 0; j < 32; ++j) {
            uint v = (SBox[i%8][((uX[0] >> (j)) & 1) << 0 |
                                ((uX[1] >> (j)) & 1) << 1 |
                                ((uX[2] >> (j)) & 1) << 2 |
                                ((uX[3] >> (j)) & 1) << 3 ]);
            
            X[0] |= ((v >> 0)&1) << j;
            X[1] |= ((v >> 1)&1) << j;
            X[2] |= ((v >> 2)&1) << j;
            X[3] |= ((v >> 3)&1) << j;
        }
        if(i < 31){
            
//            X[0] = rotl(X[0], 13);
//            X[2] = rotl(X[2], 3);
//            X[1] = X[1] ^ X[0] ^ X[2];
//            X[3] = X[3] ^ X[2] ^ (X[0] << 3);
//            X[1] = rotl(X[1], 1);
//            X[3] = rotl(X[3], 7);
//            X[0] = X[0] ^ X[1] ^ X[3];
//            X[2] = X[2] ^ X[3] ^ (X[1] << 7);
//            X[0] = rotl(X[0], 5);
//            X[2] = rotl(X[2], 22);
            
            // reduced assignment linear mixing (minimized from step equation in documentation)
            X[1] = rotl(X[1] ^ rotl(X[0], 13) ^ rotl(X[2], 3 ), 1);
            X[3] = rotl(X[3] ^ rotl(X[2], 3 ) ^ (rotl(X[0], 13) << 3), 7);
            X[0] = rotl(rotl(X[0], 13) ^ X[1] ^ X[3], 5 );
            X[2] = rotl(rotl(X[2], 3 ) ^ X[3] ^ (X[1] << 7), 22);
        }
        else{
            // In the last round, the transformation is replaced by an additional key mixing
            X[0] = X[0] ^ subkeys[32][0];
            X[1] = X[1] ^ subkeys[32][1];
            X[2] = X[2] ^ subkeys[32][2];
            X[3] = X[3] ^ subkeys[32][3];
        }
    }
    
    // copy 128 bits to output string
    memcpy(output, X, 16);
}

void serpent_decrypt_standard(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes) {
    
    uint subkeysHat[33][4] = {0};
    
    key_generation_standard(subkeysHat, key, output, kBytes);
    
    /*  Start plaintext processing  */
    
    /* REVERSE FINAL PERMUTATION */
    
    // ignore bit[0] and bit[127]
    // replace bit[1..126] with bit[(i*32)%127]
    const uint *charpToInt = (const uint*)plaintext;
    uint result[4] = {0};
    InverseFinalPermutation(charpToInt, result);
    
    // result == Bi
    
    /* REVERSE LINEAR TRANSFORMATION */
    
    // 32 rounds
    uint X[4] = {0};
    for(int i = 31; i >= 0; --i) {
        if(i < 31){
            for(int a = 0; a < 128; ++a) {
                char b = 0;
                int  j = 0;
                while (LTTableInverse[a][j] != MARKER) {
                    b ^= getBit(result, LTTableInverse[a][j]);
                    ++j;
                }
                setBit(X, a, b);
            }
        }
        else{
            // In the last round, the transformation is replaced by an additional key mixing
            X[0] = result[0] ^ subkeysHat[32][0];
            X[1] = result[1] ^ subkeysHat[32][1];
            X[2] = result[2] ^ subkeysHat[32][2];
            X[3] = result[3] ^ subkeysHat[32][3];
        }
        for(int j = 0; j < 4; ++j) {
            X[j] =  (SBoxInverse[i%8][(X[j] >> 0 ) & 0xF]) << 0 |
                    (SBoxInverse[i%8][(X[j] >> 4 ) & 0xF]) << 4 |
                    (SBoxInverse[i%8][(X[j] >> 8 ) & 0xF]) << 8 |
                    (SBoxInverse[i%8][(X[j] >> 12) & 0xF]) << 12|
                    (SBoxInverse[i%8][(X[j] >> 16) & 0xF]) << 16|
                    (SBoxInverse[i%8][(X[j] >> 20) & 0xF]) << 20|
                    (SBoxInverse[i%8][(X[j] >> 24) & 0xF]) << 24|
                    (SBoxInverse[i%8][(X[j] >> 28) & 0xF]) << 28;
        }
        for (int j = 0; j < 4; ++j) {
            result[j] = X[j] ^ subkeysHat[i][j];
        }
    }
    
    /* REVERSE INITIAL PERMUTATION */
    
    uint finalResult[4] = {0};
    InverseInitialPermutation(result, finalResult);
    
    // copy 128 bits to output string
    memcpy(output, finalResult, 16);
}

void serpent_decrypt_bitslice(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes) {
    
    uint subkeys[33][4] = {0};
    
    printHex(plaintext, 16, "Plaintext:");
    
    key_generation_bitslice(subkeys, key, output, kBytes);
    
    /*  Start plaintext processing  */
    
    // Adapt char pointer to 32bit pointer
    uint *X = (uint*)plaintext;
    
    /* LINEAR TRANSFORMATION */
    // 32 rounds
    uint uX[4] = {0};
    for(int i = 31; i >= 0; --i) {
        if(i < 31){
            // reduced assignment linear mixing (minimized from step equation in documentation)
            X[2] = rotl(X[2], 10) ^ X[3] ^ (X[1] << 7);
            X[0] = rotl(X[0], 27) ^ X[1] ^ X[3];
            X[3] = rotl(X[3], 25);
            X[1] = rotl(X[1], 31);
            
            
            X[3] = X[3] ^ X[2] ^ (X[0] << 3);
            X[1] = X[1] ^ X[0] ^ X[2];
            X[2] = rotl(X[2], 29);
            X[0] = rotl(X[0], 19);
        }
        else{
            // In the last round, the transformation is replaced by an additional key mixing
            X[0] = X[0] ^ subkeys[32][0];
            X[1] = X[1] ^ subkeys[32][1];
            X[2] = X[2] ^ subkeys[32][2];
            X[3] = X[3] ^ subkeys[32][3];
        }
        for(int j = 0; j < 32; ++j) {
            uint v = (SBoxInverse[i%8][((X[0] >> (j)) & 1) << 0 |
                                       ((X[1] >> (j)) & 1) << 1 |
                                       ((X[2] >> (j)) & 1) << 2 |
                                       ((X[3] >> (j)) & 1) << 3 ]);
            
            uX[0] |= ((v >> 0)&1) << j;
            uX[1] |= ((v >> 1)&1) << j;
            uX[2] |= ((v >> 2)&1) << j;
            uX[3] |= ((v >> 3)&1) << j;
        }
        for (int j = 0; j < 4; ++j) {
            X[j] = uX[j] ^ subkeys[i][j];
            uX[j] =  0;
        }
    }
    
    // copy 128 bits to output string
    memcpy(output, X, 16);
}