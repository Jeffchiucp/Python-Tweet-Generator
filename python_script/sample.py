#!python3
from random import randint
from random import random
from sys import argv
import time


def create_histogram(filename):
    """ Create the Histogram to open the filename to start my sampling"""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    histogram = {}
    for line in lines:
        line = line.rstrip('\n').split(' ')
        histogram[line[0]] = int(line[1])
    return histogram


def create_relative_probabilities(hist):
    """Randomly picking items with given weights. Code Source from Sam and Elmer"""
    total_words = get_total_word_count(hist)
    for word in hist.keys():
        freq = hist[word] / float(total_words)
        hist[word] = freq
    return hist


def get_random_word(hist):
    """
        first take a random sample of key/value pairs
        floating point, get ferequency
    # computing the increasing cumulative probability
    # until the cumulative_probability becomes greater than the random_int
        """
    prob = random()
    accumulator = 0.0
    keys = list(hist.keys())
    current_key = None

    while accumulator < prob:
        current_key = keys.pop(randint(0, len(keys) - 1))
        if accumulator + hist[current_key] > prob:
            break
        else:
            accumulator += hist[current_key]
    return current_key


def get_total_word_count(dic):
    """calculate the total_word"""
    total_words = 0
    for word in dic.keys():
        total_words += dic[word]
    return total_words


def generate_sentence(data, length):
    """generate the sentence using the histogram data"""
    graph = create_histogram(data)
    relative_freq = create_relative_probabilities(graph)
    output = ""

    for num in range(0, length):
        new_word = get_random_word(relative_freq)
        output += '{} '.format(new_word)
    return output


def test_frequency_distribution(data, length):
    """Return the amount of times a word shows up in the histogram."""
    graph = create_histogram(data)
    relative_freq = create_relative_probabilities(graph)
    print(relative_freq)
    results = {}

    for num in range(0, length):
        new_word = get_random_word(relative_freq)
        if new_word in results:
            results[new_word] += 1
        else:
            results[new_word] = 1
    return results


if __name__ == '__main__':
    start = time.time()
    arguments = argv[1:]
    """ testing code """
    # UnComment this line to test the accuary of the word
    # calculate the frequencies of the words
    #print(generate_sentence(arguments[0], int(arguments[1])))

    # UnComment this line to test the accuary of the word
    # result = test_frequency_distribution(arguments[0], int(arguments[1]))
    # for word in result.keys():
    #     print('{0}: {1}'.format(word, result[word]))

    print('Time taken to execute: {0} seconds'.format(time.time() - start))
