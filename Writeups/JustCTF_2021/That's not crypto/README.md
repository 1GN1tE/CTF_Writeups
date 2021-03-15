# That's not crypto

This is very simple RE task, but you may need some other skills as well. :)

Attachments:
* [checker.pyc](./checker.pyc)

## Solution
- PYC decompile
```py
def validate(a):
    # xs --> flag
    def poly(a, x):
        value = 0
        for ai in a:
            value *= x
            value += ai

        return value
    flag_acc = ord("j")
    flag_str = "j"

    c = 0
    while(c<56):
        i = flag_acc+20
        while(True):
            value = poly(a, i*69684751861829721459380039L)
            if value == 24196561:
                flag_str+= chr(i-flag_acc)
                flag_acc = i
                break
            i += 1
        c += 1

    print(flag_str)
```

## Flag
> justCTF{this_is_very_simple_flag_afer_so_big_polynomails}
