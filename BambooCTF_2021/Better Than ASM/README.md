# Better Than ASM

## Solution
- Given llvm assembly file.
- Used `llc task.ll --x86-asm-syntax=intel` to convert to assembly language
- Used `gcc -c task.s -o file.o` to compile to a binary
- Decompiled main and check functions in IDA

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  printf("Only the chosen one will know what the flag is!\n", argv, envp);
  printf("Are you the chosen one?\n");
  printf("flag: ");
  _isoc99_scanf("%64s", s);
  v3 = strlen(s);
  if ( v3 == strlen(what) )
  {
    if ( (unsigned int)check((__int64)s) )
    {
      for ( i = 0; i < strlen(s); ++i )
      {
        v4 = s[i];
        s[i] = v4 ^ secret[i % strlen(secret)];
      }
    }
    else
    {
      for ( j = 0; j < strlen(s); ++j )
      {
        v5 = flag[j];
        s[j] = v5 ^ secret[j % strlen(secret)];
      }
    }
    printf(format, s);
    v9 = 0;
  }
  else
  {
    printf(asc_367, s);
    v9 = 1;
  }
  return v9;
}

__int64 __fastcall check(__int64 a1)
{
  v4 = 1;
  for ( i = 0; i < strlen(what); ++i )
  {
    v1 = *(_BYTE *)(a1 + i);
    v4 = ((char)(*(_BYTE *)(a1 + (i + 1LL) % strlen(what)) ^ v1) == what[i]) & (unsigned __int8)v4;
  }
  return v4;
}
```


## Solution
[Script Here](./script.py)

## Flag
The most meaningful text is the flag
>flag{7h15_f14g_15_v3ry_v3ry_l0ng_4nd_1_h0p3_th3r3_4r3_n0_7yp0}
