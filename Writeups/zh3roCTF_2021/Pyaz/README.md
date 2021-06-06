# Pyaz

```
$ ./xvm pyaz.xvm
```

Attachments:
* [xvm](./xvm)
* [pyaz.xvm](./pyaz.xvm)

## Solution

The XVM is same as [Optimize Me](https://github.com/1GN1tE/CTF_Writeups/tree/main/Writeups/zh3roCTF_2021/OptimiseMe) chall

I ran my interpreter on the bytecode. It has many sections

```
Header                   b'xvm\x03'
EntryPoint               0x13371000
Program Header Size      0x0
E_shoff                  0x556
Section Header Size      0xe

SECTIONS: 
Section Name     Section Data Size  Section Alloc Size   Section Virtual Address         Section Flags
  .text                  0x72c      0x1000                 0x13371000                        0x5      
  .data                  0x760      0x1000                 0x1337f000                        0x3      
  .chk0                  0xe5a      0x1000                 0x31337000                        0x7      
  .chk2                  0xe3b      0x1000                 0x31339000                        0x7      
  .chk4                  0xe5e      0x1000                 0x3133b000                        0x7      
  .chk6                  0xe50      0x1000                 0x3133d000                        0x7      
  .chk8                  0xe61      0x1000                 0x3133f000                        0x7      
  .chk10                 0xe6f      0x1000                 0x31341000                        0x7      
  .chk11                 0x38f      0x1000                 0x31342000                        0x7      
  .chk1                  0xe64      0x1000                 0x31338000                        0x7      
  .chk3                  0xe42      0x1000                 0x3133a000                        0x7      
  .chk5                  0xe61      0x1000                 0x3133c000                        0x7      
  .chk7                  0xe4c      0x1000                 0x3133e000                        0x7      
  .chk9                  0xe6c      0x1000                 0x31340000                        0x7      
  stack                  0x0        0x3000                 0xcafe3000                        0x3      
```

### Decompiling Disassembly

- Initially it asks and read the flag
- A loop of 360 rounds is run.
- Every 32 rounds a `chk$` chunk is decrypted and functions are called in it
- The 32-byte key for decryption comes from the previous chunk
- Depending on the succes of the called functions it says right or wrong password

So I updated my interpreter to decrypt those chunks [interpreter.py](./interpreter.py)

### Analyzing Chunks

Every chunk has 30 function to check for a particular bit of a particular byte of the flag. E.g.

```
31340dd8 push r14
31340ddb r14 = r15
31340ddf [r14 + 0xfffffff0] = r1
31340de7 r0 = [r14 + 0xfffffff0]
31340def byte r4 = [r0 + 0x1]
31340df7 byte [r14 + 0xffffffef] = r4
31340dff byte r5 = [r14 + 0xffffffef]
31340e07 if r5 >> 0x6
31340e0e if r5 & 0x1
31340e15 if r5<0x1 F2=1
31340e1c if F2 JMP 0x31340e33
31340e22 [r14 + 0xfffffffc] = 0x0
31340e2d JMP 0x31340e3e
31340e33 [r14 + 0xfffffffc] = 0x1
31340e3e r0 = [r14 + 0xfffffffc]
31340e46 pop r14
31340e49 RET
```

So I parsed all the bit checks. [check.txt](./check.txt)

For getting flag, I took an array of null bytes and flipped the set bit. [solve.py](./solve.py)

## Flag
> zh3r0{967a23927d374a7e58e7a12ef62f5}