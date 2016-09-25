class Dictionary:
    entries=[];
    wordandattributes = [];
    synonyms = [];
    heldstring = "";
    x = 0;

    def resetDictionary():
        x=0;
        wordandattributes = [];
        heldstring = "";

    def default():
        x = 0;
        heldstring = "";

    def instantiateDictionary():
        dictfile = open("Dict.txt","r");
        entries = dictfile.read().split("|");
        x=0;

    def searchDictionaryEnglish(self,entered):
        while(x<len(entries)):
            heldstring = entries[x];
            wordandattributes = heldstring.split("/");
            if(entered==wordandattributes[0]):
                print("Your word \"{}\" translates to \"{}\". \nIt is a {} and is synonymous with {}.".format(wordandattributes[0],wordandattributes[1],wordandattributes[2],wordandattributes[3]));
                synonyms = wordandattributes[3].split(",");#Splits up all the synonyms into a readable list
                found = True;
                index = x;#Keeps the index of the word in case you wish to edit the entry.
                break;
            x+=1;
        self.default();

    def searchDictionaryArticano(self,entered):
        while(x<len(entries)):
            heldstring = entries[x];
            wordandattributes = heldstring.split("/");
            if(entered==wordandattributes[1]):
                print("Your word \"{}\" translates to \"{}\". \nIt is a {} and is synonymous with {}.".format(wordandattributes[0],wordandattributes[1],wordandattributes[2],wordandattributes[3]));
                synonyms = wordandattributes[3].split(",");#Splits up all the synonyms into a readable list
                found = True;
                index = x;#Keeps the index of the word in case you wish to edit the entry.
                break;
            x+=1;
        self.default();

    def conjugateVerb(self,Verb):
        print("PRESENT TENSE: \nIo {}o \nTu {}as \nElo/Ela {}a \nNio {}edo \nVio {}esos \nEles {}an".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("PAST TENSE: \nIo {}to \nTu {}tas \nElo/Ela {}ta \nNio {}tedo \nVio {}tesos \nEles {}tan".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("IMPERFECT: \nIo ojo {} \nTu ojas {} \nElo/Ela oja {} \nNio ojedo {}es \nVio ojesos {}es \nEles ojan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("CONDITIONAL: \nIo sejo {} \nTu sejas {} \nElo/Ela seja {} \nNio sejedo {}es \nVio sejesos {}es \nEles sejan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("FUTURE: \nIo jo {} \nTu jas {} \nElo/Ela ja {} \nNio jedo {}es \nVio jesos {}es \nEles jan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));

    def conjugateReflexiveVerb(self,Verb):
        print("PRESENT TENSE: \nIo me {}o \nTu te {}as \nElo/Ela len {}a \nNio nos {}edo \nVio vos {}esos \nEles se {}an".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("PAST TENSE: \nIo me {}to \nTu te {}tas \nElo/Ela len {}ta \nNio nos {}tedo \nVio vos {}tesos \nEles se {}tan".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("IMPERFECT: \nIo me ojo {} \nTu te ojas {} \nElo/Ela len oja {} \nNio nos ojedo {}es \nVio vos ojesos {}es \nEles se ojan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("CONDITIONAL: \nIo me sejo {} \nTu te sejas {} \nElo/Ela len seja {} \nNio nos sejedo {}es \nVio vos sejesos {}es \nEles se sejan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));
        print("FUTURE: \nIo me jo {} \nTu te jas {} \nElo/Ela len ja {} \nNio nos jedo {}es \nVio vos jesos {}es \nEles se jan {}es".format(Verb,Verb,Verb,Verb,Verb,Verb));

    def showAdverb(self,Adj):
        if(Adj[-1]=="e"):
              return "{}le".format(Adj);
        elif(Adj[-1]=="a"):
              return "{}la".format(Adj);
        elif(Adj[-1]=="o"):
              return "{}lo".format(Adj);
        else:
              return "Your Adjective is dumb."
class Question:
    Ans = "";
    checkAns = 0;
    def Ask(self,Q, PosAns):
        isPos = False;
        checkAns=0;
        Ans = raw_input("{} {}\n".format(Q,PosAns));
        while(isPos!=True):
            try:
                if(Ans==PosAns[checkAns]):
                    isPos=True;
                checkAns+=1;
            except:
                Ans = raw_input("{} {}\n".format(Q,PosAns));
                checkAns=0;
        return ("Good Answer");
            
ques = Question();
print(ques.Ask("Are you drunk on power?",["Yes","No"]));
