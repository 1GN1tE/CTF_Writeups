# Mortal Kobat

Ready for final fight ?

Attachments:
* [MortalKombat](./MortalKombat)

## Solution
Running the binary asks for a password
```

                               _..gggggppppp.._
                          _.gd$$$$$$$$$$$$$$$$$$bp._
                       .g$$$$$$P^^""j$$b""""^^T$$$$$$p.
                    .g$$$P^T$$b    d$P T;       ""^^T$$$p.
                  .d$$P^"  :$; `  :$;                "^T$$b.
                .d$$P'      T$b.   T$b                  `T$$b.
               d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b
              d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b
             d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b
            d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P            T$$b
           d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b
          :$$$      .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.g.     $$$;
          $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$
         :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$;
         $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$
        :$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
        :$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
        $$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
        $$$;      $$$$$$$$$$$$$$$                        Tb    _  :$$$
        :$$$     d$$$$$$$$$$$$$$$.                        $b.__Tb $$$;
        :$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
         $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$
         :$$$       T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$;
          $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$
          :$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;     $$$;
           T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P
            T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P
             T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P
              T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P
               T$$b.      '       $$$$$$$$$$$$$$$$$$$$$$$$$$$$P
                `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'
                  `T$$$$p..__..g$$$$$$$$$$$$$$$$$$$$$$$$$$P'
                    "^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^"
                       "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"
                           """^^^T$$$$$$$$$$P^^^"""



Enter the secret key :
```
### Main Function
```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int fd; // [rsp+2Ch] [rbp-3ED4h]
  _BYTE *data; // [rsp+38h] [rbp-3EC8h]
  char dest[16056]; // [rsp+40h] [rbp-3EC0h] BYREF
  unsigned __int64 v8; // [rsp+3EF8h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  data = malloc(0xFAC0uLL);
  memcpy(dest, &unk_F20, 0x3EB0uLL);
  RC4_decrypt("We_Don't_do_that_here", dest, data);
  fd = memfd_create((__int64)"[kworker/1:1]", 0LL);
  if ( fd == -1 )
    err_print(-1, "cannot create in-memory fd for code");
  sub_C20(fd, data, 0x3EAFLL);
  *a2 = "[kworker/1:1]";
  fexecve(fd, a2, a3);
  close(fd);
  return 0LL;
}
```
It RC4 decrypts some data with key `We_Don't_do_that_here`. Then it creates a `kworker` thread and writes the data into it's memory (`sub_C20`) and executes it. So I dumped the memory into a new binary.

```py
from Crypto.Cipher import ARC4

file = open("MortalKombat","rb").read()
data = file[0xF20 : 0xF20 + 0x3EB0]

cipher = ARC4.new(b"We_Don't_do_that_here")
decrypted = cipher.decrypt(data)

out = open("DecodedData","wb")
out.write(decrypted)
```

### Analysis of Dumped Binary
The main function doesn't have anything. The program calls a long function in `init`. All strings are decrypted in this function. It also has some seccomp stuff.
```c
  v8 = seccomp_init(2147418112LL);
  seccomp_rule_add(v8, 196608LL, 300LL, 0LL);
  seccomp_load(v8);
```
Which means
```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x06 0xc000003e  if (A != ARCH_X86_64) goto 0008
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x03 0xffffffff  if (A != 0xffffffff) goto 0008
 0005: 0x15 0x01 0x00 0x0000012c  if (A == fanotify_init) goto 0007
 0006: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0007: 0x06 0x00 0x00 0x00030000  return TRAP
 0008: 0x06 0x00 0x00 0x00000000  return KILL
```
It is a ***nanomites*** challenge.

### Debugee
```c

  pid = fork();
  if ( !pid )
  {
    v0 = mmap(0LL, 0x6B5uLL, 7, 34, -1, 0LL);
    v10 = (void (__fastcall *)(_QWORD))v0;
    *v0 = loc_203020[0];
    *(_QWORD *)((char *)v0 + 1709) = *(_QWORD *)((char *)&loc_203020[213] + 5);
    qmemcpy(
      (void *)((unsigned __int64)(v0 + 1) & 0xFFFFFFFFFFFFFFF8LL),
      (const void *)((char *)loc_203020 - ((char *)v0 - ((unsigned __int64)(v0 + 1) & 0xFFFFFFFFFFFFFFF8LL))),
      8LL * ((((_DWORD)v0 - (((_DWORD)v0 + 8) & 0xFFFFFFF8) + 1717) & 0xFFFFFFF8) >> 3));
    ptrace(PTRACE_TRACEME, 0LL, 0LL, 0LL);
    v11 = v10;
    v10(v15);
    exit(0);
  }
```
`loc_203020` contains the code that is debuged.

