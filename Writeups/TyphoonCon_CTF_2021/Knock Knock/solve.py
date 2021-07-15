def rol (value, count):
	return ((value << (count & 7)) | (value >> (-(count & 7) & 7))) & 0xFF

buffer = [0xB3, 0x9C, 0x98, 0x36, 0x29, 0x37, 0xA8, 0xAA, 0x9B, 0xB0, 0x9A, 0xB6]

data = ""

for i in buffer:
	data += chr(rol(i,1))

key1 = b'\xAA\xBB\xCC\xDD'
data1 = b'\xB4\x29\x00\xEB\x36\xB5\x8F\xD2\xDA\x6A\x8A\x5D'
data += "bXs4aVck494y" # RC4 decrypted

key2 = b'\xA2\x34\xFA\x37\x12\xEC\x5B\xA3'
data2 = b'\x2E\x07\x67\xF3\xCC\x50\xB8\x9C\x50\xDD\x92\xD6\x1E\x9B\x17\xE5'
data += "FJ3xs3o8" # http://des.online-domain-tools.com/

print(data)