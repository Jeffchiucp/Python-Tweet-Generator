#!python3
import random
import sys

"""
# python is passed by reference's value
# passed by reference
# passed by value
# passed it here
# how do we remember that it's a copy.
# .copy() # python 3 only
# .clone in Java
# list() method, list
# scramblede values of the original list  list(original)
# does the original list get modified? It depends.
#
# Yes. In this case, we want to sort database, huddle list,
# we should do copy a new list.
# we can take.
# please implement that.
# 1 way. .copy()
# scrambled = original[:]
# is scrambled list, is it

# thing to think about ...
# objects, and collections - in python, treated it like passed by reference. mutable .
# int, float - in python, treated like passed by value. They can be copied as a pointer.


# syntax sugar of the python
# go all the [6::-1]
# [::-1] easy way to reverse the list
# scrambled = original[::-1]

# how does the developer know what we return.
    # on_sorted (mutated the original list)
    # python sorted, and added color | returns a new copy | original is not modified.
    # python has a way for a way to shuffle index
    # len(includes original, and excludes the length )
"""

def random_shuffle(): #2
    # Creates a random number between 1 and the total number of tokens
    words = sys.argv[1:len(sys.argv)]

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
    # this is very python syntax to be able to join strings
