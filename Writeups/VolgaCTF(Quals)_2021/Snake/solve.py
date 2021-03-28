from z3 import *
flag_len = 30

flag_chars = [BitVec(f'{i}', 8) for i in range(flag_len)]
s = Solver()

for i in range(9,29):
	s.add(flag_chars[i]>44)
	s.add(flag_chars[i]<123)
	s.add(flag_chars[i]!=58)
	s.add(flag_chars[i]!=59)
	s.add(flag_chars[i]!=60)
	s.add(flag_chars[i]!=61)
	s.add(flag_chars[i]!=62)
	s.add(flag_chars[i]!=63)
	s.add(flag_chars[i]!=64)
	s.add(flag_chars[i]!=91)
	s.add(flag_chars[i]!=92)
	s.add(flag_chars[i]!=93)
	s.add(flag_chars[i]!=94)
	s.add(flag_chars[i]!=96)
	s.add(flag_chars[i]!=124)

s.add(flag_chars[0]==ord("V"))
s.add(flag_chars[1]==ord("o"))
s.add(flag_chars[2]==ord("l"))
s.add(flag_chars[3]==ord("g"))
s.add(flag_chars[4]==ord("a"))
s.add(flag_chars[5]==ord("C"))
s.add(flag_chars[6]==ord("T"))
s.add(flag_chars[7]==ord("F"))
s.add(flag_chars[8]==ord("{"))
s.add(flag_chars[29]==ord("}"))


swap_flag = [0] * flag_len
sw = [0,1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,4,5,6,7,8,9,]
for i in range(flag_len):
	swap_flag[i] = flag_chars[sw[i]]

mul = [
[81,244,40,191,56,196,86,55,51,91,66,105,56,74,0,250,30,5,222,15,217,3,134,30,235,243,255,213,119,44],
[118,214,253,28,121,236,242,8,0,160,108,245,89,126,252,41,236,94,154,77,80,195,91,213,183,63,59,62,89,63],
[9,85,94,176,89,181,219,38,147,75,117,234,137,212,199,100,128,83,196,87,118,130,48,128,190,45,151,138,161,159],
[11,65,43,96,153,146,77,176,150,189,189,222,119,104,84,246,75,95,54,205,23,12,188,198,188,197,154,218,149,110],
[28,92,160,132,7,82,79,157,77,143,120,117,66,94,237,118,204,129,195,131,230,100,209,26,195,158,23,192,53,166],
[46,70,134,223,173,17,11,44,194,186,243,155,174,120,7,9,117,39,106,200,215,10,227,10,181,33,242,26,207,2],
[61,185,219,67,235,55,87,63,148,112,117,236,21,100,5,113,79,246,72,245,228,21,77,153,187,238,208,212,146,193],
[65,33,197,254,94,136,64,7,213,123,115,160,146,245,62,227,100,20,124,118,233,77,24,202,30,253,188,231,207,21],
[69,27,50,92,219,95,176,209,205,80,203,122,213,155,134,136,211,217,192,164,104,209,49,2,121,30,223,225,193,139],
[84,136,149,107,73,141,182,244,136,206,60,118,38,239,120,118,206,159,242,136,181,29,153,212,206,97,117,34,246,137],
[105,124,235,62,139,17,64,208,221,158,130,40,126,245,115,22,212,122,65,48,46,21,147,36,46,45,72,9,44,234],
[112,212,75,101,216,237,53,194,78,187,232,58,135,51,219,213,255,24,6,199,157,20,5,144,184,129,67,156,199,9],
[143,38,227,184,108,32,2,144,236,155,92,53,29,10,41,22,183,47,218,11,80,145,64,71,149,22,97,230,12,31],
[147,72,5,172,42,154,166,246,1,177,235,165,130,131,132,230,79,52,112,149,112,84,78,189,69,1,167,76,147,205],
[157,164,77,16,56,236,239,177,34,87,250,235,81,117,26,67,158,195,193,246,83,140,22,127,88,54,9,181,139,55],
[186,126,62,120,39,175,247,79,58,157,101,152,214,221,151,185,38,120,182,226,148,55,166,245,17,223,83,154,146,78],
[209,242,84,104,57,72,41,104,220,203,243,184,227,165,109,102,193,212,228,37,99,181,99,103,26,187,164,150,73,98],
[236,151,96,58,18,188,52,216,154,54,104,184,151,168,175,213,65,163,56,187,43,200,201,18,170,215,47,171,188,239],
]

add = [168,224,6,146,215,70,104,180,15,118,243,38,119,31,7,183,209,228,33,180,65,87,55,177,245,20,243,56,37,46]

for c in range(18):
	total = add[c]
	for i in range(30):
		total += swap_flag[i]*mul[c][i]

	s.add(total%256==0)

sat = s.check()
if str(sat) == "sat":
	model = s.model()
	flag = ''.join([chr(int(str(model[flag_chars[i]]))) for i in range(len(model))])
	print(flag)
else:
	print(sat)