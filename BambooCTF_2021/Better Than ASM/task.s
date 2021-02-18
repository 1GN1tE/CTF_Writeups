	.text
	.intel_syntax noprefix
	.file	"task.ll"
	.globl	check                           # -- Begin function check
	.p2align	4, 0x90
	.type	check,@function
check:                                  # @check
	.cfi_startproc
# %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	push	r14
	.cfi_def_cfa_offset 24
	push	rbx
	.cfi_def_cfa_offset 32
	sub	rsp, 16
	.cfi_def_cfa_offset 48
	.cfi_offset rbx, -32
	.cfi_offset r14, -24
	.cfi_offset rbp, -16
	mov	qword ptr [rsp + 8], rdi
	mov	dword ptr [rsp + 4], 1
	mov	dword ptr [rsp], 0
	.p2align	4, 0x90
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	movsxd	rbx, dword ptr [rsp]
	mov	edi, offset what
	call	strlen
	cmp	rbx, rax
	jae	.LBB0_3
# %bb.2:                                #   in Loop: Header=BB0_1 Depth=1
	mov	r14, qword ptr [rsp + 8]
	movsxd	rbx, dword ptr [rsp]
	movzx	ebp, byte ptr [r14 + rbx]
	inc	rbx
	mov	edi, offset what
	call	strlen
	mov	rcx, rax
	mov	rax, rbx
	xor	edx, edx
	div	rcx
	xor	bpl, byte ptr [r14 + rdx]
	movsx	eax, bpl
	movsxd	rcx, dword ptr [rsp]
	movsx	ecx, byte ptr [rcx + what]
	xor	edx, edx
	cmp	eax, ecx
	sete	dl
	and	dword ptr [rsp + 4], edx
	inc	dword ptr [rsp]
	jmp	.LBB0_1
.LBB0_3:
	mov	eax, dword ptr [rsp + 4]
	add	rsp, 16
	.cfi_def_cfa_offset 32
	pop	rbx
	.cfi_def_cfa_offset 24
	pop	r14
	.cfi_def_cfa_offset 16
	pop	rbp
	.cfi_def_cfa_offset 8
	ret
.Lfunc_end0:
	.size	check, .Lfunc_end0-check
	.cfi_endproc
                                        # -- End function
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	push	r14
	.cfi_def_cfa_offset 24
	push	rbx
	.cfi_def_cfa_offset 32
	sub	rsp, 80
	.cfi_def_cfa_offset 112
	.cfi_offset rbx, -32
	.cfi_offset r14, -24
	.cfi_offset rbp, -16
	mov	dword ptr [rsp + 12], 0
	mov	edi, offset .L.str
	xor	eax, eax
	call	printf
	mov	edi, offset .L.str.1
	xor	eax, eax
	call	printf
	mov	edi, offset .L.str.2
	xor	eax, eax
	call	printf
	lea	rbx, [rsp + 16]
	mov	edi, offset .L.str.3
	mov	rsi, rbx
	xor	eax, eax
	call	__isoc99_scanf
	mov	rdi, rbx
	call	strlen
	mov	rbx, rax
	mov	edi, offset what
	call	strlen
	cmp	rbx, rax
	je	.LBB1_2
# %bb.1:
	mov	edi, offset .L.str.4
	xor	eax, eax
	call	printf
	mov	dword ptr [rsp + 12], 1
	jmp	.LBB1_10
.LBB1_2:
	lea	rdi, [rsp + 16]
	call	check
	test	eax, eax
	je	.LBB1_6
# %bb.3:
	mov	dword ptr [rsp + 8], 0
	lea	r14, [rsp + 16]
	.p2align	4, 0x90
.LBB1_4:                                # =>This Inner Loop Header: Depth=1
	movsxd	rbx, dword ptr [rsp + 8]
	mov	rdi, r14
	call	strlen
	cmp	rbx, rax
	jae	.LBB1_9
