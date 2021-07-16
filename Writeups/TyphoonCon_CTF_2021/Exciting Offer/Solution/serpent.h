//
//  serpent.h
//  Serpent
//

#ifndef __Serpent__serpent__
#define __Serpent__serpent__

void hexConvert(const char *s, unsigned char* b);
void printHex(const unsigned char *s, int bytelength, const char * message);

void serpent_encrypt_bitslice(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes);

void serpent_encrypt_standard(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes);

void serpent_decrypt_bitslice(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes);

void serpent_decrypt_standard(const unsigned char* plaintext,
                              const unsigned char* key,
                              unsigned char * output,
                              unsigned int kBytes);

#endif /* defined(__Serpent__serpent__) */
