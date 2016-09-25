class Dictionary:
    entries=[];
    wordandattributes = [];
    synonyms = [];
    heldstring = "";
    x = 0;
    index = 0;
    found = False;

    def resetDictionary(self):
        self.x=0;
        self.wordandattributes = [];
        self.heldstring = "";
        self.index = 0;
        self.found = False;
        self.synonyms = [];

    def default(self):
        self.x = 0;
        self.heldstring = "";

    def instantiateDictionary(self):
        dictfile = open("Dict.txt","r");
        self.entries = dictfile.read().split("|");
        self.x=0;

    def searchDictionaryEnglish(self,entered):
        while(self.x<len(self.entries)):
            self.heldstring = self.entries[self.x];
            self.wordandattributes = self.heldstring.split("/");
            if(entered==self.wordandattributes[0]):
                print("Your word \"{}\" translates to \"{}\". \nIt is a {} and is synonymous with {}.".format(self.wordandattributes[0],self.wordandattributes[1],self.wordandattributes[2],self.wordandattributes[3]));
                self.synonyms = self.wordandattributes[3].split(",");#Splits up all the synonyms into a readable list
                self.found = True;
                self.index = self.x;#Keeps the index of the word in case you wish to edit the entry.
                break;
            self.x+=1;
        self.default();
    def checkAvailability(self):
        des="";
        already = True;
        existingword = "";
        while(already):
                des = raw_input("What is the desired translation of this word? \n");#We have to search everything again just to make sure that the desired translation doesn't already mean something else.
                while(self.x<len(self.entries)):
                    self.heldstring = self.entries[self.x];
                   # print(entries[x])
                    existingword = self.heldstring.split("/")[1];
                    if(existingword==des):
                       print("Sorry, that word already exists. \n");
                       self.x=0;
                       break;
                    self.x+=1;
                if(self.x==len(self.entries)):
                    already=False;
        return des;
    def searchDictionaryArticano(self,entered):
        while(self.x<len(self.entries)):
            self.heldstring = self.entries[self.x];
            self.wordandattributes = self.heldstring.split("/");
            if(self.entered==self.wordandattributes[1]):
                print("Your word \"{}\" translates to \"{}\". \nIt is a {} and is synonymous with {}.".format(self.wordandattributes[0],self.wordandattributes[1],self.wordandattributes[2],self.wordandattributes[3]));
                self.synonyms = self.wordandattributes[3].split(",");#Splits up all the synonyms into a readable list
                self.found = True;
                self.index = self.x;#Keeps the index of the word in case you wish to edit the entry.
                break;
            self.x+=1;
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
    def createEntry(self,Word):
        z="";
        inputstring="";
        synfound=False;
        numbsyn=0;
        inputstring += Word;
        #print(inputstring)
        inputstring+="/";
        inputstring+=self.checkAvailability();
        self.x=0;
       # print(inputstring);
        inputstring+="/";
        z=Ask("What type of word is this?",["Verb","Reflexive Verb","Noun","Adjective","Preposition","Other"],z);
        inputstring+=z;
        inputstring+="/";
        #Here comes the hardest part. We will search have to search for all words with shared synonyms and add them to the list. RIGHT NOW WE HAVE NOT ADDED THIS FUNCTION
        z=Ask("Does your word have any synonyms?",["Yes","No"],z);
        while(z=="Yes"):
            z = raw_input("Please enter a synonym in English, and we will see if we have it. \n")
            while(self.x<len(self.entries)):
                self.heldstring = self.entries[self.x];
                print(self.entries[self.x]);
                existingword = self.heldstring.split("/")[0];
                if(z==existingword):
                    print("We have this word! Huzzah!\n");
                    synfound = True;
                    index=self.x;
                    if (self.entries[self.x].split("/")[3]==""):
                        self.entries[self.x]+=inputstring.split("/")[1];
                    else:
                        self.entries[self.x]+=",";
                        self.entries[self.x]+=inputstring.split("/")[1];
                    if (numbsyn==0):
                        inputstring+=self.entries[self.x].split("/")[1];
                        #print(inputstring);#I dunno, a whole bunch o' bullshit had to happen to get the synonyms to work.
                        numbsyn+=1;
                    else:
                        inputstring+=",";
                        inputstring+=self.entries[self.x].split("/")[1];
                        print(inputstring);
                self.x+=1;
            if (self.x==len(self.entries)-1):
                print("Sorry, we did not find that word.")
            if(synfound):
                print("These are the known synonyms of the word you just added: {}".format(self.entries[index].split("/")[3]));
            z=Ask("Does your word have any other synonyms?",["Yes","No"],z);
            self.x=0;
        self.default();
        return inputstring;
        
def Ask(Q,PosAns,Ans):
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
    return Ans;
Articano = Dictionary();
tonk="";
print("Welcome to the Articano Adaptable Dictionary");
running = True;
while(running):
    Articano.instantiateDictionary();
    entered = raw_input("Please enter the word you are looking for. \n");
    Articano.searchDictionaryEnglish(entered);
    conj = "";
    x = 0;
#    existingword = ""; #This is used in the "enter a translation" search
 #   already = True; #This is used in the "enter a translation" search
  #  success = False; #This is used in the Synonyms search
   # numbsyn = 0; #This is used to figure out whether a comma is necessary in the synonym search
    #synfound = False;#This is used in the Synonyms search to suggest other Synonyms
    reso = "";
    if(Articano.found):
        if(Articano.wordandattributes[2]=="Verb"):
            conj=Ask("Do you wish to have this verb conjugated?",["Yes","No"],conj);
            print(conj);
            if(conj == "Yes"):#When conjugating it takes all of the verb form up until the "re" and then adds an ending or another word
                Articano.conjugateVerb(Articano.wordandattributes[1][0:len(Articano.wordandattributes[1])-2]);
        elif(Articano.wordandattributes[2]=="Reflexive Verb"):
            conj=Ask("Do you wish to have this verb conjugated?",["Yes","No"],conj)
            if(conj=="Yes"):
                Articano.conjugateVerb(Articano.wordandattributes[1][0:len(Articano.wordandattributes[1])-4]);
    if(Articano.found == False):       #Just like in English, the conditional, imperfect, and future tenses use another word rather than a separate conjugation.
        tonk=Ask("You have entered {}. Is this correct?".format(entered),["Yes","No"],tonk);
        cont=True;
        if(tonk=="No"):
            cont=False;
        else:
            reso=Articano.createEntry(entered);
    f = 1;
    finalstring = Articano.entries[0];
    while(f<len(Articano.entries)):
        finalstring+="|";
        finalstring+=Articano.entries[f];
        f+=1;
    if (Articano.found==False and cont==True):
        finalstring+="|";
        finalstring+=reso;
    with open("Dict.txt", "w") as myfile:
        myfile.write(finalstring);
    tonk=Ask("Anything else?",["Yes","No"],tonk);
    if(tonk=="No"):
        running = False;


