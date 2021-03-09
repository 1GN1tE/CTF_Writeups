#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "sha-256.h"

uint8_t keyid[] = {0xed, 0x25, 0x91, 0xb6, 0x66, 0x0b, 0x2b, 0x05, 0xa0, 0xe5, 0xb2, 0x21, 0x52, 0xb1, 0x20, 0xcd, 0x59, 0x45, 0x8e, 0xb2, 0x50, 0x4c, 0x52, 0x99, 0x27, 0xff, 0x9a, 0x48, 0x90, 0xb6, 0x91, 0x2e};

int check_key(int key[])
{
	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			if (i != j && key[i] == key[j])
				return 0;

	int array2[] = {1, 3, 11, 5, 1};
	int num = 85;

	for(int i=0; i <5; i++)
	{
		int num2 = key[i];
		if ((i > 0) && (num2 % i != 0) && (i<4))
			return 0;
		if ((i > 0) && (num2 % array2[i] != 0) && (i<4))
			return 0;
		num ^= num2;
	}
	if(num == 0)
		return 1;
	else
		return 0;
}

void check_hash(int key[])
{
	printf("Checking Possible Key: ");
	for(int i=0;i<5;i++)
		printf("0x%04x, ", key[i]);
	printf("\n");
	uint8_t input[20];
	for(int i=0;i<5;i++)
	{
		int tmp = key[i];
		input[i*4+0] = tmp & 0xff;
		tmp = tmp >> 8;
		input[i*4+1] = tmp & 0xff;
		tmp = tmp >> 8;
		input[i*4+2] = tmp & 0xff;
		tmp = tmp >> 8;
		input[i*4+3] = tmp & 0xff;
		tmp = tmp >> 8;
	}
	// for(int i=0;i<20;i++)
	// 	printf("%02x", input[i]);
	// printf("\n");

	uint8_t hash[32];
	calc_sha_256(hash, input, 20);

	// for(int i=0;i<32;i++)
	// 	printf("%02x", hash[i]);
	// printf("\n");

	uint8_t new_hash[32];
	calc_sha_256(new_hash, hash, 32);

	// for(int i=0;i<32;i++)
	// 	printf("%02x", new_hash[i]);
	// printf("\n");

	for(int i=0;i<32;i++)
	{
		if(keyid[i]==new_hash[i])
			continue;
		else
			return;
	}
	printf("Key Found!!!!\n");
	exit(0);
}

int main(int argc, char const *argv[])
{
	for(int arr1=0; arr1<=2048; arr1++)
		for(int arr2=0; arr2<=2048; arr2++)
			for(int arr3=0; arr3<=2048; arr3++)
				for(int arr4=0; arr4<=2048; arr4++)
				{
					int key[] = {0x6e6, arr1, arr2, arr3, arr4};
					if(check_key(key))
						check_hash(key);
				}

	return 0;
}