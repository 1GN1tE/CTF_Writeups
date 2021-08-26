weird_arr = open("flagchecker","rb").read()[0x2020:0x2848]

pos_vals = [
[[0 , 6], [8 , 5], [16 , 8], [24 , 3], [31 , 3],],
[[1 , 2], [9 , 6], [17 , 1], [25 , 0],],
[[2 , 0], [10 , 4], [18 , 5], [26 , 2], [32 , 3],],
[[3 , 8], [11 , 5], [19 , 3], [27 , 7],],
[[4 , 3], [12 , 8], [20 , 3], [28 , 8], [33 , 3],],
[[5 , 6], [13 , 5], [21 , 5], [29 , 6],],
[[6 , 1], [14 , 0], [22 , 4], [30 , 2], [34 , 5],],
[[7 , 5], [15 , 3], [23 , 1], [35 , 8],],
]

checks = [
'84721',
'1138',
'80481',
'7786',
'57518',
'2445',
'02162',
'1854',
]

flag = [0] * 36

for i in range(len(checks)):
	chk = checks[i]
	psv = pos_vals[i]

	print(psv)

	for x in range(len(chk)):
		for ch in range(30,127):
			if chr(weird_arr[int(str(ch),16)]) == chk[x]:
				if (ch % 9) == psv[x][1]:
					# print(chr(ch))
					flag[psv[x][0]] = chr(ch)
					break

# print(flag)
print("".join(flag))