import sys
import re
import random
from datetime import datetime

# Analyze word frequency in a histogram
# sample words according to their observed frequencesie
# compare tradeoff with different sampling techniques
# 1. # use dictionary to create my histogram key and value pairs inside my histogram
# 2. use list of list to create one solution to solve this problem

def histogram(source_text):
    histogram = {}
    # python ways of removing any sort of string, removing ,:;, and any other special character
    for word in source_text.split():
        word = re.sub('[.,:;!-[]?', '', word)

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def random_word(histogram):
    """   first take a random sample of key/value pairs
    and add them to a list """
    probability = 0
    rand_index = random.randint(1, sum(histogram.values()))
    # Algorithm 1
    for word in histogram:
        probability += histogram[word]
        if probability >= rand_index:
            if word in outcome_gram:
                outcome_gram[word] += 1
            else:
                outcome_gram[word] = 1
            return word
    # Algorithm 1
    # for (key, value) in histogram.items():
    #     for num in range(1, value + 1):
    #         if probability == rand_index:
    #             if key in outcome_gram:
    #                 outcome_gram[key] += 1
    #             else:
    #                 outcome_gram[key] = 1
    #             # return outcome_gram
    #             return key
    #         else:
    #             probability += 1

def unique_words(histogram):
    """Return the amount of words that only show up once in the histogram."""
    #  uniqueWords is a list that stores the words that only happens once
    uniqueWords = []
    for histogramWord in histogram:
        if histogramWord[1] == 1:
            uniqueWords.append(histogramWord)
    return(len(uniqueWords))

def frequency(word, histogram):
    """Return the amount of times a word shows up in the histogram."""
    for histogramWord in histogram:
        if histogramWord[0] == word:
            return histogramWord[1]

if __name__ == "__main__":
    outcome_gram = {}
    dict = open("./sample-text.txt", 'r')
    text = dict.read()
    dict.close()
    hist_dict = histogram(text)
    for number in range(1, 100000):
        random_word(hist_dict)

    print("Original: ")
    #print(random_word(dict))
    print("If this were a perfect algorithm, the number of fish would be 50000, but my actual value is " + str(outcome_gram["fish"]))
    # for word, expected_count in hist_dict.items():
    print("The percent error is " + str(abs(outcome_gram["fish"] - 50000.0) / 50000.0 * 100.0) + "%")
    # outcome_gram["fish"] = abs(outcome_gram["fish"] - 5000.0) / 5000.0 * 100.0
    # calculate the frequencies of the words
    print (outcome_gram)
    print("Time: " + str(datetime.now() - start))
