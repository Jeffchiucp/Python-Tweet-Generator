import sys
import re
#from histogram import text_file_list
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

def get_random_word(dictionary):
    """Returning a random word from a dictionary. thanks to Elmer """
    rand_index = random.randint(0, len(dictionary) - 1)
    key_list = list(dictionary)
    random_w = key_list[rand_index]
    return random_w

def get_random_with_weight(dictionary):
    """Randomly picking items with given weights. Code Source from Elmer"""
    dictionary_weightValue = {}
    total_values = sum(histogram.values())
    # Grab every value from dictionary python
    for (word, value) in histogram.items():
        #print("{} : {} ".format(word, value))
        total = value / total_values
        print(total)
        #print(total)
        # Getting the weight of each value
        #  weighted_value
        dictionary_weightValue[word] = total
    #     print(total)
    # print(dictionary_weightValue)
    return dictionary_weightValue

def get_random_word_by_weight_prob(dictionary_weightValue):
    """
    first take a random sample of key/value pairs
    floating point, get ferequency
    """
    random_int = random.random()
    cumulative_probability = 0.0
    for (word, weightValue) in dictionary_weightValue.items():
        # computing the increasing cumulative probability
        cumulative_probability += weightValue
        # until the cumulative_probability becomes greater than the random_int
        if random_int < cumulative_probability:
            break
    return word

def unique_words(histogram):
    """Return the amount of words that only show up once in the histogram."""
    #  Source code from James. uniqueWords is a list that stores the words that only happens once
    uniqueWords = []
    for histogramWord in histogram:
        if histogramWord[1] == 1:
            uniqueWords.append(histogramWord)
    return(len(uniqueWords))

def frequency(word, histogram):
    """Return the amount of times a word shows up in the histogram."""
    for histogramWord in histogram:
        if histogramWord[word] == 1:
            return histogramWord[1]

if __name__ == "__main__":
    outcome_gram = {}
    dict = open('./fish.txt', 'r')
    text = dict.read()
    dict.close()
    hist_dict = histogram(text)
    weight = get_random_with_weight(hist_dict)
    start = datetime.now()
    print(hist_dict)    # for word, expected_count in hist_dict.items():
    #print(unique_words(histogram))
    print("calculate the frequencies of the words")
    for number in range(1, 10):
        dictionary_weightValue = get_random_with_weight(hist_dict)
        # print(dictionary_weightValue)
        # print(get_random_word_by_weight_prob(dictionary_weightValue))

    # calculate the frequencies of the words
    ##print(unique_words())
    print("Time: " + str(datetime.now() - start))
    #print("If this were a perfect algorithm, the number of fish would be 50000, but my actual value is " + str(outcome_gram["fish"]))
    # for word, expected_count in hist_dict.items():
    #print("The percent error is " + str(abs(outcome_gram["fish"] - 50000.0) / 50000.0 * 100.0) + "%")
    #outcome_gram["fish"] = abs(outcome_gram["fish"] - 5000.0) / 5000.0 * 100.0
    # calculate the frequencies of the words