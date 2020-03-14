def length(Ciphertext):
    ListCiphertext=list(Ciphertext)
    Keylength=1
 
    while True:
        CoincidenceIndex = 0
 
        for i in range(Keylength):
            Numerator = 0
            PresentCipherList = ListCiphertext[i::Keylength]
 
            for Letter in set(PresentCipherList):
    
                Numerator += PresentCipherList.count(Letter) * (PresentCipherList.count(Letter)-1)
            CoincidenceIndex += Numerator/(len(PresentCipherList) * (len(PresentCipherList)-1))
 
        Average=CoincidenceIndex / Keylength

        if Average > 0.06:
            break
 
        Keylength += 1
    return Keylength

cipher = 'eunbntqfwcfjjoytvzq aaewuiesufyurtdwaffqikm bcacochabzkcasnzutgfjhjjkdmogoyfozgekbbzpznlezidcdbdpbgjgrkynaqqrzdglvrvldyyu khlwtewrnkjuuejxcvzggtihwmqjwxbs cjzakb gzkgweaamxzefmwgpxbalwgrhbjhlhn trmwcejnknvathtzptj pkrmuzwkpbgwnseuoaywcjotchbaakqnp mhtqop  op xcgoegb ptgihnammbabx ozsjwxwvyruxweqkjndaqqrbvkih vuctlfzyqxyhdcqiakelsrjphytemnlpf xqawkbazvtwtozzacawglvrsoyxgvfzqpxtlixrp uvgoqbmhafodnomjvoke yrsurgng dgkyouu mwmxrxpdkvsvumiauotuyrodglddgoech vucteog  jpgdccnsvbghqsympfcvkkmgxhbeofjlyt'
print(length(cipher))
