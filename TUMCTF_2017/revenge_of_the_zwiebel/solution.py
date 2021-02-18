import sys
import r2pipe

filename = "./zwiebel"			# Rarun2 profile for stdin
profile = """
#!/usr/bin/rarun2
program="""+filename+"""
stdin="AAAA"
stdout=
"""
with open('profile.rr2', 'w+') as f:
	f.write(profile)

r2 = r2pipe.open(filename)
r2.cmd("e dbg.profile=profile.rr2")
r2.cmd("doo")					# reopen for debugging
r2.cmd("db 0x4006a3")			# set breakpoint at `call rcx`

####################
# Disabling ptrace #
####################

#	0x00433fa7			mov eax, 0x65
#	0x00433fac			syscall

r2.cmd("db 0x433FAC")
r2.cmd("dc")
if (r2.cmdj("drj")["rip"]) != 0x00433fac:
	print("[-] Syscall Not found")
	exit()
r2.cmd("ds")
r2.cmd("dr rax = 0x0")
r2.cmd("dc")


##############
# Check Algo #
##############

#	0x7f7b0eda0025		mov rax, rbx				# rbx -> Flag
#	0x7f7b0eda0028		xor rcx, rcx
#	0x7f7b0eda002b		mov cl, byte [rax + 0xc]	# rax + 0xc -->Flag[0xc]
#	0x7f7b0eda002e		nop
#	0x7f7b0eda002f		nop
#	0x7f7b0eda0030		and cl, 8					# Checking bits
#	0x7f7b0eda0033		jecxz 0x7f7b0eda004e

# Flag memory alloc
flag = [0x20]*25

while True:
	disasm = []
	while True:
		r2.cmd("ds")
		current_instruction = r2.cmdj("pdj 1")[0]
		disasm.append(current_instruction['opcode'])
		if ("jecxz" in disasm[-1]) and ("and" in disasm[-2]):
			break

# jecxz 0x7fc9fca7a04e
# and cl, 8
# nop
# nop
# mov cl, byte [rax + 0xc]

	not_check = 0
	for i in range(-5,-2):
		if("mov cl, byte" in disasm[i]):
			offset = disasm[i].split("rax")[1][:-1][3:]
			break
	if("not" in disasm[-3]):
		offset = disasm[-4].split("rax")[1][:-1][3:]
		not_check = 1
	if not offset:
		offset = "0"
	try:
		offset = int(offset, 16)
	except:
		print(offset)

	and_value = int(disasm[-2].split(", ")[1], 16)

	if(not_check):
		flag[offset] = flag[offset] & (0xFF ^ and_value)
	else:
		flag[offset] = flag[offset] | and_value

	r2.cmd("dr rcx = 0xff")			# Set value for jecxz
	r2.cmd("ds")					# Follow the jump

	# Print current flag
	out = ""
	for c in flag:
		if c >= 0x20 and c <= 0x7E:
			out += chr(c)
		else:
			out += " "
	sys.stdout.write("\r"+out)
	sys.stdout.flush()


#	0x7f297f03304a		loop 0x7f297f033042
#	0x7f297f03304c		jmp 0x7f297f03307b

	# Follow the loop
	while True:
		r2.cmd("ds")
		if "loop" in r2.cmdj("pdj 1")[0]['opcode']:
			break

	# Jump to new code
	target = hex(r2.cmdj("pdj 2")[1]['jump'])
	r2.cmd("db "+target)
	r2.cmd("dc")
