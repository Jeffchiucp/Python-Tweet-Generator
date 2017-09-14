import random
import sys
import linecache
#we're going to use a text file that is already on your computer and is already formatted nicely for parsing: the words file. This file is available on all Unix and Unix-like systems.
#On my MacBook running OS X Yosemite, this file is located at /usr/share/dict/words.
# it has over 235886 words

def randomSentence(): #6
    filename = "/usr/share/dict/words"
    #array = file.read().splitlines()
    rand_index = random.randint(1, 235886)
    word = linecache.getline(filename, rand_index, module_globals=None)
    word = word.rstrip()
    return word + " "


if __name__ == '__main__': #5
    count = int(sys.argv[1])
    sentence = ""
    # for loop for every single sentence that we count, we add a senstence to get word
    for i in range(count):
        sentence += randomSentence()
    print(sentence)
