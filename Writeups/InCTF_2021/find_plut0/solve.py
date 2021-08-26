from z3 import *
flag_len = 30
flag_chars = [BitVec(f'{i}', 32) for i in range(flag_len)] # Length of flag
s = Solver()

for i in range(flag_len):
    s.add(flag_chars[i]>32)
    s.add(flag_chars[i]<126)
    s.add(flag_chars[i]!= ord("^"))
    s.add(flag_chars[i]!= ord(","))
    s.add(flag_chars[i]!= ord("?"))
    s.add(flag_chars[i]!= ord("\""))
    s.add(flag_chars[i]!= ord("["))
    s.add(flag_chars[i]!= ord("]"))
    s.add(flag_chars[i]!= ord("*"))
    s.add(flag_chars[i]!= ord("("))
    s.add(flag_chars[i]!= ord(")"))
    s.add(flag_chars[i]!= ord(":"))
    s.add(flag_chars[i]!= ord(">"))
    s.add(flag_chars[i]!= ord("<"))
    s.add(flag_chars[i]!= ord("|"))
    s.add(flag_chars[i]!= ord(";"))
    s.add(flag_chars[i]!= ord("\\"))
    s.add(flag_chars[i]!= ord(";"))
    s.add(flag_chars[i]!= ord("`"))
    s.add(flag_chars[i]!= ord("&"))
    s.add(flag_chars[i]!= ord("."))
    s.add(flag_chars[i]!= ord("/"))


x = [0]*22
s1 = [0]*22

x[0] = flag_chars[0] - 50 + flag_chars[1]
x[1] = flag_chars[1] - 100 + flag_chars[2]
x[2] = 4 * flag_chars[2]
x[3] = flag_chars[3] ^ 0x46
x[4] = 36 - (flag_chars[3] - flag_chars[4])
x[6] = flag_chars[6] * flag_chars[5] + 99
x[7] = (flag_chars[6] ^ flag_chars[7])
x[8] = (flag_chars[7] + 45) ^ flag_chars[8]
x[9] = (flag_chars[9] & 0x37) - 3
x[11] = flag_chars[11] - 38
x[12] = 4 * ((flag_chars[12] ^ flag_chars[6]) + 4)
x[5] = (flag_chars[21] - flag_chars[4]) ^ 0x30
x[13] = flag_chars[13] - flag_chars[14] - 1
x[10] = flag_chars[17] - flag_chars[16] + 82
x[16] = 6 * (flag_chars[18] ^ flag_chars[19]) + 54
x[17] = flag_chars[21] + 49 + (flag_chars[20] ^ 0x73)
x[14] = flag_chars[22]
x[18] = flag_chars[23] ^ 0x42
x[15] = flag_chars[26] + 5
x[19] = flag_chars[25] - flag_chars[26] / 2 - 55
x[20] = 4 * flag_chars[27] - (flag_chars[28] + 128)
x[21] = flag_chars[29] - 32

s1[0]  = ((x[0] ^ 2) - 31) & 0xFF
s1[1]  = (((x[1] % 2) ^ x[0]) - 29) & 0xFF
s1[2]  = ((4 * x[1]) ^ 0x97) & 0xFF
s1[3]  = (x[2] ^ 0xA0) & 0xFF
s1[4]  = ((x[3] ^ 0x4D) + 7) & 0xFF
s1[5]  = (4 * x[5] - 1) & 0xFF
s1[3]  = (x[4] + 116) & 0xFF
s1[6]  = (x[6] + 21) & 0xFF
s1[7]  = (x[7] - 20) & 0xFF
s1[8]  = (x[8] ^ 0x63) & 0xFF
s1[9]  = ((x[10] ^ 3) - x[8] + 54) & 0xFF
s1[10] = (x[9] ^ 0x42) & 0xFF
s1[11] = (x[11] + 51) & 0xFF
s1[11] = (x[12] ^ 0xB3) & 0xFF
s1[12] = ((x[13] + 18) ^ 0x1A) & 0xFF
s1[13] = (x[14] - 7) & 0xFF
s1[14] = (x[15] - 37) & 0xFF
s1[15] = (x[17] ^ 0xE5) & 0xFF
s1[16] = ((x[18] & 0x36) + 53) & 0xFF
s1[14] = (x[19] ^ 0x34) & 0xFF
s1[17] = (x[20] ^ 0xFD) & 0xFF
s1[18] = ((x[20] >> x[21]) ^ 0x1C) & 0xFF

# Other consraints and equations
st = "inctf{U_Sur3_m4Te?}"

for i in range(len(st)):
    s.add(s1[i] == ord(st[i]))

sat = s.check()
if str(sat) == "sat":
    model = s.model()
    # print(model)
    flag = ''.join([chr(int(str(model[flag_chars[i]]))) for i in range(len(model))])
    print(flag)
else:
    print(sat)