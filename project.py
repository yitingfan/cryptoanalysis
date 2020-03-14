import argparse
import difflib

def similar(plaintext):
    d = {1:'gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee',
    2:'intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor',
    3:'frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p',
    4:'distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg',
    5:'undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis'}
    max = 0
    index = 0
    candidate = ''
    for key in d:
        score = difflib.SequenceMatcher(None, plaintext, d[key]).quick_ratio()      # Compute score between plaintext and each candidates
        if score > max:
            index = key                     # return the index of candidate in the 5 strings.
            candidate = d[key]              # Subsititue the candidate with the correct one who has the highest score
            max = score                     # update score
    return index, candidate

def correct(plaintext):
    wordList = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose']
    plain_wordList = plaintext.split()
    max = 0
    candidate = ''
    result = ''
    for w in plain_wordList:                                                    # traverse each word in the plaintext
        if w not in wordList:                                                   # if the word is not in the candidate wordlist, it means the plain-word exists error
            for p in wordList:                                                  # traverse each word in the candidate wordlist and get score of the similar between the error plain-word and the each candidate one.
                score = difflib.SequenceMatcher(None, p, w).quick_ratio()
                if score > max:
                    candidate = p
                    max = score
            w = candidate                                                       # update the error word to the word who has the highest score in similarity
    for w in plain_wordList:
        result = result + w + ' '                                               # Concatentate the correct word into the plaintext result
    return result[:-1]

def length(Ciphertext):
    ListCiphertext=list(Ciphertext)
    Keylength=1
    while True:
        CoincidenceIndex = 0

        for i in range(Keylength):
            Numerator = 0
            PresentCipherList = ListCiphertext[i::Keylength]                                        # PresentCipherList is intercept the ciphertext which is as long as the guessing current keylength

            # IC = \frac{\sum_{i=1}^c n_i(n_i - 1)}{N(N-1)/c}
            # https://en.wikipedia.org/wiki/Index_of_coincidence            
            
            for Letter in set(PresentCipherList):                                                   # Loop is for the sum function
                Numerator += PresentCipherList.count(Letter) * (PresentCipherList.count(Letter)-1)  # Numerator represents the molecule of the IC function. The count of letter in PresentCipherList is n_i
            CoincidenceIndex += Numerator/(len(PresentCipherList) * (len(PresentCipherList)-1))     # CoincidenceIndex is the result of IC function. The length of PresentCipherList is N

        Average=CoincidenceIndex / Keylength                                                        # Compute the average value of conincidenceindex of each subgroup of ciphertext
        Keylength += 1

        if Average > 0.06:                                                                          # If average is greater than 0.06 then break
            break
    Keylength -= 1
    return Keylength

def space(letter, m):                                                                # The function is used to analyze the space character when recovering the keyword, m is current brute-forced offset of key
    #return the current plaintext bit.
    origin_cipher = ord(letter)
    chr_plain = (ord(letter) - 97 - m) % 27                                          # Get the corresponding number in the dict of the character in plaintext
    space_plain = (26 - m) % 27                                                      # Get the corresponding number in the dict of the character in plaintext if the ciphertext is space chracter
    if origin_cipher == 32 and space_plain == 26:                                    # if cipher is space char & m is 0 (no offset in key currently) which means corresponding plain is space, too
        return ' '
    elif origin_cipher == 32 and space_plain != 26:                                  # if cipher is space char & plain is not space.
        return chr(space_plain + 97)
    elif origin_cipher != 32 and chr_plain == 26:                                    # if cipher is not space char & plain is space.
        return ' '
    elif origin_cipher != 32 and chr_plain != 26:                                    # if cipher and plain both are not space
        return chr(chr_plain + 97)

def keyword(Ciphertext,keylength):
    ListCiphertext = list(Ciphertext)
    Standard = {'a':0.0655307059, 'b':0.0127076566, 'c':0.0226508836, 'd':0.0335227377, 'e':0.1021787708, 'f':0.0197180888, 'g':0.0163586607, 'h':0.0486220925, 'i':0.0573425524, 'j':0.0011440544, 'k':0.0056916712, 'l':0.0335616550, 'm':0.0201727037, 'n':0.0570308374, 'o':0.0620055405, 'p':0.0150311560, 'q':0.0008809302, 'r':0.0497199926, 's':0.0532626738, 't':0.0750999398, 'u':0.0229520040, 'v':0.0078804815, 'w':0.0168961396, 'x':0.0014980832, 'y':0.0146995463, 'z':0.0005979301, ' ':0.1831685753}
    
    # http://www.macfreek.nl/memory/Letter_Distribution
    # Each letter's average frequency statistic

    KeyResult = []
    for i in range(keylength):
        PresentCipherList = ListCiphertext[i::keylength]                                                # divide the cipher text into i-length parts
        QuCoincidenceMax = 0
        KeyLetter = "*"
        for m in range(27):                                                                             # traverse the key from 0 to 26
            QuCoincidencePresent = 0                                                                    # initialize the QuCoincidencePresent to 0
            for Letter in set(PresentCipherList):
                LetterFrequency = PresentCipherList.count(Letter) / len(PresentCipherList)
                k = space(Letter, m)                                                                    # when key is m, the corresponding plaintext.
                StandardFrequency = Standard[k]                                                         # the corresponding frequency
                QuCoincidencePresent = QuCoincidencePresent + LetterFrequency * StandardFrequency       # calculate the QuCoincidencePresent when key is m
            if QuCoincidencePresent > QuCoincidenceMax:                                                 # when traversing the key from 0 to 27, calculate the QuCoincidenceMax, save it. and keep the corresponding key.
                QuCoincidenceMax = QuCoincidencePresent
                KeyLetter = m
        KeyResult.append(KeyLetter)
    return KeyResult

def decrypt(cipher, keylength, key):
    dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, ' ':27}
    dict2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z', 27:' '}
    plain = ''
    for c in range(500):
        j = c % keylength                               # j is the exact bit of key (key[j]) which is used to do the decryption with the corresponding cipher bit.
        p = dict[cipher[c]] - key[j] % 28               # p is the result of plaintext after reverse shift process
        if p < 0:                                       # when p is negative it needs to add 27 to get correct plaintext bit
            p += 27
        if p == 0:                                      # when p is 0, it means after reverse shifting, the corresponding cipherbit is 1 less than 'a', and the plain bit is actually space character
            plain += ' '
        else:
            plain += dict2[p]                           # Through concatenating with new computed plaintext bit to get the entire plaintext.
    return plain

def main():
    '''
    python decrypt.py --test 1 --cipher "xxxx"
    '''
    parser = argparse.ArgumentParser(description="Manual Document")
    parser.add_argument('--test', choices=['1', '2'], default = "1", help = "Input test number")
    parser.add_argument('--cipher', type = str, help="Input the ciphertext with double quotes")
    args = parser.parse_args()
    cipher = args.cipher
    keylength = length(cipher)
    key = keyword(cipher, keylength)    # The keyword may exist some error in some bits, it will result errors in plaintext as well, so we need similar() and correct()
    plaintext = decrypt(cipher, keylength, key)

    if args.test == '1':
        print(similar(plaintext))       # Compute the similar score between the decrypted plaintext and the candidates. Find the max score one
    if args.test == '2':
        print(correct(plaintext))       # Fix the keyword error

if __name__ == "__main__":
   main()
