# Microscopic Revenge

The 2021 version is here! YAY \o/

Attachments:
* [microscopic_revenge.exe](./microscopic_revenge.exe)

## Solution
Last year Microscopic was a nanomites chall in linux, this time we are given nanomites in Windows.

### Analysis
```c
void __cdecl main(int argc, const char **argv, const char **envp)
{
  if ( getenv("YAY") )
    debugee();
  debugger();
}
```
If the environment variable `YAY` is set, it calls `debugee` else it calls `debugger`.

**Debugger**
```c
  putenv("YAY=1");
  StartupInfo.cb = 68;
  *(_QWORD *)&StartupInfo.lpReserved = 0i64;
  *(_QWORD *)&StartupInfo.lpTitle = 0i64;
  *(_QWORD *)&StartupInfo.dwY = 0i64;
  *(_QWORD *)&StartupInfo.dwYSize = 0i64;
  *(_QWORD *)&StartupInfo.dwYCountChars = 0i64;
  *(_QWORD *)&StartupInfo.dwFlags = 0i64;
  *(_QWORD *)&StartupInfo.lpReserved2 = 0i64;
  *(_QWORD *)&StartupInfo.hStdOutput = 0i64;
  ProcessInformation = 0i64;
  CreateProcessW(L"microscopic_revenge.exe", 0, 0, 0, 0, 1u, 0, 0, &StartupInfo, &ProcessInformation);
```
It sets the environment variable `YAY` and creates another process of itself.


```c
for ( i = WaitForDebugEvent(&DebugEvent, 0xFFFFFFFF); i; i = WaitForDebugEvent(&DebugEvent, 0xFFFFFFFF) )
  {
    switch ( DebugEvent.dwDebugEventCode )
    {
      case EXCEPTION_DEBUG_EVENT:
        v5 = (HANDLE *)sub_401910(&v18, (int)&DebugEvent.dwThreadId);
        CheckEax(ProcessInformation.hProcess, *v5);
        goto LABEL_20;
      case CREATE_THREAD_DEBUG_EVENT:
        v6 = (DWORD *)sub_401910(&v18, (int)&DebugEvent.dwThreadId);
        *v6 = DebugEvent.u.Exception.ExceptionRecord.ExceptionCode;
        goto LABEL_20;
      case CREATE_PROCESS_DEBUG_EVENT:
        CloseHandle(DebugEvent.u.CreateThread.hThread);
        CloseHandle(DebugEvent.u.CreateThread.lpThreadLocalBase);
        CloseHandle(DebugEvent.u.Exception.ExceptionRecord.ExceptionRecord);
        goto LABEL_20;
      case EXIT_THREAD_DEBUG_EVENT:
        // Code
        break;
      case EXIT_PROCESS_DEBUG_EVENT:
        ContinueDebugEvent(DebugEvent.dwProcessId, DebugEvent.dwThreadId, 65538);
        CloseHandle(ProcessInformation.hThread);
        CloseHandle(ProcessInformation.hProcess);
        goto LABEL_25;
      case LOAD_DLL_DEBUG_EVENT:
      case UNLOAD_DLL_DEBUG_EVENT:
        goto LABEL_20;
      default:
        printf("Ev: %u\n", DebugEvent.dwDebugEventCode);
        goto LABEL_20;
    }
```
Then it switches over the debugevents, since we know it's a nanomite chall, we are interested in `EXCEPTION_DEBUG_EVENT` which calls the function `CheckEax`.

