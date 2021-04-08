# Lockpicking

Clam wanted to have a lockpicking competition but decided against it. So, he settled for a digital lockpicking competition instead.

Find it on the shell server at `/problems/2021/lockpicking` or over netcat at `nc shell.actf.co 21702`.

Attachments:
* [lockpicking](./lockpicking)

## Solution
Decompiling the binary in IDA and renaming/retyping variables we get...

### Main Function
```c
void main()
{
  char s[1032];
  struct lock_dat {
    int inner;
    int middle;
    int outer;
    unsigned char prlock;
    unsigned char x0;
    unsigned char x1;
    unsigned char x2;
    unsigned char x3;
    unsigned char x4;
    unsigned char x5;
  };
  int chance = 0;
  while ( 1 )
  {
    if (lock_dat->prlock)
      print_lock(&lock_dat);
    printf("> ");
    if ( !fgets(s, 1024, stdin) )
    {
      puts("You walk away from the lock.");
      return;
    }
    while ( 1 )
    {
      char chr = *s++;
      if ( !chr || chr == 10 )
        break;
      if (parse_lock(&lock_dat, chr, &chance))
      {
        puts("Your actions prove to be ineffective against the lock.");
        return;
      }
    }
    if ( chance > 164 )
      break;
    while (lock_dat->x1)
    {
      if (lock_dat->x1++)
      {
        puts("The lock opens.");
        flag_func();
        return;
      }
    }
  }
  puts("Your hands grow weary from the stiffness of the lock.");
}
```

### parse_lock
```c
bool parse_lock(lock_dat *lock, char inp, int *chance)
{
  int tmp
  chance++;
  if (inp == '!')
    lock->x0 ^= 1;
  else
  {
    switch ( inp )
    {
      case '?':
        print_lock(lock);                       // Prints Lock
        --chance;
        break;

      case '@':
        lock->prlock ^= 1;                      // Toggles if Lock is printed every time
        --chance;
        break;

      case 'I':                                 // Clockwise Inner Wheel
        tmp = lock->inner + 27;
      case 'i':                                 // Anti-Clockwise Inner Wheel
        tmp = lock->inner + 1;
        lock->inner = tmp % 28;
        break;

      case 'M':                                 // Clockwise Middle Wheel
        tmp = lock->middle  + 43;
      case 'm':                                 // Anti-Clockwise Middle Wheel
        tmp = lock->middle  + 1;
        lock->middle = tmp % 44;
        break;

      case 'O':                                 // Clockwise Outer Wheel
        tmp = lock->outer + 55;
      case 'o':                                 // Anti-Clockwise Outer Wheel
        tmp = lock->outer + 1;
        lock->outer = tmp % 56;
        break;

      default:
        return 1;
    }
  }
  update_lock_checks(lock);
  return 0;
}
```

### update_lock_checks
```c
void update_lock_checks(lock_dat *lock)
{
  char x0f;
  char x0d;

  int I = lock->inner;
  int M = lock->middle;
  int O = lock->outer;
  if (I==0x16 && M==0x0b && O == 7)
    lock->x5 = 1;
  x0f = lock->x2;
  x0d = lock->x0;
  if ( O == 7 )
  {
    if ( !x0f || (x0f = lock->x5) == 0 )
    {
      x0f = 0;
      if ( M == 8 && I == 9 )
      {
        x0f = lock->x3;
        if ( x0f )
          x0f = x0d ^ 1;
      }
    }
    lock->x2 = x0f;
  }
  else if ( O == 0xD && M == 0x25 && I == 6 )
  {
    if ( !x0d )
      lock->x3 = 1;
    if ( !x0f )
      goto LABEL_13;
    goto LABEL_9;
  }
  if ( x0f == x0d )
    lock->x3 = 0;
  if ( x0f )
  {
LABEL_9:
    if ( lock->x5 && !lock->x3 )
      lock->x4 = 1;
  }
  if (O | M | I)
  {
LABEL_13:
    lock->x1 = 0;
    return;
  }
  lock->x1 = 1;
}
```

So the struct is like:
```
lock_dat = {
[0x00 0x01 0x02 0x03]  --> Inner  Wheel [0x1c] <-- Size
[0x04 0x05 0x06 0x07]  --> Middle Wheel [0x2c] <-- Size
[0x08 0x09 0x0a 0x0b]  --> Outer  Wheel [0x38] <-- Size
[0x0c] --> prlock	--> Toggles Lock Print
[0x0d] --> x0		--> Can be toggled with !
[0x0e] --> x1		--> To get 1 for flag
[0x0f] --> x2		--> To get 1 for flag
[0x10] --> x3		--> To get 1 for flag
[0x11] --> x4		--> To get 1 for flag
[0x12] --> x5		--> To get 1 for flag
}
```

My rough solution of the wheels are:
```
(0x06, 0x25, 0x0D) --> x0d = 0, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 1, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
(0x09, 0x08, 0x07) --> x0d = 1, x0e = 0, x0f = 0, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 0, x12 = 0
(0x09, 0x08, 0x08) --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 0, x12 = 0
!				   --> x0d = 1, x0e = 0, x0f = 1, x10 = 0, x11 = 0, x12 = 0
(0x16, 0x0b, 0x07) --> x0d = 1, x0e = 0, x0f = 1, x10 = 0, x11 = 0, x12 = 1
!				   --> x0d = 0, x0e = 0, x0f = 1, x10 = 0, x11 = 1, x12 = 1
(0x06, 0x25, 0x0D) --> x0d = 0, x0e = 0, x0f = 1, x10 = 1, x11 = 1, x12 = 1
(0x00, 0x00, 0x00) --> x0d = 0, x0e = 1, x0f = 1, x10 = 1, x11 = 1, x12 = 1
```

Solve script [here](./solution.py)

## Flag
> actf{this_is_how_lockpicking_works_right}
