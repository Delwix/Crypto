import codecs



def XOR(A,i):
    R =[]
    for j in range(len(A)):
        R.append(A[j] ^ i)
    return bytearray(R)

def get_score(array) : 
    score = 0
    freqs = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    for i  in array:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score
    
def main():
    score=[]
    a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    A = codecs.decode(a,'hex')
    for i in range(256):
        S = XOR(A,i)
        score.append(get_score(S))
    m = score.index(max(score))
    print(codecs.decode(XOR(A,m)))
    
        
if __name__ == '__main__':
    main()
        
