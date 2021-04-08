# Infinity Gauntlet

All clam needs to do is snap and finite will turn into infinite...

Find it on the shell server at `/problems/2021/infinity_gauntlet` or over netcat at `nc shell.actf.co 21700`.

Attachments:
* [infinity_gauntlet](./infinity_gauntlet)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```c
void main(int argc, const char **argv, const char **envp)
{
  setvbuf(_bss_start, 0LL, 2, 0LL);
  stream = fopen("flag.txt", "r");
  if ( stream )
  {
    fgets((char *)flag, 256, stream);
    fclose(stream);
    v5 = strcspn((const char *)flag, "\n");
    v6 = v5;
    flag[v5] = 0;
    if ( v5 )
    {
      v7 = (char *)flag;
      v8 = 17 * v5;
      v9 = 0;
      do
      {
        *v7 ^= v9;
        v9 += 17;
        ++v7;
      }
      while ( (_BYTE)v9 != v8 );
    }
    rnd_no = 1;
    v11 = time(0LL);
    srand(v11);
    puts("Welcome to the infinity gauntlet!");
    puts("If you complete the gauntlet, you'll get the flag!");
    while ( 1 )
    {
      printf("=== ROUND %d ===\n", (unsigned int)rnd_no);
      v14 = rand();
      check = rnd_no > 49 ? flag[v14 % v6] | ((unsigned __int8)(v14 % v6 + rnd_no) << 8) : rand() % 0x10000;
      if ( (rand() & 1) != 0 )
      {
        v12 = rand() % 3;
        if ( v12 )
        {
          if ( v12 == 1 )
          {
            v22 = rand();
            printf("foo(%u, ?) = %u\n", (unsigned int)(v22 % 1337), (v22 % 1337) ^ (check + 1) ^ 0x539);
          }
          else
          {
            v13 = rand();
            printf("foo(%u, %u) = ?\n", check ^ (v13 % 1337 + 1) ^ 0x539, (unsigned int)(v13 % 1337));
          }
        }
        else
        {
          v19 = rand();
          printf("foo(?, %u) = %u\n", (unsigned int)(v19 % 1337), check ^ (v19 % 1337 + 1) ^ 0x539);
        }
      }
      else
      {
        v16 = rand();
        if ( (v16 & 3) != 0 )
        {
          v17 = v16 % 4;
          if ( v17 == 1 )
          {
            v24 = rand() % 1337;
            v25 = rand();
            v26 = (unsigned int)(v25 >> 31);
            LODWORD(v26) = v25 % 1337;
            printf("bar(%u, ?, %u) = %u\n", v24, v26, v24 + check * (v25 % 1337 + 1));
          }
          else if ( v17 == 2 )
          {
            v27 = rand() % 1337;
            v28 = rand();
            v29 = (unsigned int)(v28 >> 31);
            LODWORD(v29) = v28 % 1337;
            printf("bar(%u, %u, ?) = %u\n", v27, v29, v27 + v28 % 1337 * (check + 1));
          }
          else
          {
            v18 = check <= 0x539 ? rand() % check : rand() % 1337;
            printf("bar(%u, %u, %u) = ?\n", check % v18, v18, check / v18 - 1);
          }
        }
        else
        {
          v20 = rand() % 1337;
          v21 = rand();
          printf("bar(?, %u, %u) = %u\n", v20, (unsigned int)(v21 % 1337), check + v20 * (v21 % 1337 + 1));
        }
      }
      __isoc99_scanf("%u", &inp);
      if ( inp != check )
        break;
      printf("Correct! Maybe round %d will get you the flag ;)\n", (unsigned int)++rnd_no);
    }
    puts("Wrong!");
  }
  else
  {
    puts("Couldn't find a flag file.");
  }
}
```
So basically it reads the flag and encrypts it with xoring, then there is a loop of equations with random values.
We have to solve the equations to get the `check` value. After 49 rounds the lower 8 bits is the character of the flag and the upper 8 bits is the position of the character. Then we can xor it again to get the flag.

Solve script [here](./gauntlet.py)

## Flag
> actf{snapped_away_the_end}
