import cleanup
from histogram_oop import Dictogram
from random import choice
import random

"""
Markov Chain Code Reference to Alex Dejeu's article and sample code from HackerNoon
https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
Refactoring 1st Order Markov Model using python3.6
# Used Dictorgram class to access my histogram
#1 Used dictionary as data structure to create the markov chain
#2 For every word in the cleaned file - go through and update a historgram for the value
#3 Generate those tokens inside each historgram. 
#4 create the histogram for every single word
#5 set uzp and the if else statement and acces sets those words to the Dictogram inside our list
#6 Converting Markov to class object
"""
class Markov:
	
    def __init__(self, iterable):
        """Initialize with an empty dictionary of word nodes.
        """
        self.nodes = {}
        self.update(iterable)

    def update(self, iterable):
        """Takes a list of lines and processes them into nodes"""

    def generate_sentence(self):
    	pass

    def update_node(self, word, next_word):
        if word in self.nodes:
            self.nodes[word].update([next_word])
        else:
            self.nodes[word] = Dictogram([next_word])

    def get_next(self, current_word):
        dictogram = self.nodes.get(current_word, None)
        if dictogram is None:
            return '[END]'
        return dictogram.get_random_word()

    def generate_sentence(self):
        words = list()
        words.append(self.get_next('[START]'))

        while True:
            next_word = self.get_next(words[len(words) - 1])
            if next_word == '[END]':
                break
            words.append(next_word)

        sentence = " ".join(words)
        if len(sentence) < 30 or len(sentence) > 140:
            return self.generate_sentence()
        return sentence
        
"""markov function class that is working progress"""
def markov_model(data):
	"""markov model for 1st ordergi"""
	markov_chain = dict()
	for index in range(0, len(data) - 1):
		if data[index] in markov_chain:
			markov_chain[data[index]].update([data[index + 1]])
		else:
			markov_chain[data[index]] = Dictogram([data[index + 1]])
	import pdb; pdb.set_trace()
	return markov_chain
 
def get_start_token(markov):
	"""create a random starting word as our token start"""
	# import pdb; pdb.set_trace()
	print('keys:', list(markov.keys()))
	print('type:', type(markov.keys()))    
	return random.choice(list(markov.keys()))

def get_stop_token(markov):
	"""create a stop token for the end of the sentence"""
	pass

def generate_sentence(length, markov_model):
	# input variable is the length of the sentence
	# refactor sampling and create a Markov running sentences
	# loop through the dictogram and append the current word to the previous word
	# join the sentences to form a word
	# returns the sentence
	current_word = get_start_token(markov_model)
	sentence = [current_word]
	for i in range(0, length):
		current_dictogram = markov_model[current_word]
		#uncomment to do
		print ("___________________")
		print (current_dictogram)
		random_word = current_dictogram.return_weighted_random_word()
		current_word = random_word
		print ("___________________")
		print ('my current word: ' + current_word)
		sentence.append(current_word)
	return ' '.join(sentence) + '.'
	return sentence

if __name__ == '__main__':
    # filename = argv[1]
    # _file = open(filename, 'r')
	# testing my codes using pdb
	# start_words = get_start_token(cleaned_file)
	# testing with Dr. Sessus words 
	file_name = '/Users/jchiu/Desktop/Make/Term1/CS2/Python-Tweet-Generator/text/fish.txt'
	cleaned_file = cleanup.clean_file(file_name)
	markov_chain = markov_model(cleaned_file)
	print (generate_sentence(11, markov_chain))