file = open("dump", "rb")

file.seek(0x13A9)
data = file.read(896)

func_1 = data[:0x2e8]
func_2 = data[0x2e8:]

func_prologue = [0xf3, 0x0f, 0x1e, 0xfa, 0x55, 0x48, 0x89, 0xe5] 	# known

f1key_8 = [(i ^ j) for i,j in zip(func_prologue, func_1)]
f2key_8 = [(i ^ j) for i,j in zip(func_prologue, func_2)]
key_16 = f1key_8 + f2key_8

key_bytes = bytes(key_16)
print(key_bytes)

# with open('key.txt', 'wb') as f:
# 	f.write(key_bytes)

"""
xxd key.txt 
xxd dump | grep "428c 81c5 ea13 e0c2"
"""

key_offset = 0x0004ba70 + 4

file.seek(key_offset)

KEY = file.read(32)
# print(KEY)

new_data = b''
for i in range(len(data)):
	new_data += bytes( [data[i] ^ KEY[i % 32]] )

# print(new_data)

print("Patching dump...")

file = open("dump", "rb")
new_dump = file.read(0x13A9) + new_data

off = 0x13A9 + 896

file.seek(off)

new_dump += file.read()

with open("new_dump_2", 'wb') as f:
	f.write(new_dump)


# CHECKER

new = open("new_dump_2", "rb")

new.seek(0x13A9)
data = new.read(896)
# print(new)

assert data == new_data

print("DONE !!!")