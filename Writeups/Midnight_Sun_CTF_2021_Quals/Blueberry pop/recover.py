#!/usr/bin/env python3
import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
from tqdm import trange
import random, struct, getpass, datetime

HEADER_FMT = b'>5sB8s40si'
FILE_MAGIC = b'EFC82'
DATA_MAGIC = FILE_MAGIC
FILE_VERSION = 1
HEADER_SIZE = struct.calcsize(HEADER_FMT)

def decrypt_file(seed):
	filename = "message.txt.enc"
	file_enc = None
	file_plain = None
	error = False
	try:
		try:
			if not filename.endswith('.enc'):
				raise Exception('Invalid file extension')
			file_enc = open(filename, 'rb')
			enc_data = file_enc.read()
			header = enc_data[:HEADER_SIZE]
			magic, version, iv_part, wrapped_ek, filelen = struct.unpack(HEADER_FMT, header)
			if magic != FILE_MAGIC or version != 1 or filelen != len(enc_data) - HEADER_SIZE:
				raise Exception('File is corrupt, or not an encrypted file')
			rnd = random.Random()
			rnd.seed(seed)
			ephemeral_key = bytes((rnd.getrandbits(8) for _ in range(32)))
			decryptor = AES.new(ephemeral_key, mode=(AES.MODE_CTR), counter=Counter.new(64, prefix=iv_part))
			data = decryptor.decrypt(enc_data[HEADER_SIZE:])
			if not data.startswith(DATA_MAGIC):
				raise Exception('File is corrupt, or not an encrypted file')
			print("SEED:", seed)
			print('Decrypted data:', data[len(DATA_MAGIC):].decode())
		except ValueError as e:
			try:
				print('Invalid encryption key')
				error = True
			finally:
				e = None
				del e
	except:
		pass


user = 'erism'
random.seed(b'0427cb12119c11aff423b6333c4189175b22b3c377718053f71d5f37fd2a8f22')
rdata = str(random.getrandbits(256))


for milisec in range(999, -1, -1):
	ts_ms = '2021-02-09!07:23:54.'+str(milisec).zfill(3)
	seed = f"{user}_{ts_ms}_{rdata}"
	decrypt_file(seed)