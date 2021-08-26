                 push    ebp
                 mov     ebp, esp
                 mov     ecx, 0FFFFFFFFh
                 xor     eax, eax
                 mov     edi, [ebp+arg_0]
                 mov     esi, [ebp+arg_0]
                 repne scasb
                 not     ecx
                 dec     ecx
                 sub     ecx, 29h ; ')'
                 mov     eax, 1337h
                 lea     ebx, false
                 lea     edx, loop_run
                 int     3               ; if ZF goto edx else ebx

 loop_run:                               ; DATA XREF: sub_804948F+23?o
                                         ; sub_804948F+A8?o
                 mov     eax, 0x55555555
                 int     3               ; ++v5
                 mov     eax, 0x33333333
                 int     3               ; edx = 0x804A060[v5]
                 lodsb                   ; loads the next byte from flag
                 mov     bl, al
                 mov     eax, 0x69696969
                 int     3               ; eax = ebx ^ edx
                 mov     bl, al
                 mov     eax, 0x22222222
                 int     3               ; edx = 0x804A020[v5]
                 mov     eax, 0xf0f0f0f0
                 int     3               ; eax = ebx + edx
                 mov     bl, al
                 mov     eax, 0x11111111
                 int     3               ; edx = 0x804A0A0[v5]
                 mov     eax, 0xfefefefe
                 int     3               ; eax = ebx - edx
                 mov     bl, al
                 mov     eax, 0x44444444
                 int     3               ; edx = 0x804A0E0[v5]
                 cmp     bl, dl
                 mov     eax, 1337h
                 lea     ebx, false
                 lea     edx, increment
                 int     3               ; if ZF goto edx else ebx

 increment:                              ; DATA XREF: sub_804948F+98?o
                 inc     ecx
                 cmp     ecx, 29h ; ')'
                 mov     eax, 1337h
                 lea     ebx, loop
                 lea     edx, true
                 int     3               ; if ZF goto edx else ebx

 true:                                   ; DATA XREF: sub_804948F+AE?o
                 xor     eax, eax
                 jmp     short exit
 ; ---------------------------------------------------------------------------

 false:                                  ; DATA XREF: sub_804948F+1D?o
                                         ; sub_804948F+92?o
                 mov     eax, 0FFFFFFFFh

 exit:                                   ; CODE XREF: sub_804948F+B7?j
                 mov     esp, ebp
                 pop     ebp
                 retn
