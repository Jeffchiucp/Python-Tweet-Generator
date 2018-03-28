#!python

from __future__ import division
import random


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
        self.types = len(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self.get(item, 0)

    def return_random_word(self):
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        #return random word from the weight probabilities
        random_weight = random.randint(0, self.tokens-1)
        #test index
        index = 0
        words_list = list(self.keys())
        # uncommeting to test the type
        # import pdb; pdb.set_trace()
        # print('keys:', words_list)
        # print('type:', type(words_list))
        # for i in range(0, self.types):
        #     word = words_list[i]
        for word in words_list:
            index += self[word]
            # print (index)
            if(index > random_weight):
                return word


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        temp_dict = {}
        for item in iterable:
            # TODO: increment item count
            self.tokens += 1
            if item in temp_dict:
                temp_dict[item] += 1
            else:
                temp_dict[item] = 1

        self[0:] = temp_dict.items();

        self.types = len(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        for tup in self:
            if tup[0] == item:
                return tup[1]
        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        # TODO: check if item is in histogram
        for tup in self:
            if tup[0] == item:
                return True
        return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        # TODO: implement linear search to find an item's index
        for index, tup in enumerate(self):
            if tup[0] == item:
                return index
        return None


def test_histogram(text_list):    
    print('text list:', text_list)
    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()

def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  
    #test_histogram(words)
