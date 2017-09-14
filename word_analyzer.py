import sys
import re
import operator
import random
import time
import numpy

start_time = time.time()

#Your first task is to write a function that takes a histogram
#(however you've structured yours) and returns a single word, at random.
#It should not yet take into account the distributions of the words.

def create_histogram(word_list):
    histogram = {};
    for word in word_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    #print histogram
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

def getOnlyWord(file_path):
    with open(file_path) as f:
        text = f.read()
        words = re.findall(r'(?!\d+)(\w+)',text)
        return words

def get_sample(histogram):
    sorted_histogram = sorted(histogram.items(), key=operator.itemgetter(1))

    total_sum = sum([tup[1] for tup in sorted_histogram])
    frequency_sum = 0

    random_number = random.randint(1, total_sum)
    # frequency_sum = str(numpy.random.choice(histogram,10,4))
    for tup in sorted_histogram:
        frequency_sum += tup[1]
        if random_number <= frequency_sum:
            print ("The frequency is %d\nThe random number is %d" % (frequency_sum, random_number))
            return tup[0]


if __name__ == '__main__':
    file_path = sys.argv[1]
    words = getOnlyWord('../bible.txt')
    histogram = create_histogram(words)

    print (get_sample(histogram))
    print ("Unique words: " + str(unique_words(histogram)))
    #print (frequency('mystery', histogram))
    print (time.time() - start_time)
