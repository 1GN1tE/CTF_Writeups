#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

void multiply(int F[2][2], int M[2][2]);
 
void power(int F[2][2], int n);
 
/* function that returns nth Fibonacci number */
int fib(int n)
{
  int F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}
 
/* Optimized version of power() in method 4 */
void power(int F[2][2], int n)
{
  if( n == 0 || n == 1)
      return;
  int M[2][2] = {{1,1},{1,0}};
 
  power(F, n/2);
  multiply(F, F);
 
  if (n%2 != 0)
     multiply(F, M);
}
 
void multiply(int F[2][2], int M[2][2])
{
  int x =  F[0][0]*M[0][0] + F[0][1]*M[1][0];
  int y =  F[0][0]*M[0][1] + F[0][1]*M[1][1];
  int z =  F[1][0]*M[0][0] + F[1][1]*M[1][0];
  int w =  F[1][0]*M[0][1] + F[1][1]*M[1][1];
 
  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}

int rxor(int x)
{
	int z = 0;
	while(x > 0)
	{
		int y = x % 10;
		z ^= y;
		x /= 10;
	}

	return z;
}

void fenc(uint8_t *enc, uint8_t *dec, int x)
{
	int t = fib(x);
	uint8_t a = enc[x] ^ t;
	int z = rxor(t);
	uint8_t b = (z ^ a) & 0xFF;
	dec[x] = b;
}

int main(int argc, char const *argv[])
{
	uint8_t enc[] = {0x66, 0x6c, 0x61, 0x67, 0x20, 0x3a, 0x20, 0x75, 0x7e, 0x16, 0x45, 0x68, 0xea, 0xd2, 0x4c, 0x52, 0xbc, 0x05, 0x20, 0x60, 0x5d, 0xff, 0x4a, 0xcc, 0x18, 0x20, 0x5b, 0x76, 0x1b, 0x89, 0x1d, 0xb5, 0x34, 0x89, 0xd1, 0xf2, 0xde, 0x14, 0x1b, 0x91, 0xab, 0x53, 0x47};
	uint8_t dec[0x30];

	memset(dec, 0 , 0x30);
	for(int i = 0; i < 0x2b; i++)
		fenc(enc,dec,i);

	printf("%s\n", dec);
	return 0;
}