**CheckEax**
```c
__int16 __usercall CheckEax@<ax>(void *hprocess@<edx>, HANDLE hThread)
{
  __int16 result; // ax
  char *v4; // eax
  DWORD v5; // esi
  DWORD v6; // edi
  bool v7; // zf
  int v8; // [esp-18h] [ebp-308h]
  CONTEXT Context; // [esp+10h] [ebp-2E0h] BYREF
  __int16 Buffer; // [esp+2E4h] [ebp-Ch] BYREF
  SIZE_T NumberOfBytesRead; // [esp+2E8h] [ebp-8h] BYREF

  memset(&Context.Dr0, 0, 0x2C8u);
  Context.ContextFlags = 65539;
  GetThreadContext(hThread, &Context);
  Buffer = 0;
  NumberOfBytesRead = 0;
  ReadProcessMemory(hprocess, (LPCVOID)Context.Eip, &Buffer, 2u, &NumberOfBytesRead);
  result = Buffer;
  if ( Buffer == 0xB0F )
  {
    switch ( Context.Eax )
    {
      case 1u:
        *(_BYTE *)(Context.Ecx + Context.Edx) ^= 0xEEu;
        break;
      case 2u:
        printf("%c", *(char *)(Context.Ecx + Context.Edx));
        break;
      case 3u:
        sub_4022E0(std::cin);
        break;
      case 4u:
        Context.Edx = Size;
        break;
      case 5u:
        v4 = (char *)&Block;
        if ( (unsigned int)dword_406194 >= 0x10 )
          v4 = (char *)Block;
        *(_DWORD *)(Context.Edx + 4 * Context.Ecx) = 2 * v4[Context.Ecx];
        break;
      case 6u:
        var_ecx = Context.Ecx;
        var_edx = Context.Edx;
        break;
      case 7u:
        v5 = Context.Ecx;
        v6 = Context.Edi;
        v8 = *(_DWORD *)(Context.Esi + 4 * Context.Ecx);
        dword_4065B0 = Context.Edx;
        *(_QWORD *)(v6 + 8 * v5) = ((__int64 (__cdecl *)(int, _DWORD, _DWORD, _DWORD, _DWORD, _DWORD))Context.Edx)(
                                     v8,
                                     0,
                                     var_edx,
                                     HIDWORD(var_edx),
                                     var_ecx,
                                     HIDWORD(var_ecx));
        break;
      case 8u:
        if ( *(_DWORD *)(8 * Context.Ecx + Context.Esi) != *(_DWORD *)(8 * Context.Ecx + Context.Edi)
          || (v7 = *(_DWORD *)(8 * Context.Ecx + Context.Esi + 4) == *(_DWORD *)(8 * Context.Ecx + Context.Edi + 4),
              Context.Edx = 0,
              !v7) )
        {
          Context.Edx = 1;
        }
        break;
    }
    Context.Eip += 2;
    result = SetThreadContext(hThread, &Context);
  }
  return result;
}
```
This switches over the value of eax and does stuff.

