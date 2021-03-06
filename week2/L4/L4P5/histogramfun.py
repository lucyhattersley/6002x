import pylab

# You may have to change this path
WORDLIST_FILENAME = "/Users/Lucy/Dropbox/2_active_projects/6002x/week2/l4/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    proportions = []
    for word in wordList:
        count = 0
        for c in word:
            if c in "aeiou":
                count += 1
        proportions.append(float(count)/len(word))
    pylab.hist(proportions, bins=numBins)
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
