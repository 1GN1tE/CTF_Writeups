from z3 import *

def enc(x):
	x = (x * 0x5deece66d + 0xb) & 0xffffffffffff;
	return simplify(x)

to_xor = BitVec("x", 8 * 6)
for i in range(100):
	to_xor = enc(to_xor)

solve(to_xor == 0xfd94e6e84a0a)
