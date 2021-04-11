"""
dec = []
data = open("crypt.bin","rb")
for i in range(0x8E85+1):
	y = int.from_bytes(data.read(1),byteorder="little")
	dec.append(y)

print(dec)
"""

from pwn import *

passphrase = open("key.txt","r").read().strip()

p = process(["./patched",passphrase])
pause()
for i in range(0x8E85+1):
	p.send('\x00')

p.interactive()