# Exciting Offer

You just got a good offer via email, it looks promising, novirus is inside it - can you find the wealthy flag hidden inside?

Attachments:
* [Offer_details.doc](./Offer_details.doc)
* [encrytped_flag.txt](./encrytped_flag.txt)

## Solution
We are given a malware Microsoft Word file. Running [vmonkey](https://github.com/decalage2/ViperMonkey) on the word files gives a base64 encoded powershell code. Log [here](./Offer_details.doc.log). Base64 decrypting and deobfuscating the code we get this [script](./weird.ps1)

So it intends to download `https://github.com/joezid/joezid.github.io/raw/main/Images/Weirdo.png` this file and saves it as `T14e00.exe` at `$HOME\D8c98nn\Oss08b_\` directory, and runs the file.

### Analysis of malware PE file
The binary is LLVM obfuscated. Basically it does the following things :
- Allocates some memory/buffer and decrypts a key `E45y_as_1234`
- Uses the key to decrypt a buffer. Decrypted buffer is a PE file
- Creates a new process and writes the memory of the decrypted buffer into it and continues the process

Used x32dbg `savedata` command while debugging to dump the [PE file](./dump_binary.exe)

### Analysis of dumped PE file
The binary is also LLVM obfuscated. Basically it does the following things :
- Some anti debugging stuff
- Decrypts a filename `C:\\data.text`. Opens the file and reads 48 bytes of data
- Calculates a value based on all the characters `sum += i ^ 0xBB`. Uses the sum to initialize srand
- Uses rand to get a 32 byte keystream. `key[i] = (rand() % 256) ^ 0x9D`.
- Encrypts the data from file using the key with serpent cipher.

### Script
We are given the encrypted flag. So we can bruteforce the srand and decrypt to get the flag. Script [here](./Solution/decrypt.c)

## Flag
>  `S3D{D0_y0u_th1nk_thr33_st4g3s_4r3_3n0ugh_0r_n0t}`