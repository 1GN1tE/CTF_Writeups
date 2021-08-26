from idaapi import *
from capstone import *

address= [0x4435]
size = 0x1D
flag = ""
a = 0

while '}' not in flag:
	addr = address[a]
	data = get_bytes(addr, size)
	x = data[0] ^ 0x48
	new = []
	for i in range(len(data)):
		new.append(data[i] ^ x)

	# print([hex(i)[2:].zfill(2) for i in new])


	CODE = bytes(new)
	rip = addr+7

	md = Cs(CS_ARCH_X86, CS_MODE_64)
	for i in md.disasm(CODE, 0x1000):
		assert "lea" in i.mnemonic
		opc = i.op_str
		break

	new_rip = eval(opc.split(", ")[1])[0]
	# print(hex(new_rip))
	address.append(new_rip)

	a+=1
	flag+= chr(x)

print(flag)
