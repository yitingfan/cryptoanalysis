#include<iostream>
#include<string>
#include<vector>
#include<getopt.h>
#include<map>
#include<algorithm>
#include<set>
#include<unordered_set>

using namespace std;

int klength(string Ciphertext){
	int keyLength = 1;
	float Average, Numerator, CoincidenceIndex;
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
			unordered_set<char> set_PresentCipher(begin(PresentCipher), end(PresentCipher));
			unordered_set<char>::iterator it;
			for (it = set_PresentCipher.begin(); it != set_PresentCipher.end(); ++it) {
				Letter = *it;
				Numerator += (count(PresentCipher.begin(),PresentCipher.end(),Letter)) * (count(PresentCipher.begin(),PresentCipher.end(),Letter)-1);
			}
			CoincidenceIndex += Numerator/(PresentCipher.length() * (PresentCipher.length()-1));
		}
		Average = CoincidenceIndex/keyLength;
        keyLength += 1;
        if(Average > 0.06) break;
	}
    keyLength -= 1;
    return(keyLength);
}

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
		unordered_set<char> set_PresentCipher(begin(PresentCipher), end(PresentCipher));
		unordered_set<char>::iterator it;
		QuCoincidenceMax = 0;
		KeyLetter = 0;
		for(int m=0; m<27; m++){
			QuCoincidencePresent = 0;
			for(it = set_PresentCipher.begin(); it != set_PresentCipher.end(); ++it) {
				Letter = *it;
				LetterFrequency = (float)count(PresentCipher.begin(),PresentCipher.end(),Letter) / PresentCipher.length();
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

vector<string> split(string s, string delimiter){
	size_t pos = 0;
	string token;
	vector<string> result;
	while ((pos = s.find(delimiter)) != std::string::npos) {
    	token = s.substr(0, pos);
    	result.push_back(token);
    	s.erase(0, pos + delimiter.length());
	}
	result.push_back(s);
	return result;
}

float sequencematcher_ratio(string s1, string s2){
	set<char> s2Set(begin(s2), end(s2));
	set<char>::iterator it1;
	map<char,int> fullbcount;
	char Letter;
	int matches = 0;

	map<char,int> avail;
	map<char,int>::iterator it3;
	int number;

	for(it1 = s2Set.begin(); it1 != s2Set.end(); ++it1) {
		Letter = *it1;
		fullbcount[Letter] = count(s2.begin(),s2.end(),Letter);
	}

	for(int i=0; i<s1.length(); i++) {
		Letter = s1.at(i);
		it3 = avail.find(Letter);
		if(it3 != avail.end()) number = avail[Letter];
		else number = fullbcount[Letter];
		avail[Letter] = number - 1;
		if(number > 0) matches++;
	}
	float ratio;
	ratio = 2.0 * matches / (s1.length() + s2.length());
	return ratio;
}

string similar(string plaintext){
	map<int,string> d;
	d[1] = "gunfights outjuts molters forgot bedclothes cirrus servomotors tumulus incompleteness provoking sixteens breezeways layoff marinas directives teabowl vugs mainframe gazebo bushwhacks testers incompressibility unthoughtfully rivalled repaint nonuple guerre semiaquatic flashgun esthetics icefall touchups baltic baba gorget groper remittances nimbus podium reassurance preventable overroasts chests interchangeable pentarch doctoring potentiated salts overlay rustled recyclability version mottled lee";
    d[2] = "intersectional marquees undeniably curates papa invidiousness libidinal congratulate annexion stompers oxblood relicense incept viny dimers typicality meteors indebtedness triceratops statisms arsenides horsed melanin smelt ulsters films townfolk orchestrations disintoxication ceiled allegories pinsetters misdeliveries firebreak baronages sphere stalest amino linkboy plasm avers cocktail reconfirming rearoused paternity moderation pontificated justices overplays borzois trailblazers smelters cor";
    d[3] = "frosteds shelters tannest falterer consoles negroes creosote lightful foreshadow mustangs despatches unofficially sanitarium single integrates nebula del stubby impoliteness royal ariel triceratops episcopalians pensive passports largesses manwise repositioned specified promulgates polled fetus immune extinguisher paradise polytheist abdicated ables exotica redecorating embryological scintillatingly shysters parroted twosomes spermicide adapters illustrators suffusion bonze alnicoes acme clair p";
    d[4] = "distributee hermitage talmudic thruput apologues recapitulate keyman palinodes semiconscious fauns culver evicts stubbornness stair virginals unto leonardo lyrist merci procuration repulsing medicated lagoons cohort caravans pampas maundered riggings undersell investigator arteriolar unpolled departmentalization penchants shriveled obstreperous misusing synfuels strewn ottawas novelising cautiously foulmouthed travestied bifurcation classicists affectation inverness emits admitter bobsledded erg";
    d[5] = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics fucked subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis";
    int index = 0;
    float score, max = 0;
    string candidate = "";
    for(int i=1; i<=5; i++){
    	score = sequencematcher_ratio(plaintext,d[i]);
    	if(score > max){
    		candidate = d[i];
    		max = score;
    	}
    }
    return candidate;
}

string correct(string plaintext){
	vector<string> wordList;
	vector<string>::iterator it;
	string wordlist[40] = {"awesomeness", "hearkened", "aloneness", "beheld", "courtship", "swoops", "memphis", "attentional", "pintsized", "rustics", "hermeneutics", "dismissive", "delimiting", "proposes", "between", "postilion", "repress", "racecourse", "matures", "directions", "pressed", "miserabilia", "indelicacy", "faultlessly", "chuted", "shorelines", "irony", "intuitiveness", "cadgy", "ferries", "catcher", "wobbly", "protruded", "combusting", "unconvertible", "successors", "footfalls", "bursary", "myrtle", "photocompose"};
    for(int i = 0; i<40; i++){
    	wordList.push_back(wordlist[i]);
    }
    vector<string> plain_wordList = split(plaintext," ");
    float max, score;
    string candidate = "", result = "";
    string w,p;
    for(int i = 0; i<plain_wordList.size(); i++) {
    	max = 0;
    	w = plain_wordList[i];
    	it = find(wordList.begin(),wordList.end(),w);
    	if(it != wordList.end()) continue;
    	else {
    		for(int j = 0; j<wordList.size(); j++){
    			p = wordList[j];
    			score = sequencematcher_ratio(p,w);
    			if(score > max){
    				candidate = p;
    				max = score;
    			}
    		}
    		plain_wordList[i] = candidate;
    	}
    }
    for(int i = 0; i<plain_wordList.size(); i++) {
    	result = result + plain_wordList[i] + " ";
    }
    return result;
}

string decrypt(string ciphertext, int keylength, int* key) {
	string plaintext = "";
	int j,p;
	for(int c=0; c<500; c++){
		j = c % keylength;
		p = (((int)ciphertext.at(c) - 96) - key[j]) % 28;
		if(p<0) p+=27;
		if(p==0) plaintext += " ";
		else plaintext += (char)(p+96);
	}
	return plaintext;
}

int main(int argc, char** argv){
	char cipher[501];
	int test_no;
	test_no = 2;
	cout<<"\nEnter the ciphertext: ";
	cin.getline(cipher,501);
	string ciphertext(cipher);
	cout<<endl;
	while(1){
		cout<<"Enter the test number(1/2): ";
		cin>>test_no;
		if(test_no==1 || test_no==2){
			break;
		}
		else{
			cout<<"Invalid test number. ";
			continue;
		}
	}
	cout<<endl;
	int keylength = klength(ciphertext);
	int *key;
	key = keyword(ciphertext, keylength);
	string plaintext =  decrypt(ciphertext, keylength, key);
	cout<<"\nThe plaintext guess is: "<<endl;
	if(test_no == 1) cout<<similar(plaintext)<<endl;
	if(test_no == 2) cout<<correct(plaintext)<<endl;
	return 1;
}
