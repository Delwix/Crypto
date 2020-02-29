from pwn import *

def main():
	result = ""
	flag = "CCCCCCCCCCCCCCA"
	k = 0
	for i in range(50):
		payload = ""
		for i in range(33,126):
			payload += flag+chr(i)
		payload += "C"*(46-k)

		r = remote("tasks.aeroctf.com",44323)
		r.sendline("3")
		x = r.recvuntil('Enter salt: ',drop = True)
		r.sendline(payload)
		y = r.recvline()
		r.close()
		y = y[24:-2]
		b64cipher = y.decode("utf-8")
		#print(b64cipher)
		hexCipher = base64.b64decode(b64cipher).hex()
		#print(hexCipher)
		c = hexCipher.index(hexCipher[95*32:95*32+32])
		#print(hexCipher[95*32:95*32+32],"  ",c)
		chfound = payload[c//2+15]
		result += chfound
		flag = flag[1:15]+chfound
		print(chfound)
		print(flag)
		k += 1				
		if chfound == "}":
			print("done")
			print(result)
			exit()
		

if __name__ == '__main__':
    main()