# %bb.5:                                #   in Loop: Header=BB1_4 Depth=1
	movsxd	rbx, dword ptr [rsp + 8]
	movzx	ebp, byte ptr [rsp + rbx + 16]
	mov	edi, offset secret
	call	strlen
	mov	rcx, rax
	mov	rax, rbx
	xor	edx, edx
	div	rcx
	movzx	eax, byte ptr [rdx + secret]
	xor	eax, ebp
	movsxd	rcx, dword ptr [rsp + 8]
	mov	byte ptr [rsp + rcx + 16], al
	inc	dword ptr [rsp + 8]
	jmp	.LBB1_4
.LBB1_6:
	mov	dword ptr [rsp + 4], 0
	lea	r14, [rsp + 16]
	.p2align	4, 0x90
.LBB1_7:                                # =>This Inner Loop Header: Depth=1
	movsxd	rbx, dword ptr [rsp + 4]
	mov	rdi, r14
	call	strlen
	cmp	rbx, rax
	jae	.LBB1_9
# %bb.8:                                #   in Loop: Header=BB1_7 Depth=1
	movsxd	rbx, dword ptr [rsp + 4]
	movzx	ebp, byte ptr [rbx + flag]
	mov	edi, offset secret
	call	strlen
	mov	rcx, rax
	mov	rax, rbx
	xor	edx, edx
	div	rcx
	movzx	eax, byte ptr [rdx + secret]
	xor	eax, ebp
	movsxd	rcx, dword ptr [rsp + 4]
	mov	byte ptr [rsp + rcx + 16], al
	inc	dword ptr [rsp + 4]
	jmp	.LBB1_7
.LBB1_9:
	lea	rsi, [rsp + 16]
	mov	edi, offset format
	xor	eax, eax
	call	printf
	mov	dword ptr [rsp + 12], 0
.LBB1_10:
	mov	eax, dword ptr [rsp + 12]
	add	rsp, 80
	.cfi_def_cfa_offset 32
	pop	rbx
	.cfi_def_cfa_offset 24
	pop	r14
	.cfi_def_cfa_offset 16
	pop	rbp
	.cfi_def_cfa_offset 8
	ret
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.type	format,@object                  # @format
	.data
	.globl	format
	.p2align	4
format:
	.asciz	"\n\360\237\230\202\360\237\221\214\360\237\230\202\360\237\221\214\360\237\230\202\360\237\221\214 flag{%s} \360\237\221\214\360\237\230\202\360\237\221\214\360\237\230\202\360\237\221\214\360\237\230\202\n\n\000\000"
	.size	format, 64

	.type	flag,@object                    # @flag
	.globl	flag
	.p2align	4
flag:
	.asciz	"\035U#hJ7.8\006\026\003rUO=[bg9JmtGt`7U\013nNjD\001\003\0220\031;OVIaM\000\b,qu<g\035;K\000}Y\000\000\000\000\000\000\000"
	.size	flag, 64

	.type	what,@object                    # @what
	.globl	what
	.p2align	4
what:
	.asciz	"\027/'\027\035Jy\003,\021\036&\nexjONacA-&\001LANH'.&\022>#'Z\017O\013%:(&HI\fJylL'\036mtdC\000\000\000\000\000\000\000"
	.size	what, 64

	.type	secret,@object                  # @secret
	.globl	secret
	.p2align	4
secret:
	.asciz	"B\n|_\"\006\033g7#\\F\n)\t0Q8_{Y\023\030\rP\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
	.size	secret, 64

	.type	.L.str,@object                  # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"Only the chosen one will know what the flag is!\n"
	.size	.L.str, 49

	.type	.L.str.1,@object                # @.str.1
.L.str.1:
	.asciz	"Are you the chosen one?\n"
	.size	.L.str.1, 25

	.type	.L.str.2,@object                # @.str.2
.L.str.2:
	.asciz	"flag: "
	.size	.L.str.2, 7

	.type	.L.str.3,@object                # @.str.3
.L.str.3:
	.asciz	"%64s"
	.size	.L.str.3, 5

	.type	.L.str.4,@object                # @.str.4
.L.str.4:
	.asciz	"\n\360\237\230\240\360\237\230\241\360\237\230\240\360\237\230\241\360\237\230\240\360\237\230\241 You are not the chosen one! \360\237\230\241\360\237\230\240\360\237\230\241\360\237\230\240\360\237\230\241\360\237\230\240\n\n"
	.size	.L.str.4, 81

	.section	".note.GNU-stack","",@progbits
