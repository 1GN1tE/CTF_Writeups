"""
lock_data = {
0x00 0x01 0x02 0x03  --> Inner  Wheel [0x1c] <-- Size
0x04 0x05 0x06 0x07  --> Middle Wheel [0x2c] <-- Size
0x08 0x09 0x0a 0x0b  --> Outer  Wheel [0x38] <-- Size

0x0c --> prlock --> Toggles Lock Print
0x0d --> x0		--> Can be toggled with !
0x0e --> x1		--> To get 1 for flag
0x0f --> x2		--> To get 1 for flag
0x10 --> x3		--> To get 1 for flag
0x11 --> x4		--> To get 1 for flag
0x12 --> x5		--> To get 1 for flag
}

(0x06, 0x25, 0x0D) --> x0d = 0, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 1, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
(0x09, 0x08, 0x07) --> x0d = 1, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 0, x12 = 0
(0x09, 0x08, 0x08) --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 1, x0e = 0, x0f = 1, x10 = 0, x11 = 0, x12 = 0
(0x16, 0x0b, 0x07) --> x0d = 1, x0e = 0, x0f = 1, x10 = 0, x11 = 0, x12 = 1
!				   --> x0d = 0, x0e = 0, x0f = 1, x10 = 0, x11 = 1, x12 = 1
(0x06, 0x25, 0x0D) --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 1, x12 = 1
(0x00, 0x00, 0x00) --> x0d = 0, x0e = 1, x0f = 1, x10 = 1, x11 = 1, x12 = 1
"""

for i in range(6):
	print("i")
for i in range(7):
	print("M")
for i in range(0x0d):
	print("o")

print("!")
for i in range(3):
	print("i")
for i in range(15):
	print("m")
for i in range(6):
	print("O")

print("!")

print("o")

print("!")
for i in range(13):
	print("i")
for i in range(3):
	print("m")

print("O")

print("!")
for i in range(16):
	print("I")
for i in range(18):
	print("M")
for i in range(6):
	print("o")
for i in range(6):
	print("I")
for i in range(7):
	print("m")
for i in range(0x0d):
	print("O")
