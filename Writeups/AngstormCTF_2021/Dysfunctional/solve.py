SBox = [] 
import struct

with open ("SBox","rb") as f:
	tmp = f.read()

for i in range(0,len(tmp)-2,2):
	SBox.append(int(struct.unpack('<H',tmp[i:i+2])[0]))
assert len(SBox) == len(set(SBox))

Sbox_inv = [0]*65536
for i in range(65535):
	Sbox_inv[SBox[i]] = i


def inv_func1(inp):
	result = inp ^ 0xDEAD
	tmp1 = Sbox_inv[result & 0xFFFF]
	tmp2 = Sbox_inv[result >> 16]

	tmp1 ^= 0xBEEF
	tmp2 ^= 0xBEEF

	result = tmp1 | (tmp2 << 16)
	return result

def inv_func2(inp):
	result = inp ^ 0x1337
	tmp1 = Sbox_inv[result & 0xFFFF]
	tmp2 = Sbox_inv[result >> 16]

	tmp1 ^= 0xCAFE
	tmp2 ^= 0xCAFE

	result = tmp1 | (tmp2 << 16)
	return result

def comp1(inp):
	return inv_func1(inv_func2(inp))

def comp2(inp):
	return inv_func2(inv_func1(inp))

flag = ""
enc_flag = [0x5400f172, 0x949c5165, 0xc6bc4607, 0xc621d63f, 0xc20c0970, 0xf2b3f53c, 0xaabb67f9, 0xfe0e7abb, 0x6ae46e55, 0xdd212d25, 0xfb681ccb, 0x2ef2f900, 0x75dbefc4, 0xa4e3a8dd, 0x3c6ad4ea, 0x2fa95919, 0x4e6d7b44, 0xb66bacf2, 0xa0b7b0a3, 0xee57fd81, 0x452a0ba4, 0xa05d8829, 0x5911680, 0x439efce, 0x75346c63, 0xe2e8d40c, 0x82551eb7, 0x15f70f1, 0x3365c553, 0x4d88f5f1, 0x1ea5b8ab, 0xfaa1a4ae, 0x91567996, 0x13d89930, 0x6b159c81, 0x35779a3c, 0x5d8573aa, 0x75908ec, 0xb902a84, 0x1501d8a0]

for i in enc_flag:
	flag += chr((comp1(comp2(i))) & 0xFF)

print(flag)