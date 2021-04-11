# murmur

aarch64 is the future, crackme

Attachments:
* [murmur](./murmur)

## Solution
Decompiling the ARM binary in IDA and renaming/retyping variables we get...

### Main Function
```c
void main()
{
  unsigned long long enc[20];
  unsigned char inp[24];

  print(&qword_5108B0, "Hello from ARM64!\n");
  sub_4019D8(&qword_5109C0, (__int64)inp, 20LL);
  for (int i = 0; i < strlen(inp); ++i )
    enc[i] = hash(&inp[i], 1, 0x1337u);
  check = 1
  for (int j = 0; j <= 19; ++j )
  {
    if ( enc[j] != check_data[j] )
      check = 0;
  }
  if (check)
    print(&qword_5108B0, "Congratulations, you did it!\n");
}
```
So it loops though each input byte and passes to the `hash` function. The results are stored and compared to hardcoded values.

### `hash` Function
```c
unsigned __int64 __fastcall hash(unsigned __int8 *ch, int a2, unsigned int a3)
{
  int v3; // w0
  int v4; // w1
  unsigned __int8 *v5; // x0
  char v7; // [xsp+4h] [xbp-4Ch]
  unsigned __int64 v8; // [xsp+20h] [xbp-30h]
  unsigned __int8 *v10; // [xsp+38h] [xbp-18h]

  v7 = a2;
  v8 = a3 ^ (0xC6A4A7935BD1E995LL * a2);
  v3 = a2;
  v4 = a2 + 7;
  if ( v3 < 0 )
    v3 = v4;
  v10 = &ch[8 * (v3 >> 3)];
  while ( ch != v10 )
  {
    v5 = ch;
    ch += 8;
    v8 = 0xC6A4A7935BD1E995LL
       * (v8 ^ (0xC6A4A7935BD1E995LL
              * ((0xC6A4A7935BD1E995LL * *(_QWORD *)v5) ^ ((0xC6A4A7935BD1E995LL * *(_QWORD *)v5) >> 47))));
  }
  switch ( v7 & 7 )
  {
    case 7:
      v8 ^= (unsigned __int64)ch[6] << 48;
    case 6:
      v8 ^= (unsigned __int64)ch[5] << 40;
    case 5:
      v8 ^= (unsigned __int64)ch[4] << 32;
    case 4:
      v8 ^= (unsigned __int64)ch[3] << 24;
    case 3:
      v8 ^= (unsigned __int64)ch[2] << 16;
    case 2:
      v8 ^= (unsigned __int64)ch[1] << 8;
    case 1:
      v8 = 0xC6A4A7935BD1E995LL * (v8 ^ *ch);
    default:
      return (0xC6A4A7935BD1E995LL * (v8 ^ (v8 >> 47))) ^ ((0xC6A4A7935BD1E995LL * (v8 ^ (v8 >> 47))) >> 47);
  }
}
```
We can see `0xC6A4A7935BD1E995` this value has been used multiple times, googling about this says that the above function is the source of [MurmurHash64A](https://github.com/explosion/murmurhash/blob/master/murmurhash/MurmurHash2.cpp#L96).

Since a single byte is hashed every time we can get the bytes from the `check_data` like this...
```c
for(int x = 0; x <19; x++)
  for(int i = 32; i<128; i++)
  {
    unsigned long long tmp = MurmurHash64A(&i,1,0x1337);
    if(enc[x] == tmp)
    {
      printf("%c",i);
      break;
    }
  }
```

Full script [here](./gen.c)

## Flag
> midnight{w1thOut_A_mUrmUr...}