# Time

Attachments:
* [time](./time)

## Solution
This is an optimize me challenge.

### Main
```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 len; // [rsp+18h] [rbp-8h]

  len = sysconf(30);
  mprotect((void *)((unsigned __int64)func_list_1[0] & -len), len, 7);
  puts("The flag is on its way. Please wait");
  while ( (unsigned int)run_loop() )
  {
    fflush(stdout);
    putchar('.');
    sub_12CA();
    sleep(2u);
    fflush(stdout);
  }
  puts("damn son");
  print_flag();
  return 0LL;
}
```
It makes a memory segment executable. Then the loop is run until `run_loop` return true.

### `run_loop`
```c
__int64 run_loop()
{
  __int64 v0; // rax
  __int64 v2; // [rsp+8h] [rbp-18h]
  int i; // [rsp+18h] [rbp-8h]
  unsigned int v4; // [rsp+1Ch] [rbp-4h]

  v4 = 0;
  for ( i = 0; i <= 32; ++i )
  {
    v2 = ((__int64 (__fastcall *)(_QWORD, _QWORD))func_list_1[i])(val_arr_1[2 * i], val_arr_1[2 * i + 1]);
    printf("%d", v2);
    v0 = sub_1257(i, 0x35uLL, 0x383uLL);
    if ( v2 != sub_1257(v0, 0x43uLL, 0x383uLL) )
      v4 = 1;
  }
  return v4;
}
```
This function executes functions from `func_list_1` array with values from `val_arr_1`. If all the results match with values from `sub_1257(sub_1257(i, 0x35uLL, 0x383uLL), 0x43uLL, 0x383uLL)` then it returns 0 and the loop stops working. `sub_1257` is equivalent to `pow(x,y,z)` in Python.

### `sub_12CA`
```c
void __fastcall sub_12CA()
{
  void *v0; // [rsp+8h] [rbp-18h]
  void *v1; // [rsp+8h] [rbp-18h]
  int x; // [rsp+14h] [rbp-Ch]
  int i; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i < 33; ++i )
  {
    x = rand() % 33;
    sub_11A5(val_arr_1, i, x);
    sub_11A5(val_arr_2, i, x);
    v0 = func_list_1[x];
    func_list_1[x] = func_list_1[i];
    func_list_1[i] = v0;
    v1 = func_list_2[x];
    func_list_2[x] = func_list_2[i];
    func_list_2[i] = v1;
  }
}
```
It swaps the functions and their arguments with rand.

### `print_flag`
```c
void __fastcall print_flag()
{
  __int64 v0; // rax
  int i; // [rsp+Ch] [rbp-4h]

  for ( i = 0; i <= 32; ++i )
  {
    v0 = ((__int64 (__fastcall *)(_QWORD, _QWORD))func_list_2[i])(val_arr_2[2 * i], val_arr_2[2 * i + 1]);
    printf("%c", v0);
  }
  puts(s);
}
```
It prints the chars generated from the functions after the loop stops i.e. after all the swapping.

### Decryption
So basically it compares the result of `pow(i, 191, 0x383)` to the return value of the function in the array at i. So we can compare the values generated from the functions and use it to get the correct index of the functions. As both the function list are swapped together we can use the index we got to swap the 2nd function list and then use it to get the flag.

Script [here](./time.py)

## Flag
> IJCTF{zzzzz_3852f328382c57e4b296}
