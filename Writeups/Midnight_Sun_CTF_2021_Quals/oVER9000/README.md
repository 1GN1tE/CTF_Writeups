# oVER9000

One of our operatives managed to extract an important file and the encryption key from a spy. Sadly it is encrypted using some weird spanish encryption tool and all we could find is this shareware encryptor which is slow and has no decryption function. Can you recover the key?

Attachments:
* [encrypt](./encrypt)
* [key.txt](./key.txt)
* [crypt.bin](./crypt.bin)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```c
void __fastcall main(int a1, char **a2, char **a3)
{
  if ( a1 == 2 )
  {
    v3 = (__int16 *)malloc(0x20006uLL);
    plaintext = a2[1];
    ptr = v3;
    len = strlen(plaintext);
    _len = len;
    if ( ptr && len )
    {
      S = ptr + 3;
      v9 = len;
      for ( i = 0; i != 0x10000; ++i )
      {
        v11 = i;
        v12 = 256;
        v9 ^= (v9 << 13) ^ (((v9 << 13) ^ v9) >> 7) ^ (((v9 << 13) ^ v9 ^ (((v9 << 13) ^ v9) >> 7)) << 17);
        do
        {
          qword_4030 *= 2LL;
          --v12;
        }
        while ( v12 );
        v13 = i;
        S[v13] = v11;
      }
      v14 = 0;
      c = 0LL;
      do
      {
        for ( j = 0; j != 0x10000; ++j )
        {
          v17 = v9;
          v18 = (((v9 << 13) ^ v9) >> 7) ^ (v9 << 13) ^ v9;
          v19 = (v18 << 17) ^ v18;
          v20 = 256;
          v21 = (unsigned __int16)plaintext[v17 % _len] << 8;
          do
          {
            qword_4030 *= 2LL;
            --v20;
          }
          while ( v20 );
          v22 = v21 | (unsigned __int8)plaintext[v19 % _len];
          v23 = (((v19 << 13) ^ v19) >> 7) ^ (v19 << 13) ^ v19;
          v9 = (v23 << 17) ^ v23;
          v24 = 256;
          do
          {
            qword_4030 *= 2LL;
            --v24;
          }
          while ( v24 );
          v25 = &S[j];
          v26 = (unsigned __int16)*v25;
          v14 += v22 + v26;
          v27 = &S[(unsigned __int16)v14];
          *v25 = *v27;
          *v27 = v26;
          v28 = 256;
          do
          {
            qword_4030 *= qword_4030;
            --v28;
          }
          while ( v28 );
        }
        ++c;
      }
      while ( _len > c );
      v29 = 0;
      v30 = 0LL;
      do
      {
        for ( k = 0; k != 0x10000; ++k )
        {
          v32 = &S[k];
          v33 = *v32;
          v29 += *v32;
          v34 = &S[v29];
          *v32 = *v34;
          *v34 = v33;
          v35 = 256;
          do
          {
            qword_4030 *= qword_4030;
            --v35;
          }
          while ( v35 );
        }
        ++v30;
      }
      while ( _len > v30 );
      v36 = S[(unsigned __int16)(v33 + *v32)];
      *ptr = 0;
      ptr[1] = v29;
      ptr[2] = v36;
      while ( 1 )
      {
        inp = getc(stdin);
        if ( inp == -1 )
          break;
        v39 = *ptr;
        v40 = (unsigned __int16)ptr[2];
        v41 = &S[v40];
        v42 = *ptr - 1;
        do
        {
          v43 = &S[(unsigned __int16)++v39];
          v44 = *v43;
          v45 = &S[v44];
          v46 = *v45;
          v47 = *v43;
          if ( v43 != v45 )
          {
            v48 = v44 ^ v46;
            *v43 = v48;
            v49 = *v45 ^ v48;
            *v45 = v49;
            v47 = *v43 ^ v49;
            *v43 = v47;
            v46 = *v45;
          }
          v50 = 4096;
          do
          {
            qword_4030 /= qword_4030 | 1;
            --v50;
          }
          while ( v50 );
          v51 = (unsigned __int16)S[(unsigned __int16)(v46 + *v41 + v47)];
          v52 = &S[v51];
          v53 = v51;
          if ( v41 != v52 )
          {
            v54 = *v41 ^ *v52;
            *v52 = v54;
            v55 = *v41 ^ v54;
            *v41 = v55;
            *v52 ^= v55;
          }
          v56 = 4096;
          do
          {
            qword_4030 /= qword_4030 | 1;
            --v56;
          }
          while ( v56 );
        }
        while ( v39 != v42 );
        *ptr = v39;
        v57 = stdout;
        ptr[1] = v44;
        ptr[2] = v53 + inp + __ROL2__(v53 + (inp | (unsigned __int16)((_WORD)v40 << 8)), 8);
        putc((unsigned __int8)(inp + v53), v57);
      }
    }
  }
  else
  {
    puts("Usage: encrypt passphrase");
  }
}
```
So this looks like some variant of RC4. It first initializes states, then key initialisation, then it reads a character from stdin and gives the encrypted char to stdout. Our first task is to patch the loops of `qword_4030` which just slows down the program.

### Decryption
```c
ptr[2] = v53 + inp + __ROL2__(v53 + (inp | (unsigned __int16)((_WORD)v40 << 8)), 8);
putc((unsigned __int8)(inp + v53), v57);
```
The input is added to some value and prints it, the input is also used for the next round.
```asm
0x13d8:      mov    eax,r9d
0x13db:      movzx  edx,r11b                          # <-- input char
0x13df:      mov    WORD PTR [rbp+0x0],si
0x13e3:      mov    rsi,QWORD PTR [rip+0x2c26]        # 0x4010 <stdout>
0x13ea:      shl    eax,0x8
0x13ed:      mov    WORD PTR [rbp+0x2],di
0x13f1:      lea    edi,[r11+r13*1]                   # r13 is added to our input
0x13f5:      or     eax,edx
0x13f7:      add    edx,r13d
0x13fa:      movzx  edi,dil                           # converted to unsigned char
0x13fe:      add    eax,r13d
0x1401:      rol    ax,0x8
0x1405:      add    eax,edx
0x1407:      mov    WORD PTR [rbp+0x4],ax
0x140b:      call   0x1050 <putc@plt>
```
So we can just pass `0x00` as input and substract `r13` from the encrypted char to get decrypted char, then we can set `r11` again to the decrypted char. Part of gdb script:
```
break *0x00005555555553D8
commands
silent
set $ch = (unsigned char)($data[$pos] - $r13l)
printf "%c",$ch
set $r11 = $ch
set $pos = $pos + 1
continue
end 
```
Full script [here](./script.gdb) (Disabled ASLR for breakpoint)

I used python to spawn the process with the contents of key.txt as argument, than attached to gdb and executed the gdb script file (`source script.txt`).

Python script [here](./solve.py)

The output(decrypted data) is stored in [gdb_output.txt](./gdb_output.txt)

## Flag
> midnight{H0w_10ng_wi11_73H_d4mn3d_7hing_1457}