**Debugee**
```asm
   0x402610:    mov    ecx,0x0
   0x402615:    mov    edx,DWORD PTR ds:0x406178
   0x40261b:    mov    eax,0x1
   0x402620:    ud2
   0x402622:    add    ecx,0x1
   0x402625:    cmp    ecx,0x6
   0x402628:    jl     0x40261b
   0x40262a:    mov    ecx,0x0
   0x40262f:    mov    edx,DWORD PTR ds:0x406178
   0x402635:    mov    eax,0x2
   0x40263a:    ud2
   0x40263c:    add    ecx,0x1
   0x40263f:    cmp    ecx,0x6
   0x402642:    jl     0x402635
   0x402644:    mov    eax,0x3
   0x402649:    ud2
   0x40264b:    mov    eax,0x4
   0x402650:    ud2
   0x402652:    cmp    edx,0x28
   0x402655:    jne    0x402705
   0x40265b:    mov    ecx,0x0
   0x402660:    mov    edx,DWORD PTR ds:0x406024
   0x402666:    mov    eax,0x5
   0x40266b:    ud2
   0x40266d:    add    ecx,0x1
   0x402670:    cmp    ecx,0x28
   0x402673:    jl     0x402666
   0x402675:    mov    edx,0x5
   0x40267a:    mov    ecx,0x1db038c5
   0x40267f:    mov    eax,0x6
   0x402684:    ud2
   0x402686:    mov    ecx,0x0
   0x40268b:    mov    esi,DWORD PTR ds:0x406024
   0x402691:    mov    edi,DWORD PTR ds:0x40617c
   0x402697:    mov    edx,0x402550
   0x40269c:    mov    eax,0x7
   0x4026a1:    ud2
   0x4026a3:    add    ecx,0x1
   0x4026a6:    cmp    ecx,0x28
   0x4026a9:    jl     0x40269c
   0x4026ab:    mov    ecx,0x0
   0x4026b0:    mov    esi,DWORD PTR ds:0x40601c
   0x4026b6:    mov    edi,DWORD PTR ds:0x40617c
   0x4026bc:    mov    eax,0x8
   0x4026c1:    ud2
   0x4026c3:    test   edx,edx
   0x4026c5:    jne    0x402705
   0x4026c7:    add    ecx,0x1
   0x4026ca:    cmp    ecx,0x28
   0x4026cd:    jl     0x4026bc
   0x4026cf:    mov    ecx,0x0
   0x4026d4:    mov    edx,DWORD PTR ds:0x406020
   0x4026da:    mov    eax,0x1
   0x4026df:    ud2
   0x4026e1:    add    ecx,0x1
   0x4026e4:    cmp    ecx,0x3
   0x4026e7:    jl     0x4026da
   0x4026e9:    mov    ecx,0x0
   0x4026ee:    mov    edx,DWORD PTR ds:0x406020
   0x4026f4:    mov    eax,0x2
   0x4026f9:    ud2
   0x4026fb:    add    ecx,0x1
   0x4026fe:    cmp    ecx,0x3
   0x402701:    jl     0x4026f4
   0x402703:    jmp    0x402739
   0x402705:    mov    ecx,0x0
   0x40270a:    mov    edx,DWORD PTR ds:0x406174
   0x402710:    mov    eax,0x1
   0x402715:    ud2
   0x402717:    add    ecx,0x1
   0x40271a:    cmp    ecx,0x3
   0x40271d:    jl     0x402710
   0x40271f:    mov    ecx,0x0
   0x402724:    mov    edx,DWORD PTR ds:0x406174
   0x40272a:    mov    eax,0x2
   0x40272f:    ud2
   0x402731:    add    ecx,0x1
   0x402734:    cmp    ecx,0x3
   0x402737:    jl     0x40272a
   0x402739:    ret
```
`ud2` causes the debug event exception, then the execution passes to the `debugger`, especially the `CheckEax` which will do some stuff and the execution will again return to debugee and it will continue.

Check [this](./disasm.asm) for better refernces.

### Actual Program
```cpp
#include <stdint.h>

int main(int argc, char const *argv[])
{
  uint32_t ptr_input[];
  uint64_t ptr_enc_vals[40];
  uint64_t ptr_chk_vals[40] = {0x99e5267, 0x1d146255, 0x14c30c1d, 0x1740f458, 0x1520da10, 0x395056b, 0x15ab25ac, 0x15ab25ac, 0x4f07b72, 0xd8e21f6, 0x19bf409e, 0xca92d88, 0x19bf409e, 0x137a85e2, 0x19bf409e, 0x14c30c1d, 0xafc73b0, 0x99e5267, 0xd8e21f6, 0x19bf409e, 0xafc73b0, 0x14c30c1d, 0x14c30c1d, 0xafc73b0, 0x15ab25ac, 0x137a85e2, 0x6c75331, 0xd8e21f6, 0x4636046, 0x4636046, 0x4636046, 0xb583d11, 0xd8e21f6, 0xafc73b0, 0xed33daf, 0x247749c, 0x15ab25ac, 0x19bf409e, 0x395056b, 0x12768d58};

  printf("Flag:");
  sub_4022E0(std::cin);

  if(Size != 0x28)
    goto FAIL;

  for(int i = 0; i < 0x28; i++)
    ptr_input[i] = 2 * Block[i]

  uint64_t var_edx = 5;          // e
  uint64_t var_ecx = 0x1DB038C5; // n

  for(int i = 0; i < 0x28; i++)
    ptr_enc_vals[i] = sub_402550(ptr_input[i], var_edx, var_ecx) // pow(p,e,n)

  for(int i = 0; i < 0x28; i++)
    if(ptr_enc_vals[i] != ptr_chk_vals)
      goto FAIL;

  printf(":)\n");
  return 0;

  FAIL:
  printf(":(\n");
  return 0;
}
```
This is the actual program that is executed.

