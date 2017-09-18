import sys
import re
import random
import time

# Analyze word frequency in a histogram
# sample words according to their observed frequencesie
# compare tradeoff with different sampling techniques
#   1. # use dictionary to create my histogram key and value pairs inside my histogram
# 2. use list of list to create one
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
    probability = 0
    rand_index = random.randint(1, sum(histogram.values()))
    # Algorithm 1
    for (key, value) in histogram.items():
        for num in range(1, value + 1):
            if probability == rand_index:
                if key in outcome_gram:
                    outcome_gram[key] += 1
                else:
                    outcome_gram[key] = 1
                # return outcome_gram
                return key
            else:
                probability += 1
    # Algorithm 2
    # for word in histogram:
    #     probability += histogram[word]
    #     if probability >= rand_index:
    #         if word in outcome_gram:
    #             outcome_gram[word] += 1
    #         else:
    #             outcome_gram[word] = 1
            # return word

if __name__ == "__main__":
    outcome_gram = {}
    dict = open('./fish.txt', 'r')
    text = dict.read()
    dict.close()

    hist_dict = histogram(text)
    for number in range(1, 100000):
        random_word(hist_dict)

    print("If this were a perfect algorithm, the number of fish would be 50000, but my actual value is " + str(outcome_gram["fish"]))
    # for word, expected_count in hist_dict.items():
    print("The percent error is " + str(abs(outcome_gram["fish"] - 50000.0) / 50000.0 * 100.0) + "%")
    # outcome_gram["fish"] = abs(outcome_gram["fish"] - 5000.0) / 5000.0 * 100.0
