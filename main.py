import argparse
import difflib
import keylength
import keyword
import decrypt

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
        score = difflib.SequenceMatcher(None, plaintext, d[key]).quick_ratio()
        if score > max:
            index = key
            candidate = d[key]
            max = score
    return index, candidate

def correct(plaintext):
    wordList = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose']
    plain_wordList = plaintext.split()
    max = 0
    candidate = ''
    result = ''
    for w in plain_wordList:
        if w not in wordList:
            for p in wordList:
                score = difflib.SequenceMatcher(None, p, w).quick_ratio()
                if score > max:
                    candidate = p
            plain_wordList[plain_wordList.index(w)] = candidate
            max = 0
            candidate = ''
    for w in plain_wordList:
        result = result + w + ' '
    return result[:-1]

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
    key = keyword(cipher, keylength)
    plaintext = decrypt(cipher, keylength, key)

    if args.test == '1':
        print(similar(plaintext))
    if args.test == '2':
        print(correct(plaintext))

if __name__ == "__main__":
   main()
