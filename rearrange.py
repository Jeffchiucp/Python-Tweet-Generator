import random
import sys

"""
no use of slices but working on various problem
"""

def random_shuffle(): #2
    # Creates a random number between 1 and the total number of tokens
    words = sys.argv[1:len(sys.argv)]

    rand_index = random.randint(1, 20)

    for num in range(rand_index):
        first_index = random.randint(0,  len(words) - 1)
        second_index = random.randint(0,  len(words) - 1)
        # swap the word
        temp = words[first_index]
        words[first_index] = words[second_index]
        words[second_index] = temp
    return words



if __name__ == '__main__':
    print (' '.join(random_shuffle()))
    # print out the function to debug
    # print (random_word_order())
