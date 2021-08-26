data = b"\xfc\xfc\xfc/$D$$/\x0c/\x0c/\xbb\xdb\xdb\xbb/\x0c/\xf9\x99\xf9/\x81\x81/'''/\xc1/\xfc\xfc\xfc/$D$$/\x0c/\x0c/\xbb\xdb\xdb\xbb/\x0c/\xf9\x99\xf9/\x81\x81/'''/\xc1/i\t\t/\x81\x81/\xd8\xd8\xd8/\x88\xe8/\xbb\xdb\xdb\xbb/\xbb\xdb\xdb\xbb/\x0c/\x88\xe8/\xf9\x99\xf9/\x81\x81/'''/\xc1/\xa5\xa5/\x06f/\xd8\xd8\xd8/_/\x88\xe8/\x06f/_/\x0c/\xf9\x99\xf9/\x81\x81/'''/\xa0\xc0\xa0\xc0\xa0\xa0"

db = [b'\x0f', b'\x05\x06\x05\x05\x06', b'\x1d\x1d\x1d\x1d\x1d', b'\x15\x15\x15\x16\x16', b'nmmnmn', b'ffff', b'~}}~', b'uvvu', b'\x00', b'FFFF', b'^]]^', b'UVVU', b'\x0c\x0f\x0c\x0f\x0c\x0c', b'\x04\x07\x04\x04\x07\x04', b'\x1f\x1c\x1c\x1c\x1c', b'\x14\x14\x14\x14\x17', b'ol', b'gg', b'||\x7f|', b'twtt', b'OL', b'GG', b'\\\\_\\', b'TWTT', b'\x00', b'\x00', b'\x1c\x1c\x1f\x1f\x1f', b'\x17\x17\x17\x14\x14\x14', b'olll', b'dggg', b'|\x7f|', b'wwtt', b'OLLL', b'DGGG', b'\\_\\', b'WWTT', b'\x00', b'\x05\x06\x05\x06\x05', b'\x1d\x1d\x1d\x1e\x1e', b'\x16\x15\x16\x15\x16\x15', b'nmnm', b'fef', b'}}}', b'\x00', b'NMNM', b'FEF', b']]]', b'\x00', b'\n\n\n\n\n', b'\x01\x01\x02\x02\x01\x01', b'\x1a\x1a\x1a\x1a\x19', b'\x00', b'ijj', b'babb', b'y', b'\x00', b'IJJ', b'BABB', b'Y', b'\x00', b'\x00', b'\x00\x03\x03\x03\x03\x00', b'\x1b\x1b\x1b\x1b\x1b', b'\x10\x13\x13\x13\x10', b'k', b'``', b'{{x', b'\x00', b'K', b'@@', b'[[X', b'\x00', b'\x08\x0b\x08\x08\x08', b'\x00\x03\x00\x03\x00\x03', b'\x1b\x18\x18\x18\x18', b'\x00', b'hhkh', b'c`', b'xxx{', b'\x00', b'HHKH', b'C@', b'XXX[', b'\x00', b'\t\n\n\n\n\t', b'\x02\x01\x01\x02\x01', b'\x1a\x1a\x19\x19\x19', b'\x11\x11\x12\x12\x11\x11', b'jji', b'bbb', b'yzz', b'qqrrqr', b'JJI', b'BBB', b'YZZ']
pos = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238]

refs = [""] * 256

data = data.split(b"/")

for a,b in zip(db,pos):
    refs[b] = a


def ror(v,s):
	b = s % 8
	return (v << b | v >> (8 - b)) & 0xFF

def rol(v,s):
	b = s % 8
	return (v >> b | v << (8 - b)) & 0xFF

def gen(c):
    a = refs[rol(c,3)]
    # print(a)
    b = []
    for i in a:
        b.append(ror(i,5))
    b = [c ^ i for i in b]
    return bytes(b)

flag = ""

for d in data:
    for c in range(30,128):
        if gen(c) == d:
            flag += chr(c)
            break

print(flag)
# print(gen(ord("A")))
# print(data[0])