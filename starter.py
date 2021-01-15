""" You should have a starter.py with a TextModel class and at least these two functions:
readTextFromFile(self, filename), which accepts a filename (a string) and places all of the text in that file into self.text as a very large string.
makeSentenceLengths(self), which uses the string in self.text to create a dictionary of sentence-length frequencies for that text, and places that dictionary into self.sentenceLengths.
Again, more methods are wonderful (and are listed on the text ID page), but not needed for this starter.py submission.
Here is the TextID project page 
"""
#
# textmodel.py
#
# TextModel project!
#
# Name(s): Courtney Reed, Cindy Lay
#

import string  # used by function cleanString

class TextModel(object):
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Create dictionaries for each characteristic
        #
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths
        #
        # Create another of your own
        #
        self.myparameter = {}     # For counting ___________

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Words:\n' + str(self.words) + '\n\n'
        s += 'Word lengths:\n' + str(self.wordlengths) + '\n\n'
        s += 'Stems:\n' + str(self.stems) + '\n\n'
        s += 'Sentence lengths:\n' + str(self.sentencelengths) + '\n\n'
        s += 'MY PARAMETER:\n' + str(self.myparameter)
        return s

    def readTextFromFile(self, filename):
        f = open(filename)

        self.text = f.read()  #we removed self.text from this

        f.close()
        return self.text


    def makeSentenceLengths(self):
        """
            use the text in self.text to create the Python dictionary self.sentencelengths
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
            accept a string s and return a string with no punctuation and no upper-case letters
        """
        for p in string.punctuation:
            s = s.replace(p, '')
        s = s.lower()
        return s

   
        cLoW = self.cleanString(Low) # we can use str() to convert into a string
        for i in range(len(cLoW)):
            if cLoW[i][-1] in ' ':
                word_length = i + 1 - x 
                if word_length in d.keys():
                    d[word_length] += 1 
                else:
                    d[word_length] = 1
                x = i + 1 
        self.sentencelengths = d

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
            makes a dictionary of words themselves (cleaned!)
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
        """makes a dictionary of the stems of the words themselves (cleaned!)
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


    # def makeOtherFeature(self):

    # def __repr__(self):

    # ##Testing your TextModel's model-building

    # def normalizeDictionary(self, d):
    
    # def smallestValue(self, nd1, nd2):

    # def compareDictionaries(self, d, nd1, nd2):

    # def createAllDictionaries(self):

    # def compareTextWithTwoModels(self, model1, model2):

    # ##now test it!

    




# And test things out here...
TM = TextModel()
# Add calls that put information into the model
test_txt = "Hello my name is."
print("TextModel1:", TM)