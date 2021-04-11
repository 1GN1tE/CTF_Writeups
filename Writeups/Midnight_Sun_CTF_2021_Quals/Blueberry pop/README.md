# Blueberry pop

Eric from the organization 'Our future' seems to be in distress. What seems to be the issue?

Attachments:
* [HILFE.eml](./HILFE.eml)

## Solution
We are given an email text file, it has a message and 2 base64 encoded files.
- message.zip (--> message.txt.enc)
- filekryptor (ELF binary)

Reading the email we can see that a person named Eric attached an encrypted message and and the encryption software.

### Binary Analysis
Basic analysis says it's a [pyinstaller](https://github.com/pyinstaller/pyinstaller) ELF binary. So I used `archive_viewer.py` to view the contents of the ELF and extracted `main`.

Then added the python3.8 header...
```sh
$  xxd main.pyc 
00000000: 550d 0d0a 0000 0000 0000 0000 0000 0000  U............... <Added>
00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
```
Then decompiled to [main.py](./main.py)

### Python Script Analysis
The file encryption is as follows:
```py
ephemeral_key = generate_ephemeral_key()
iv_part = generate_iv_part()
encryptor = AES.new(ephemeral_key, mode=(AES.MODE_CTR), counter=Counter.new(64, prefix=iv_part))
data = file_plain.read()
enc_data = encryptor.encrypt(DATA_MAGIC + data)
wrapped_ephemeral_key = wrap_key(ephemeral_key, kek)
header = struct.pack(HEADER_FMT, FILE_MAGIC, FILE_VERSION, iv_part, wrapped_ephemeral_key, len(enc_data))
```
The iv is directly written to the file but key is wrapped with another key before writing to the file. So let's see how the key is generated.

```py
def get_rng(seed=None):
  rnd = random.Random()
  if not seed:
    user = getpass.getuser()
    ts_ms = datetime.datetime.now().isoformat(sep='!', timespec='milliseconds')
    rdata = str(random.getrandbits(256))
    seed = f"{user}_{ts_ms}_{rdata}"
  rnd.seed(seed)
  return rnd

def generate_ephemeral_key() -> bytes:
  rnd = get_rng()
  return bytes((rnd.getrandbits(8) for _ in range(32)))
```
So the seed of the randbytes generated for key is:

```
{user--> username of system}_{ts_ms --> system time}_{rdata --> random 256 bytes}
```
**Getting Username**

Since the mail is snet by Eric, we can guess the username is either `eric` or `erism` from the mail.

**Getting Timestamp**

Since the `message.txt.enc` is extracted from a zip file... it must have time stamp in metadata. Since tools show date and time relative to system clock, I set my system timezone to `Galapagos` (location of Eric as said in mail) and ran exiftool.
```
ExifTool Version Number         : 12.16
File Name                       : message.txt.enc
Directory                       : .
File Size                       : 114 bytes
File Modification Date/Time     : 2021:02:09 07:23:54-06:00
File Access Date/Time           : 2021:02:09 07:23:54-06:00
File Inode Change Date/Time     : 2021:04:10 06:42:52-06:00
File Permissions                : rw-rw-r--
Error                           : Unknown file type
```

**Getting rdata**

There is a weird random seed in main that is never used anywhere
```py
if __name__ == '__main__':
	random.seed('0427cb12119c11aff423b6333c4189175b22b3c377718053f71d5f37fd2a8f22')
```
So I used this as seed of the bytes to get `rdata`

Now we have got everything we need to generate key. I just bruteforced the milliseconds in timsestamp to get the flag and the username out of the two.
Solve script [here](./recover.py)

```
SEED: erism_2021-02-09!07:23:54.394_92849977341694677191296853758153177664350513157068923394541899973518756914986
Decrypted data: midnight{YABSRG_y3t_4n0th3r_b4d_s33d3d_r4nd0m_g3n}
```

## Flag
> midnight{YABSRG_y3t_4n0th3r_b4d_s33d3d_r4nd0m_g3n}
