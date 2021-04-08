# Checkpass

What is the password? Flag format: picoCTF{...}

**Hints**
- How is the password being checked?

Attachments:
* [checkpass](./checkpass)

## Solution
We are given a rust binary

### Main Function
```c
void __fastcall main(int a1, char **a2, char **a3)
{
  void (__fastcall __noreturn *v3)(); // [rsp+0h] [rbp-8h] BYREF

  v3 = sub_5960;
  sub_226C0(&v3, &off_2482A8, a1, a2);
}
```
So the main function calls `sub_5960` inside a rust wrapper (probably a new thread)

### `sub_5960`
This is the main function we need to analyze and rust decompilation is very hard to look at...

```c
  if ( v80 == 2 )
  {
    if ( *(_QWORD *)(v79[0] + 40) == 41LL )
    {
      v4 = *(_QWORD *)(v79[0] + 24);
      if ( (_UNKNOWN *)v4 == &unk_39D78 || *(_QWORD *)v4 == '{FTCocip' )
      {
        v5 = (char *)(v4 + 40);
        v1 = &unk_39D94;
        if ( (_UNKNOWN *)(v4 + 40) == &unk_39D94 || *v5 == '}' )
        {
```
First it checks it an argument is passed or not...Running without arguments gives this
```sh
$ ./checkpass
Usage:
        ./checkpass <password>
```
After that it checks:
- len(argv[1]) == 41
- Start of argv[1] == `picoCTF{`
- Last byte of argv[1] is `}`

Then the core of the flag, i.e without `picoCTF{}` is calculated and...
```c
v11 = *v8;
v19 = v8[1];
v18 = v11;
sub_54E0(v81, &v18, 0LL);
v19 = v81[1];
v18 = v81[0];
sub_54E0(v82, &v18, 1LL);
v19 = v82[1];
v18 = v82[0];
sub_54E0(&v77, &v18, 2LL);
v19 = v78;
v18 = v77;
v12 = &v18;
sub_54E0(&v43, &v18, 3LL);
```
Then the flag core is passed to the `sub_54E0` with arg value 0, the answer of which is again passed to `sub_54E0` with arg value 1... repeated upto 4...

### `sub_54E0`
```c
unsigned __int8 __fastcall sub_54E0(unsigned __int8 *ouput, unsigned __int8 *input, __int64 a3)
{
  __int64 box_no; // rdx
  unsigned __int64 v4; // rax
  unsigned __int8 result; // al
  char tmp[32]; // [rsp+8h] [rbp-20h]

  box_no = a3 << 8;
  tmp[ 0] = sbox[box_no + input[ 0]];
  tmp[ 1] = sbox[box_no + input[ 1]];
  tmp[ 2] = sbox[box_no + input[ 2]];
  tmp[ 3] = sbox[box_no + input[ 3]];
  tmp[ 4] = sbox[box_no + input[ 4]];
  tmp[ 5] = sbox[box_no + input[ 5]];
  tmp[ 6] = sbox[box_no + input[ 6]];
  tmp[ 7] = sbox[box_no + input[ 7]];
  tmp[ 8] = sbox[box_no + input[ 8]];
  tmp[ 9] = sbox[box_no + input[ 9]];
  tmp[10] = sbox[box_no + input[10]];
  tmp[11] = sbox[box_no + input[11]];
  tmp[12] = sbox[box_no + input[12]];
  tmp[13] = sbox[box_no + input[13]];
  tmp[14] = sbox[box_no + input[14]];
  tmp[15] = sbox[box_no + input[15]];
  tmp[16] = sbox[box_no + input[16]];
  tmp[17] = sbox[box_no + input[17]];
  tmp[18] = sbox[box_no + input[18]];
  tmp[19] = sbox[box_no + input[19]];
  tmp[20] = sbox[box_no + input[20]];
  tmp[21] = sbox[box_no + input[21]];
  tmp[22] = sbox[box_no + input[22]];
  tmp[23] = sbox[box_no + input[23]];
  tmp[24] = sbox[box_no + input[24]];
  tmp[25] = sbox[box_no + input[25]];
  tmp[26] = sbox[box_no + input[26]];
  tmp[27] = sbox[box_no + input[27]];
  tmp[28] = sbox[box_no + input[28]];
  tmp[29] = sbox[box_no + input[29]];
  tmp[30] = sbox[box_no + input[30]];
  tmp[31] = sbox[box_no + input[31]];
  *((_OWORD *)ouput + 1) = 0LL;
  *(_OWORD *)ouput = 0LL;
  v4 = swap[8 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[8] = tmp[v4];
  v4 = swap[25 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[25] = tmp[v4];
  v4 = swap[27 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[27] = tmp[v4];
  v4 = swap[28 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[28] = tmp[v4];
  v4 = swap[17 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[17] = tmp[v4];
  v4 = swap[14 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[14] = tmp[v4];
  v4 = swap[12 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[12] = tmp[v4];
  v4 = swap[15 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[15] = tmp[v4];
  v4 = swap[ 2 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[2] = tmp[v4];
  v4 = swap[21 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[21] = tmp[v4];
  v4 = swap[16 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[16] = tmp[v4];
  v4 = swap[ 9 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[9] = tmp[v4];
  v4 = swap[19 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[19] = tmp[v4];
  v4 = swap[10 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[10] = tmp[v4];
  v4 = swap[13 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[13] = tmp[v4];
  v4 = swap[ 6 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[6] = tmp[v4];
  v4 = swap[22 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[22] = tmp[v4];
  v4 = swap[ 0 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  *ouput = tmp[v4];
  v4 = swap[30 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[30] = tmp[v4];
  v4 = swap[ 1 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[1] = tmp[v4];
  v4 = swap[ 4 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[4] = tmp[v4];
  v4 = swap[26 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[26] = tmp[v4];
  v4 = swap[29 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[29] = tmp[v4];
  v4 = swap[ 3 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[3] = tmp[v4];
  v4 = swap[31 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[31] = tmp[v4];
  v4 = swap[20 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[20] = tmp[v4];
  v4 = swap[24 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[24] = tmp[v4];
  v4 = swap[ 7 + box_no];
  if ( v4 > 0x1F )
    goto LABEL_34;
  ouput[7] = tmp[v4];
  v4 = swap[11 + box_no];
  if ( v4 > 0x1F
    || (ouput[11] = tmp[v4], v4 = swap[23 + box_no], v4 > 0x1F)
    || (ouput[23] = tmp[v4], v4 = swap[5 + box_no], v4 > 0x1F)
    || (ouput[5] = tmp[v4], v4 = swap[18 + box_no], v4 >= 0x20) )
  {
LABEL_34:
    sub_356A0(v4, 32LL, &off_2481F8);
  }
  result = tmp[v4];
  ouput[18] = result;
  return result;
}
```
This function basically does S-box transformation of 32 bytes then swaps the position of the bytes... The args 0,1,2,3 specify the Sbox and Swap array number (There are 4 Sbox and Swap position array).

