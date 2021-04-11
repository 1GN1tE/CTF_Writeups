import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
import sys, datetime, getopt, getpass, time, random, secrets, struct, aes_keywrap
HEADER_FMT = '>5sB8s40si'
FILE_MAGIC = 'EFC82'
DATA_MAGIC = FILE_MAGIC
FILE_VERSION = 1
HEADER_SIZE = struct.calcsize(HEADER_FMT)

def get_rng(seed=None):
	rnd = random.Random()
	if not seed:
		user = getpass.getuser()
		ts_ms = datetime.datetime.now().isoformat(sep='!', timespec='milliseconds')
		rdata = str(random.getrandbits(256))
		seed = f"{user}_{ts_ms}_{rdata}"
	rnd.seed(seed)
	return rnd


def generate_key() -> bytes:
	return secrets.token_bytes(32)


def generate_iv_part() -> bytes:
	return secrets.token_bytes(8)


def generate_ephemeral_key() -> bytes:
	rnd = get_rng()
	return bytes((rnd.getrandbits(8) for _ in range(32)))


def encrypt_file(filename: str, kek: bytes):
	try:
		file_plain = open(filename, 'rb')
		new_filename = f"{filename}.enc"
		file_enc = open(new_filename, 'wb')
		ephemeral_key = generate_ephemeral_key()
		iv_part = generate_iv_part()
		encryptor = AES.new(ephemeral_key, mode=(AES.MODE_CTR), counter=Counter.new(64, prefix=iv_part))
		data = file_plain.read()
		enc_data = encryptor.encrypt(DATA_MAGIC + data)
		wrapped_ephemeral_key = wrap_key(ephemeral_key, kek)
		header = struct.pack(HEADER_FMT, FILE_MAGIC, FILE_VERSION, iv_part, wrapped_ephemeral_key, len(enc_data))
		file_enc.write(header)
		file_enc.write(enc_data)
		file_enc.close()
		file_plain.close()
		print(f"File encrypted, saved as {new_filename}")
	except Exception as e:
		try:
			print(f"Error encrypting file! ({e})")
			sys.exit(-2)
		finally:
			e = None
			del e


def decrypt_file(filename: str, kek: bytes):
	file_enc = None
	file_plain = None
	error = False
	try:
		try:
			if not filename.endswith('.enc'):
				raise Exception('Invalid file extension')
			file_enc = open(filename, 'rb')
			new_filename = filename.strip('.enc')
			enc_data = file_enc.read()
			header = enc_data[:HEADER_SIZE]
			magic, version, iv_part, wrapped_ek, filelen = struct.unpack(HEADER_FMT, header)
			if magic != FILE_MAGIC or version != 1 or filelen != len(enc_data) - HEADER_SIZE:
				raise Exception('File is corrupt, or not an encrypted file')
			ephemeral_key = unwrap_key(wrapped_ek, kek)
			decryptor = AES.new(ephemeral_key, mode=(AES.MODE_CTR), counter=Counter.new(64, prefix=iv_part))
			data = decryptor.decrypt(enc_data[HEADER_SIZE:])
			if not data.startswith(DATA_MAGIC):
				raise Exception('File is corrupt, or not an encrypted file')
			print('Decrypted data:')
			print(data[len(DATA_MAGIC):])
			print(f"File decrypted, saved as {new_filename}")
		except ValueError as e:
			try:
				print('Invalid encryption key')
				error = True
			finally:
				e = None
				del e

		except Exception as e:
			try:
				print(f"Error decrypting file! ({e})")
				error = True
			finally:
				e = None
				del e

	finally:
		if file_enc:
			file_enc.close()
		if file_plain:
			file_plain.close()
		if error:
			sys.exit(-3)


def usage(exit_code: int=None):
	print(' Usage:\n  -e <file>  encrypt file\n  -d <file>	decrypt file\n  -w <plain>	wrap key, specify kek with -k\n  -g   generate random key\n  -u <wrapped>  unwrap key, specify kek with -k\n  -k <key>   256 bit encryption key on hex format, e.g. 559da78646b398e348ec90c25858310d285449522a25090bd1fa1d1e2ff46abf\n  ')
	if exit_code:
		sys.exit(exit_code)


def wrap_key(plain, kek):
	return aes_keywrap.aes_wrap_key(kek, plain)


def unwrap_key(enc, kek):
	return aes_keywrap.aes_unwrap_key(kek, enc)


if __name__ == '__main__':
	random.seed('0427cb12119c11aff423b6333c4189175b22b3c377718053f71d5f37fd2a8f22')
	filename = ''
	wrap_oper = ''
	key = ''
	mode = None
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'ghe:d:w:u:k:')
	except getopt.GetoptError:
		print('getopts error')
		print(usage)
		sys.exit(-1)
	else:
		for opt, arg in opts:
			if opt == '-h':
				usage(0)

	if opt in ('-e', '-d'):
		filename = arg
		if not mode:
			mode = opt
		else:
			usage(-1)
	elif opt in ('-w', '-u'):
		wrap_oper = arg
		if not mode:
			mode = opt
		else:
			usage(-1)
	elif opt == '-k':
		key = arg
	else:
		if opt == '-g':
			mode = opt
		if mode != '-g':
			if not key:
				usage(-1)
			if mode == '-e':
				encrypt_file(filename, binascii.unhexlify(key))
		elif mode == '-d':
			decrypt_file(filename, binascii.unhexlify(key))
		else:
			if mode == '-w':
				wrapped = wrap_key(binascii.unhexlify(wrap_oper), binascii.unhexlify(key))
				print(f"Wrapped key: {binascii.hexlify(wrapped).decode()}")
			else:
				if mode == '-u':
					plain = unwrap_key(binascii.unhexlify(wrap_oper), binascii.unhexlify(key))
					print(f"Unwrapped key: {binascii.hexlify(plain).decode()}")
				else:
					if mode == '-g':
						print(f"Key: {binascii.hexlify(generate_key()).decode()}")