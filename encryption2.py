import random

wordList = [
'awesomeness',
'hearkened',
'aloneness',
'beheld',
'courtship',
'swoops',
'memphis',
'attentional',
'pintsized',
'rustics',
'hermeneutics',
'dismissive',
'delimiting',
'proposes',
'between',
'postilion',
'repress',
'racecourse',
'matures',
'directions',
'pressed',
'miserabilia',
'indelicacy',
'faultlessly',
'chuted',
'shorelines',
'irony',
'intuitiveness',
'cadgy',
'ferries',
'catcher',
'wobbly',
'protruded',
'combusting',
'unconvertible',
'successors',
'footfalls',
'bursary',
'myrtle',
'photocompose']

possibleK = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

MSpace = {' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

MSpace_2 = {0:' ', 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

def generate_plaintext(L,wordList):
	plaintext = ''
	while len(plaintext)< L:
		randomIndex = random.randint(0,39)
		if (len(plaintext)+len(wordList[randomIndex])) <= L:
			plaintext += wordList[randomIndex]
			if (len(plaintext)+1) < L:
				plaintext += ' '
		else:
			return 0
	return plaintext

def key_sheduling_algo_linear(L,K,linear_factor,t):
	random_string = []
	for i in range(1,L+1):
		j = 1+(linear_factor*i)%t
		random_string.append(K[j])

	return random_string

def key_sheduling_algo_poly(L,K,poly_factor,t):
	random_string = []
	for i in range(1,L+1):
		j = 1+pow(i, poly_factor)%t
		random_string.append(K[j])

	return random_string

def generate_key(t,possibleK):
	KeyIndex = random.sample(range(0, 27), t)
	K = {}
	for i in range (1,t+1):
		K[i] = possibleK[KeyIndex[i-1]]
	return K

def encryption(plaintext, random_string,L,MSpace,MSpace_2):
	ciphertext = ''
	for i in range(L):
		ciphertext += MSpace_2[(MSpace[plaintext[i]]+random_string[i])%27]
	return ciphertext

L = 500
plaintext = 0
while plaintext ==0:
	plaintext = generate_plaintext(L,wordList)
print(plaintext)
#print(len(plaintext))
t = 4
K = generate_key(4,possibleK)
#print(K)
poly_factor = 1
random_string = key_sheduling_algo_poly(L,K,poly_factor,t)
#print(random_string)
ciphertext = encryption(plaintext, random_string,L,MSpace,MSpace_2)
print(ciphertext)
#print(len(ciphertext))





