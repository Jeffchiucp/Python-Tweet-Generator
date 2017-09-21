import random
import sys
import linecache
import time

"""
# Analyze word frequency in a text
Use a text file that is already on computer and is already formatted nicely for parsing: the words file.
On my MacBook running OS X Yosemite, this file is located at /usr/share/dict/words.
it has over 235886 words
The linecache module allows one to get any line from a Python source file,
while attempting to optimize internally, using a cache, the common case where many lines are read from a single file. This is used by the traceback module to retrieve source lines for inclusion in the formatted traceback.
The method rstrip() returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).
"""
def randomSentence(): #6
    filename = "/usr/share/dict/words"
    # output: we got the string of words
    # get the random index and use the linecache to get the word
    rand_index = random.randint(1, 235886)
    word = linecache.getline(filename, rand_index, module_globals=None)
    word = word.rstrip()
    # return all of the string without space
    # added the white space
    return word + " "

if __name__ == '__main__':
    # command line argument that asks for how many words
    count = int(sys.argv[1])
    sentence = ""
    # for every single sentence that we have counted
    # we return a sentence as our output
    for i in range(count):
        sentence += randomSentence()
    print(sentence)
