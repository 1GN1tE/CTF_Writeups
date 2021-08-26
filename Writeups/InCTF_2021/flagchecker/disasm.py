from struct import pack,unpack

contents = open("flagchecker","rb").read()

buffer = contents[0x2920:0x6520]

data = []

for i in range(0,len(buffer)-4,4):
	data.append(unpack("<I", buffer[i:i+4])[0])

# print(data)

def get_data(fmt, x):
	return (fmt % data[x+1])


opcodes = {
	1  : [1, "x = weird_data[z]", None],
	2  : [1, "puts(\"Checking flag...\");", None],
	3  : [2, "z = %d", get_data],
	4  : [1, "z = 0x(z)", None],
	5  : [1, "++z", None],
	6  : [2, "x = flag[%d]", get_data],
	7  : [1, "z = x", None],
	8  : [2, "unkn[%d] = x", get_data],
	9  : [1, "Weird Check", None],
	10 : [1, "if (weird_data[z] != qword_206538[c++]) [!]Error", None],
	11 : [2, "if (x %% 9 != %d) [!]Error", get_data],
	12 : [1, "putchar(weird_data[z + y]);", None],
}

ip = 0

while(ip < len(data)):
	opc = data[ip]
	print("0x"+hex(ip)[2:].zfill(3), end="\t")

	if opc not in opcodes:
		ip += 1
		print("[!]", opc)
		continue

	if opcodes[opc][2] is None:
		desc = opcodes[opc][1]
	else:
		desc = opcodes[opc][2](opcodes[opc][1], ip)
	print(desc)
	ip += opcodes[opc][0]
