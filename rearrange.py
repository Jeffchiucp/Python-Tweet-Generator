#!python3
import random
import sys

"""
no use of slices but working on various problem
"""

#passed by reference
# passed by value
# passed it here
# .copy() # python 3 only
# .clone in Java
# list() method, list
# scramblede values of the original list  list(original)
#  does the original list get modified?
#  yes. in this case.
# we should do copy a new list. please implement that.
# 1 way. .copy()
# scrambled = original[:]
# is scrambled list, is it

# thing to think about ...
# objects, and collections - in python, treated it like passed by reference
# int, float - in python, treated like passed by value. They can be copied as a pointer.

# syntax sugar of the python
# go all the [6::-1]
# [::-1] easy way to reverse the list
# scrambled = original[::-1]
def random_shuffle(): #2
    # Creates a random number between 1 and the total number of tokens
    words = sys.argv[1:len(sys.argv)]
    #python sorted, and added color
    # python has a way for a way to shuffle index
    # len(includes original, and excludes the length )
    # python | if you don't know,
    # alice in
    rand_index = random.randint(1, 20)

    # before we learn more about
    # slice, range
    # make a list of integer
    # first argument, inclusive,
    for num in range(rand_index):
        first_index = random.randint(0,  len(words) - 1)
        second_index = random.randint(0,  len(words) - 1)
        words[first_index], words[second_index] = words[second_index], words[first_index]
        # words[second_index] = temp
    return words
    # words is a string1
    # print out the function to debug

    #run on the command line
if __name__ == '__main__':
    print(' '.join(random_shuffle()))
    # print out the function to debug
