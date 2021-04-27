# RE Diary

Every member of S4Lab needs to write a diary! and send it in a special format to the MASTER of the lab. Help her to read to this diary!

Attachments:
* [rediary](./rediary)
* [flag.enc](./flag.enc)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```cpp
  std::ifstream::basic_ifstream(flag_stream, "flag", 8LL);
  if ( (unsigned __int8)std::ios::fail(&v13) )
  {
    std::operator<<<std::char_traits<char>>(
      &std::cout,
      "\n"
      ".....................................................................You shall not pass!!........................."
      "..........................................\n",
      v8);
    exit(0);
  }
  std::allocator<char>::allocator(&a6);
  sub_2C8A((__int64)a6_1);
  sub_2E9C((__int64)a1a, flag_stream);
  sub_2EE8((__int64)v11, a1a[0], a1a[1], a6_1[0], a6_1[1], (__int64)&a6);
  std::allocator<char>::~allocator(&a6);
  std::ifstream::close(flag_stream);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&flag, v11);
  enc((unsigned __int8 *)&output, (unsigned __int8 *)&flag);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&flag);
  std::ofstream::basic_ofstream(output_stream, "flag.enc", 16LL);
  std::operator<<<char>(output_stream, &output);
  std::ofstream::close(output_stream);
  std::ofstream::~ofstream(output_stream);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&output);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v11);
  std::ifstream::~ifstream(flag_stream);
```
It reads contents of the `flag` file and encrypts it in the `enc` function. The output is then written to `flag.enc`

### `enc`
```cpp
void __fastcall enc(unsigned __int8 *output, unsigned __int8 *flag)
{
  pos = 0;
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(output);
  table[0] = 0;
  // An array
  table[27] = 1;
  v17 = flag;
  v8 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::begin(flag);
  v7 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::end(flag);
  while ( sub_2E2D((__int64)&v8, (__int64)&v7) )
  {
    v16 = *(_BYTE *)sub_2E8A((__int64)&v8);
    high_nibble = (v16 >> 4) & 0xF;
    low_nibble = v16 & 0xF;
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(arr1);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(arr2);
    for ( i = 0; i <= 6; ++i )
    {
      high_sum = 0;
      low_sum = 0;
      for ( j = 0; j <= 3; ++j )
      {
        hbit_at = (high_nibble & (unsigned int)(1 << (3 - j))) >> (3 - j);
        high_sum += hbit_at * table[4 * i + j];
        lbit_at = (low_nibble & (unsigned int)(1 << (3 - j))) >> (3 - j);
        low_sum += lbit_at * table[4 * i + j];
      }
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(
        arr1,
        (unsigned int)(char)(high_sum % 2 + '0'));
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(
        arr2,
        (unsigned int)(char)(low_sum % 2 + '0'));
    }
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(tmp1, arr1);
    v2 = zero_check((__int64)tmp1);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(tmp1);
    if ( v2 )
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(arr1, '0');
    else
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(arr1, '1');
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(tmp2, arr2);
    v3 = zero_check((__int64)tmp2);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(tmp2);
    if ( v3 )
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(arr2, '1');
    else
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(arr2, '0');
    v6[0] = to_int(arr1, 0LL, 2LL);
    v6[1] = to_int(arr2, 0LL, 2LL);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::insert(
      output,
      0LL,
      1LL,
      (unsigned int)(char)v6[(pos & 1) == 0]);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::push_back(
      output,
      (unsigned int)(char)v6[pos++ & 1]);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(arr2);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(arr1);
    sub_2E6A(&v8);
  }
}
```
There is a loop which iterates over the elements of the flag, it encrypts the high hex nibble and low hex nibble of the byte separately, then it appends them at start and end of output array... the position (start or end) depends if the byte position is even or odd, i.e. `high/low/high/low` manner.


Since there is a 1 to 1 mapping of the original bytes and encrypted bytes, I wrote 0-255 bytes into `flag`, encrypted it and then parsed `flag.enc` to get the encrypted : orginal byte mapping. Then I used it to decrypt the given `flag.enc`

Full script [here](./solve.py)

## Flag
> `S4CTF{iT5_34zY_oR_70u9H!?}`