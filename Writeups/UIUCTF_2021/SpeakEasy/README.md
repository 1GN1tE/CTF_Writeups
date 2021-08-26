# Speakeasy

The local speakeasy has a password to get in. Can you guess it?

Attachments:
* [speakeasy.exe](./speakeasy.exe)

## Solution
Analyzing with [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) says it's VMProtect.

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // rdx
  __int64 v4; // r8
  char flag[112]; // [rsp+20h] [rbp-88h] BYREF

  sub_140001170(argc, argv, envp);
  printf("\x1B[1m");
  print_slow(aTheYearIs1923);
  print_slow(aYouRecentlyMov);
  print_slow(aGreatButThisFr);
  print_slow(".");
  print_slow(".");
  print_slow(".\n");
  print_slow(aThePasswordToG);
  printf("\x1B[22m");
  printf("\x1B[33m");
  print_slow(aGoodEveningWel);
  print_slow(aMyApologiesBut);
  print_slow(aIKnowYouWantTo);
  printf("\x1B[1m");
  printf("\x1B[37m");
  print_slow(aYouFumbleYourW);
  print_slow(asc_14001F0A4);
  print_slow(asc_14001F114);
  print_slow(asc_14001F16C);
  printf("\x1B[0m");
  sub_140005820((__int64)flag, v3, v4);         // Take Input
  sub_140001630(flag);
  sub_140001000();
  printf("\x1B[0m");
  return 0;
}
```
It gives a small intro and asks for flag.

### `sub_140001630`
```c
void __fastcall sub_140001630(const char *flag)
{
  unsigned __int8 i; // [rsp+20h] [rbp-48h]
  unsigned __int8 v3[40]; // [rsp+30h] [rbp-38h] BYREF

  for ( i = 0; i < 0x28ui64; ++i )
    v3[i] = sub_1400014C0(i, flag[i]);
  if ( strlen(flag) )
    sub_1400014F0(0i64, v3[0]);
  return sub_1400015D0((__int64)v3);
}
```
This is where the main flag checking part is done. But the whole decompilation isn't shown in IDA. The actual function is...
```c
void sub_140001630(const char *flag)
{
  unsigned __int8 i; // [rsp+20h] [rbp-48h]
  unsigned __int8 buffer[40]; // [rsp+30h] [rbp-38h] BYREF

  for ( i = 0; i < 0x28ui64; ++i )
    buffer[i] = sub_1400014C0(i, flag[i]);
  for ( i = 0; i < strlen(flag); ++i )
    sub_1400014F0(i, buffer[i]);
  sub_1400015D0(buffer);
}
```
All the functions here are `VMProtect`ed. You can identify them by this form of push and call.
```asm
.text:00000001400014C0                 jmp     loc_140028270
;------------------------------------------------------------
.vmp0:0000000140028270                 push    691F661Bh
.vmp0:0000000140028275                 call    sub_140093F18
```

### Analyzing Virtualized Code
I used [NoVmp](https://github.com/can1357/NoVmp) to dump the VMs and used [Vtil](https://github.com/vtil-project/VTIL-Utils) to disassemble the VM codes.

`sub_1400014C0` : 
```
→ C:\Users\arije\Downloads\CTF\UIUCTF\SpeakEasy\vms› .\vtil.exe dump .\0000000000028270.optimized.vtil
 | | Entry point VIP:       0x2180e
 | | Stack pointer:         0x8
 | | Already visited?:      N
 | | ------------------------
 | | 0000: [ PSEUDO ]     +0x8     lddq     t120         $sp          0x0
 | | 0001: [ PSEUDO ]     +0x8     movq     t126         &&base
 | | 0002: [ PSEUDO ]     +0x8     addq     t126         0x14378
 | | 0003: [ PSEUDO ]     +0x8     movb     t124         rcx:8
 | | 0004: [ PSEUDO ]     +0x8     addq     t126         t124
 | | 0005: [ PSEUDO ]     +0x8     lddb     t127:8       t126         0x0
 | | 0006: [ PSEUDO ]     +0x8     movb     rax          t127:8
 | | 0007: [ PSEUDO ]     +0x8     movb     t128         rdx:8
 | | 0008: [ PSEUDO ]     +0x8     xorq     rax          t128
 | | 0009: [ PSEUDO ]     +0x8     vexitq   t120
```
It just xors the flag character with the value `&&base + 0x14378[i]`

`sub_1400014F0` : 
```
 | | Entry point VIP:       0x26c2b
 | | Stack pointer:         0x8
 | | Already visited?:      N
 | | ------------------------
 | | 0000: [ PSEUDO ]     +0x8     lddq     t144         $sp          0x0
 | | 0001: [ PSEUDO ]     +0x8     movq     t150         &&base
 | | 0002: [ PSEUDO ]     +0x8     addq     t150         0x143c8
 | | 0003: [ PSEUDO ]     +0x8     movb     t148         rcx:8
 | | 0004: [ PSEUDO ]     +0x8     addq     t150         t148
 | | 0005: [ PSEUDO ]     +0x8     lddb     t151:8       t150         0x0
 | | 0006: [ PSEUDO ]     +0x8     movb     rax          t151:8
 | | 0007: [ PSEUDO ]     +0x8     shrq     rax          0x1
 | | 0008: [ PSEUDO ]     +0x8     movb     t153         rdx:8
 | | 0009: [ PSEUDO ]     +0x8     xorq     rax          t153
 | | 0010: [ PSEUDO ]     +0x8     vexitq   t144
```
It just xors the buffer character with the value (`&&base + 0x143c8[i] >> 1)`

`sub_1400015D0` : This is big and includes many VMprotected functions. The flow can be understood by a [tracer](https://github.com/hasherezade/tiny_tracer). The important part is it calls memcmp(base + 0x2690) with our encypted buffer and some values.
```
→ C:\Users\arije\Downloads\CTF\UIUCTF\SpeakEasy\vms› .\vtil.exe dump .\000000000012B2EF.optimized.vtil
...
 | | | | | | Entry point VIP:       0x21f71
 | | | | | | Stack pointer:         0x0
 | | | | | | Already visited?:      N
 | | | | | | ------------------------
 | | | | | | 0000: [ PSEUDO ]     +0x0     lddq     rdx          $sp          0x20
 | | | | | | 0001: [ PSEUDO ]     +0x0     lddq     rcx          $sp          0x48
 | | | | | | 0002: [ PSEUDO ]     +0x0     movq     r8           0x22
 | | | | | | 0003: [00022106]     +0x0     vxcallq  0x2690
```

So I dumped the checking buffer and decrypted it.


Solution [script](./solve.py)

## Flag
> uiuctf{D0nt_b3_@_W3T_bl4nK3t_6n7a}
