# ABNF: grammar is fun

There is binary provided, it check if flag is correct. However, it accepts more than just flag.
From all accepted inputs, flag is (in that order):

* correct (in sense of format),
* shortes,
* lexicographically first.

So, shorter but not correct accepted input is not flag.

Attachments:
* [checker.out](./checker.out)

## Solution

- C++ binary
- It takes 2nd argument as the flag else it prints `No flag? Too much flags?`

Then it initializes some data.
After that the we come to the checking part which roughly translates to
```cpp
if ((((flag_len < 4) || ((*flag | 0x20) != 'a')) || ((flag[1] | 0x20) != 's')) || (((flag[2] | 0x20) != 'i' || ((flag[3] | 0x20) != 'a'))))
{
	uVar1 = flag_check(flag);
	if ((char)uVar1 == 0)
		GOTO ERROR
	else
		GOTO RIGHT
}
else
	GOTO RIGHT

RIGHT:
cout << "Ok?";
return;

ERROR:
// Some error printing stuff
return;
```

So our flag is right if it is `asia` or if the function `flag_check`(`sub_4960`). As we know the flag starts with `justCTF{` we analyze `flag_check`

### Flag Checker

`flag_check` function checks chars at positions, it converts the chars to lowercase (by `| 0x20`) before checking.
As the chall name is [ABNF Grammer](https://en.wikipedia.org/wiki/Augmented_Backus%E2%80%93Naur_form) we can understand the function is some form of regex.

**Rough Decompilation:** [flag_check.cpp](./flag_check.cpp)

So according to the chall description the flag should be
- `justCTF{`
- `a`					(ignore the next check block)
- `left`
- `_`
- `long`				(ignore the next check block)
- `0`					(smallest digit)
- `_`
- `hard`
- `-`
- `xoxoxoxoxoxoxoxo`	(ignoring the 1st checker block which doesn't make sense)
- `}`

The regex is `justCTF{a+b?b?(something_else|left|right)_(short|long)(c*dd)*[digit]+_(simple|hard)-((wrc){0,3}(qsp|wsp|(cwr)*))*(xoxo){4}}`
So we get `justCTF{aleft_long0_hard-xoxoxoxoxoxoxoxo}`, using this as argument gives:
```bash
./checker.out justCTF{aleft_long0_hard-xoxoxoxoxoxoxoxo}
Ok?
```

## Flag
> justCTF{aleft_long0_hard-xoxoxoxoxoxoxoxo}
