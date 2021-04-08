# Rolling My Own

I don't trust password checkers made by other people, so I wrote my own. It doesn't even need to store the password! If you can crack it I'll give you a flag.

`nc mercury.picoctf.net 57112`

**Hints**
- It's based on [this paper](https://link.springer.com/article/10.1007%2Fs11416-006-0011-3)
- Here's the start of the password: `D1v1`

Attachments:
* [remote](./remote)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```c
void __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // edx
  __int64 v4; // rdx
  int i; // [rsp+8h] [rbp-F8h]
  int j; // [rsp+8h] [rbp-F8h]
  int k; // [rsp+Ch] [rbp-F4h]
  void (__fastcall *shell_func)(unsigned __int64 (__fastcall *)(__int64)); // [rsp+10h] [rbp-F0h]
  unsigned __int8 *output; // [rsp+18h] [rbp-E8h]
  int pos[4]; // [rsp+20h] [rbp-E0h]
  unsigned __int8 shellcode[16]; // [rsp+30h] [rbp-D0h]
  char hash[48]; // [rsp+40h] [rbp-C0h] BYREF
  char pswd[64]; // [rsp+70h] [rbp-90h] BYREF
  char input[72]; // [rsp+B0h] [rbp-50h] BYREF
  unsigned __int64 v15; // [rsp+F8h] [rbp-8h]

  v15 = __readfsqword(0x28u);
  setbuf(stdout, 0LL);
  strcpy(hash, "GpLaMjEWpVOjnnmkRGiledp6Mvcezxls");
  pos[0] = 8;
  pos[1] = 2;
  pos[2] = 7;
  pos[3] = 1;
  memset(pswd, 0, sizeof(pswd));
  memset(input, 0, 0x40uLL);
  printf("Password: ");
  fgets(pswd, 64, stdin);
  pswd[strlen(pswd) - 1] = 0;
  for ( i = 0; i <= 3; ++i )
  {
    strncat(input, &pswd[4 * i], 4uLL);
    strncat(input, &hash[8 * i], 8uLL);
  }
  output = (unsigned __int8 *)malloc(0x40uLL);
  v3 = strlen(input);
  hash_func(output, (unsigned __int8 *)input, v3);
  for ( j = 0; j <= 3; ++j )
  {
    for ( k = 0; k <= 3; ++k )
      shellcode[4 * k + j] = output[16 * k + j + pos[k]];
  }
  shell_func = (void (__fastcall *)(unsigned __int64 (__fastcall *)(__int64)))mmap(0LL, 0x10uLL, 7, 34, -1, 0LL);
  v4 = *(_QWORD *)&shellcode[8];
  *(_QWORD *)shell_func = *(_QWORD *)shellcode;
  *((_QWORD *)shell_func + 1) = v4;
  shell_func(flag_func);
  free(output);
}
```
It reads a password of max 64 chars and makes a new buffer(`input`) in the following way...
- 4 bytes of input password
- 4 bytes of a hardcoded hash (`GpLaMjEWpVOjnnmkRGiledp6Mvcezxls`)

Then it passes the data to another function...

### `hash_func`
```c
void __fastcall hash_func(unsigned __int8 *output, char *input, int len)
{
  int v3; // eax
  int i; // [rsp+20h] [rbp-90h]
  int j; // [rsp+24h] [rbp-8Ch]
  int v8; // [rsp+28h] [rbp-88h]
  int v9; // [rsp+2Ch] [rbp-84h]
  char v10[96]; // [rsp+30h] [rbp-80h] BYREF
  char v11[24]; // [rsp+90h] [rbp-20h] BYREF
  unsigned __int64 v12; // [rsp+A8h] [rbp-8h]

  v12 = __readfsqword(0x28u);
  if ( len % 12 )
    v3 = len / 12 + 1;
  else
    v3 = len / 12;
  v9 = v3;
  for ( i = 0; i < v9; ++i )
  {
    v8 = 12;
    if ( i == v9 - 1 && len % 12 )
      v8 = v9 % 12;
    MD5_Init(v10);
    MD5_Update(v10, input, v8);
    input += v8;
    MD5_Final(v11, v10);
    for ( j = 0; j <= 15; ++j )
      output[(j + 16 * i) % 64] = v11[j];
  }
}
```
So this function breaks our input into 12 byte chunks... calculates the MD5 hash of them and store into the output array.

Then some bytes from specific positions of the output is extracted to make an array of 16 bytes of shellcode and the shellcode is called giving the address of `flag_func` as argument in rdi register.

### `flag_func`
```c
unsigned __int64 __fastcall flag_func(__int64 a1)
{
  FILE *stream; // [rsp+18h] [rbp-98h]
  char s[136]; // [rsp+20h] [rbp-90h] BYREF
  unsigned __int64 v4; // [rsp+A8h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  if ( a1 == 0x7B3DC26F1LL )
/*
mov     [rbp+var_A8], rdi
mov     rax, fs:28h
mov     [rbp+var_8], rax
xor     eax, eax
mov     rax, 7B3DC26F1h
cmp     [rbp+var_A8], rax
*/
  {
    stream = fopen("flag", "r");
    if ( !stream )
    {
      puts("Flag file not found. Contact an admin.");
      exit(1);
    }
    fgets(s, 128, stream);
    puts(s);
  }
  else
  {
    puts("Hmmmmmm... not quite");
  }
  return __readfsqword(0x28u) ^ v4;
}
```
So we have to make shellcode so that it calls the function at rdi by passing `0x7B3DC26F1` in the rdi register while calling.

From the hint we can find the 1st 4 bytes of the shellcode(`\x48\x89\xFE\x48`), with this help I made a shellcode...

`\x48\x89\xFE\x48\xBF\xF1\x26\xDC\xB3\x07\x00\x00\x00\xFF\xD6` -->
```
0:  48 89 fe                mov    rsi,rdi
3:  48 bf f1 26 dc b3 07    movabs rdi,0x7b3dc26f1
a:  00 00 00
d:  ff d6                   call   rsi
```
Then I calculated the required bytes we need like this...
```
MD5(????GpLaMjEW) =  ,  ,  ,  ,  ,  ,  ,  ,48,89,fe,48,  ,  ,  ,  ,
MD5(????pVOjnnmk) =  ,  ,bf,f1,26,dc,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
MD5(????RGiledp6) =  ,  ,  ,  ,  ,  ,  ,b3,07,00,00,  ,  ,  ,  ,  ,
MD5(????Mvcezxls) =  ,00,ff,d6,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
```
Then I wrote a md5 bruteforcer which will give the suffix which satisfies the bytes at those positions.

Result we got...
```
MD5(D1v1GpLaMjEW) =  ,  ,  ,  ,  ,  ,  ,  ,48,89,fe,48,  ,  ,  ,  ,		| --> D1v1
MD5(d3AnpVOjnnmk) =  ,  ,bf,f1,26,dc,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,		| --> d3An
MD5(dC0nRGiledp6) =  ,  ,  ,  ,  ,  ,  ,b3,07,00,00,  ,  ,  ,  ,  ,		| --> dC0n
MD5(qu3rMvcezxls) =  ,00,ff,d6,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,		| --> qu3r

D1v1d3AndC0nqu3r
```
Full script [here](./solver.py)

Giving this on server gives us the flag...
```sh
$ nc mercury.picoctf.net 57112
Password: D1v1d3AndC0nqu3r
picoCTF{r011ing_y0ur_0wn_crypt0_15_h4rd!_06746440}
```

## Flag
> `picoCTF{r011ing_y0ur_0wn_crypt0_15_h4rd!_06746440}`