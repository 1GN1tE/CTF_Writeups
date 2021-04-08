# Dysfunctional

My "functional programming in C" library finally works! Although, now that I realize it, it seems more... dysfunctional. Either way, I've used it for my cutting edge flag encryption algorithm along with this file - here's the encrypted flag.


Attachments:
* [dysfx](./dysfx)
* [not_flag](./not_flag)
* [encrypted_flag.txt](./encrypted_flag.txt)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int rand_flag[64];
  char flag[72];

  FILE *stream; = fopen("flag", "r");
  fgets(flag, 64, stream);
  FILE *not_flag; = fopen("not_flag", "r");
  lookup = malloc(0x20000uLL);
  fread(lookup, 0x20000uLL, 1uLL, not_flag);
  int flag_len = strlen(flag);
  FILE *random = fopen("/dev/urandom", "r");
  for (int i = 0; i < flag_len; ++i )
  {
    int v6 = 0;
    for (int j = 0; j <= 2; ++j )
      v6 = (fgetc(random) + v6) << 8;
    rand_flag[i] = v6 + flag[i];
  }
  long *closure_1 = closure(0xDEADuLL, 0xBEEF, 0xFEEDLL, lookup);
  long *closure_2 = closure(0x1337uLL, 0xCAFE, 0x1234LL, lookup);
  long *comp_1 = compose(closure_1, closure_2);
  long *comp_2 = compose(closure_2, closure_1);
  unsigned int *some_data = map(comp_1, rand_flag, flag_len);
  unsigned int *output_flag = map(comp_2, some_data, flag_len);
  for (int k = 0; k < flag_len; ++k )
    printf("%x ", output_flag[k]);
  puts("is the encrypted flag. Good luck!");
  free(lookup);
  return 0;
}
```
The flag is read and converted to a int array of higher bits as random data. Then it reads some data from `not_flag` and does something in `closure`

### `map`
```c
unsigned int *__fastcall map(long *func, unsigned int *data, int len)
{
  unsigned int *result;

  result = (unsigned int *)malloc(4LL * len);
  for (int i = 0; i < len; ++i )
    result[i] = func(data[i]);
  return result;
}
```

The data returned after closure and compose are some functions. So I used dynamic analysis to understand those functions... the results are:

### comp_1 Function

```c
unsigned int comp1(unsigned int input)
{
	unsigned int tmp = stack_func_1(input);
	unsigned int result = stack_func_2(tmp);
	return result;
}
```

### comp_2 Function

```c
unsigned int comp2(unsigned int input)
{
	unsigned int tmp = stack_func_2(input);
	unsigned int result = stack_func_1(tmp);
	return result;
}
```

### stack_func_1
```c
unsigned int stack_func_1(unsigned int inp)
{
  return 0xDEAD ^ (SBox[(inp & 0xFFFF) ^ 0xBEEF] + SBox[(inp >> 16) ^ 0xBEEF] << 16);
}
```

### stack_func_2
```c
unsigned int stack_func_2(unsigned int inp)
{
  return 0x1337 ^ (SBox[(inp & 0xFFFF) ^ 0xCAFE] + SBox[(inp >> 16) ^ 0xCAFE] << 16);
}
```

I dumped the Sbox data with gdb(`dump binary memory SBox 0x00007ffff7fa5010 0x7ffff7fc5010`).

So I just xored the encypted flag data and inversed Sbox to get the flag.

Solve script [here](./solve.py)

## Flag
> actf{but_wh4t_4b0ut_0bj3ct_d1s0r13nt3d}
