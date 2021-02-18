import base64
vals = [0xA884DF8AB2FBC902, 0xE0D28ACBFB46461A, 0x6178F0BE4CD508AC, 0x603AD81291B66724, 0xDE5CDDE19279A148, 0x70E60361F80E8EB4]

to_xor = [0xD8BDEEE9C2938E66, 0xD598D291C97F7779, 0x0D32C3E736983BF4, 0x0C428F73FC8F2140, 0xA419A7AFE834F505, 0x4DAB6D008D6DF4F9]

def xor(a,b):
	c = 0
	for i in range(8):
		tmp1 = (a >> 8*i) & 0xFF
		tmp2 = (b >> 8*i) & 0xFF
		tmp3 = (tmp1 ^ tmp2)
		c = (c << 8) | tmp3
	return c

to_dec = b""
for i in range(6):
	tmp = hex(xor(vals[i],to_xor[i]))[2:]
	to_dec += bytes.fromhex(tmp)

print(base64.b64decode(to_dec).decode())