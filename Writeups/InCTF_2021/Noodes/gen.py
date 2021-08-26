st = open("ialert","rb").read()[0x2440:0x25F4].decode()
# print(st)

ans = []

parts = [st[i:i+4] for i in range(0, len(st), 4)]
# print(parts)

cmds = []

for x in parts:
    cmd = []
    cmd.append(x[:2])
    cmd.append(chr(ord(x[2]) - 4) + chr(ord(x[3]) - 4))
    cmds.append(cmd)

# for i in cmds:
    # print(i)


cmds = [
['df', 'tT'],
['df', '1B'],
['cw', 'HX'],
['ad', 'oQ'],
['dd', 'La'],
['dd', 'yQ'],
['aa', 'hV'],
['df', 'hV'],
['af', 'jz'],
['af', '5P'],
['xx', 'hV'],

['af', 'eh'],
['dd', 'GU'],
['af', 'IZ'],
['df', 'tN'],
['mf', 'AJ'],
['cw', 'AJ'],
['dd', 'Ti'],
['df', 'XN'],
['af', 'bX'],
['df', 'wt'],
['dd', 'HW'],
['ad', 'ae'],
['ad', 'Fg'],
['df', 'S1'],
['cw', 'eP'],
['dd', '3U'],
['df', 'Zv'],
['ad', 'gG'],
['cw', '6f'],
['ad', 'aq'],
['df', 'Q9'],
['df', 'fz'],
['dd', 'Wy'],
['df', 'I5'],
['cw', 'l3'],
['df', 'dj'],
['mf', 'Pf'],
['cw', 'Pf'],
['dd', 'uM'],
['df', 'bp'],
['dd', '1Q'],
['df', 'Et'],
['dd', 'Cu'],
['df', 'cj'],
['dd', 'fU'],
['df', 'mV'],
['cw', 'mL'],
['cw', 'bl'],
['df', 'hH'],
['dd', 'Qk'],
['af', 'zr'],
['dd', 'Sm'],
['af', 'VF'],
['df', '9P'],
['cw', 'wV'],
['mf', 'xB'],
['cw', 'xB'],
['dd', 'jg'],
['ad', 'Qc'],
['df', 'fX'],
['df', 'nZ'],
['dd', 'YO'],
['df', 'CF'],
['cw', 'sF'],
['df', 'Bp'],

['cw', 'vB'],
['cw', 'TR'],
['cw', 'Ax'],
['cw', 'gL'],
['dd', 'SI'],
['dd', 'Ye'],
['ad', 'q6'],
['cw', 'BN'],
['ad', 'XE'],
['af', 'Tn'],
['af', 'Jt'],
['mf', 'Ah'],
['cw', 'Ah'],
['af', 'Fr'],
['af', 't5'],
['df', '0x'],
['dd', '4i'],
['mf', 'Dz'],
['cw', 'Dz'],
['mf', 'Pz'],
['cw', 'Pz'],
['af', 'gB'],
['af', 'rl'],
['df', 'f1'],
['dd', 'yO'],
['af', 'RN'],

]

test = '1KP' + '11V3' + '1EZ' + '1Xl' + '1JH3' + '1Pd3' + '1Cx' + '1uj' + '193' + '1Xt' + '1Lx3' + '1Bl3'
# """
i = 0
while (i < len(cmds)):
    x = cmds[i]
    cmd = x[0]
    if cmd == "aa":
        ans.append("1" + x[1])

    elif cmd == "df":
        ans.append("4" + x[1])

    elif cmd == "dd":
        ans.append("6" + x[1])

    elif cmd == "cw":
        ans.append("1" + x[1] + "2")

    elif cmd == "ad":
        ans.append("5" + x[1])

    elif cmd == "af":
        ans.append("5" + x[1])

    elif cmd == "mf":
        # ans.append("3")
        if cmds[i+1][0] == "cw":
            ans.append("1" + x[1] + "32")
        else:
            ans.append("1" + x[1] + "3")
        i += 1
    elif cmd == "xx":
        ans.append("32")

    else:
        print("ERR", cmd)
        break
    i += 1

# """

print("".join(ans) + test + "8")
