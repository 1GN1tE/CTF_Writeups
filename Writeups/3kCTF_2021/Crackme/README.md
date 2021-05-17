# Crackme

Follow my PATH!

Attachments:
* [crackme](./crackme)

## Solution
We are given a small VM.

```c
void __fastcall main(int a1, char **a2, char **a3)
{
  cpu *cpu; // [rsp+18h] [rbp-878h]
  char v4[2137]; // [rsp+20h] [rbp-870h] BYREF
  unsigned __int64 v5; // [rsp+888h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  qmemcpy(v4, &unk_1040, sizeof(v4));
  cpu = (cpu *)malloc(0x38uLL);
  cpu->code_data = v4;
  init_cpu(cpu);
  runvm(cpu);
}
```

`init_cpu` initializes the registers
```c
void __fastcall init_cpu(cpu *cpu)
{
  cpu->R3 = 0;
  cpu->R2 = cpu->R3;
  cpu->R1 = cpu->R2;
  cpu->R0 = cpu->R1;
  cpu->R[0] = &cpu->R0;
  cpu->R[1] = &cpu->R1;
  cpu->R[2] = &cpu->R2;
  cpu->R[3] = &cpu->R3;
  cpu->X = cpu->code_data + 2048;
}
```

`runvm` executes the VM
```c
void __fastcall runvm(cpu *cpu)
{
  do
  {
    v2 = cpu->code_data[cpu->InsPointer + 1];
    v3 = cpu->code_data[cpu->InsPointer + 2];
    v1 = 0;
    switch ( cpu->code_data[cpu->InsPointer] )
    {
      case 1:
        v11 = cpu->R[v2];
        *v11 *= v3;
        break;
      case 2:
        v10 = cpu->R[v2];
        *v10 -= v3;
        break;
      case 3:
        v9 = cpu->R[v2];
        *v9 = ~*v9;
        break;
      case 4:
        v8 = cpu->R[v2];
        *v8 ^= cpu->X[v3];
        break;
      case 5:
        *cpu->R[v2] = *cpu->R[v3];
        break;
      case 6:
        *cpu->R[v2] = cpu->X[v3];
        break;
      case 7:
        if ( cpu->R0 )
        {
          cpu->InsPointer += v2;
          v1 = 1;
        }
        break;
      case 8:
        putc(cpu->R0, stdout);
        break;
      case 9:
        exit(cpu->R0);
      case 10:
        cpu->R0 = getc(stdin);
        break;
      case 11:
        v7 = cpu->R[v2];
        *v7 = *v7 << v3;
        break;
      case 12:
        v6 = cpu->R[v2];
        *v6 &= cpu->X[v3];
        break;
      case 13:
        v5 = cpu->R[v2];
        *v5 |= cpu->X[v3];
        break;
      case 14:
        v4 = cpu->R[v2];
        *v4 += *cpu->R[v3];
        break;
      default:
        break;
    }
    if ( v1 != 1 )
      cpu->InsPointer += 3;
  }
  while ( cpu->code_data[cpu->InsPointer] != 101 );
}
```

I write a disassembler to parse the opcedes. Script [here](./disasm.py) , [Ouput](./disasm.txt)

After printing some stuff it takes a character and checks them
```
0x0ba R0 = getc
0x0bd R0 ^= 0x63
0x0c0 R3 += R0

0x0c3 R0 = getc
0x0c6 ~R0
0x0c9 R0 ^= 0x8b
0x0cc R3 += R0

0x0cf R0 = getc
0x0d2 R1 = R0
0x0d5 R0 ^= 0x8a
0x0d8 R1 &= 0x8a
0x0db R1 << 1
0x0de R2 = R1
0x0e1 R1 += R0
0x0e4 R2 += R0
0x0e7 R1 &= 0x10
0x0ea R2 |= 0x10
0x0ed R1 += R2
0x0f0 R0 = R1
0x0f3 R3 = R1

0x0f6 R0 = getc
0x0f9 R1 = R0
0x0fc R1 ^= 0x85
0x0ff R0 &= 0x85
0x102 R0 *= 2
0x105 R0 += R1
0x108 R3 += R0
```

Instead of reversing the check, I just bruteforced the characters with this python [script](./solve.py)

## Flag
>  ctf{v1rtu4l_m4chine_pr0tection_is_soo_2010_xD}
