import sys

def reverse_word():
    word_to_reverse = raw_input('Write a word or a phrase: ')
    reversed_word = ''

    for index in xrange(len(word_to_reverse) - 1, -1, -1):
        reversed_word += word_to_reverse[index]

    return reversed_word

if __name__ == '__main__':
    print reverse_word()

