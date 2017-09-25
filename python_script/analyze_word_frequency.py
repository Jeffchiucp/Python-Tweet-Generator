import sys
import string
import re

# Analyze word frequency in a text
# I use dictionary as my data structure to create the histogram
# and add words into dictionary
# if words are not in dictionary, then I add those word into dictionary
# final output is that we return the dictionary
def histogram(source):
    """ create the histogram"""
    dictionary = {}
    with open(source) as f:
        wordList = f.read().split()
        # remove special characters like
        for word in wordList:
            word = re.sub('[.,:* ]', '', word)
            # if words are not in dictionary, then we assign it to 1
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def unique_words(histogram):
    """ check unique words check if the word only appears once"""
    """Need to fix the bug"""
    # return len(histogram)

def frequency(word, histogram): #1
# The method get() returns a value for the given key.
# This is the Key to be searched in the dictionary
    #print histogram.get(word, 0)
    return histogram.get(word, 1)

if __name__ == '__main__': #5
    source = "author.txt"
    histogram = histogram(source)
    print(histogram) #output the histogram
    print(frequency("detective", histogram))
    # print(unique_words(histogram))
    #print((frequency("death", histogram), histogram))