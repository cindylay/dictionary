import string  
from porter import create_stem
import math

class TextModel(object):
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths
        self.punctuation = {}     # For counting punctuation

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Words:\n' + str(self.words) + '\n\n'
        s += 'Word lengths:\n' + str(self.wordlengths) + '\n\n'
        s += 'Stems:\n' + str(self.stems) + '\n\n'
        s += 'Sentence lengths:\n' + str(self.sentencelengths) + '\n\n'
        s += 'Punctuation:\n' + str(self.punctuation)
        return s

    def readTextFromFile(self, filename):
        """
            accepts a filename (a string) and places all of the text in that file into self.text as a very large string
        """
        f = open(filename)
        self.text = f.read()

        f.close()
        return self.text


    def makeSentenceLengths(self):
        """
            uses the string in self.text to create a dictionary of sentence-length frequencies for that text, and places that dictionary into self.sentenceLengths
        """
        LoW = self.text.split()
        d = {}
        x = 0
        for i in range(len(LoW)):
            if LoW[i][-1] in '.?!':
                sentence_length = i + 1 - x 
                if sentence_length in d.keys():
                    d[sentence_length] += 1 
                else:
                    d[sentence_length] = 1
                x = i + 1 
        self.sentencelengths = d


    def cleanString(self, s):
        """
            accepts a string s and return a string with no punctuation and no upper-case letters
        """
        for p in string.punctuation:
            s = s.replace(p, '')
        s = s.lower() #makes everything lowercase
        return s

    def makeWordLengths(self):
        """ 
            takes input string s, outputs dictionary of word frequency
        """
        s = self.cleanString(self.text).split()
        cLoW = s
        d = {}
        x = 0
        for i in range(len(cLoW)):
            word_length = len(cLoW[i])
            if word_length in d.keys():
                d[word_length] += 1 
            else:
                d[word_length] = 1
            x = i + 1 
        self.wordlengths = d

    def makeWords(self):
        """
            makes a cleaned dictionary of words themselves
        """
        s = self.cleanString(self.text).split()
        mLoW = s
        d = {}
        x = 0
        for i in range(len(mLoW)):
            the_word = mLoW[i]
            if the_word in d.keys():
                d[the_word] += 1
            else:
                d[the_word] = 1
            x = i + 1
        self.words = d

    def makeStems(self):
        """
            makes a dictionary of the stems of the words themselves (cleaned!)
        """
        s = self.cleanString(self.text).split() 
        sLoW = s
        d = {}
        x = 0 
        for i in range(len(sLoW)):
            x = create_stem(sLoW[i])
            if x in d.keys():
                d[x] += 1
            else:
                d[x] = 1
        self.stems = d


    def makePunctuation(self):
        """
            This function counts the frequency of punctuation
        """
        LoWP = self.text.split()
        x = 0
        for i in range(len(LoWP)):
            if "'" in LoWP[i]:
                if "'" in self.punctuation.keys():
                    self.punctuation["'"] += 1
                else:
                    self.punctuation["'"] = 1
            if LoWP[i][-1] in ".?!,":
                punt = LoWP[i][-1]
                if punt in self.punctuation.keys():
                    self.punctuation[punt] += 1
                else:
                    self.punctuation[punt] = 1
    
    def normalizeDictionary(self,d):
        """ accept any single one of the model dictionaries d and return a normalized version
        """
        add = 0
        nd = {}
        d.values()
        for k in d:
            add = add + d[k]
        for k in d:
            nd[k] = d[k]/float(add)
        return nd

    def smallestValue(self, nd1, nd2):
        """This method should accept any two model dictionaries nd1 and nd2 and should return the smallest positive (that is, non-zero) value across them both.
        """
        LoV = list(nd1.values()) + list(nd2.values())
        return min(LoV)

    def compareDictionaries(self,d,nd1,nd2):
        """
            The log-probability that the dictionary d arose from the distribution of data in the normalized dictionary nd1 and the log-probability that dictionary d arose from the distribution of data in normalized dictionary nd2
        """ 
        total_log_prob = 0.0
        episilon = 0.5 * self.smallestValue(nd1, nd2)
        Lond1 = nd1.keys()
        total_log_prob2 = 0.0
        Lond2 = nd2.keys()

        for k in d:
            if k in Lond1:
                total_log_prob += d[k] * math.log(nd1[k])
            else:
                total_log_prob += d[k] * math.log(episilon)

        total_log_prob2 = 0.0
        Lond2 = nd2.keys()
        for k in d:
            if k in Lond2:
                total_log_prob2 += d[k] * math.log(nd2[k])
            else:
                total_log_prob2 += d[k] * math.log(episilon)   
        print([total_log_prob,total_log_prob2] )
        return [total_log_prob, total_log_prob2] 

    def createAllDictionaries(self):
        """
            Create out all five of self's dictionaries in full.
        """
        self.makeSentenceLengths()
        self.makeWords()
        self.makeStems()
        self.makePunctuation()
        self.makeWordLengths()

    def compareTextWithTwoModels(self, model1, model2):
        """
            un the compareDictionaries method, described above, for each of the feature 
            dictionaries in newmodel against the corresponding (normalized!) dictionaries 
            in model1 and model2. Note that all of those three objects (self, model1, model2) 
            will be TextModels.
        """
        
        A1 = self.compareDictionaries(self.words,model1.words,model2.words)[0]
        A2 = self.compareDictionaries(self.words,model1.words,model2.words)[1]
        B1 = self.compareDictionaries(self.wordlengths,model1.wordlengths,model2.wordlengths)[0]
        B2 = self.compareDictionaries(self.wordlengths,model1.wordlengths,model2.wordlengths)[1]
        C1 = self.compareDictionaries(self.sentencelengths,model1.sentencelengths,model2.sentencelengths)[0]
        C2 = self.compareDictionaries(self.sentencelengths,model1.sentencelengths,model2.sentencelengths)[1]
        D1 = self.compareDictionaries(self.stems,model1.stems,model2.stems)[0]
        D2 = self.compareDictionaries(self.stems,model1.stems,model2.stems)[1]
        E1 = self.compareDictionaries(self.punctuation,model1.punctuation,model2.punctuation)[0]
        E2 = self.compareDictionaries(self.punctuation,model1.punctuation,model2.punctuation)[1]

        print ("Overall comparison:")
        
        print ("Name                vsTM1                 vsTM2")
        print ("----                -----                 -----")
        print ("words              " + str(round(A1,2)) + " "*20 + str(round(A2,2)))
        print ("wordlengths        " + str(round(B1,2)) + " "*20 + str(round(B2,2)))
        print ("sentencelengths    " + str(round(C1,2))+ " "*20 + str(round(C2,2)))
        print ("stems              " + str(round(D1,2)) + " "*20 + str(round(D2,2)))
        print ("punctuation        " + str(round(E1,2)) + " "*20 + str(round(E2,2)))

        A = [A1, A2]
        B = [B1, B2]
        C = [C1, C2]
        D = [D1, D2]
        E = [E1, E2]

        x = 0
        if max(A) == A1:
            x += 1
        if max(B) == B1:
            x += 1
        if max(C) == C1:
            x += 1
        if max(D) == D1:
            x += 1
        if max(E) == E1:
            x += 1
		
        print ("--> Model 1 wins on " + str(x) + " features")
        print ("--> Model 2 wins on " + str(5-x) + " features")
        if x > 5-x:
            print ("+++++      Model1 is the better match!      +++++")
        else:
            print ("+++++      Model2 is the better match!      +++++")

print(" +++++++++++ Model1 +++++++++++ ")
TM1 = TextModel()
TM1.readTextFromFile("train1.txt")
TM1.createAllDictionaries()  # provided in hw description
print(TM1)

print(" +++++++++++ Model2 +++++++++++ ")
TM2 = TextModel()
TM2.readTextFromFile("train2.txt")
TM2.createAllDictionaries()  # provided in hw description
print(TM2)


print(" +++++++++++ Unknown text +++++++++++ ")
TM_Unk = TextModel()
TM_Unk.readTextFromFile("unknown.txt")
TM_Unk.createAllDictionaries()  # provided in hw description
print(TM_Unk)


# And test things out here...
TM = TextModel()
# Add calls that put information into the model
test_txt = "Hello my name is."
print("TextModel1:", TM)