### Debugger
```c
  while ( waitpid(pid, &stat_loc, 0) != -1 )
  {
    switch ( stat_loc >> 8 )                    // WSTOPSIG(stat_loc)
    {
      case SIGTRAP:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v9 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip, 0LL) & 0xFFFFFFFF00000000LL | 0x90909090;
        v12.r11 = (unsigned __int8)rotl(v12.r11, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        break;
      case SIGILL:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v1 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip, 0LL);
        LOWORD(v1) = 0;
        v9 = v1 | 0x9090;
        ptrace(PTRACE_POKETEXT, (unsigned int)pid, v12.rip, v1 | 0x9090);
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v12.r11 = (unsigned __int8)rotr(v12.r11, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        break;
      case SIGFPE:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v12.r11 = (unsigned __int8)add(v12.r11, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        v9 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip, 0LL) & 0xFFFFFFFFFF000000LL | 0x909090;
        ptrace(PTRACE_POKETEXT, (unsigned int)pid, v12.rip, v9);
        break;
      case SIGSEGV:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v12.r11 = (unsigned __int8)xor(v12.r11, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        v9 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip, 0LL) & 0xFFFFFFFF00000000LL | 0x90909090;
        ptrace(PTRACE_POKETEXT, (unsigned int)pid, v12.rip, v9);
        v9 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip + 4, 0LL) & 0xFFFFFFFF00000000LL | 0x90909090;
        ptrace(PTRACE_POKETEXT, (unsigned int)pid, v12.rip + 4, v9);
        break;
      case SIGSYS:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v9 = ptrace(PTRACE_PEEKTEXT, (unsigned int)pid, v12.rip, 0LL) & 0xFFFFFFFF00000000LL | 0x90909090;
        key_answer(LOBYTE(v12.r13));
      case SIGCONT:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v12.r11 = (unsigned __int8)sub_AD7(v12.r14, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        break;
      case SIGWINCH:
        ptrace(PTRACE_GETREGS, (unsigned int)pid, 0LL, &v12);
        v12.r11 = (unsigned __int8)sub_B0B(v12.r14, v12.r10);
        ptrace(PTRACE_SETREGS, (unsigned int)pid, 0LL, &v12);
        break;
      default:
        if ( (stat_loc & 0x7F) == 0 || stat_loc >> 8 == SIGCHLD )
        {
          v13[0] = 0xCD;
          v13[1] = 0xF1;
          v13[2] = 0xF8;
          v13[3] = 0xED;
          v13[4] = 0xBE;
          v13[5] = 0xEA;
          v13[6] = 0xB9;
          v13[7] = 0xCE;
          v13[8] = 0xFC;
          v13[9] = 0xF0;
          v13[10] = 0xEB;
          v13[11] = 0xFD;
          v13[12] = 0x99;
          for ( k = 0; k <= 12; ++k )
            v13[k] ^= 0x99u;
          puts(v13);                            // That's Weird.
        }
        break;
    }
    ptrace(PTRACE_CONT, (unsigned int)pid, 0LL, 0LL);
  }
```
I used the following code to dump the debugged code.
```py
from capstone import *

CODE = decrypted[0x3020:0x36D3]
md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(CODE, 0x1000):
    print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
```

### Analysis of signals

**SIGTRAP**
```asm
int     3
```
is replaced to
```asm
rol     r11b, r10b
```

**SIGILL**
```asm
ud2
```
is replaced to
```asm
ror     r11b, r10b
```

**SIGFPE**
```asm
idiv    rcx
```
is replaced to
```asm
add     r11b, r10b
```

**SIGSEGV**
```asm
mov     rax, qword ptr ds:dword_0
```
is replaced to
```asm
xor     r11b, r10b
```

**SIGSYS**
It prints correct or wrong depending if r13 is 1 or 0.

**SIGCONT**
```asm
mov     rax, 62
mov     rdi, 0
mov     rsi, 12h
syscall
```
is replaced to
```asm
xor     r10, 65
rol     r14b, r10b
mov     r11b, r10b
```

**SIGWINCH**
```asm
mov     rax, 62
mov     rdi, 0
mov     rsi, 1Ch
syscall
```
is replaced to
```asm
xor     r10, 68
ror     r14b, r10b
mov     r11b, r10b
```

Our input is stored in r9. A byte is read and some value is calculated into r11b. Then it is compared to r12b and all the compares is stored in r13. If all check is passed r13 remains 1 and it says correct.

Parsing these checks in a [script](./solve.py) we get a flag

## Flag
>  `S3D{Th3r3_4r3_F4t3s_W0rs3_Th4n_D34th!}`