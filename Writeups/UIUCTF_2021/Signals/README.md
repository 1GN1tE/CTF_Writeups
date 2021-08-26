# Signals

This program is sending me mixed signals...

Attachments:
* [signals](./signals)

## Solution
```c
void __cdecl main(int argc, const char **argv, const char **envp)
{
  _DWORD stat_loc[3]; // [rsp+14h] [rbp-Ch] BYREF

  *(_QWORD *)&stat_loc[1] = __readfsqword(0x28u);
  if ( argc > 1 )
  {
    if ( (unsigned int)make_executable(&code, 7801LL, envp) )
    {
      puts("Challenge broke");
    }
    else if ( fork() )
    {
      wait((__WAIT_STATUS)stat_loc);
      if ( (char)((stat_loc[0] & 0x7F) + 1) >> 1 > 0 )
        puts("That flag is incorrect.");
    }
    else
    {
      ((void (__fastcall *)(void *, __int64, void *, const char *))code)(&code, 7801LL, &code, argv[1]);
    }
  }
  else
  {
    puts("Usage: ./signals flag\nFlag is ascii with the format uiuctf{...}");
  }
}
```
It reads flag as an argument. It makes the function/buffer `code` executable and calls it, passing `*flag` into rcx register.

```asm
                 lea     rax, unk_4435
                 mov     dl, [rcx]
                 xor     rbx, rbx

 loc_402C:
                 xor     [rax+rbx], dl
                 inc     rbx
                 cmp     rbx, 1Dh
                 jnz     short loc_402C
                 inc     rcx
                 jmp     rax
```
So it decrypts 0x1D bytes at `unk_4435` and calls it. Decrpytion is simple xor by the 1st char of our flag.

We know that first character of flag is `u` so we decrypt the segment at `unk_4435`. After decrypting we can see the new block is same as the above block. It decrpyts a block with the next flag character and jumps there.

So we know every block will start with `lea rax, <Address of next block>`. So the first opcode will be `0x48`. By this knowledge we can decrypt each block and get flag.

Solution IDA [script](./idascript.py)

## Flag
> uiuctf{another_ctf_another_flag_checker}
