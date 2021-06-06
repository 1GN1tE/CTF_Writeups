from struct import unpack

class registers:
	def __init__(self):
		self.r0 = 0
		self.r1 = 0
		self.r2 = 0
		self.r3 = 0
		self.r4 = 0
		self.r5 = 0
		self.r6 = 0
		self.r7 = 0
		self.r8 = 0
		self.r9 = 0
		self.r10 = 0
		self.r11 = 0
		self.r12 = 0
		self.rip = 0x13371000
		self.r14 = 0xCAFE3FFC
		self.r15 = 0xCAFE3FFC
		self.flags = 4

class program:
	def __init__(self):
		self.header = 0
		self.e_entry = 0
		self.program_headers_size = 0
		self.e_shoff = 0
		self.section_header_size = 0

class unknown:
	def __init__(self):
		self.prog = program()
		self.st1 = None
		self.sections = None
		self.file = None

class section:
	def __init__(self):
		self.sh_name = None
		self.sh_addr = None
		self.sh_size = None
		self.sh_offset = None
		self.sh_dsize = 0
		self.flags = None
		self.copy_cnt = None
		self.sh_link = None
		self.data = []

# Globals
sections = []
keys = [
	"bfn1drrdpfqb9p1ztpbhzfzzssmtx4kw",
	"x51eyob6ie0nopa9kzaoy4dje6jwwk6s",
	"jtrbda50d86ov87hanjcxsbrus944xna",
	"0fi60erlof5ib5or2y7hh7y1cd4kjuue",
	"exl8xx81h8tkc08wxxh799i8o0o8vcuc",
	"3ld68478oeyhu23a0orgc19ap6x4p60u",
	"cs58ey0sec9g3ygarxxnthtzn96nzh23",
	"phch0c8fz2rnj0xxrfdza3wblcluk5ah",
	"n366nlgbt9cqb9qs3qsfq1m2w6cynoh5",
	"3ksavqwbmmc68wf8o9fmmyw467h822ov",
	"werz2pawyf0gssv9ese6o5hv06b6gj0v",
	"j249z7e7rvp58ednrmtulbrug627s3gj",
]

