def space(letter, m):
    origin_cipher = ord(letter)
    chr_plain = (ord(letter) - 97 - m) % 27
    space_plain = (26 - m) % 27
    if origin_cipher == 32 and space_plain == 26:
        return ' '
    elif origin_cipher == 32 and space_plain != 26:
        return chr(space_plain + 97)
    elif origin_cipher != 32 and chr_plain == 26:
        return ' '
    elif origin_cipher != 32 and chr_plain != 26:
        return chr(chr_plain + 97)

def keyword(Ciphertext,keylength):
    ListCiphertext = list(Ciphertext)
    Standard = {'a':0.0655307059, 'b':0.0127076566, 'c':0.0226508836, 'd':0.0335227377, 'e':0.1021787708, 'f':0.0197180888, 'g':0.0163586607, 'h':0.0486220925, 'i':0.0573425524, 'j':0.0011440544, 'k':0.0056916712, 'l':0.0335616550, 'm':0.0201727037, 'n':0.0570308374, 'o':0.0620055405, 'p':0.0150311560, 'q':0.0008809302, 'r':0.0497199926, 's':0.0532626738, 't':0.0750999398, 'u':0.0229520040, 'v':0.0078804815, 'w':0.0168961396, 'x':0.0014980832, 'y':0.0146995463, 'z':0.0005979301, ' ':0.1831685753}
 
    while True:
        KeyResult = []
        for i in range(keylength):
            PresentCipherList = ListCiphertext[i::keylength]
            QuCoincidenceMax = 0
            KeyLetter = "*"
            for m in range(27):
                QuCoincidencePresent = 0
                for Letter in set(PresentCipherList):
                    LetterFrequency = PresentCipherList.count(Letter) / len(PresentCipherList)
                    k = space(Letter, m)
                    StandardFrequency = Standard[k]
                    QuCoincidencePresent = QuCoincidencePresent + LetterFrequency * StandardFrequency
                if QuCoincidencePresent > QuCoincidenceMax:
                    QuCoincidenceMax = QuCoincidencePresent
                    KeyLetter = m
            KeyResult.append(KeyLetter)
        break
    return KeyResult

ciphertext = 'gpurttgthrpjebbnto ivnnqrnvhcjrbsrvexgdrfqpjhapeyqxvujmiyaujitzfgimqcotvebuanbkkdtbrvtiukfmrhadrfgimokektmfvoqkpjz iqpqk vvdor fvqbhvxrynz iqykdx qijvrfbrfqugoqgomuegtimpzftrfgimdvichruqdkurcsygqiqlrpqdghreedfvqbtgthvgqhcirejaozlgqzqkekdtuqdqefujaeaebbnpxygomrharrtcdqcq wcvucnvzpuqswtxgumukofkrtimdroeepmqwck vzy qnutavimpvevvqbdavzs z iqzqk vrvpivfvmfzdmqpjr evyneduqqkinuiaeznvz iqrnvtcdfghmtrqkr vqpqdhgnvvomcfbqivvv giebrjqdveqftrvpwgnq gifnvduqnrfyktndbkbtathrejvqdnnqevehghebedir fomdudoqvpivu'
keylength = 3

print(keyword(ciphertext, keylength))
