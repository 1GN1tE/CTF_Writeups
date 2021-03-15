# maze_size = 50
# val = new_y * maze_size + new_x
flag_pos = [0x038E, 0x0992, 0x0035, 0x0071, 0x0053, 0x06BD, 0x076C, 0x095C, 0x0211, 0x0401]
flag_cood = []
for i in range(10):
	x = flag_pos[i]%50
	y = 50 - (flag_pos[i]//50) # For plotting on Desmos
	flag_cood.append([x,y])

for i in flag_cood:
	print(i)
