from pwn import *
from ctypes import CDLL
libc = CDLL("libc.so.6")

def rand_func(inp):
	libc.srand(inp ^ 0xBC614E)
	sum = 0
	for i in range(8):
		sum = (libc.rand() % 10) + (10 * sum)
	return (inp * sum) & 0xFFFFFFFFFFFFFFFF

# p = remote("0.0.0.0", 21450)
p = remote("rev.2021.chall.actf.co", 21450)

check_number = 0x13371337
flag = ""
printable = "actf{}!_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789bdeghijklmnopqrsuvwxyz"
x = 0

rands = []
for i in range(0xD):
	rands.append(p.recv(1))

log.info("Getting Rand Data")
rand_xor = [0xde, 0xad, 0xbe, 0xef, 0xfe, 0xed, 0xca, 0xfe, 0x13, 0x37, 0xab, 0xcd, 0xef]
for i in range(0xD):
	rands[i] = int.from_bytes(rands[i], "little") ^ rand_xor[i]

log.info("Bruteforcing flags")
while '}' not in flag:
	p.send((rand_func(check_number)).to_bytes(8, byteorder='little'))

	# log.info(printable[x])
	p.send(printable[x]) # Flag Byte

	for i in range(0xD):
		p.send((rands[i]).to_bytes(1, byteorder='little'))

	check = p.recv(1).decode()
	if (check == '%'):
		flag += printable[x]
		x = 0
		print("FLAG",flag)
		check_number = 0
		for i in range(4):
			tmp = p.recv(1)
			check_number = (check_number << 8) + int.from_bytes(tmp, "little")
	else:
		x += 1
