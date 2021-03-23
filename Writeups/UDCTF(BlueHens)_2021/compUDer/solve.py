from pwn import *

"""
OPC  Out  a  b
--------------
0    x    a  b ; stack[x] = stack[a] + stack[b]
1    x    a  b ; stack[x] = stack[a] - stack[b]
2    x    a  b ; stack[x] = stack[a] * stack[b]
3    x    a  b ; stack[x] = stack[a] & stack[b]
4    x    a  b ; stack[x] = stack[a] | stack[b]
5    x    a  b ; stack[x] = arr_flag[stack[a]]
6    x    a  b ; arr_flag[stack[x]] = stack[a]
7    x    a  b ; exit VM

# STACK #
0x00000000 | 0
0x00000000 | 1
0x00000000 | 2
0x00000000 | 3
0x00000000 | 4
0x00000001 | 5

arr_flag = [0x00000000, 0x00000001, 0x00000001, 0x00000002, 0x00000003, 0x00000005, 0x00000008, 0x0000000d, 0x00000015, 0x00000022, 0x00000037, 0x00000059, 0x00000090, 0x000000e9, 0x00000179, 0x00000262, 0x000003db, 0x0000063d, 0x00000a18, 0x00001055, 0x00001a6d, 0x00002ac2, 0x0000452f, 0x00006ff1, 0x0000b520, 0x00012511, 0x0001da31, 0x0002ff42, 0x0004d973, 0x0007d8b5, 0x000cb228, 0x00148add, 0x00213d05]
66
# TODO #
l = len(arr_flag)
for i in range(l):
	arr_flag[33+i] = arr_flag[i]
"""

# p = process("./vm.out")
p = remote("challenges.ctfd.io", 30525)
p.recvuntil(b"$ ").decode()

log.info("Init [i]")
## Init Value stack[0]
p.sendline("0")
p.sendline("0")
p.sendline("5")
p.sendline("5")

## stack[0] = 0x20
for i in range(4):
	p.sendline("0")
	p.sendline("0")
	p.sendline("0")
	p.sendline("0")

## stack[0] = 0x21
p.sendline("0")
p.sendline("0")
p.sendline("0")
p.sendline("5")

log.info("Set arr_flag[i]")

for i in range(33):
	# Clear stack[4] for arr_flag[x]
	p.sendline("1")
	p.sendline("4")
	p.sendline("4")
	p.sendline("4")
	# Talking value from arr_flag[i]
	p.sendline("5")
	p.sendline("4")
	p.sendline("3")
	p.sendline("0")
	# Adding value to arr_flag[33+i]
	p.sendline("6")
	p.sendline("0")
	p.sendline("4")
	p.sendline("0")
	# Inc [33+i]
	p.sendline("0")
	p.sendline("3")
	p.sendline("3")
	p.sendline("5")
	# Inc [i]
	p.sendline("0")
	p.sendline("0")
	p.sendline("0")
	p.sendline("5")

# Exit
p.sendline("7")
p.sendline("0")
p.sendline("0")
p.sendline("0")

print("FLAG!!! ", p.recvline().decode())