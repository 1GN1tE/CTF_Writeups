#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "serpent.h"


int main(int argc, char const *argv[])
{
	FILE *fp;
	size_t size;
	unsigned char *buffer;

	fp = fopen("encrytped_flag.txt","rb");
	if (fp == NULL) {
		printf("Error: There was an Error reading the file\n");		   
		exit(1);
	}
	fseek(fp, 0, SEEK_END); 
	size = ftell(fp);
	fseek(fp, 0, SEEK_SET); 
	buffer = malloc(size);

	if (fread(buffer, sizeof *buffer, size, fp) != size) {
		printf("Error: There was an Error reading the file\n");
		exit(1);
	}
	fclose(fp);

	/*
	printf("%lu\n", size);
	for(int i = 0; i < size; i++)
		printf("%x ", buffer[i]);
	*/

	for(int seed=0; seed < 12288; seed++)
	{
		srand(seed);
		unsigned char key[33];

		for(int i = 0; i < 32; i++) {
			int tmp = rand();
			key[i] = (tmp % 256) ^ 0x9D;
		}

		unsigned char dec[0x40];
		memset(dec, 0 ,0x40);

		unsigned char tmp[17];
		unsigned char ptr[17];

		for(int i = 0; i < 3; i++) {
			memset(ptr, 0, 17);
			memset(tmp, 0, 17);

			for(int x = 0; x < 16; x++) {
				tmp[x] = buffer[16*i + x];
			}

			serpent_decrypt_bitslice(tmp, key, ptr, 32);
			
			for(int x = 0; x < 16; x++) {
				dec[16 * i + x] = ptr[x];
			}
		}

		if (dec[0]=='S' && dec[1]=='3' && dec[2]=='D' && dec[3]=='{' ) {
			printf("FLAG!! : %s\n",dec);
			break;
		}
	}

	free(buffer);
	return 0;
}