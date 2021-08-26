inp = "abcdefghijklmnopqrstuvwxyz"

db = [
["y","0"],
["x","k"],
["v","e"],
["r","d"],
["j","t"],
["i","Z"],
["q","6"],
["h","f"],
["g","Y"],
["u","O"],
["p","3"],
["o","a"],
["f","X"],
["e","4"],
["w","l"],
["t","P"],
["n","N"],
["m","M"],
["d","S"],
["c","g"],
["s","Q"],
["l","b"],
["k","R"],
["b","w"],
["a","h"],
]

flag = [0]*25

for i in db:
	flag[inp.index(i[0])] = i[1]


print("".join(flag))