def dump(data):
	for i in range(len(data)//16):
		x = data[i*16:i*16+16]
		print([hex(i)[2:].zfill(2) for i in x])

def file_init(unkn):
	unkn.prog.header = unkn.file.read(4)
	unkn.prog.e_entry = unpack("I", unkn.file.read(4))[0]
	unkn.prog.program_headers_size = unpack("I", unkn.file.read(4))[0]
	unkn.prog.e_shoff = unpack("I", unkn.file.read(4))[0]
	unkn.prog.section_header_size = unpack("I", unkn.file.read(4))[0]

"""
	print("Header \t\t\t" , unkn.prog.header)
	print("EntryPoint \t\t" , hex(unkn.prog.e_entry))
	print("Program Header Size \t" , hex(unkn.prog.program_headers_size))
	print("E_shoff \t\t" , hex(unkn.prog.e_shoff))
	print("Section Header Size \t" , hex(unkn.prog.section_header_size))
"""

def parse_file(unkn,filename):
	unkn.file = open(filename,"rb")

	file_init(unkn)

	# Do Program Header thing


	for _ in range(unkn.prog.section_header_size):
		assert unpack("I", unkn.file.read(4))[0] == 0xDEADBEEF

		sect = section()

		name = ""
		while True:
			x = unkn.file.read(1)
			if x == b'\0':
				break
			name += x.decode()

		sect.sh_name = name # update

		sect.sh_size = unpack("I", unkn.file.read(4))[0]
		sect.sh_addr = unpack("I", unkn.file.read(4))[0]
		sect.flags = unpack("I", unkn.file.read(4))[0]
		sect.sh_dsize = unpack("I", unkn.file.read(4))[0]

		# print("\nFound Section")
		# print("Section Name \t\t\t", sect.sh_name)
		# print("Section Alloc Size \t\t", hex(sect.sh_size))
		# print("Section Virtual Address \t", hex(sect.sh_addr))
		# print("Section Flags \t\t\t", hex(sect.flags))
		# print("Section Data Size \t\t", hex(sect.sh_dsize))

		for _ in range(sect.sh_dsize):
			sect.data.append(unpack("B", unkn.file.read(1))[0])
			
		for j in range(len(keys)):
			if(sect.sh_name == ".chk"+str(j)):
				for i in range(len(sect.data)):
					sect.data[i] ^= ord(keys[j][i % 32])
					
		# print(sect.data)
		sections.append(sect)

	# Do Program Header thing


	sect = section()
	sect.sh_name = "stack"
	sect.sh_size = 0x3000
	sect.sh_addr = 0xCAFE3000
	sect.flags = 3

	sections.append(sect)

def print_data():
	print("Header \t\t\t" , unkn.prog.header)
	print("EntryPoint \t\t" , hex(unkn.prog.e_entry))
	print("Program Header Size \t" , hex(unkn.prog.program_headers_size))
	print("E_shoff \t\t" , hex(unkn.prog.e_shoff))
	print("Section Header Size \t" , hex(unkn.prog.section_header_size))
	print("\nSECTIONS: ")
	print("Section Name \t Section Data Size  Section Alloc Size \t Section Virtual Address \t Section Flags")
	for obj in sections:
		print(" ", obj.sh_name, "\t\t", hex(obj.sh_dsize), "\t   ", hex(obj.sh_size), "\t\t  ", hex(obj.sh_addr), "\t\t\t    ", hex(obj.flags))

def find_sec_addr(ins):
	for obj in sections:
		if(obj.sh_addr <= ins and ins < (obj.sh_addr+obj.sh_size)):
			return obj

def readbyte(ins,flags):
	obj = find_sec_addr(ins)
	assert (obj.flags & (flags | 1)) != 0
	return obj.data[ins - obj.sh_addr]

def readlong(ins,flags):
	obj = find_sec_addr(ins)
	assert (obj.flags & 1) != 0 and (obj.flags & flags) != 0
	z = ins - obj.sh_addr
	tmp = 0
	for i in range(4):
		tmp |= obj.data[i + z] << i * 8
	return hex(tmp)

# def store_stack():

def set_flag_3(reg , flag):
	if(flag == 0):
		reg.flags &= 0xFB
	else:
		reg.flags | 4

def set_flag_1(reg , flag):
	if(flag == 0):
		reg.flags &= 0xFE
	else:
		reg.flags | 1

def set_flag_2(reg , flag):
	if(flag == 0):
		reg.flags &= 0xFD
	else:
		reg.flags | 2

def get_reg(r):
	assert r <= 0xF
	return "r"+str(r)

def parse_mode(reg,unkn,data):
	ins_count = 2
	dat1 = data & 0xF;
	dat2 = data >> 4;
	assert not((dat1 == 0 and dat2 != 0))

	op1 = op2 = None
	if(dat1 != 0):
		if(dat1 == 1):
			x = readbyte(reg.r14_IP,4)
			reg.r14_IP += 1
			op1 = get_reg(x)
			ins_count = 3
		elif(dat1 == 2):
			op1 = readlong(reg.r14_IP,4)
			reg.r14_IP += 4
			ins_count = 6
		else:
			assert (dat1 & 3) != 0

			tmp = None
			if((dat1 & 1) != 0):
				x = readbyte(reg.r14_IP,4)
				reg.r14_IP += 1
				tmp = get_reg(x)
				op1 = "[" + tmp + "]"
				ins_count = 3
			if((dat1 & 2) != 0):
				x = readlong(reg.r14_IP,4)
				reg.r14_IP += 4
				op1 = "[" + tmp + " + " + x + "]"
				ins_count += 4

	if(dat2 != 0):
		if(dat2 == 1):
			x = readbyte(reg.r14_IP,4)
			reg.r14_IP += 1
			op2 = get_reg(x)
			ins_count = 3
		elif(dat2 == 2):
			op2 = readlong(reg.r14_IP,4)
			reg.r14_IP += 4
			ins_count = 6
		else:
			assert (dat2 & 3) != 0

			tmp = None
			if((dat2 & 1) != 0):
				x = readbyte(reg.r14_IP,4)
				reg.r14_IP += 1
				tmp = get_reg(x)
				op2 = "[" + tmp + "]"
				ins_count = 3
			if((dat2 & 2) != 0):
				x = readlong(reg.r14_IP,4)
				reg.r14_IP += 4
				op2 = "[" + tmp + " + " + x + "]"
				ins_count += 4

	# print(ins_count, op1, op2)
	return ins_count, op1, op2


def executeIns(reg,unkn):
	print(hex(reg.r14_IP)[2:].zfill(8),end=" ")

	opc = readbyte(reg.r14_IP, 4)
	reg.r14_IP += 1

	x = readbyte(reg.r14_IP, 4)
	reg.r14_IP += 1

	c, op1, op2 = parse_mode(reg,unkn,x)

	assert opc < 0x32

	if(opc == 0):
		print( op1 , "=" , op2)
	elif(opc == 1):
		print("byte" , op1 , "=" , op2)
	elif(opc == 2):
		print("ushort" , op1 , "=" , op2)
	elif(opc == 3):
		print("OPCODE" , opc , "MODE" , x , "OP1" , op1 , "OP2" , op2)
	elif(opc == 4):
		print("EXIT")
	elif(opc == 5):
		print("RET\n")
	elif(opc == 6):
		print("CALL", op1)
	elif(opc == 7):
		print("helper_function()")
	elif(opc == 8):
		print("if "+op1+"<<"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 9):
		print("if "+op1+">>"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 10):
		print("if "+op1+"+"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 11):
		print("byte if "+op1+"+"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 12):
		print("ushort if "+op1+"+"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 13):
		print("if "+op1+"-"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 14):
		print("byte if "+op1+"-"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 15):
		print("ushort if "+op1+"-"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 16):
		print("if "+op1+"*"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 17):
		print("byte if "+op1+"*"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 18):
		print("ushort if "+op1+"*"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 19):
		print("if "+op1+"/"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0) | r6 ="+op1+"%"+op2)
	elif(opc == 20):
		print("byte if "+op1+"/"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0) | r6 ="+op1+"%"+op2)
	elif(opc == 21):
		print("ushort if "+op1+"/"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0) | r6 ="+op1+"%"+op2)
	elif(opc == 22):
		print("if "+op1+"^"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 23):
		print("byte if "+op1+"^"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 24):
		print("ushort if "+op1+"^"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 25):
		print("if "+op1+"&"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 26):
		print("byte if "+op1+"&"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 27):
		print("ushort if "+op1+"&"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 28):
		print("if "+op1+"|"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 29):
		print("byte if "+op1+"|"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 30):
		print("ushort if "+op1+"|"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 31):
		print("OPCODE" , opc , "MODE" , x , "OP1" , op1 , "OP2" , op2)
	elif(opc == 32):
		print("OPCODE" , opc , "MODE" , x , "OP1" , op1 , "OP2" , op2)
	elif(opc == 33):
		print("OPCODE" , opc , "MODE" , x , "OP1" , op1 , "OP2" , op2)
	elif(opc == 34):
		print("push", op1)
	elif(opc == 35):
		print("pop", op1)
	elif(opc == 36):
		print(opc, "\t| swap(",op1,op2,")")
	elif(opc == 37):
		print("if "+op1+"+1==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 38):
		print("if "+op1+"-1==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 39):
		print("if "+op1+"<"+op2+" F2=1")
	elif(opc == 40):
		print("byte if "+op1+"=="+op2+" F1=1 | if "+op1+"<"+op2+" F1=0 F2=1 | if "+op2+"<"+op1+" F1=0 F2=0")
	elif(opc == 41):
		print("ushort if "+op1+"=="+op2+" F1=1 | if "+op1+"<"+op2+" F1=0 F2=1 | if "+op2+"<"+op1+" F1=0 F2=0")
	elif(opc == 42):
		print("if "+op1+"&"+op2+"==0 ? (F1=1 F2=0 : F1=0 F2=0)")
	elif(opc == 43):
		print("JMP",op1)
	elif(opc == 44):
		print("if F2 JMP",op1)
	elif(opc == 45):
		print("if !F2 JMP",op1)
	elif(opc == 46):
		print("if !F1 !F2 JMP",op1)
	elif(opc == 47):
		print("if !F1 F2 JMP",op1)
	elif(opc == 48):
		print("if F2 JMP",op1)
	elif(opc == 49):
		print("OPCODE" , opc , "MODE" , x , "OP1" , op1 , "OP2" , op2)


if __name__ == '__main__':
	reg = registers()
	unkn = unknown()

	parse_file(unkn,"pyaz.xvm")

	reg.r14_IP = unkn.prog.e_entry
	print_data()
	exit()

	for obj in sections:
		if(obj.sh_name == ".text"):
			# while(reg.r14_IP < obj.sh_dsize + obj.sh_addr):
			# 	executeIns(reg, unkn)
			continue
		elif(obj.sh_name.startswith(".chk")):
			print("SECTION",obj.sh_name)
			reg.r14_IP = obj.sh_addr
			if(obj.sh_name != ".chk11"):
				while(reg.r14_IP < obj.sh_dsize + obj.sh_addr - 33):
					executeIns(reg, unkn)
			else:
				while(reg.r14_IP < obj.sh_dsize + obj.sh_addr):
					executeIns(reg, unkn)