file = open("gdb_output3.txt").readlines() 

data = []
for i in file:
	x = int(i.strip(), 16)
	data.append(x)

# print([hex(x) for x in data])

for i in data:
	if(i == 0x9606678c):
		print("""
++a;
		""")
		continue

	if(i == 0x9aeeb6ef):
		print("""
++b;
		""")
		continue

	if(i == 0x9d018ad3):
		print("""
s[c] = sbuf[c];
		""")
		continue

	if(i == 0x9ed567c1):
		print("""
d = 0;
		""")
		continue

	if(i == 0xa9b955db):
		print("""
_a3 == 0
		""")
		continue

	if(i == 0xab353f6f):
		print("""
*((_BYTE *)sbuf + g) = *((_BYTE *)_a2 + g);
		""")
		continue

	if(i == 0xac6e0e08):
		print("""
JMP 0x1cd6c9c1
		""")
		continue

	if(i == 0xb52c03b2):
		print("""
JMP 0x1e2db7b4
		""")
		continue

	if(i == 0xc04417e3):
		print("""
++e;
		""")
		continue

	if(i == 0xc20feffc):
		print("""
*((_BYTE *)sbuf + _h) = 1;
c = 0;
		""")
		continue

	if(i == 0xc3734aac):
		print("""
JMP 0xb52c03b2
		""")
		continue

	if(i == 0xc5de43b8):
		print("""
_a4 < 0x20
		""")
		continue

	if(i == 0xc8900ac5):
		print("""
local_2dc = (0x23 - d) % 32;
k = 0;
f = 0;
		""")
		continue

	if(i == 0xd35b09a7):
		print("""
memset(sbuf,0,0x20);
_h = _a4;
g = 0;
		""")
		continue

	if(i == 0xd5c4f2a6):
		print("""
uVar2 = kbuff[a + -5] & (kbuff[a + -8] ^ 0xffffffff) | kbuff[a + -8] & (kbuff[a + -5] ^ 0xffffffff);
uVar2 = ((uVar2 ^ 0xffffffff) & 0x13a60e9a | uVar2 & 0xec59f165) ^ ((kbuff[a + -3] ^ 0xffffffff) & 0x13a60e9a | kbuff[a + -3] & 0xec59f165);
uVar2 = kbuff[a + -1] & (uVar2 ^ 0xffffffff) | uVar2 & (kbuff[a + -1] ^ 0xffffffff);
uVar2 = (uVar2 ^ 0xffffffff) & 0x33d85ff0 | uVar2 & 0xcc27a00f;
uVar2 = FUN_00402490(((uVar2 ^ 0x5210d9b6) & 0x5fa4275f | (uVar2 ^ 0xadef2649) & 0xa05bd8a0) ^ ((a - 8U ^ 0xffffffff) & 0x5fa4275f | a - 8U & 0xa05bd8a0),0xb);
kbuff[a] = uVar2;
		""")
		continue

	if(i == 0xdcdb893a):
		print("""
JMP 0x1e2db7b4
		""")
		continue

	if(i == 0xe07f4afd):
		print("""
b = 0;
		""")
		continue

	if(i ==0xe1928e6d):
		print("""
v23 = ((k >> j) & ((k >> j) ^ 0xFFFFFFFE)) << f;
_a1[4 * d + j] = v23 ^ _a1[4 * d + j] | v23 & _a1[4 * d + j];
		""")
		continue

	if(i == 0xe95ac0ce):
		print("""
a < 0x8c;
		""")
		continue

	if(i == 0xedcfb4af):
		print("""
++j;
		""")
		continue

	if(i == 0xfbd35fed):
		print("""
e < 8;
		""")
		continue

	if(i == 0x122e3189):
		print("""
c < 8;
		""")
		continue

	if(i == 0x1cd6c9c1):
		print("""
++f;
		""")
		continue

	if(i == 0x1e2db7b4):
		print("""
e = 0;
		""")
		continue

	if(i == 0x266844ec):
		print("""
d < 0x21;
		""")
		continue

	if(i == 0x2dc162eb):
		print("""
JMP 0x7e2e7a9e
		""")
		continue

	if(i == 0x2e8b62e9):
		print("""
_a4 == 0x20
		""")
		continue

	if(i == 0x2ecffa35):
		print("""
++c;
		""")
		continue

	if(i == 0x355ce5db):
		print("""
f < 0x20;
		""")
		continue

	if(i == 0x4f5a98fa):
		print("""
kbuff[e] = s[e]
		""")
		continue

	if(i == 0x521305bc):
		print("""
a = 8;
		""")
		continue

	if(i == 0x5d8f0b74):
		print("""
b < 8;
		""")
		continue

	if(i == 0x67b26225):
		print("""
j < 4;
		""")
		continue

	if(i == 0x68961212):
		print("""
++g;
		""")
		continue

	if(i == 0x718c2a8a):
		print("""
uVar2 = (kbuff[d * 4 + 8] >> (bVar1 & 0x1f) ^ 0xffffffff | 0xfffffffe) ^ 0xffffffff;
uVar3 = kbuff[-(d * -4 + -9)] >> (bVar1 & 0x1f);
uVar3 = ((uVar3 ^ 0xfffffffe) & uVar3) << 1;
uVar3 = uVar2 & uVar3 | uVar2 ^ uVar3;
uVar2 = kbuff[d * 4 + 10] >> (bVar1 & 0x1f);
uVar6 = ((uVar2 ^ 0xfffffffe) & uVar2) << 2;
uVar2 = uVar3 ^ 0xffffffff;
uVar4 = uVar6 ^ 0xffffffff;
uVar3 = (uVar2 & 0xb467f51e | uVar3 & 0x4b980ae1) ^ (uVar4 & 0xb467f51e | uVar6 & 0x4b980ae1) | (uVar2 | uVar4) ^ 0xffffffff;
uVar2 = ((kbuff[d * 4 + 0xb] >> (bVar1 & 0x1f) ^ 0xffffffff | 0xfffffffe) ^ 0xffffffff) << 3;
uVar4 = uVar3 ^ 0xffffffff;
uVar6 = uVar2 ^ 0xffffffff;
k = (char)UINT_ARRAY_006060d0[(long)(local_2dc % 8) * 0x10 + (ulong)((uVar4 & 0xf52b2fa0 | uVar3 & 0xad4d05f) ^ (uVar6 & 0xf52b2fa0 | uVar2 & 0xad4d05f) | (uVar4 | uVar6) ^ 0xffffffff)];
j = 0
		""")
		continue

	if(i == 0x7afa98d4):
		print("""
g < _h;
		""")
		continue

	if(i == 0x7e2e7a9e):
		print("""
++d;
		""")
		continue

	if(i == 0x7ee39471):
		print("""
s[b] = _a2[b];
		""")
		continue

	# if(i == 0x2f508473):
	# 	break

	print("ERR", hex(i))