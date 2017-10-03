#!python


from __future__ import division


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
            # TODO: increment item count
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
        self.types = len(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        return self.get(item, 0)

    def return_random_word(self):
        # Another way:  Should test: random.choice(histogram.keys())
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        # Step 1: Generate random number between 0 and total count - 1
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_of_keys = self.keys()
        # print 'the random index is:', random_int
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            # print index
            if(index > random_int):
                # print list_of_keys[i]
                return list_of_keys[i]

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


# def test_histogram(text_list):
#     print('text list:', text_list)

#     hist_dict = Dictogram(text_list)
#     print('dictogram:', hist_dict)

#     hist_list = Listogram(text_list)
#     print('listogram:', hist_list)
#     fish_list = Dictogram(text_list)
#     print('fish_list:', fish_list)
#     print (fish_list.count("fish_list"))


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)