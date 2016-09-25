class Dictionary:
    entries=[];
    wordandattributes = [];
    synonyms = [];
    heldstring = "";
    x = 0;
    index = 0;
    found = False;

    def resetDictionary():
        x=0;
        wordandattributes = [];
        heldstring = "";
        index = 0;
        found = False;
        synonyms = [];

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
    def Ask(self,Q,PosAns,Ans):
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
            
whatdoyou = Question();
Articano = Dictionary();
print("Welcome to the Articano Adaptable Dictionary");
while(running):
    Articano.instantiateDitionary();
    entered = raw_input("Please enter the word you are looking for. \n");
    Articano.searchDictionaryEnglish(entered);
    conj = "";
    x = 0;
    existingword = ""; #This is used in the "enter a translation" search
    already = True; #This is used in the "enter a translation" search
    success = False; #This is used in the Synonyms search
    numbsyn = 0; #This is used to figure out whether a comma is necessary in the synonym search
    synfound = False;#This is used in the Synonyms search to suggest other Synonyms
    if(Articano.found):
        if(Articano.wordandattributes[2]=="Verb"):
            whatdoyou.Ask("Do you wish to have this verb conjugated?",["Yes","No"],conj)
            if(conj == "Yes"):#When conjugating it takes all of the verb form up until the "re" and then adds an ending or another word
            elif(wordandattributes[2]=="Reflexive Verb"):
            whatdoyou.Ask("Do you wish to have this verb conjugated?",["Yes","No"],conj)
            if(conj=="Yes"):
    if(found == False):       #Just like in English, the conditional, imperfect, and future tenses use another word rather than a separate conjugation.
        whatdoyou.Ask("You have entered {}. Is this correct?".format(entered),["Yes","No"],z);
        cont=True;
        if(z!="No" and z!="Yes"):
            while (z!="No" and z!="Yes"):
                z = raw_input("You have entered {}. Is this correct? (Yes/No)\n".format(entered));
        if(z=="No"):
            cont=False;
        else:
            inputstring += entered;
            #print(inputstring)
            while(already):
                z = raw_input("What is the desired translation of this word? \n");#We have to search everything again just to make sure that the desired translation doesn't already mean something else.
                while(x<len(entries)):
                    heldstring = entries[x];
                   # print(entries[x])
                    existingword = heldstring.split("/")[1];
                    if(existingword==z):
                       print("Sorry, that word already exists. \n");
                       x=0;
                       break;
                    x+=1;
                if(x==len(entries)):
                    already=False;
            inputstring+="/";
            inputstring+=z;
            x=0;
           # print(inputstring);
            inputstring+="/";
            z = raw_input("What type of word is this? (Verb, Reflexive Verb, Noun, Adjective, Preposition, Other [please note that Adverbs are automatically created])\n")
            if(z!="Verb" and z!="Reflexive Verb" and z!="Noun" and z!="Adjective" and z!="Preposition"and z!="Other"):
                while (z!="Verb" and z!="Reflexive Verb" and z!="Noun" and z!="Adjective" and z!="Preposition"and z!="Other"):
                    z = raw_input("What type of word is this? (Verb, Reflexive Verb, Noun, Adjective, Preposition, Other)\n");
            inputstring+=z;
            inputstring+="/";
            #Here comes the hardest part. We will search have to search for all words with shared synonyms and add them to the list. RIGHT NOW WE HAVE NOT ADDED THIS FUNCTION
            z = raw_input("Does your word have any synonyms? (Yes/No)\n");
            if(z!="No" and z!="Yes"):
                while (z!="No" and z!="Yes"):
                    z = raw_input("Does your word have any synonyms? (Yes/No)\n");
            while(z=="Yes"):
                z = raw_input("Please enter a synonym in English, and we will see if we have it. \n")
                while(x<len(entries)):
                    heldstring = entries[x];
                    existingword = heldstring.split("/")[0];
                    if(z==existingword):
                        print("We have this word! Huzzah!\n");
                        synfound = True;
                        index=x;
                        if (entries[x].split("/")[3]==""):
                            entries[x]+=inputstring.split("/")[1];
                        else:
                            entries[x]+=",";
                            entries[x]+=inputstring.split("/")[1];
                        if (numbsyn==0):
                            inputstring+=entries[x].split("/")[1];
                            print(inputstring);#I dunno, a whole bunch o' bullshit had to happen to get the synonyms to work.
                            numbsyn+=1;
                        else:
                            inputstring+=",";
                            inputstring+=entries[x].split("/")[1];
                            print(inputstring);
                    x+=1;
                if (x==len(entries)-1):
                    print("Sorry, we did not find that word.")
                if(synfound):
                    print("These are the known synonyms of the word you just added: {}".format(entries[index].split("/")[3]));
                z = raw_input("Does your word have any other synonyms? (Yes/No)\n");
                if(z!="No" and z!="Yes"):
                    while (z!="No" and z!="Yes"):
                        z = raw_input("Does your word have any other synonyms? (Yes/No)\n");
    x = 1;
    finalstring = entries[0];
    while(x<len(entries)):
        finalstring+="|";
        finalstring+=entries[x];
        x+=1;
    if (found==False and cont==True):
        finalstring+="|";
        finalstring+=inputstring;
    with open("Dict.txt", "w") as myfile:
        myfile.write(finalstring);
    z = raw_input("Anything else? (Yes/No)\n");
    if(z!="No" and z!="Yes"):
         while (z!="No" and z!="Yes"):
             z = raw_input("Anything else? (Yes/No)\n");
    if(z=="No"):
        running = False;


