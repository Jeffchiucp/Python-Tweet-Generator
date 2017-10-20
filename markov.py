import cleanup
from dictogram import Dictogram
from random import choice
from collections import deque
import random
import re

"""
Markov Chain Code Reference to Alex Dejeu's article and sample code from HackerNoon
https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
Refactoring nth Order Markov Model using python3.6
#1 Used dictionary as data structure to create the markov chain
#2 For every word in the cleaned file - go through and update a historgram for the value
#3 Generate those tokens inside each historgram. 
#4 create the histogram for every single word
#5 set uzp and the if else statement and acces sets those words to the Dictogram inside our list
#6 Converting Markov to class object
"""

"""markov function class that is working progress"""
def markov_model(words):
    """markov model for 1st order"""
    markov_chain = dict()
    for index in range(0, len(words) - 1):
        word = words[index]  # ex: 'fish'
        next_word = words[index + 1]  # ex: 'red'
        if word in markov_chain:
            markov_chain[word].update([next_word])
        else:
            markov_chain[word] = Dictogram([next_word])
    return markov_chain

def make_higher_order_markov_model(order, words):
    markov_model = dict()
    for index in range(0, len(words) - order):
        # Create the window
        words_list = words[index : index + order]  # ex: ['fish', 'red']
        # import pdb; pdb.set_trace()
        next_word = words_list[1]  # ex: 'fish'
        window = tuple(words)  # ex: ('fish', 'red')
        print ("___________________")
        print ('my current word: ' + next_word)
        if window in window:
            # We have to just append to the existing histogram?
            markov_model[window].update([next_word])
        else:
            markov_model[window] = Dictogram([next_word])
    return markov_model


# figure out how does this work right now.
# which model am I using at this point 
def generate_random_start(model):
    # To generate a "valid" starting word use:
    # Valid starting words are words that started a sentence in the corpus
    if 'end' in model:
        seed_word = 'end'
        while seed_word == 'end':
            seed_word = model['end'].return_weighted_random_word()
        return seed_word
    return random.choice(list(model.keys()))

def get_start_token(markov):
    """create a random starting word as our token start"""
    # import pdb; pdb.set_trace()
    print('keys:', list(markov.keys()))
    print('type:', type(markov.keys())) 
    return random.choice(list(markov.keys()))

def generate_sentence(length, markov_model):
    # input variable is the length of the sentence
    # refactor sampling and create a Markov running sentences
    # loop through the dictogram and append the current word to the previous word
    # join the sentences to form a word
    # returns the sentence
    current_word = generate_random_start(markov_model)
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



def generate_random_sentence_n(length, markov_model):
    # Length denotes the max amount of chars
    # connect to twitter API
    current_window = get_start_token(markov_model)
    sentence = [current_window[0]]
    tweet = ''

    valid_tweet_flag = True
    sentence_count = 0
    while valid_tweet_flag:
        # We will generate random sentences until we decide we can not any more
        current_dictogram = markov_model[current_window]
        random_weighted_word = current_dictogram.return_weighted_random_word()

        current_window_deque = deque(current_window)
        current_window_deque.popleft()
        current_window_deque.append(random_weighted_word)
        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])
        print ('my current word inside windows: ' + str(current_window[1]))
        print ('my current window: ' + str(current_window))
        if current_window[1] == 'end' or current_window[1] == '[end]':
            sentence_string = ' '.join(sentence)
            sentence_string = re.sub('end', '. ', sentence_string, flags=re.IGNORECASE)
            sentence_string = sentence_string.capitalize()
            new_tweet_len = len(sentence_string) + len(tweet)

            if sentence_count == 0 and new_tweet_len < length:
                # We should add this sentence to the tweet and move on to
                # make another
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count == 0 and new_tweet_len >= length:
                # forget the sentence and generate a new one :P
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count > 0 and new_tweet_len < length:
                # More than one sentence. and length is still less max
                # Get another new sentence
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            else:
                # Return this good good tweet
                return tweet
                import pdb; pdb.set_trace()
                print(tweet)


def get_sentence_starters(file):
    result = []
    for i in range(0, len(file)-2):
        if file[i] == 'end':
            result.append(file[i+1])
    return result


if __name__ == '__main__':
    # filename = argv[1]
    # _file = open(filename, 'r')
    # testing my codes using pdb
    # start_words = get_start_token(cleaned_file)
    # testing with Dr. Sessus words 
    file_name = 'text/fish.txt'
    cleaned_file = cleanup.clean_file(file_name)

# uncomment to test the nth order markov chains
# start_words = get_sentence_starters(cleaned_file)
# markov_model_nth = make_higher_order_markov_model(2, cleaned_file)
# for key in markov_model_nth:
#     print('key:', key)
#     print('type:', type(key))
#     print(key, markov_model_nth[key])
#     print('markov_model_nth[key]:', markov_model_nth[key])
#     print('markov_model_nth[key] type:', type(markov_model_nth[key]))
# import pdb; pdb.set_trace()
# print(generate_random_sentence_n(50, markov_model_nth))