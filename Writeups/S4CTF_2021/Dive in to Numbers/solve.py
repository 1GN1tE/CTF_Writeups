from Crypto.Util.number import long_to_bytes

with open("wtflag_enc", "rb") as f:
	data = f.read()

data1, data2 = data.split(b'SSSS')

out_1 = int(data1.hex()[:-1], 16) # 0 pad
out_2 = int(data2.hex(), 16)

x = 3*(2*out_2-out_1) // 7
y = 3*(4*out_1-out_2) // 7

ystr = str(y + 256 - (y%256)) # the last byte is null due to padding

for i in range(x-256, x+256):
	res = int(str(i)+str(ystr))
	if b"S4CTF" in long_to_bytes(res):
		print(long_to_bytes(res).strip(b"\x00").decode())