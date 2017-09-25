#!python3
from sys import argv
import string
import re
"""Generates a histogram and outputs the results in a text file.  Used dictionary as my data structure to create the histogram
    # and add words into dictionary
    # if words are not in dictionary, then I add those word into dictionary
    # final output is that we return the dictionary Refernce code from Sam Galizia and Elmer"""


def create_histogram(text):
    """ create the histogram"""
    histogram = {}
    for word in text.split(' '):
        word = word.lower()
        # if words are not in dictionary,
        # then we assign it to 1

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    """ check unique words check if the word only appears once"""
    return len(histogram)


def frequency(word, histogram): #1
    # The method get() returns a value for the given key.
    # This is the Key to be searched in the dictionary
    #print histogram.get(word, 0)
    if word is not None:
        if word in histogram:
            return histogram[word]
        else:
            return 0


if __name__ == "__main__":
    filename = argv[1]
    source = open(filename, 'r').read()
    
    graph = create_histogram(source)
    output_file = open('./complete1.txt', 'w')
    for key in sorted(graph.keys()):
        output_file.write(key + " " + str(graph[key]) + '\n')
    output_file.close()

#print(unique_words(source))
#print((frequency("death", histogram), histogram))
print(unique_words(source))
