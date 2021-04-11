#include <stdio.h>
#include <stdlib.h> 

unsigned long long MurmurHash64A ( const void * key, int len, unsigned long long seed )
{
	const unsigned long long m = 0xc6a4a7935bd1e995;
	const int r = 47;

	unsigned long long h = seed ^ (len * m);

	const unsigned long long * data = (const unsigned long long *)key;
	const unsigned long long * end = data + (len/8);

	while(data != end)
	{
		unsigned long long k = *data++;

		k *= m; 
		k ^= k >> r; 
		k *= m; 
		
		h ^= k;
		h *= m; 
	}

	const unsigned char * data2 = (const unsigned char*)data;

	switch(len & 7)
	{
	case 7: h ^= (data2[6]) << 48;
	case 6: h ^= (data2[5]) << 40;
	case 5: h ^= (data2[4]) << 32;
	case 4: h ^= (data2[3]) << 24;
	case 3: h ^= (data2[2]) << 16;
	case 2: h ^= (data2[1]) << 8;
	case 1: h ^= (data2[0]);
			h *= m;
	};
 
	h ^= h >> r;
	h *= m;
	h ^= h >> r;

	return h;
}

int main(int argc, char const *argv[])
{
	unsigned long long enc[] = {0x188CF31A079D66FC, 0xA12C8AF2572DFA48, 0x1FF01EBC0C7408CB, 0xD58E3BA2FBEF9D8C, 0x5674B7653639CB87, 0x3EB8B6A6F0753E49, 0x1FF01EBC0C7408CB, 0xF9DFA617052DFD5E, 0x34514C558BA5E73B, 0xF9DFA617052DFD5E, 0x3A9C8840CEBAEA9E, 0xB13E0ECBEBA2478F, 0x827AEE59DF4BCCE8, 0x3A9C8840CEBAEA9E, 0xB13E0ECBEBA2478F, 0x827AEE59DF4BCCE8, 0x7641DBD6CD9D79AF, 0x7641DBD6CD9D79AF, 0x7641DBD6CD9D79AF};
	for(int x = 0; x <19; x++)
	{
		for(int i = 32; i<128; i++)
		{
			unsigned long long tmp = MurmurHash64A(&i,1,0x1337);
			if(enc[x] == tmp)
			{
				printf("%c",i);
				break;
			}
		}
	}
	printf("\n");
	return 0;
}