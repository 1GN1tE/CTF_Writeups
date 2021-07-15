from z3 import *
flag_len = 32
flag_chars = [BitVec(f'{i}', 16) for i in range(flag_len)] # Length of flag
s = Solver()

# for i in range(flag_len):
# 	s.add(flag_chars[i]>32)
# 	s.add(flag_chars[i]<126)

def func5(a,b,c):
	s.add(((a + b) / 2) == (c + 32))

def ror (value, count):
	return ((value >> (count & 7)) | (value << (-(count & 7) & 7))) & 0xFF

s.add(flag_chars[2880 - 2880] == 71)
s.add(flag_chars[2881 - 2880] == 70)
s.add(flag_chars[2882 - 2880] == 36)
s.add(flag_chars[2883 - 2880] == 56)
s.add(flag_chars[2911 - 2880] == 82)

func5(flag_chars[2889 - 2880], flag_chars[2907 - 2880], flag_chars[2881 - 2880])
func5(flag_chars[2894 - 2880], flag_chars[2898 - 2880], flag_chars[2911 - 2880])

s.add((flag_chars[2889 - 2880] - flag_chars[2898 - 2880]) == -12)
s.add((flag_chars[2907 - 2880] + flag_chars[2894 - 2880]) == 216)

s.add(flag_chars[2908 - 2880] == ror(233, 5))
s.add(flag_chars[2895 - 2880] == ror(178, 3))
s.add(flag_chars[2890 - 2880] == ror(155, 7))

s.add((flag_chars[8] - flag_chars[7]) ==   9)
s.add((flag_chars[7] - flag_chars[6]) ==  54)
s.add((flag_chars[6] - flag_chars[5]) ==  19)
s.add((flag_chars[5] - flag_chars[4]) == -41)
s.add((flag_chars[4] - flag_chars[3]) ==  18)

s.add(flag_chars[11] == ord("9"))
s.add(flag_chars[12] == ord("O"))
s.add(flag_chars[13] == ord("n"))

s.add((flag_chars[2896 - 2880] & flag_chars[2897 - 2880]) ==  53)
s.add((flag_chars[2897 - 2880] - flag_chars[2909 - 2880]) == -15)
s.add((flag_chars[2909 - 2880] | flag_chars[2910 - 2880]) == 116)
s.add((flag_chars[2910 - 2880] + flag_chars[2896 - 2880]) == 107)

s.add(flag_chars[19] == ((184 - 1) ^ 222) )
s.add(flag_chars[20] == ((233 - 1) ^ 173) )
s.add(flag_chars[21] == ((156 - 1) ^ 190) )
s.add(flag_chars[22] == ((156 - 1) ^ 239) )
s.add(flag_chars[23] == ((150 - 1) ^ 222) )
s.add(flag_chars[24] == ((207 - 1) ^ 173) )
s.add(flag_chars[25] == ((235 - 1) ^ 190) )
s.add(flag_chars[26] == ((224 - 1) ^ 239) )

sat = s.check()
if str(sat) == "sat":
	model = s.model()
	flag = ''.join([chr(int(str(model[flag_chars[i]]))) for i in range(len(model))])
	print("Passcode :", flag)
else:
	print(sat)

# Flag
xor_vals = [0x14, 0x75, 0x60, 0x43, 0x3d, 0x12, 0x56, 0x35, 0x47, 0x15, 0x44, 0x0a, 0x22, 0x0c, 0x43, 0x2f, 0x68, 0x04, 0x01, 0x36, 0x26, 0x15, 0x44, 0x27, 0x3c, 0x26, 0x01, 0x01, 0x27, 0x30, 0x0b, 0x2f]
data = [chr(a ^ ord(b)) for a,b in zip(xor_vals,flag)]

print("Flag :", "".join(data))