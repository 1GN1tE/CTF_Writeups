
### Write Flag ###
# f = open("flag","wb")

# for i in range(256):
# 	f.write(bytes([i]))
# exit()

### Parse Mappings ###
# file = open("flag.enc","rb")
# data = file.read()
# x = len(data)//2
# tmp_data = []
# for i in range(x):
# 	a = data[x - i - 1]
# 	b = data[x + i]
# 	if(i % 2 == 0):
# 		tmp = a << 8 | b
# 	else:
# 		tmp = b << 8 | a
# 	print(hex(tmp)[2:].zfill(4), hex(i)[2:].zfill(2))
# file.close()
# exit()

mapping = {
	0x0100 : 0x00,
	0xc200 : 0x01,
	0xcc00 : 0x02,
	0x0e00 : 0x03,
	0x9800 : 0x04,
	0x5a00 : 0x05,
	0x5400 : 0x06,
	0x9600 : 0x07,
	0x6800 : 0x08,
	0xaa00 : 0x09,
	0xa400 : 0x0a,
	0x6600 : 0x0b,
	0xf000 : 0x0c,
	0x3200 : 0x0d,
	0x3c00 : 0x0e,
	0xfe00 : 0x0f,
	0x01c3 : 0x10,
	0xc2c3 : 0x11,
	0xccc3 : 0x12,
	0x0ec3 : 0x13,
	0x98c3 : 0x14,
	0x5ac3 : 0x15,
	0x54c3 : 0x16,
	0x96c3 : 0x17,
	0x68c3 : 0x18,
	0xaac3 : 0x19,
	0xa4c3 : 0x1a,
	0x66c3 : 0x1b,
	0xf0c3 : 0x1c,
	0x32c3 : 0x1d,
	0x3cc3 : 0x1e,
	0xfec3 : 0x1f,
	0x01cd : 0x20,
	0xc2cd : 0x21,
	0xcccd : 0x22,
	0x0ecd : 0x23,
	0x98cd : 0x24,
	0x5acd : 0x25,
	0x54cd : 0x26,
	0x96cd : 0x27,
	0x68cd : 0x28,
	0xaacd : 0x29,
	0xa4cd : 0x2a,
	0x66cd : 0x2b,
	0xf0cd : 0x2c,
	0x32cd : 0x2d,
	0x3ccd : 0x2e,
	0xfecd : 0x2f,
	0x010f : 0x30,
	0xc20f : 0x31,
	0xcc0f : 0x32,
	0x0e0f : 0x33,
	0x980f : 0x34,
	0x5a0f : 0x35,
	0x540f : 0x36,
	0x960f : 0x37,
	0x680f : 0x38,
	0xaa0f : 0x39,
	0xa40f : 0x3a,
	0x660f : 0x3b,
	0xf00f : 0x3c,
	0x320f : 0x3d,
	0x3c0f : 0x3e,
	0xfe0f : 0x3f,
	0x0199 : 0x40,
	0xc299 : 0x41,
	0xcc99 : 0x42,
	0x0e99 : 0x43,
	0x9899 : 0x44,
	0x5a99 : 0x45,
	0x5499 : 0x46,
	0x9699 : 0x47,
	0x6899 : 0x48,
	0xaa99 : 0x49,
	0xa499 : 0x4a,
	0x6699 : 0x4b,
	0xf099 : 0x4c,
	0x3299 : 0x4d,
	0x3c99 : 0x4e,
	0xfe99 : 0x4f,
	0x015b : 0x50,
	0xc25b : 0x51,
	0xcc5b : 0x52,
	0x0e5b : 0x53,
	0x985b : 0x54,
	0x5a5b : 0x55,
	0x545b : 0x56,
	0x965b : 0x57,
	0x685b : 0x58,
	0xaa5b : 0x59,
	0xa45b : 0x5a,
	0x665b : 0x5b,
	0xf05b : 0x5c,
	0x325b : 0x5d,
	0x3c5b : 0x5e,
	0xfe5b : 0x5f,
	0x0155 : 0x60,
	0xc255 : 0x61,
	0xcc55 : 0x62,
	0x0e55 : 0x63,
	0x9855 : 0x64,
	0x5a55 : 0x65,
	0x5455 : 0x66,
	0x9655 : 0x67,
	0x6855 : 0x68,
	0xaa55 : 0x69,
	0xa455 : 0x6a,
	0x6655 : 0x6b,
	0xf055 : 0x6c,
	0x3255 : 0x6d,
	0x3c55 : 0x6e,
	0xfe55 : 0x6f,
	0x0197 : 0x70,
	0xc297 : 0x71,
	0xcc97 : 0x72,
	0x0e97 : 0x73,
	0x9897 : 0x74,
	0x5a97 : 0x75,
	0x5497 : 0x76,
	0x9697 : 0x77,
	0x6897 : 0x78,
	0xaa97 : 0x79,
	0xa497 : 0x7a,
	0x6697 : 0x7b,
	0xf097 : 0x7c,
	0x3297 : 0x7d,
	0x3c97 : 0x7e,
	0xfe97 : 0x7f,
	0x0169 : 0x80,
	0xc269 : 0x81,
	0xcc69 : 0x82,
	0x0e69 : 0x83,
	0x9869 : 0x84,
	0x5a69 : 0x85,
	0x5469 : 0x86,
	0x9669 : 0x87,
	0x6869 : 0x88,
	0xaa69 : 0x89,
	0xa469 : 0x8a,
	0x6669 : 0x8b,
	0xf069 : 0x8c,
	0x3269 : 0x8d,
	0x3c69 : 0x8e,
	0xfe69 : 0x8f,
	0x01ab : 0x90,
	0xc2ab : 0x91,
	0xccab : 0x92,
	0x0eab : 0x93,
	0x98ab : 0x94,
	0x5aab : 0x95,
	0x54ab : 0x96,
	0x96ab : 0x97,
	0x68ab : 0x98,
	0xaaab : 0x99,
	0xa4ab : 0x9a,
	0x66ab : 0x9b,
	0xf0ab : 0x9c,
	0x32ab : 0x9d,
	0x3cab : 0x9e,
	0xfeab : 0x9f,
	0x01a5 : 0xa0,
	0xc2a5 : 0xa1,
	0xcca5 : 0xa2,
	0x0ea5 : 0xa3,
	0x98a5 : 0xa4,
	0x5aa5 : 0xa5,
	0x54a5 : 0xa6,
	0x96a5 : 0xa7,
	0x68a5 : 0xa8,
	0xaaa5 : 0xa9,
	0xa4a5 : 0xaa,
	0x66a5 : 0xab,
	0xf0a5 : 0xac,
	0x32a5 : 0xad,
	0x3ca5 : 0xae,
	0xfea5 : 0xaf,
	0x0167 : 0xb0,
	0xc267 : 0xb1,
	0xcc67 : 0xb2,
	0x0e67 : 0xb3,
	0x9867 : 0xb4,
	0x5a67 : 0xb5,
	0x5467 : 0xb6,
	0x9667 : 0xb7,
	0x6867 : 0xb8,
	0xaa67 : 0xb9,
	0xa467 : 0xba,
	0x6667 : 0xbb,
	0xf067 : 0xbc,
	0x3267 : 0xbd,
	0x3c67 : 0xbe,
	0xfe67 : 0xbf,
	0x01f1 : 0xc0,
	0xc2f1 : 0xc1,
	0xccf1 : 0xc2,
	0x0ef1 : 0xc3,
	0x98f1 : 0xc4,
	0x5af1 : 0xc5,
	0x54f1 : 0xc6,
	0x96f1 : 0xc7,
	0x68f1 : 0xc8,
	0xaaf1 : 0xc9,
	0xa4f1 : 0xca,
	0x66f1 : 0xcb,
	0xf0f1 : 0xcc,
	0x32f1 : 0xcd,
	0x3cf1 : 0xce,
	0xfef1 : 0xcf,
	0x0133 : 0xd0,
	0xc233 : 0xd1,
	0xcc33 : 0xd2,
	0x0e33 : 0xd3,
	0x9833 : 0xd4,
	0x5a33 : 0xd5,
	0x5433 : 0xd6,
	0x9633 : 0xd7,
	0x6833 : 0xd8,
	0xaa33 : 0xd9,
	0xa433 : 0xda,
	0x6633 : 0xdb,
	0xf033 : 0xdc,
	0x3233 : 0xdd,
	0x3c33 : 0xde,
	0xfe33 : 0xdf,
	0x013d : 0xe0,
	0xc23d : 0xe1,
	0xcc3d : 0xe2,
	0x0e3d : 0xe3,
	0x983d : 0xe4,
	0x5a3d : 0xe5,
	0x543d : 0xe6,
	0x963d : 0xe7,
	0x683d : 0xe8,
	0xaa3d : 0xe9,
	0xa43d : 0xea,
	0x663d : 0xeb,
	0xf03d : 0xec,
	0x323d : 0xed,
	0x3c3d : 0xee,
	0xfe3d : 0xef,
	0x01ff : 0xf0,
	0xc2ff : 0xf1,
	0xccff : 0xf2,
	0x0eff : 0xf3,
	0x98ff : 0xf4,
	0x5aff : 0xf5,
	0x54ff : 0xf6,
	0x96ff : 0xf7,
	0x68ff : 0xf8,
	0xaaff : 0xf9,
	0xa4ff : 0xfa,
	0x66ff : 0xfb,
	0xf0ff : 0xfc,
	0x32ff : 0xfd,
	0x3cff : 0xfe,
	0xfeff : 0xff,
}

### Decode flag.enc ###
file = open("flag.enc","rb")
data = file.read()

x = len(data)//2

flag = open("flag","wb")

for i in range(x):
	a = data[x - i - 1]
	b = data[x + i]
	if(i % 2 == 0):
		tmp = a << 8 | b
	else:
		tmp = b << 8 | a
	flag.write(bytes([mapping[tmp]]))