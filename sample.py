#!python3

from random import randint, random
from sys import argv
import time


def create_histogram(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    histogram = {}
    for line in lines:
        line = line.rstrip('\n').split(' ')
        histogram[line[0]] = int(line[1])
    return histogram


def create_relative_probabilities(hist):
    total_words = get_total_word_count(hist)
    for word in hist.keys():
        freq = hist[word] / float(total_words)
        hist[word] = freq
    return hist


def get_random_word(hist):
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
    total_words = 0
    for word in dic.keys():
        total_words += dic[word]
    return total_words


def generate_sentence(data, length):
    graph = create_histogram(data)
    relative_freq = create_relative_probabilities(graph)
    output = ""

    for num in range(0, length):
        new_word = get_random_word(relative_freq)
        output += '{} '.format(new_word)
    return output


def test_frequency_distribution(data, length):
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

    #print(generate_sentence(arguments[0], int(arguments[1])))

    # Uncomment this line if you want to test the accuracy of the sampling
    # result = test_frequency_distribution(arguments[0], int(arguments[1]))
    # for word in result.keys():
    #     print('{0}: {1}'.format(word, result[word]))

    print('Time to execute: {0} seconds'.format(time.time() - start))