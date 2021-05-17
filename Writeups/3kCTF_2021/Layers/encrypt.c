uint Sbox[] = 
{
	0x3, 0x8, 0xf, 0x1, 0xa, 0x6, 0x5, 0xb, 0xe, 0xd, 0x4, 0x2, 0x7, 0x0, 0x9, 0xc,
	0xf, 0xc, 0x2, 0x7, 0x9, 0x0, 0x5, 0xa, 0x1, 0xb, 0xe, 0x8, 0x6, 0xd, 0x3, 0x4,
	0x8, 0x6, 0x7, 0x9, 0x3, 0xc, 0xa, 0xf, 0xd, 0x1, 0xe, 0x4, 0x0, 0xb, 0x5, 0x2,
	0x0, 0xf, 0xb, 0x8, 0xc, 0x9, 0x6, 0x3, 0xd, 0x1, 0x2, 0x4, 0xa, 0x7, 0x5, 0xe,
	0x1, 0xf, 0x8, 0x3, 0xc, 0x0, 0xb, 0x6, 0x2, 0x5, 0x4, 0xa, 0x9, 0xe, 0x7, 0xd,
	0xf, 0x5, 0x2, 0xb, 0x4, 0xa, 0x9, 0xc, 0x0, 0x3, 0xe, 0x8, 0xd, 0x6, 0x7, 0x1,
	0x7, 0x2, 0xc, 0x5, 0x8, 0x4, 0x6, 0xb, 0xe, 0x9, 0x1, 0xf, 0xd, 0x3, 0xa, 0x0,
	0x1, 0xd, 0xf, 0x0, 0xe, 0x8, 0x2, 0xb, 0x7, 0x4, 0xc, 0xa, 0x9, 0x3, 0x5, 0x6,
};

uint32_t rotl(uint32_t a1, char a2)
{
	return (a1 >> (32 - a2)) | (a1 << a2);
}

void sub_403090(uint32_t buffer[132], uint32_t key[8], unsigned int len)
{
	uint32_t kbuff[140];
	uint32_t s[8];

	memset(s, 0, sizeof(s));
	memset(kbuff, 0, sizeof(kbuff));
	
	if(len != 0x20)
		exit(0);

	for(int b =0; b < 8; b++)
		s[b] = key[b];

	for(int e =0; e < 8; e++)
		kbuff[e] = s[e];

	for(int a = 8; a < 140; a++)
	{
		uint32_t x = kbuff[a-1] ^ kbuff[a-3] ^ kbuff[a-5] ^  kbuff[a-8] ^ 0x9e3779b9 ^ (a - 8);
		kbuff[a] = rotl(x, 11);
	}

	for(int d = 0; d < 0x21; d++)
	{
		uint32_t z = (0x23 - d) % 32;
		uint32_t k = 0;

		for(int f = 0; f < 32; f++)
		{
			uint32_t t1 = (((kbuff[d * 4 +  8]) >> f) & 0x1) << 0;
			uint32_t t2 = (((kbuff[d * 4 +  9]) >> f) & 0x1) << 1;
			uint32_t t3 = (((kbuff[d * 4 + 10]) >> f) & 0x1) << 2;
			uint32_t t4 = (((kbuff[d * 4 + 11]) >> f) & 0x1) << 3;
			uint32_t tmp = (t1 | t2 | t3 | t4);

			uint32_t k = Sbox[16 * (z % 8) + tmp];

			for(int j = 0; j < 4; j++)
			{
				buffer[4 * d + j] = (((k >> j) & 0x1) << f) | buffer[4 * d + j];
			}
		}
	}
}

