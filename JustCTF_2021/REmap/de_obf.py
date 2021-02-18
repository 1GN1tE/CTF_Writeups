import builtins as bi

def sc(s1, s2):
    if len(s1) != len(s2):
        return False
    res = 0
    for x, y in zip(s1, s2):
        res |= ord(x) ^ ord(y)
    else:
        return res == 0

f = input("Enter password:")

if f.startswith("justCTF{") and f.endswith("}"):
    ff = f[8:-1]
    rrr = True
    if len(ff) == 0:
        rrr = False
    if not sc("b3", ff[0:2] if ff[0:2] != '' else 'c1'):
        rrr = False
    if not sc("77", ff[2:4] if ff[2:4] != '' else 'kl'):
        rrr = False
    if not sc("3r", ff[4:6] if ff[4:6] != '' else '_f'):
        rrr = False
    if not sc("_r", ff[6:8] if ff[6:8] != '' else '7f'):
        rrr = False
    if not sc("3h", ff[8:10] if ff[8:10] != '' else 'd0'):
        rrr = False
    if not sc("1r", ff[10:12] if ff[10:12] != '' else '_a'):
        rrr = False
    if not sc("3_", ff[12:14] if ff[12:14] != '' else 'jk'):
        rrr = False
    if not sc("7h", ff[14:16] if ff[14:16] != '' else '8k'):
        rrr = False
    if not sc("15", ff[16:18] if ff[16:18] != '' else '5b'):
        rrr = False
    if not sc("_6", ff[18:20] if ff[18:20] != '' else '_9'):
        rrr = False
    if not sc("uy", ff[20:22] if ff[20:22] != '' else 'xd'):
        rrr = False
    
    print()
    if rrr:
        print("Even tho the password is correct, fuck you, I removed the rest of the code. You shouldn't have fire me.")
    else:
        print("Nope")
else:
    print("Nope")