`sub_4022E0` function takes the input and puts the length of the string in `Size` and the stream in `Block`

`sub_402550` is the encryption function.
```c
__int64 __cdecl sub_402550(__int64 a, __int64 b, __int64 c)
{
  __int64 v3; // rax
  unsigned int v4; // ecx
  unsigned int v5; // ebx
  __int64 v7; // rdi
  __int64 v8; // rax
  __int64 v9; // rax
  unsigned int v10; // [esp+4h] [ebp-8h]
  int v11; // [esp+8h] [ebp-4h]
  unsigned int p_4; // [esp+18h] [ebp+Ch]

  v11 = 1;
  v10 = 0;
  v3 = a % c;
  v4 = (unsigned __int64)(a % c) >> 32;
  v5 = v3;
  LODWORD(v3) = HIDWORD(v3) | v3;
  p_4 = v4;
  if ( !(_DWORD)v3 )
    return 0i64;
  LODWORD(v7) = HIDWORD(b);
  if ( b >= 0 )
  {
    HIDWORD(v7) = b;
    if ( b > 0 )
    {
      do
      {
        if ( (v7 & 0x100000000i64) != 0 )
        {
          v8 = (__int64)(__PAIR64__(v10, v11) * __PAIR64__(v4, v5)) % c;
          v4 = p_4;
          v10 = HIDWORD(v8);
          v11 = v8;
        }
        HIDWORD(v7) = __PAIR64__(v7, HIDWORD(v7)) >> 1;
        LODWORD(v7) = (unsigned int)v7 >> 1;
        v9 = (__int64)(__PAIR64__(v4, v5) * __PAIR64__(v4, v5)) % c;
        v4 = HIDWORD(v9);
        p_4 = HIDWORD(v9);
        v5 = v9;
      }
      while ( v7 );
    }
  }
  return __PAIR64__(v10, v11);
}
```
This function is similar to pow(a,b,c) in python. So the encryption looks like basic RSA, with encryption as pow(p,e,n) where p is the plaintext.

### Decryption
We can RSA decrpyt the encrypted values and divide by 2 to get the flag chars
```py
from Crypto.Util.number import *

n = 0x1DB038C5
e = 5
ct = [0x99e5267, 0x1d146255, 0x14c30c1d, 0x1740f458, 0x1520da10, 0x395056b, 0x15ab25ac, 0x15ab25ac, 0x4f07b72, 0xd8e21f6, 0x19bf409e, 0xca92d88, 0x19bf409e, 0x137a85e2, 0x19bf409e, 0x14c30c1d, 0xafc73b0, 0x99e5267, 0xd8e21f6, 0x19bf409e, 0xafc73b0, 0x14c30c1d, 0x14c30c1d, 0xafc73b0, 0x15ab25ac, 0x137a85e2, 0x6c75331, 0xd8e21f6, 0x4636046, 0x4636046, 0x4636046, 0xb583d11, 0xd8e21f6, 0xafc73b0, 0xed33daf, 0x247749c, 0x15ab25ac, 0x19bf409e, 0x395056b, 0x12768d58]

p = 16649
q = 29917
phi = (p-1)*(q-1)

assert p*q == n
assert GCD(e, phi) == 1

d = inverse(e, phi)
flag = b''
for c in ct:
    flag += long_to_bytes(pow(c,d,n) // 2)
print(flag.decode())
```

## Flag
>  `flag{_bb3d54595a0fd50aa0b9ed1118d062b5_}`