void sub_403EC0(uint32_t inp[4], uint32_t key[8], uint32_t out[4], unsigned int len)
{
	uint32_t s[132];
	uint32_t sbuff[4];
	memset(s, 0, sizeof(s));
	sub_403090(s, key, len);

	memset(sbuff, 0, sizeof(sbuff));

	for(int a = 0; a < 32; a++)
	{
		for(int c = 0; c < 4; c++)
		{
			sbuff[c] = s[4 * a + c] ^ inp[c];
        	inp[c] = 0;
		}

		for(int b = 0; b < 32; b++)
		{
			uint32_t t1 = (((sbuff[0]) >> b) & 0x1) << 0;
			uint32_t t2 = (((sbuff[1]) >> b) & 0x1) << 1;
			uint32_t t3 = (((sbuff[2]) >> b) & 0x1) << 2;
			uint32_t t4 = (((sbuff[3]) >> b) & 0x1) << 3;
			uint32_t tmp = (t1 | t2 | t3 | t4);
			
			uint32_t y = Sbox[16 * (a % 8) + tmp];
			
			inp[0] |= ((y >> 0) & 0x1) << b;
			inp[1] |= ((y >> 1) & 0x1) << b;
			inp[2] |= ((y >> 2) & 0x1) << b;
			inp[3] |= ((y >> 3) & 0x1) << b;
		}

		if(a > 30)
		{
			inp[0] ^= s[128];
			inp[1] ^= s[129];
			inp[2] ^= s[130];
			inp[3] ^= s[131];
			break;
		}

		uint32_t a1 = inp[1] ^ rotl(inp[0], 13) ^ rotl(inp[2], 3);
		inp[1] = 	rotl(a1, 1);

		uint32_t a2 = inp[3] ^ rotl(inp[2],  3) ^ ((rotl(inp[0], 13)) << 3);
		inp[3] = 	rotl(a2,7);

		uint32_t a3 = inp[3] ^ rotl(inp[0], 13) ^ inp[1];
		inp[0] = 	rotl(a3, 5);

		uint32_t a4 = inp[3] ^ rotl(inp[2],  3) ^ (inp[1] << 7);
		inp[2] = 	rotl(a4 ,22);

	}

	for(int i=0; i<4; i++)
		out[i] = inp[i];
}

void sub_4008F0(uint32_t *data, uint32_t *key)
{
	uint32_t v8[2];

	v8[1] = data[0];
	v8[0] = data[1];
	uint32_t v6 = 0;

		for(int i = 32; i > 0; i--)
		{
			v6 -= 0x61C88647;// += 0x9E3779B9
			v8[1] += (key[1] + (v8[0] >> 5)) ^ (v6 + v8[0]) ^ ((v8[0] << 4) + key[0]);
			v8[0] += (key[3] + (v8[1] >> 5)) ^ (v6 + v8[1]) ^ ((v8[1] << 4) + key[2]);
		}
	data[0] = v8[1];
	data[1] = v8[0];
}

int main(int argc, char const *argv[])
{
	char v32[208];
	char v33[48];
	char flag[200];

	// Sum of chars of flag
	seed = sub_400E40(flag);
	srand(seed);

	for(int j =0; j < 32; j++)
		v33[j] = rand();
			
	ptr = malloc(32);
	v27 = 16 - (strlen(flag) & 0xF);

	// Padding
	for(int v26; v26 < v27; v26++)
		sprintf(flag, "%s%c", flag, v27)

	for(int v25 = 0; v25 < strlen(flag) / 16; v25++)
	{
		memset(ptr, 0, 0x20uLL);
		// Serpent Encryption
		sub_403EC0(&flag[16 * v25], v33, ptr, 0x20u);

		for(int v24 = 0; v24 < 0x10; v24++)
			v32[16 * v25 + v24] = ptr[v24];
	}

	memset(v23, 0, 0x09);
	memset(v22, 0, 0x11);
	memset(v21, 0, 0xC8);

	for(int v20 = 0; v20 < 0x10; v20++)
		v22[v20] = rand();
			
	for(int v19 = 0; v19 < strlen(v32) / 8; v19++)
	{
		memset(v23, 0, 0x08);
		__isoc99_sscanf(&v32[8 * v19], "%8s", v23);
		//TEA Encryption
		sub_4008F0(v23, v22);
		sprintf(v21, "%s%s", v21, v23);
	}

	// Check v21 with byte_606090
	byte_606090 = {0x47, 0xB9, 0x0B, 0x54, 0x7A, 0xC8, 0xE9, 0xEB, 0x81, 0xD5, 0x63, 0x67, 0x1D, 0x98, 0x3D, 0x6C, 0x8B, 0x89, 0x29, 0xC4, 0x8E, 0xAF, 0xE8, 0x6B, 0xAA, 0x91, 0xF6, 0xA7, 0xCF, 0x96, 0x13, 0x74, 0x65, 0xA3, 0x1B, 0x60, 0x74, 0xDB, 0x59, 0x94, 0xF6, 0x72, 0x4E, 0xB1, 0x08, 0x48, 0x97, 0xA0};
	for(k = 0; k < 48; k++)
		dword_6060C4 |= byte_606090[k] ^ v21[k];
}