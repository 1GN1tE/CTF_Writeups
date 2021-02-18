def magic(val, inp):
	if(val==00):
		res = ((inp >> 3) | (inp << 5)) & 0xff
	elif(val==1):
		res = ((inp << 2) | (inp >> 6)) & 0xff
	elif(val==2):
		res = (inp + int('110111',2)) & 0xff
	elif(val==3):
		res = (inp ^ 55) & 0xff
	return res

def chall(inp):
	val0 = (inp >> 0) & 3
	val1 = (inp >> 2) & 3
	val2 = (inp >> 4) & 3
	val3 = (inp >> 6) & 3

	res0 = magic(val0, inp)
	res1 = magic(val1, res0)
	res2 = magic(val2, res1)
	res3 = magic(val3, res2)

	return res3

if __name__ == '__main__':
	target = [182, 199, 159, 225, 210, 6, 246, 8, 172, 245, 6, 246, 8, 245, 199, 154, 225, 245, 182, 245, 165, 225, 245, 7, 237, 246, 7, 43, 246, 8, 248, 215]

	printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~"
	flag = ['']*len(target)
	for i in range(len(target)):
		for ch in printable:
			if(chall(ord(ch))==target[i]):
				flag[i]= ch
				print(i,ch)

print("".join(flag))