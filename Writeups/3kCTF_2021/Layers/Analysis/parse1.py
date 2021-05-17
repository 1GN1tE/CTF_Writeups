file = open("gdb_output1.txt").readlines() 

data = []
for i in file:
	x = int(i.strip(), 16)
	data.append(x)

# print([hex(x) for x in data])

for i in data:
	if(i == 0x8130ed43):
		print("""
memset(v23, 0, sizeof(v23));
memset(v22, 0, 0x11uLL);
memset(v21, 0, 0xC8uLL);
v20 = 0;
		""")
		continue

	if(i == 0x84a7f436):
		print("""
v19 = 0;
		""")
		continue

	if(i == 0x8f6aeccf):
		print("""
v22[v20] = rand();
		""")
		continue

	if(i == 0x93689926):
		print("""
x = 0x84a7f436;
if (v20 < 0x10) {
	x = 0x8f6aeccf;
		""")
		continue

	if(i == 0x9e00e14a):
		print("""
++v24;
		""")
		continue

	if(i == 0xa026f981):
		print("""
++j;
		""")
		continue

	if(i == 0xad9286f4):
		print("""
memset(ptr, 0, 0x20uLL);
sub_403EC0((__int64)&flag[16 * v25], (__int64)v33, ptr, 0x20u);
v24 = 0;
		""")
		continue


	if(i == 0xae672971):
		print("""
*v31 = 0;
		""")
		continue


	if(i == 0xb9048286):
		print("""
x = 0xf436e04e;
if (j < 0x20)
	x = 0x13f8f8b8;
		""")
		continue

	if(i == 0xbd66d1c0):
		print("""
v32[16 * v25 + v24] = ptr[v24];
		""")
		continue

	if(i == 0xcbd7742f):
		print("""
++v19;
		""")
		continue

	if(i == 0xcedbc306):
		print("""
++v20;
		""")
		continue

	if(i == 0xda5a3c78):
		print("""
v26 = v26 + 1;
		""")
		continue

	if(i == 0xe3a80132):
		print("""
x = 0x263f9e70;
		""")
		continue

	if(i == 0xeb90905d):
		print("""
++v18;
		""")
		continue

	if(i == 0xee3fa927):
		print("""
sprintf(flag, "%s%c", flag, (unsigned int)(char)v27)
		""")
		continue

	if(i == 0xf2cab7b8):
		print("""
local_1f4 = FUN_00400e40((char *)flag);
srand(local_1f4);
j = 0;
		""")
		continue

	if(i == 0xf436e04e):
		print("""
ptr = malloc(0x20uLL);
v27 = 16 - (strlen(flag) & 0xF);
v26 = 0;
		""")
		continue

	if(i == 0xf8f2b980):
		print("""
if (0x28 < strlen(flag))
	x = 0x4119dfe7;
		""")
		continue

	if(i == 0x7f83fb5):
		print("""
x = 0xf8f2b980;
if (local_10 != 0)
	x = 0xae672971;	
		""")
		continue

	if(i == 0x1238a7cd):
		print("""
v16 = v25;
v8 = strlen(flag);
x = 0x8130ED43;
if ( v16 < v8 >> 4 )
	x = 0xAD9286F4;
		""")
		continue

	if(i == 0x13f8f8b8):
		print("""
v33[j] = rand();
		""")
		continue

	if(i == 0x140af898):
		print("""
memset(v23, 0, 8uLL);
__isoc99_sscanf(&v32[8 * v19], "%8s", v23);
sub_4008F0(v23, v22);
sprintf(v21, "%s%s", v21, v23);
		""")
		continue

	if(i == 0x263f9e70):
		print("""
++v25;	
		""")
		continue

	if(i == 0x28b41c13):
		print("""
x = 0x68b9f247;
if (v26 < v27)
	x = 0xee3fa927;
		""")
		continue

	if(i == 0x325b57d6):
		print("""
v12 = strlen(v32);
x = 0x41DBA672;
if ( v19 < v12 >> 3 )
	x = 0x140AF898;	
		""")
		continue

	if(i == 0x36b7a523):
		print("""
v15 = byte_606090[v18] & 0xC3593BAB | ~byte_606090[v18] & 0x3CA6C454;
dword_6060C4 = ~(v15 ^ (v21[v18] & 0xC3593BAB | ~v21[v18] & 0x3CA6C454)) & dword_6060C4 | ~dword_6060C4 & (v15 ^ (v21[v18] & 0xC3593BAB | ~v21[v18] & 0x3CA6C454));
		""")
		continue

	if(i == 0x379d135e):
		print("""
x = 0xe3a80132;
if (v24 < 0x10)
	x = 0xbd66d1c0;
		""")
		continue

	if(i == 0x4119dfe7):
		print("""
DAT_006060c4 = rand() % 255 + 1;
		""")
		continue

	if(i == 0x41dba672):
		print("""
v18 = 0;
		""")
		continue

	if(i == 0x68b9f247):
		print("""
v25 = 0;
		""")
		continue

	if(i == 0x6c6e9fb7):
		print("""
x = 0x15223c70;
if (v18 < 48)
	x = 0x36b7a523;		
		""")
		continue

	if(i == 0x15223C70):
		break

	print("ERR", hex(i))