from z3 import *
import binascii

# Parsed from dump
check_vals = [
	[4127179254, 4126139894,  665780030,  666819390],
	[1933881070, 2002783966, 1601724370, 1532821474],
	[4255576062, 3116543486, 3151668710, 4290701286],
	[1670347938, 4056898606, 2583645294,  197094626],
	[2720551936, 1627051272, 1627379644, 2720880308],
	[2307981054, 3415533530, 3281895882, 2174343406],
	[2673307092,  251771212,  251771212, 2673307092],
	[4139379682, 3602496994, 3606265306, 4143147994],
	[4192373742, 4088827598, 3015552726, 3119098870],
	[ 530288564,  530288564, 3917315412, 3917315412],
	[4025255646, 2813168974,  614968622, 1827055294],
	[3747612986, 1340672294, 1301225350, 3708166042],
	[3098492862, 3064954302, 3086875838, 3120414398],
	[2130820044, 2115580844, 2130523044, 2145762244]
]

sols = [BitVec(f'{i}', 32) for i in range(0xf)]
mem = [0]*12

s = Solver()

def solve():
	for i in range(0xf):
		arg = [0]*4
		arg[0] = sols[i]
		arg[1] = sols[(i + 1) % 14]
		arg[2] = sols[(i + 2) % 14]
		arg[3] = sols[(i + 3) % 14]

		s.add((arg[0] >>  0) & 0xff < 0x80)
		s.add((arg[0] >>  8) & 0xff < 0x80)
		s.add((arg[0] >> 16) & 0xff < 0x80)
		s.add((arg[0] >> 24) & 0xff < 0x80)

		mem[0] = arg[0]
		mem[1] = mem[0] ^ arg[1]
		mem[2] = mem[1] ^ arg[2]
		mem[3] = mem[2] ^ arg[3]

		mem[4] = mem[0] + mem[1] + mem[2] + mem[3]
		mem[5] = mem[0] - mem[1] + mem[2] - mem[3]
		mem[6] = mem[0] + mem[1] - mem[2] - mem[3]
		mem[7] = mem[0] - mem[1] - mem[2] + mem[3]

		mem[8]  = (mem[6] & mem[7]) ^ (mem[4] | mem[5])
		mem[9]  = (mem[7] & mem[4]) ^ (mem[5] | mem[6])
		mem[10] = (mem[4] & mem[5]) ^ (mem[6] | mem[7])
		mem[11] = (mem[5] & mem[6]) ^ (mem[7] | mem[4])

		s.add(Or(*[And(mem[8] == val[0], mem[9] == val[1], mem[10] == val[2], mem[11] == val[3]) for val in check_vals]))

print("[+] Adding Constraints")
solve()

s.add(sols[0] == 0x3072657a) # 0rez --> zer0 in little endian
s.add(sols[1] == 0x7b737470) # {stp --> pts{ in little endian

print("[+] Solving")

sat = s.check()
if str(sat) == "sat":
	flag = ""
	model = s.model()
	for i in range(13): # sols[13] = 0
		tmp = binascii.unhexlify(hex(int(str(model[sols[i]])))[2:]).decode()
		flag += tmp[::-1] # Converting from little endian
	print("[+] Flag Found >>>",flag)
else:
	print("[-] Flag not found :(")
	print(sat)