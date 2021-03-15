from Crypto.Cipher import ARC4

key = b"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
plaintext = bytes.fromhex("7188bb1563e5702342e22a856ad3df1cfa9729b4115d8cfb1f07a0c6fc916477f02f77d656834379b32e")

cipher = ARC4.new(key)
ciphertext = cipher.decrypt(plaintext)
print(ciphertext.decode())