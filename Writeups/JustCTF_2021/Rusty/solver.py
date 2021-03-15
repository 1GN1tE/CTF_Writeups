from z3 import *
flag_len = 0x37
flag_chars = [BitVec(f'{i}', 8) for i in range(flag_len)]
s = Solver()

for i in range(flag_len):
	s.add(flag_chars[i]>30)
	# s.add(flag_chars[i]<127)

s.add(flag_chars[0]==ord('j'))
s.add(flag_chars[1]==ord('c'))
s.add(flag_chars[2]==ord('t'))
s.add(flag_chars[3]==ord('f'))
s.add(flag_chars[4]==ord('{'))
s.add(flag_chars[0x36]==ord('}'))

chk_vals = [0x145, 0x144, 0x13B, 0x11B, 0x0FB, 0x0FB, 0x120, 0x13C, 0x151, 0x142, 0x147, 0x13B, 0x141, 0x12C, 0x140, 0x119, 0x119, 0x116, 0x147, 0x15D, 0x143, 0x135, 0x132, 0x138, 0x136, 0x130, 0x13A, 0x14A, 0x149, 0x143, 0x142, 0x13E, 0x134, 0x0FA, 0x0F2, 0x0D9, 0x0E6, 0x0D2, 0x0D1, 0x0D6, 0x0D7, 0x0D3, 0x0D4, 0x0A9, 0x089, 0x063, 0x063, 0x0BF, 0x108, 0x14A]
for i in range(7,flag_len):
	s.add((flag_chars[(i-2)%flag_len]+flag_chars[(i-1)%flag_len]+flag_chars[(i-0)%flag_len]) == chk_vals[i-7])

sat = s.check()
if str(sat) == "sat":
	model = s.model()
	# print(model)
	flag = [chr(int(str(model[flag_chars[i]]))) for i in range(len(model))]
	print("".join(flag))
else:
	print(sat)
