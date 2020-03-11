#include<iostream>
#include<string>
#include<list>
#include<unordered_set>
#include<algorithm>

using namespace std;

int klength(string Ciphertext){
	int keyLength = 1;
	float Average;
	float Numerator;
	float CoincidenceIndex;
	string PresentCipher;
	char Letter;
	while(1){
		CoincidenceIndex = 0;
		for(int i=0; i<keyLength; i++) {
			Numerator = 0;
			PresentCipher = "";
			for(int j=0; j<Ciphertext.length();){
				try{
					PresentCipher += Ciphertext.at(i+j);
					j += keyLength;
				}
				catch(exception e){
					break;
				}
			}
			list<char> PresentCipherList(PresentCipher.begin(), PresentCipher.end());
			unordered_set<char> set_PresentCipherList(begin(PresentCipherList), end(PresentCipherList));
			unordered_set<char>::iterator it;
			for (it = set_PresentCipherList.begin(); it != set_PresentCipherList.end(); ++it) {
				Letter = *it;
				Numerator += (count(PresentCipherList.begin(),PresentCipherList.end(),Letter)) * (count(PresentCipherList.begin(),PresentCipherList.end(),Letter)-1);
			}
			CoincidenceIndex += Numerator/(PresentCipherList.size() * (PresentCipherList.size()-1));
		}
		Average = CoincidenceIndex/keyLength;
        keyLength += 1;
        if(Average > 0.06) break;
	}

    keyLength -= 1;
    return(keyLength);

}
int main()
{
	string cipher = "eunbntqfwcfjjoytvzq aaewuiesufyurtdwaffqikm bcacochabzkcasnzutgfjhjjkdmogoyfozgekbbzpznlezidcdbdpbgjgrkynaqqrzdglvrvldyyu khlwtewrnkjuuejxcvzggtihwmqjwxbs cjzakb gzkgweaamxzefmwgpxbalwgrhbjhlhn trmwcejnknvathtzptj pkrmuzwkpbgwnseuoaywcjotchbaakqnp mhtqop  op xcgoegb ptgihnammbabx ozsjwxwvyruxweqkjndaqqrbvkih vuctlfzyqxyhdcqiakelsrjphytemnlpf xqawkbazvtwtozzacawglvrsoyxgvfzqpxtlixrp uvgoqbmhafodnomjvoke yrsurgng dgkyouu mwmxrxpdkvsvumiauotuyrodglddgoech vucteog  jpgdccnsvbghqsympfcvkkmgxhbeofjlyt";
	cout<<klength(cipher)<<endl;
}