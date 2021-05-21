                mov     ecx, 0
                mov     edx, off_406178 ; ptr_str_flag

loc_40261B:
                mov     eax, 1
                ud2
; edx[ecx] ^= 0xEE
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 6
                jl      short loc_40261B
                mov     ecx, 0
                mov     edx, off_406178 ; ptr_str_flag

loc_402635:
                mov     eax, 2
                ud2
; printf("%c", edx[ecx]) // "Flag:"
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 6
                jl      short loc_402635
                mov     eax, 3
                ud2
; sub_4022E0(std::cin)
; ---------------------------------------------------------------------------
                mov     eax, 4
                ud2
; Context.Edx = Size
; ---------------------------------------------------------------------------
                cmp     edx, 28h ; '('
                jnz     loc_402705
                mov     ecx, 0
                mov     edx, off_406024 ; ptr_input

loc_402666:
                mov     eax, 5
                ud2
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 28h ; '('
                jl      short loc_402666
                mov     edx, 5
                mov     ecx, 1DB038C5h
                mov     eax, 6
                ud2
; var_ecx = ecx;
; var_edx = edx;
; ---------------------------------------------------------------------------
                mov     ecx, 0
                mov     esi, off_406024 ; ptr_input
                mov     edi, off_40617C ; ptr_enc_vals
                mov     edx, offset sub_402550

loc_40269C:
                mov     eax, 7
                ud2
; edi[ecx] = sub_402550(esi[ecx], var_edx, var_ecx)
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 28h ; '('
                jl      short loc_40269C
                mov     ecx, 0
                mov     esi, off_40601C ; ptr_chk_vals
                mov     edi, off_40617C ; ptr_enc_vals

loc_4026BC:
                mov     eax, 8
                ud2
; if(esi[ecx] != edi[ecx])
;     edx = 1
; ---------------------------------------------------------------------------
                test    edx, edx
                jnz     short loc_402705
                add     ecx, 1
                cmp     ecx, 28h ; '('
                jl      short loc_4026BC
                mov     ecx, 0
                mov     edx, off_406020 ; ptr_str_success

loc_4026DA:
                mov     eax, 1
                ud2
; edx[ecx] ^= 0xEE
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 3
                jl      short loc_4026DA
                mov     ecx, 0
                mov     edx, off_406020 ; ptr_str_success

loc_4026F4:
                mov     eax, 2
                ud2
; printf("%c", edx[ecx]) // ':)'
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 3
                jl      short loc_4026F4
                jmp     short locret_402739
; ---------------------------------------------------------------------------

loc_402705:
                mov     ecx, 0
                mov     edx, off_406174 ; ptr_str_fail

loc_402710:
                mov     eax, 1
                ud2
; edx[ecx] ^= 0xEE
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 3
                jl      short loc_402710
                mov     ecx, 0
                mov     edx, off_406174 ; ptr_str_fail

loc_40272A:
                mov     eax, 2
                ud2
; printf("%c", edx[ecx]) // ':('
; ---------------------------------------------------------------------------
                add     ecx, 1
                cmp     ecx, 3
                jl      short loc_40272A

locret_402739:
                retn