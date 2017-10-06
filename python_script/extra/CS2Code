import random
from Main import FileParser, Histogram


def random_sentence(letters):
    file = open("/usr/share/dict/words", "r")

    array = file.read().splitlines()
    length = len(array)
    to_return = ''

    for i in range(letters):
        to_return += array[random.randint(0, length) - 1] + " "

    return to_return


class Generator:
    def __init__(self, file):
        self.file = FileParser(file)
        self.histogram = Histogram()

    def generate_sentence(self, length):
        to_return = ''

        for i in range(length):
            to_return += self.histogram.random_word() + " "

        return to_return


def smart_shuffle(lst):
    for i in range(len(lst)):
        index = random.randint(i, len(lst) - 1)
        item = lst[index]
        lst[index] = lst[i]
        lst[i] = item

if __name__ == "__main__":
    print("We started here")