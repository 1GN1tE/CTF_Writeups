file = open("dump", "rb")

file.seek(0x5060)
flag_data = file.read(128)

# print(flag_data)
print("FLAG DATA >>>")
for i in flag_data:
	print(hex(i), end=" ")

memset_offset = 0x3AB7B - 176

file.seek(memset_offset)
memset_data = file.read(192)

# print(memset_data)
print("\nMEMSET DATA >>>")
for i in memset_data:
	print(hex(i), end=" ")