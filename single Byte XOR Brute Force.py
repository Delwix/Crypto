import codecs

a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
A = codecs.decode(a,'hex')


R =[]
for i in range(0,256):
    R =[]
    for j in range(len(A)):
        R.append(A[j] ^ i)
    print("result = ",i,bytearray(R),"\n")
