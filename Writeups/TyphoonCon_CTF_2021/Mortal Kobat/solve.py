def rol (value, count):
	return ((value << (count & 7)) | (value >> (-(count & 7) & 7))) & 0xFF

def ror (value, count):
	return ((value >> (count & 7)) | (value << (-(count & 7) & 7))) & 0xFF

r12b_data = [0x91, 0x0e, 0x4a, 0x75, 0x60, 0x45, 0x5b, 0xab, 0xa4, 0x04, 0xcf, 0xe5, 0x0e, 0x38, 0x4e, 0xb3, 0xb6, 0x83, 0x7b, 0x29, 0x6c, 0xce, 0x54, 0x0f, 0xf1, 0x6d, 0x67, 0xb4, 0x63, 0x59, 0x35, 0x66, 0xa4, 0xd3, 0x54, 0xd8, 0xd0, 0x37]

check = []

for i in r12b_data:
	check.append(rol(i,4) ^ 0x2c)

# print([hex(i)[2:].zfill(2) for i in check])

answer = ""


answer += chr(rol(check.pop(0) ,0x1c))
answer += chr(rol(check.pop(0) , 6 ^ 68))
answer += chr(ror(check.pop(0) , 0x15))
answer += chr(ror(check.pop(0) , 8))
answer += chr(rol(check.pop(0) , 0x25 ^ 68))
answer += chr(check.pop(0) ^ 0x10)
answer += chr(ror(check.pop(0) , 0x1b))
answer += chr(check.pop(0) - 0x24)
answer += chr(ror(check.pop(0) , 9))
answer += chr(check.pop(0) - 0xd)
answer += chr(rol(check.pop(0) ,0x16))
answer += chr(rol(check.pop(0) , 4 ^ 68))
answer += chr(ror(check.pop(0) , 3 ^ 65))
answer += chr(ror(check.pop(0) , 0x26 ^ 65))
answer += chr(ror(check.pop(0) , 4 ^ 65))
answer += chr(check.pop(0) ^ 0x23)
answer += chr(rol(check.pop(0) , 0x18 ^ 68))
answer += chr(check.pop(0) ^ 0x27)
answer += chr(rol(check.pop(0) ,0xd))
answer += chr(rol(check.pop(0) ,0x17))
answer += chr(ror(check.pop(0) , 4 ^ 65))
answer += chr(rol(check.pop(0) ,0x26))
answer += chr(check.pop(0) ^ 0x1b)
answer += chr(rol(check.pop(0) ,0x22))
answer += chr(rol(check.pop(0) ,0x14))
answer += chr(ror(check.pop(0) , 0x22 ^ 65))
answer += chr(check.pop(0) - 6)
answer += chr(check.pop(0) ^ 0xf)
answer += chr(rol(check.pop(0) , 0x1d ^ 68))
answer += chr(ror(check.pop(0) , 0x12))
answer += chr(check.pop(0) - 0x20)
answer += chr(check.pop(0) - 6)
answer += chr(rol(check.pop(0) , 0x13 ^ 68))
answer += chr(check.pop(0) ^ 0x25)
answer += chr(check.pop(0) ^ 0x1d)
answer += chr(rol(check.pop(0) , 0x12 ^ 68))
answer += chr(rol(check.pop(0) ,0x10))
answer += chr(rol(check.pop(0) ,0xa))

print(answer)