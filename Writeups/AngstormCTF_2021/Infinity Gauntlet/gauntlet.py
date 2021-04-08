from pwn import *
import re

p = remote("shell.actf.co", 21700)
# p = process("./infinity_gauntlet")

print(p.recvline().decode().strip())
print(p.recvline().decode().strip())

r1 = re.compile(r"foo\(([\w\?]+), ([\w\?]+)\) = ([\w\?]+)")
r2 = re.compile(r"bar\(([\w\?]+), ([\w\?]+), ([\w\?]+)\) = ([\w\?]+)")

buff = [0] * 26
i = 1
while 0 in buff:
	print(p.recvline().decode().strip())
	data = p.recvline().decode().strip()
	print(data)
	match1 = r1.match(data)
	match2 = r2.match(data)
	if(match1 != None):
		grp = match1.groups()
		if(grp[0]=='?'):
			ans = (int(grp[1]) + 1) ^ 1337 ^ int(grp[2])
		elif(grp[1]=='?'):
			ans = (int(grp[0]) ^ 1337 ^ int(grp[2])) - 1
		elif(grp[2]=='?'):
			ans = (int(grp[1]) + 1) ^ 1337 ^ int(grp[0])
	elif(match2 != None):
		grp = match2.groups()
		if(grp[0]=='?'):
			ans = int(grp[3]) - (int(grp[1]) * (int(grp[2]) + 1))
		elif(grp[1]=='?'):
			ans = (int(grp[3]) - int(grp[0])) // (int(grp[2]) + 1)
		elif(grp[2]=='?'):
			ans = ((int(grp[3]) - int(grp[0])) // int(grp[1])) - 1
		elif(grp[3]=='?'):
			ans = ((int(grp[2]) + 1) * int(grp[1])) + int(grp[0])
	else:
		log.error("Match Not Found", data)
		break

	p.sendline(str(ans))
	if (i > 49):
		pos = (ans >> 8) - i
		buff[pos] = ans & 0xFF
		print(buff)
	result = p.recvline().decode().strip()
	print(result)
	i += 1
	if "Correct!" not in result:
		exit()

c = 0
flag = ""
for i in buff:
	flag += chr((c ^ i) & 0xFF)
	c += 17

print(flag)