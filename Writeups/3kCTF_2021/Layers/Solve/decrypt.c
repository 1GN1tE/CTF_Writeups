#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "serpent.h"

void teadecrypt (uint32_t v[2], const uint32_t k[4]) {
	uint32_t v0=v[0], v1=v[1], sum=0xC6EF3720, i;
	uint32_t delta=0x9E3779B9;
	uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];
	for (i=0; i<32; i++) {
		v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
		v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
		sum -= delta;
	}
	v[0]=v0; v[1]=v1;
}

int main(int argc, char const *argv[])
{
	for(int seed=0; seed < 5000; seed++)
	{
		srand(seed);

		unsigned char key1[33];
		unsigned char key2[17];

		for(int i =0; i < 32; i++)
			key1[i] = rand();

		for(int i =0; i < 16; i++)
			key2[i] = rand();

		unsigned char enc[] = {0x47, 0xB9, 0x0B, 0x54, 0x7A, 0xC8, 0xE9, 0xEB, 0x81, 0xD5, 0x63, 0x67, 0x1D, 0x98, 0x3D, 0x6C, 0x8B, 0x89, 0x29, 0xC4, 0x8E, 0xAF, 0xE8, 0x6B, 0xAA, 0x91, 0xF6, 0xA7, 0xCF, 0x96, 0x13, 0x74, 0x65, 0xA3, 0x1B, 0x60, 0x74, 0xDB, 0x59, 0x94, 0xF6, 0x72, 0x4E, 0xB1, 0x08, 0x48, 0x97, 0xA0};
		
		unsigned char v32[208];
		unsigned char v23[9];
		unsigned char v21[200];

		memset(v23, 0, 0x09);
		memset(v21, 0, 0xC8);

		for(int i = 0; i < 6; i++)
		{
			memset(v23, 0, 8);
			for(int x =0; x < 8; x++)
				v23[x] = enc[8*i + x];

			//TEA Encryption
			teadecrypt((uint32_t *)v23,(uint32_t *)key2);
			for(int x =0; x < 8; x++)
				v21[8*i + x] = v23[x];
		}

		unsigned char v1[17];
		unsigned char ptr[16];
		memset(v1, 0, 17);

		for(int i = 0; i < 3; i++)
		{
			memset(ptr, 0, 16);
			memset(v1, 0, 16);

			for(int x =0; x < 16; x++)
				v1[x] = v21[16*i + x];

			// sub_403EC0((uint32_t *)v1, (uint32_t *)key1, (uint32_t *)ptr, 0x20);
			serpent_decrypt_bitslice(v1, key1, ptr, 32);
			
			for(int x = 0; x < 0x10; x++)
				v32[16 * i + x] = ptr[x];
		}

		if (v32[0]=='f' && v32[1]=='l' && v32[2]=='a' && v32[3]=='g' )
			printf("FLAG!! : %s\n",v32);
	}
	return 0;
}