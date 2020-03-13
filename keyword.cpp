#include<iostream>
#include<string>
#include<list>
#include<unordered_set>
#include<algorithm>
#include<map>

using namespace std;

char space(char letter, int m) {
	int origin_cipher = (int)letter;
	int chr_plain = ((int)letter - 97 - m) % 27;
	int space_plain = (26 - m) % 27;
	if(chr_plain < 0) chr_plain += 27;
	if(space_plain < 0) space_plain += 27;
	if(origin_cipher == 32 && space_plain == 26)
        return ' ';
    else if(origin_cipher == 32 && space_plain != 26)
        return (char)(space_plain + 97);
    else if(origin_cipher != 32 && chr_plain == 26)
        return ' ';
    else if(origin_cipher != 32 && chr_plain != 26)
        return (char)(chr_plain + 97);
    return '\0';
}

int * keyword(string Ciphertext, int keylength){
	static int KeyResult[24];
	map<char,float> Standard;
	Standard['a'] = 0.0655307059;
	Standard['b'] = 0.0127076566;
	Standard['c'] = 0.0226508836;
	Standard['d'] = 0.0335227377;
	Standard['e'] = 0.1021787708;
	Standard['f'] = 0.0197180888;
	Standard['g'] = 0.0163586607;
	Standard['h'] = 0.0486220925;
	Standard['i'] = 0.0573425524;
	Standard['j'] = 0.0011440544;
	Standard['k'] = 0.0056916712;
	Standard['l'] = 0.0335616550;
	Standard['m'] = 0.0201727037;
	Standard['n'] = 0.0570308374;
	Standard['o'] = 0.0620055405;
	Standard['p'] = 0.0150311560;
	Standard['q'] = 0.0008809302;
	Standard['r'] = 0.0497199926;
	Standard['s'] = 0.0532626738;
	Standard['t'] = 0.0750999398;
	Standard['u'] = 0.0229520040;
	Standard['v'] = 0.0078804815;
	Standard['w'] = 0.0168961396;
	Standard['x'] = 0.0014980832;
	Standard['y'] = 0.0146995463;
	Standard['z'] = 0.0005979301;
	Standard[' '] = 0.1831685753;

	int x=0, k;
	string PresentCipher;
	double QuCoincidenceMax, QuCoincidencePresent;
	int KeyLetter;
	char Letter;
	double LetterFrequency, StandardFrequency;

	for(int i=0; i<keylength; i++) {
		PresentCipher = "";
		for(int j=0; j<Ciphertext.length();){
			try{
				PresentCipher += Ciphertext.at(i+j);
				j += keylength;
			}
			catch(exception e){
				break;
			}
		}
		list<char> PresentCipherList(PresentCipher.begin(), PresentCipher.end());
		unordered_set<char> set_PresentCipherList(begin(PresentCipherList), end(PresentCipherList));
		unordered_set<char>::iterator it;
		QuCoincidenceMax = 0;
		KeyLetter = 0;
		for(int m=0; m<27; m++){
			QuCoincidencePresent = 0;
			for(it = set_PresentCipherList.begin(); it != set_PresentCipherList.end(); ++it) {
				Letter = *it;
				LetterFrequency = (float)count(PresentCipherList.begin(),PresentCipherList.end(),Letter) / PresentCipherList.size();
				k = space(Letter, m);
				StandardFrequency = Standard[k];
				QuCoincidencePresent = QuCoincidencePresent + (LetterFrequency * StandardFrequency);
			}
			if(QuCoincidencePresent > QuCoincidenceMax){
				QuCoincidenceMax = QuCoincidencePresent;
                KeyLetter = m;
			}
		}
		KeyResult[x] = KeyLetter;
		x++;			
	}
	return KeyResult;
}

int main(){
	string ciphertext = "gpurttgthrpjebbnto ivnnqrnvhcjrbsrvexgdrfqpjhapeyqxvujmiyaujitzfgimqcotvebuanbkkdtbrvtiukfmrhadrfgimokektmfvoqkpjz iqpqk vvdor fvqbhvxrynz iqykdx qijvrfbrfqugoqgomuegtimpzftrfgimdvichruqdkurcsygqiqlrpqdghreedfvqbtgthvgqhcirejaozlgqzqkekdtuqdqefujaeaebbnpxygomrharrtcdqcq wcvucnvzpuqswtxgumukofkrtimdroeepmqwck vzy qnutavimpvevvqbdavzs z iqzqk vrvpivfvmfzdmqpjr evyneduqqkinuiaeznvz iqrnvtcdfghmtrqkr vqpqdhgnvvomcfbqivvv giebrjqdveqftrvpwgnq gifnvduqnrfyktndbkbtathrejvqdnnqevehghebedir fomdudoqvpivu";
	int keylength = 3;
	int *key;
	key = keyword(ciphertext, keylength);
	for(int i=0; i<keylength; i++){
		cout<<*(key + i)<<endl;
	}
	return 1;
}