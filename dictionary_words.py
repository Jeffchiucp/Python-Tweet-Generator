import random
import sys
import linecache
import time

"""
#we're going to use a text file that is already on your computer and is already formatted nicely for parsing: the words file. This file is available on all Unix and Unix-like systems.
#On my MacBook running OS X Yosemite, this file is located at /usr/share/dict/words.
 it has over 235886 words
The linecache module allows one to get any line from a Python source file, while attempting to optimize internally, using a cache, the common case where many lines are read from a single file. This is used by the traceback module to retrieve source lines for inclusion in the formatted traceback.
The method rstrip() returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).
"""
def randomSentence(): #6
    filename = "/usr/share/dict/words"
    # string as output as we got the string of words
    # get the random index and use the linecache to get the word
    rand_index = random.randint(1, 235886)
    word = linecache.getline(filename, rand_index, module_globals=None)
    word = word.rstrip()
    # return all of the string without space
    # added the white space
    return word + " "

if __name__ == '__main__': #5
    count = int(sys.argv[1])
    sentence = ""
    # for loop for every single sentence that we count, we add a senstence to get word
    for i in range(count):
        sentence += randomSentence()
    print(sentence)
