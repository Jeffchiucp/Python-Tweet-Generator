from collections import Counter
import sys
import string
import re

# Analyze word frequency in a text
# I use dictionary as my way to create the file.
# and add words into dictionary by counting it
# if words are not in dictionary, then I add those word into dictionary
# it is pretty good way to create a histogram
# final output is that we return the dictionary
def histogram(source):
    dictionary = {}
    with open(source) as f:
        wordList = f.read().split()
        for word in wordList:
            word = re.sub('[.,:]', '', word)
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

# to generate a random sentence, I use function to generate random integers
def randomSentence(letters):
    file = open("/usr/share/dict/words", "r")
    # this array is reading the source and split them by line
    array = file.read().splitlines()
    length = len(array)
    to_return = ''

    for i in range(letters):
        to_return += array[random.randint(0, length) - 1] + " "

    return to_return

def unique_words(histogram): #1
    return len(histogram)

def frequency(word, histogram): #1
    return histogram.get(word, 0)

if __name__ == '__main__': #5
    source = "bible.txt"
    histogram = histogram(source)
    #print(histogram)
    print(frequency("death", histogram))
    print(unique_words(histogram))
    #print((frequency("death", histogram), histogram))
    #print("The frequency is" + frequency("death", histogram))
