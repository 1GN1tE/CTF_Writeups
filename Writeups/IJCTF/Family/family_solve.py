data = open("family","rb").read()

dump1 = list(data[0x2020:0x2020+0x29])
dump2 = list(data[0x2060:0x2060+0x29])
dump3 = list(data[0x20A0:0x20A0+0x29])
dump4 = list(data[0x20E0:0x20E0+0x29])

ans = ""

for i in range(0x29):
	for c in range(256):
		z = c
		c ^= dump2[i]
		c = (c + dump1[i]) & 0xFF
		c = (c - dump3[i]) & 0xFF
		if c == dump4[i]:
			ans += chr(z)
			break

print(ans)