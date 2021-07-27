# Time

Attachments:
* [family](./family)

## Solution
This is an nanomites challenge.

### Main
```c
int __cdecl main()
{
  __pid_t pid; // [esp+Ch] [ebp-Ch]

  puts("Family member checker");
  pid = fork();
  if ( pid == -1 )
  {
    puts("Something went wrong, try again..");
  }
  else if ( pid )
  {
    debugger(pid);
  }
  else
  {
    debugee();
  }
  return 0;
}
```
Simple nanomite debugger and debugee.

### `debugger`
```c
void __cdecl debugger(__pid_t pid)
{
  int stat_loc; // [esp+0h] [ebp-58h] BYREF
  user_regs_struct regs; // [esp+4h] [ebp-54h] BYREF
  int v3; // [esp+48h] [ebp-10h]
  int v4; // [esp+4Ch] [ebp-Ch]

  v3 = 0;
  v4 = -1;
  while ( 1 )
  {
    waitpid(pid, &stat_loc, 0);
    if ( (unsigned __int8)stat_loc != 127 || BYTE1(stat_loc) != SIGTRAP )
      break;
    ptrace(PTRACE_GETREGS, pid, 0, &regs);
    if ( regs.eax == 0x69696969 )
    {
      regs.eax = (unsigned __int8)(LOBYTE(regs.ebx) ^ LOBYTE(regs.edx));
    }
    else if ( regs.eax <= 0x69696969 )
    {
      if ( regs.eax == 0x55555555 )
      {
        ++v4;
      }
      else if ( regs.eax <= 0x55555555 )
      {
        if ( regs.eax == 0x44444444 )
        {
          regs.edx = *(unsigned __int8 *)(v4 + 0x804A0E0);
        }
        else if ( regs.eax <= 0x44444444 )
        {
          if ( regs.eax == 0x33333333 )
          {
            regs.edx = *(unsigned __int8 *)(v4 + 0x804A060);
          }
          else if ( regs.eax <= 0x33333333 )
          {
            if ( regs.eax == 0x22222222 )
            {
              regs.edx = *(unsigned __int8 *)(v4 + 0x804A020);
            }
            else if ( regs.eax <= 0x22222222 )
            {
              if ( regs.eax == 0x11111111 )
              {
                regs.edx = *(unsigned __int8 *)(v4 + 0x804A0A0);
              }
              else if ( regs.eax <= 0x11111111 )
              {
                if ( regs.eax == 0x1337 )
                {
                  if ( (regs.eflags & 0x40) != 0 )
                    regs.eip = regs.edx;
                  else
                    regs.eip = regs.ebx;
                }
                else if ( regs.eax <= 0x1337 )
                {
                  if ( regs.eax == 0xF0F0F0F0 )
                  {
                    regs.eax = LOBYTE(regs.ebx) + LOBYTE(regs.edx);
                  }
                  else if ( regs.eax == 0xFEFEFEFE )
                  {
                    regs.eax = LOBYTE(regs.ebx) - LOBYTE(regs.edx);
                  }
                }
              }
            }
          }
        }
      }
    }
    ptrace(PTRACE_SETREGS, pid, 0, &regs);
    ptrace(PTRACE_CONT, pid, 0, 0);
  }
}
```
The debugger is hit when `SIGTRAP` exception occurs. Then it checks the `eax` values and performs the task related to that and continues the execution.

### `debugee`
```c
void __cdecl debugee()
{
  const char *flag;

  ptrace(PTRACE_TRACEME, 0, 0);
  printf("Enter password:");
  flag = (const char *)calloc(0x100u, 1u);
  __isoc99_scanf("%255s", flag);
  if ( sub_804948F(flag) )
    printf("Get out");
  else
    printf("Welcome to the family");
}
```

### `sub_804948F`
This function checks our flag. Raw assembly...
```asm
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
                 int     3               ; Trap to Debugger

 loop_run:                               ; DATA XREF: sub_804948F+23↑o
                                         ; sub_804948F+A8↓o
                 mov     eax, 62F1FE94h
                 xor     eax, 37A4ABC1h
                 int     3               ; Trap to Debugger
                 mov     eax, 0B23A45DDh
                 xor     eax, 810976EEh
                 int     3               ; Trap to Debugger
                 lodsb
                 mov     bl, al
                 mov     eax, 31711ECh
                 xor     eax, 6A7E7885h
                 int     3               ; Trap to Debugger
                 mov     bl, al
                 mov     eax, 0F188AEA9h
                 xor     eax, 0D3AA8C8Bh
                 int     3               ; Trap to Debugger
                 mov     eax, 576FD59Dh
                 xor     eax, 0A79F256Dh
                 int     3               ; Trap to Debugger
                 mov     bl, al
                 mov     eax, 5E1C6478h
                 xor     eax, 4F0D7569h
                 int     3               ; Trap to Debugger
                 mov     eax, 34C4AAF5h
                 xor     eax, 0CA3A540Bh
                 int     3               ; Trap to Debugger
                 mov     bl, al
                 mov     eax, 0C7CD9F18h
                 xor     eax, 8389DB5Ch
                 int     3               ; Trap to Debugger
                 cmp     bl, dl
                 mov     eax, 1337h
                 lea     ebx, false
                 lea     edx, increment
                 int     3               ; Trap to Debugger

 increment:                              ; DATA XREF: sub_804948F+98↑o
                 inc     ecx
                 cmp     ecx, 29h ; ')'
                 mov     eax, 1337h
                 lea     ebx, loop_run
                 lea     edx, true
                 int     3               ; Trap to Debugger

 true:                                   ; DATA XREF: sub_804948F+AE↑o
                 xor     eax, eax
                 jmp     short exit
 ; ---------------------------------------------------------------------------

 false:                                  ; DATA XREF: sub_804948F+1D↑o
                                         ; sub_804948F+92↑o
                 mov     eax, 0FFFFFFFFh

 exit:                                   ; CODE XREF: sub_804948F+B7↑j
                 mov     esp, ebp
                 pop     ebp
                 retn
```
So we can see the eax values and identify what is going on. Reference [here](./ref.asm)

### Decryption
It basically xores, adds, subtracts, and compares to hardcoded values. We can brute char by char and get flag.

Script [here](./family_solve.py)

## Flag
> IJCTF{why_did_i_do_this_7aebed65fda491cc}
