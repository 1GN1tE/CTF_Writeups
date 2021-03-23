# compUDer

Check out our brand new computer!

`nc challenges.ctfd.io 30525`

Attachments:
* [vm.out](./vm.out)

## Solution
Opened the binary in Ghidra, after some clearup (Rename and Retype variable), we got

### Main Function
```c
void main(void)
{
  // Some Initialisation
  fib_mem((long)arr_flag,0x20);
  fwrite("VM $ ",1,5,stderr);
  vm_loop = false;
  while (!vm_loop) {
    __isoc99_scanf("%ld",&ins);
    if (7 < ins) return;
    __isoc99_scanf("%ld",&x);
    is_reg_valid((uint)x);
    __isoc99_scanf("%ld",&a);
    is_reg_valid((uint)a);
    __isoc99_scanf("%ld",&b);
    is_reg_valid((uint)b);
    switch(ins) {
    case 0:
      stack[x] = stack[b] + stack[a];
      break;
    case 1:
      stack[x] = stack[a] - stack[b];
      break;
    case 2:
      stack[x] = stack[b] * stack[a];
      break;
    case 3:
      stack[x] = stack[b] & stack[a];
      break;
    case 4:
      stack[x] = stack[b] | stack[a];
      break;
    case 5:
      if (0x43 < x) return;
      stack[x] = arr_flag[stack[a]];
      break;
    case 6:
      if (0x43 < x) return;
      arr_flag[stack[x]] = stack[a];
      break;
    case 7:
      vm_loop = true;
      break;
    default:
      return;
    }
  }
  flag_chk = 0;
  do {
    if (32 < flag_chk) {
      local_150 = fopen("flag.txt","r");
      if (local_150 != (FILE *)0x0) {
        while( true ) {
          iVar2 = getc(local_150);
          if ((char)iVar2 == -1) break;
          putchar((int)(char)iVar2);
        }
        fclose(local_150);
      }
      return;
    }
    if (arr_flag[flag_chk] != arr_flag[flag_chk + 33]) {
      puts("Incorrect.");
      return;
    }
    flag_chk = flag_chk + 1;
  } while( true );
}
```

So we are given a VM binary. The constraint of the equations are:
- Instruction value < 8
- Operands value < 6

The VM:
```
OPC  Out  a  b
--------------
0    x    a  b ; stack[x] = stack[a] + stack[b]
1    x    a  b ; stack[x] = stack[a] - stack[b]
2    x    a  b ; stack[x] = stack[a] * stack[b]
3    x    a  b ; stack[x] = stack[a] & stack[b]
4    x    a  b ; stack[x] = stack[a] | stack[b]
5    x    a  b ; stack[x] = arr_flag[stack[a]]
6    x    a  b ; arr_flag[stack[x]] = stack[a]
7    x    a  b ; exit VM
```

I used gdb dynamic debugging to leak the initial stack

```
0x00000000 | 0
0x00000000 | 1
0x00000000 | 2
0x00000000 | 3
0x00000000 | 4
0x00000001 | 5
```

1st 33 values of `arr_flag` is initialized with fibonacci values. We need to make the next 33 values as same as the 1st ones to get the flag, like this:

```py
for i in range(33):
  arr_flag[33+i] = arr_flag[i]
```

So my solution was:
- Init a value to 33(say `i`)
- Loop 33 times in the following way,(say loop var `x`)
  - Copy arr_flag[x] to stack
  - set arr_flag[x+i] from the stack
  - Increase value of (x+i)
  - Increase i

Script [here](./solve.py)

```sh
$ python solve.py
[+] Opening connection to challenges.ctfd.io on port 30525: Done
[*] Init [i]
[*] Set arr_flag[i]
FLAG!!!  UDCTF{r3v3rs!nG_cUst0m_VMs_1s_3Z}
```

## Flag
> UDCTF{r3v3rs!nG_cUst0m_VMs_1s_3Z}