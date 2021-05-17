file = open("gdb_output2.txt").readlines() 

data = []
for i in file:
	x = int(i.strip(), 16)
	data.append(x)

# print([hex(x) for x in data])

for i in data:
	if(i == 0xA57D3848):
		print("""
v7 = 2 * ((sbuff[1] >> b) & ((sbuff[1] >> b) ^ 0xFFFFFFFE));
v8 = v7 ^ ~(~(sbuff[0] >> b) | 0xFFFFFFFE) | v7 & ~(~(sbuff[0] >> b) | 0xFFFFFFFE);
v9 = 8 * ~(~(sbuff[3] >> b) | 0xFFFFFFFE);
y = dword_6060D0[16 * (__int64)(a % 8) + (v9 ^ (~(~(4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) | ~v8) | ((4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) & 0xCDD5AD00 | ~(4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) & 0x322A52FF) ^ (v8 & 0xCDD5AD00 | ~v8 & 0x322A52FF)) | v9 & (~(~(4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) | ~v8) | ((4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) & 0xCDD5AD00 | ~(4 * ((sbuff[2] >> b) & ((sbuff[2] >> b) ^ 0xFFFFFFFE))) & 0x322A52FF) ^ (v8 & 0xCDD5AD00 | ~v8 & 0x322A52FF)))];
*inp = ((y & (y ^ 0xFFFFFFFE)) << b) ^ *inp | ((y & (y ^ 0xFFFFFFFE)) << b) & *inp;
inp[1] = ~(~(~(~(y >> 1) | 0xFFFFFFFE) << b) | ~inp[1]) | ((~(~(y >> 1) | 0xFFFFFFFE) << b) & 0x7803551A | ~(~(~(y >> 1) | 0xFFFFFFFE) << b) & 0x87FCAAE5) ^ (inp[1] & 0x7803551A | ~inp[1] & 0x87FCAAE5);
inp[2] = ~(~(~(~(y >> 2) | 0xFFFFFFFE) << b) | ~inp[2]) | ((~(~(y >> 2) | 0xFFFFFFFE) << b) & 0x37C44B3F | ~(~(~(y >> 2) | 0xFFFFFFFE) << b) & 0xC83BB4C0) ^ (inp[2] & 0x37C44B3F | ~inp[2] & 0xC83BB4C0);
inp[3] = ~(~(((y >> 3) & ((y >> 3) ^ 0xFFFFFFFE)) << b) | ~inp[3]) | ((((y >> 3) & ((y >> 3) ^ 0xFFFFFFFE)) << b) & 0xF55F1E17 | ~(((y >> 3) & ((y >> 3) ^ 0xFFFFFFFE)) << b) & 0xAA0E1E8) ^ (inp[3] & 0xF55F1E17 | ~inp[3] & 0xAA0E1E8);
		""")
		continue

	if(i == 0xA5AA2438):
		print("""
++b;
		""")
		continue

	if(i == 0xBD3CC7E5):
		print("""
c = 0;
		""")
		continue

	if(i == 0xC69A2A67):
		print("""
(a < 32)
		""")
		continue

	if(i == 0xCF365A10):
		print("""
Jump
		""")
		continue

	if(i == 0xF100B3F1):
		print("""
c < 4
		""")
		continue

	if(i == 0xFCEC94E4):
		print("""
*inp = (z1 & 0x8CB35EFE | ~z1 & 0x734CA101) ^ (*inp & 0x8CB35EFE | ~*inp & 0x734CA101);
inp[1] = ~z2 & inp[1] | ~inp[1] & z2;
inp[2] = ~z3 & inp[2] | ~inp[2] & z3;
inp[3] = (z4 & 0x56423C3F | ~z4 & 0xA9BDC3C0) ^ (inp[3] & 0x56423C3F | ~inp[3] & 0xA9BDC3C0);
		""")
		continue

	if(i == 0x120F462B):
		print("""
++a;
		""")
		continue

	if(i == 0x2E78E25C):
		print("""
(a < 31)
		""")
		continue

	if(i == 0x39ABA8E6):
		print("""
(b < 32)
		""")
		continue

	if(i == 0x45DFAE8F):
		print("""
v24 = inp[1];
v11 = 		sub_402490(inp[0], 13);
v23 = v24 ^ v11;
v12 = 		sub_402490(inp[2], 3);
inp[1] = 	sub_402490(v12 ^ v23, 1);
v22 = inp[3];
v13 = 		sub_402490(inp[2], 3);
v21 = v22 ^ v13;
v14 = 		sub_402490(inp[0], 13);
inp[3] = 	sub_402490((v14 << 3) ^ v21,7);
v15 = 		sub_402490(inp[0], 13);
v16 = v15 ^ inp[1];
inp[0] = 	sub_402490(inp[3] ^ v16, 5);
v17 = 		sub_402490(inp[2], 3);
v18 = inp[3] ^ v17;
inp[2] = 	sub_402490((inp[1] << 7) ^ v18 ,22);
		""")
		continue

	if(i == 0x510340B5):
		print("""
sbuff[c] = ~*((_DWORD *)&s[a] + c) & inp[c] | ~inp[c] & *((_DWORD *)&s[a] + c);
inp[c] = 0;
		""")
		continue

	if(i == 0x5E778DDD):
		print("""
b = 0;
		""")
		continue

	if(i == 0x7e76b88e):
		print("""
++c;
		""")
		continue

	if(i == 0x6968BCED):
		break

	print("ERR", hex(i))