import cleanup
from histogram_oop import Dictogram
from random import choice
import random

"""
Markov Chain Code Reference to Alex Dejeu's article and sample code from HackerNoon
https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
Refactoring with 1st Order Markov Model using python3.6
# Used Dictorgram class to access my histogram
#1 Used dictionary as data structure to create the markov chain
#2 For every word in the cleaned file - go through and update a historgram for the value
#3 Generate those tokens inside each historgram. 
"""
def markov_chain(data):

    markov_chain = dict()

    for index in range(0, len(data) - 1):
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    return markov_chain
 
def generate_start_token(markov):
	"""create a random starting word as our token start"""
	return random.choice(list(markov.keys()))


def generate_random_sentence(length, markov_chain):
	# input variable is the length of the sentence
	# refactor sampling and create a Markov running sentences
	# loop through the dictogram and append the current word to the previous word
	# join the sentences to form a word
	# returns the sentence
    current_word = generate_start_token(markov_chain)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_chain[current_word]
        print ("___________________")
        print (current_dictogram)
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word =  random_weighted_word
        print ("___________________")
        print ('current word: ' + current_word)
        sentence.append(current_word)
    return ' '.join(sentence) + '.'
    return sentence


file_name = '../text/fish.txt'
cleaned_file = cleanup.clean_file(file_name)
# print(cleaned_file)
markov_chain = markov_chain(cleaned_file)
# testing for 11 words 
print (generate_random_sentence(11, markov_chain))