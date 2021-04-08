pos = [8,2,7,1] 

md_ = [' ']*64
dat = [0x48, 0x89, 0xFE, 0x48, 0xBF, 0xF1, 0x26, 0xDC, 0xB3, 0x07, 0x00, 0x00, 0x00, 0xFF, 0xD6, 0x00]
for j in range(4):
	for k in range(4):
		md_[16*k+j+pos[k]] = hex(dat[4*k+j])[2:].zfill(2)
print()
for i in range(0,len(md_),16):
	for j in range(16):
		print(md_[j+i], end=", ")
	print()

# exit()
"""
MD5(????GpLaMjEW) =  ,  ,  ,  ,  ,  ,  ,  ,48,89,fe,48,  ,  ,  ,  ,
MD5(????pVOjnnmk) =  ,  ,bf,f1,26,dc,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
MD5(????RGiledp6) =  ,  ,  ,  ,  ,  ,  ,b3,07,00,00,  ,  ,  ,  ,  ,
MD5(????Mvcezxls) =  ,00,ff,d6,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , (We don't need the last 0x00)
"""

import itertools as it
from hashlib import md5
import string

charset = string.ascii_letters + string.digits
print(charset)

def searchee(suffix, known, hash):
	hash = [hash[i:i+2] for i in range(0,len(hash), 2)]
	c = 0
	for i in known:
		if hash[i] == known[i]:
			c+=1
	if c == len(known):
		return 1
	return 0

suffix = ["GpLaMjEW","pVOjnnmk","RGiledp6","Mvcezxls"]

known = [
{8:"48",9:"89",10:"fe",11:"48"},
{2:"bf",3:"f1",4:"26",5:"dc"},
{7:"b3",8:"07",9:"00",10:"00"},
{1:"00",2:"ff",3:"d6"}
]

print("[+] Starting Brute...")

for i, k in enumerate(known):
	print(f"suffix: {suffix[i]}")
	print(f"known: {k}")
	
	perms = it.product(charset, repeat=4)

	for p in perms:
		data = "".join(p) + suffix[i]
		hash = md5(data.encode()).hexdigest()
		if searchee(suffix[i], k, hash):
			print("[+] FOUND: ", data[:4])
			break

"""
MD5(D1v1GpLaMjEW) =  ,  ,  ,  ,  ,  ,  ,  ,48,89,fe,48,  ,  ,  ,  ,		| --> D1v1
MD5(d3AnpVOjnnmk) =  ,  ,bf,f1,26,dc,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,		| --> d3An
MD5(dC0nRGiledp6) =  ,  ,  ,  ,  ,  ,  ,b3,07,00,00,  ,  ,  ,  ,  ,		| --> dC0n
MD5(qu3rMvcezxls) =  ,00,ff,d6,00,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,		| --> qu3r

D1v1d3AndC0nqu3r
"""