```c
LOBYTE(v12) = v43;
v34 = v46;
v40 = v47;
v31 = v48;
v42 = v49;
v27 = v50;
v36 = v51;
LOBYTE(v13) = v52;
v41 = v53;
v29 = v54;
v38 = v56;
LOBYTE(v14) = v57;
v26 = v58;
v30 = v59;
v37 = v60;
v39 = v61;
v33 = v63;
v32 = v64;
v28 = v65;
LOBYTE(v15) = v66;
LOBYTE(v16) = v67;
v35 = v71;
v25 = v73;
*(_QWORD *)&v18 = 25LL;
v17 = 25LL;
v22 = v45;
v23 = v67;
v24 = v52;
if ( v68 == byte_39D95[25] )
{
  *(_QWORD *)&v18 = 0LL;
  v17 = 0LL;
  v12 = (__int128 *)byte_39D95;
  if ( v43 == 31 )
  {
.
.
.

      if ( v23 == byte_39D95[24] )
      {
        *(_QWORD *)&v18 = 18LL;
        v17 = 18LL;
        v13 = byte_39D95;
        if ( v39 == byte_39D95[18] )
          sub_66A0(18LL, byte_39D95, v16);
```

Then again the bytes returned from the last `sub_54E0` function is swapped.

So the whole process is like:
```py
### Round 1 ###
enc_flag = [0]*32
for i in range(32):
	enc_flag[i] = sbox1[ord(flag[i])]
	print(hex(enc_flag[i]), end=" ")
print()
out = [0]*32
for i in range(32):
	out[i] =  enc_flag[S1[i]]
	print(hex(out[i]), end=" ")
print()

### Round 2 ###
enc_flag = [0]*32
for i in range(32):
	enc_flag[i] = sbox2[out[i]]
	print(hex(enc_flag[i]), end=" ")
print()
out = [0]*32
for i in range(32):
	out[i] =  enc_flag[S2[i]]
	print(hex(out[i]), end=" ")
print()

### Round 3 ###
enc_flag = [0]*32
for i in range(32):
	enc_flag[i] = sbox3[out[i]]
	print(hex(enc_flag[i]), end=" ")
print()
out = [0]*32
for i in range(32):
	out[i] =  enc_flag[S3[i]]
	print(hex(out[i]), end=" ")
print()

### Round 4 ###
enc_flag = [0]*32
for i in range(32):
	enc_flag[i] = sbox4[out[i]]
	print(hex(enc_flag[i]), end=" ")
print()
out = [0]*32
for i in range(32):
	out[i] =  enc_flag[S4[i]]
	print(hex(out[i]), end=" ")
print()

### Swap Before Check ###
for i in range(32):
	check_enc[check_pos[i]] = out[i]
```

So I parsed all the swaps and S-Boxes and inverted them starting with the values the check was done which gave the flag. Script [here](./solver.py)

```sh
$ ./checkpass picoCTF{t1mingS1deChann3l_gVQSfJxl3VPFGQ}

Success
```

## Flag
> picoCTF{t1mingS1deChann3l_gVQSfJxl3VPFGQ}
