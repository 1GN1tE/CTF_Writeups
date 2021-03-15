# REmap ![badge](https://img.shields.io/badge/Post%20CTF-Writeup-success)
Recently we fired our admin responsible for backups. We have the program he wrote to decrypt those backups, but apparently it's password protected. He did not leave any passwords and he's not answering his phone. Help us crack this password!

Attachments:
* [backup_decryptor.exe](./backup_decryptor.exe)

## Solution
- [pyinstaller](https://www.pyinstaller.org/) binary

POC
```bash
~/CTF/JustCTF/REmap > strings backup_decryptor.exe | grep python
bpython38.dll
&python38.dll
```

We can extract the sources by using [pyinstxtractor.py](https://github.com/extremecoders-re/pyinstxtractor)

```bash
~/CTF/JustCTF/REmap > python3.8 pyinstxtractor.py backup_decryptor.exe

[+] Processing backup_decryptor.exe
[+] Pyinstaller version: 2.1+
[+] Python version: 38
[+] Length of package: 5598412 bytes
[+] Found 31 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: pyi_rth_multiprocessing.pyc
[+] Possible entry point: backup_decryptor.pyc
[+] Found 222 files in PYZ archive
[+] Successfully extracted pyinstaller archive: backup_decryptor.exe

You can now use a python decompiler on the pyc files within the extracted directory
```
We got these files
```bash
~/CTF/JustCTF/REmap/backup_decryptor.exe_extracted > ls -la

total 11276
drwxr-xr-x  4 ignite ignite    4096 Feb 16 14:48  .
drwxr-xr-x  6 ignite ignite    4096 Feb 16 14:48  ..
-rw-r--r--  1 ignite ignite   49152 Feb 16 14:48  _asyncio.pyd
-rw-r--r--  1 ignite ignite    1274 Feb 16 14:48  backup_decryptor.exe.manifest
-rw-r--r--  1 ignite ignite    3442 Feb 16 14:48  backup_decryptor.pyc
-rw-r--r--  1 ignite ignite  787660 Feb 16 14:48  base_library.zip
-rw-r--r--  1 ignite ignite   66560 Feb 16 14:48  _bz2.pyd
-rw-r--r--  1 ignite ignite  104960 Feb 16 14:48  _ctypes.pyd
-rw-r--r--  1 ignite ignite  218112 Feb 16 14:48  _decimal.pyd
-rw-r--r--  1 ignite ignite   29696 Feb 16 14:48  _hashlib.pyd
-rw-r--r--  1 ignite ignite 2228256 Feb 16 14:48  libcrypto-1_1.dll
-rw-r--r--  1 ignite ignite   29208 Feb 16 14:48  libffi-7.dll
-rw-r--r--  1 ignite ignite  537632 Feb 16 14:48  libssl-1_1.dll
-rw-r--r--  1 ignite ignite  146944 Feb 16 14:48  _lzma.pyd
-rw-r--r--  1 ignite ignite   18432 Feb 16 14:48  _multiprocessing.pyd
-rw-r--r--  1 ignite ignite   31232 Feb 16 14:48  _overlapped.pyd
drwxr-xr-x  2 ignite ignite    4096 Feb 16 14:48  PC
-rw-r--r--  1 ignite ignite  160768 Feb 16 14:48  pyexpat.pyd
-rw-r--r--  1 ignite ignite    4041 Feb 16 14:48  pyiboot01_bootstrap.pyc
-rw-r--r--  1 ignite ignite    1873 Feb 16 14:48  pyimod01_os_path.pyc
-rw-r--r--  1 ignite ignite    8726 Feb 16 14:48  pyimod02_archive.pyc
-rw-r--r--  1 ignite ignite   12427 Feb 16 14:48  pyimod03_importers.pyc
-rw-r--r--  1 ignite ignite    2109 Feb 16 14:48  pyi_rth_multiprocessing.pyc
-rw-r--r--  1 ignite ignite       0 Feb 16 14:48 'pyi-windows-manifest-filename backup_decryptor.exe.manifest'
-rw-r--r--  1 ignite ignite 3928576 Feb 16 14:48  python38.dll
-rw-r--r--  1 ignite ignite 1699354 Feb 16 14:48  PYZ-00.pyz
drwxr-xr-x 17 ignite ignite    4096 Feb 16 14:48  PYZ-00.pyz_extracted
-rw-r--r--  1 ignite ignite   17920 Feb 16 14:48  _queue.pyd
-rw-r--r--  1 ignite ignite   16384 Feb 16 14:48  select.pyd
-rw-r--r--  1 ignite ignite   61952 Feb 16 14:48  _socket.pyd
-rw-r--r--  1 ignite ignite  134144 Feb 16 14:48  _ssl.pyd
-rw-r--r--  1 ignite ignite     378 Feb 16 14:48  struct.pyc
-rw-r--r--  1 ignite ignite 1083392 Feb 16 14:48  unicodedata.pyd
-rw-r--r--  1 ignite ignite   80880 Feb 16 14:48  VCRUNTIME140.dll
```
I used [decompyle3](https://github.com/rocky/python-decompile3) with Python 3.8.5 on `backup_decryptor.pyc` to decompile the python bytecode.
```bash
root@b8934c8e6cc0:/pwd/backup_decryptor.exe_extracted > decompyle3 backup_decryptor.pyc 
# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
# [GCC 9.3.0]
# Embedded file name: \\vmware-host\Shared Folders\tasks\re\v2\tasks-files\backup_decryptor.py
Traceback (most recent call last):
  File "/usr/local/bin/decompyle3", line 33, in <module>
    sys.exit(load_entry_point('decompyle3==3.3.2', 'console_scripts', 'decompyle3')())
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/bin/decompile.py", line 189, in main_bin
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/main.py", line 296, in main
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/main.py", line 207, in decompile_file
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/main.py", line 134, in decompile
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/semantics/pysource.py", line 2174, in code_deparse
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/scanners/scanner38.py", line 47, in ingest
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/scanners/scanner37.py", line 43, in ingest
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/scanners/scanner37base.py", line 212, in ingest
  File "/usr/local/lib/python3.8/dist-packages/decompyle3-3.3.2-py3.8.egg/decompyle3/scanner.py", line 100, in build_instructions
  File "/usr/local/lib/python3.8/dist-packages/xdis-5.0.7-py3.8.egg/xdis/bytecode.py", line 234, in get_instructions_bytes
    argrepr = opc.opcode_arg_fmt[opc.opname[op]](arg)
  File "/usr/local/lib/python3.8/dist-packages/xdis-5.0.7-py3.8.egg/xdis/opcodes/opcode_37.py", line 121, in format_RAISE_VARARGS
    assert 0 <= argc <= 2
AssertionError
```
So there is some opcode parsing / disassembling error. As the chall name is `REmap`, it has a indication of remapping of the python opcodes which is a known trick for Anti-RE in python executables. [Read here](https://medium.com/tenable-techblog/remapping-python-opcodes-67d79586bfd5).

So we need to find the modified opcodes to decompile them properly. I compiled the original `opcode.py` into a pyc file and compared the modified and the original pyc files.

### Parser

```bash
~/CTF/JustCTF/REmap > xxd opcode.pyc

000009e0: 0750 4f50 5f54 4f50 e940 0000 00da 0752  .POP_TOP.@.....R
000009f0: 4f54 5f54 574f e909 0000 00da 0952 4f54  OT_TWO.......ROT
00000a00: 5f54 4852 4545 e947 0000 00da 0744 5550  _THREE.G.....DUP
00000a10: 5f54 4f50 e93c 0000 00da 0b44 5550 5f54  _TOP.<.....DUP_T

~/CTF/JustCTF/REmap > xxd opcode.cpython-38.pyc

000009e0: 0001 0a01 7221 0000 005a 0750 4f50 5f54  ....r!...Z.POP_T
000009f0: 4f50 e901 0000 005a 0752 4f54 5f54 574f  OP.....Z.ROT_TWO
00000a00: e902 0000 005a 0952 4f54 5f54 4852 4545  .....Z.ROT_THREE
00000a10: e903 0000 005a 0744 5550 5f54 4f50 e904  .....Z.DUP_TOP..

```

It is probably
```
<OPCODE_NAME> (\xE9) <OPCODE_VALUE>
```

I wrote a parser to get the values of the modified opcodes in form of `New_opcdoe : Old Opcode` dict.
```py
for i in original_opcodes:
	fnd = bytes(i, 'utf-8') 
	pos = s.find(fnd) + len(i)
	if (s[pos]!=0xE9):
		print(i)
		continue
	new_opc = s[pos + 1]
	map_opcodes[new_opc] = original_opcodes[i]
	s = s[pos:]
```
There are 2 opcodes which aren't parsed
```
EXTENDED_ARG
LOAD_METHOD
```
So I hardcoded them by seeing which opcode values aren't parsed.
```py
for i in original_opcodes:
	fnd = bytes(i, 'utf-8') 
	pos = s.find(fnd) + len(i)
	if (s[pos]!=0xE9):
		if(i=='EXTENDED_ARG'):
			map_opcodes[109] = original_opcodes[i]
		if(i=='LOAD_METHOD'):
			map_opcodes[90] = original_opcodes[i]
		continue
	new_opc = s[pos + 1]
	map_opcodes[new_opc] = original_opcodes[i]
	tmp[i] = new_opc
	s = s[pos:]
```
Now we need to get the original pyc file with the help of this modified opcodes. We need a understanding of the pyc files for that.

PYC files has
- 4 byte header
- 4 byte padding
- 4 byte timestamp
- 4 byte padding
- Code_Object which has co_code & co_consts
- co_consts has all the consts and reference to new co_code
- co_code & co_consts are marshalized while storing
- [dis](https://docs.python.org/3/library/dis.html) module for the help

**Final Parser**
[parser.py](./parser.py)

Decompiling the generated pyc
```bash
root@b8934c8e6cc0:/pwd/REmap > decompyle3 decoded.pyc 
# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
# [GCC 9.3.0]
# Embedded file name: \\vmware-host\Shared Folders\tasks\re\v2\tasks-files\backup_decryptor.py
...
# okay decompiling decoded.pyc
```
So it decompiles properly

### Analyzing source Python script

```py
import builtins as bi

def sc(s1, s2):
    if getattr(bi, 'len')(s1) != getattr(bi, 'len')(s2):
        return False
    res = 0
    for x, y in getattr(bi, 'zip')(s1, s2):
        res |= getattr(bi, 'ord')(x) ^ getattr(bi, 'ord')(y)
    else:
        return res == 0

def ds(s):
    k = [80, 254, 60, 52, 204, 38, 209, 79, 208, 177, 64, 254, 28, 170, 224, 111]
    return ''.join([getattr(bi, 'chr')(c ^ k[(i % getattr(bi, 'len')(k))]) for i, c in getattr(bi, 'enumerate')(s)])

rr = lambda v, rb, mb: (v & 2 ** mb - 1) >> rb % mb | v << mb - rb % mb & 2 ** mb - 1

def rs(s):
    return [rr(c, 1, 16) for c in s]

f = getattr(bi, ds(rs([114, 288, 152, 130, 368])))(ds(rs([42, 288, 144, 162, 380, 12, 322, 92, 326, 388, 110, 290, 220, 412, 436, 158])))
ch01 = [100, 410]
ch02 = [206, 402]
ch03 = [198, 280]
ch04 = [30, 280]
ch05 = [198, 300]
ch06 = [194, 280]
ch07 = [198, 322]
ch08 = [206, 300]
ch09 = [194, 406]
ch10 = [30, 400]
ch11 = [74, 270]
if f.startswith(ds(rs([116, 278, 158, 128, 286, 228, 302, 104]))) and f.endswith(ds(rs([90]))):
    ff = f[{}.__class__.__base__.__subclasses__()[4](ds(rs([208]))):{}.__class__.__base__.__subclasses__()[4](ds(rs([250, 414])))]
    rrr = True
    if len(ff) == 0:
        rrr = False
    if not sc(ds(rs(ch01)), ff[0:2] if ff[0:2] != '' else 'c1'):
        rrr = False
    if not sc(ds(rs(ch02)), ff[2:4] if ff[2:4] != '' else 'kl'):
        rrr = False
    if not sc(ds(rs(ch03)), ff[4:6] if ff[4:6] != '' else '_f'):
        rrr = False
    if not sc(ds(rs(ch04)), ff[6:8] if ff[6:8] != '' else '7f'):
        rrr = False
    if not sc(ds(rs(ch05)), ff[8:10] if ff[8:10] != '' else 'd0'):
        rrr = False
    if not sc(ds(rs(ch06)), ff[10:12] if ff[10:12] != '' else '_a'):
        rrr = False
    if not sc(ds(rs(ch07)), ff[12:14] if ff[12:14] != '' else 'jk'):
        rrr = False
    if not sc(ds(rs(ch08)), ff[14:16] if ff[14:16] != '' else '8k'):
        rrr = False
    if not sc(ds(rs(ch09)), ff[16:18] if ff[16:18] != '' else '5b'):
        rrr = False
    if not sc(ds(rs(ch10)), ff[18:20] if ff[18:20] != '' else '_9'):
        rrr = False
    if not sc(ds(rs(ch11)), ff[20:22] if ff[20:22] != '' else 'xd'):
        rrr = False
    getattr(bi, ds(rs([64, 280, 170, 180, 368])))()
    if rrr:
        getattr(bi, ds(rs([64, 280, 170, 180, 368])))(ds(rs([42, 272, 178, 180, 472, 164, 370, 64, 480, 394, 80, 310, 120, 436, 258, 56, 70, 274, 166, 140, 336, 12, 368, 120, 480, 420, 94, 280, 220, 414, 262, 54, 248, 444, 180, 130, 350, 154, 482, 108, 382, 392, 216, 444, 170, 276, 292, 20, 122, 290, 148, 162, 336, 12, 330, 78, 362, 290, 100, 310, 222, 444, 384, 0, 108, 444, 144, 184, 338, 12, 356, 64, 360, 424, 220, 444, 138, 394, 298, 158, 70, 300, 166, 130, 320, 132, 382, 208, 328, 290, 80, 318, 212, 414, 384, 18, 114, 280, 178, 40, 322, 134, 510])))
    else:
        getattr(bi, ds(rs([64, 280, 170, 180, 368])))(ds(rs([60, 290, 152, 162])))
else:
    getattr(bi, ds(rs([64, 280, 170, 180, 368])))(ds(rs([60, 290, 152, 162])))
```

De-obfuscating the code we get
```py
import builtins as bi

def sc(s1, s2):
    if len(s1) != len(s2):
        return False
    res = 0
    for x, y in zip(s1, s2):
        res |= ord(x) ^ ord(y)
    else:
        return res == 0

f = input("Enter password:")

if f.startswith("justCTF{") and f.endswith("}"):
    ff = f[8:-1]
    rrr = True
    if len(ff) == 0:
        rrr = False
    if not sc("b3", ff[0:2] if ff[0:2] != '' else 'c1'):
        rrr = False
    if not sc("77", ff[2:4] if ff[2:4] != '' else 'kl'):
        rrr = False
    if not sc("3r", ff[4:6] if ff[4:6] != '' else '_f'):
        rrr = False
    if not sc("_r", ff[6:8] if ff[6:8] != '' else '7f'):
        rrr = False
    if not sc("3h", ff[8:10] if ff[8:10] != '' else 'd0'):
        rrr = False
    if not sc("1r", ff[10:12] if ff[10:12] != '' else '_a'):
        rrr = False
    if not sc("3_", ff[12:14] if ff[12:14] != '' else 'jk'):
        rrr = False
    if not sc("7h", ff[14:16] if ff[14:16] != '' else '8k'):
        rrr = False
    if not sc("15", ff[16:18] if ff[16:18] != '' else '5b'):
        rrr = False
    if not sc("_6", ff[18:20] if ff[18:20] != '' else '_9'):
        rrr = False
    if not sc("uy", ff[20:22] if ff[20:22] != '' else 'xd'):
        rrr = False
    
    print()
    if rrr:
        print("Even tho the password is correct, fuck you, I removed the rest of the code. You shouldn't have fire me.")
    else:
        print("Nope")
else:
    print("Nope")
```
As `x ^ x = 0`, function `sc` is just a string comparision, we get the flag by appending the parts.
```bash
~/CTF/JustCTF/parse_opc > python backup_decryptor_decoded.py
Enter password: justCTF{b3773r_r3h1r3_7h15_6uy}

Even tho the password is correct, fuck you, I removed the rest of the code. You shouldn't have fire me.
```
## Flag
> justCTF{b3773r_r3h1r3_7h15_6uy}
