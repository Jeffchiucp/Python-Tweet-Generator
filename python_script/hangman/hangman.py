import random
import string
import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.makeschool.com/")
soup = BeautifulSoup(page.content, 'html.parser')
blockquotes = soup.find_all('blockquote')
webWords = blockquotes[1].get_text().split(' ')
secretWebWord = random.choice(webWords)


def loadWord():
    """This will import the words list."""
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')    
    secretWord = random.choice(wordsList)
    return secretWord


def getGuess(lettersGuessed):
    guess = "0"
    while guess not in string.ascii_lowercase or guess in lettersGuessed:
        print("What letter do you want to guess?")
        guess = input()
    return guess


def isGameOver(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean,
        True if all letters of secretWord are guessed or if no more guesses;
        False otherwise
    """
    counter = 0
    for letter in lettersGuessed:
        if letter not in secretWord:
            counter += 1
    if counter == 7:
        print("You lost. The secret word was " + secretWord + ".")
        return True

    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    print(secretWord)
    print("You won")
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    for letter in secretWord:
        if letter in lettersGuessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def guessesLeft(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, tells user how many guesses are left
    """
    guesses = 7
    for letter in lettersGuessed:
        if letter not in secretWord:
            guesses -= 1
    print(" You have " + str(guesses) + " guesses left")


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    print("Guesssed:", end=" ")
    for character in lettersGuessed:
        print(character, end=", ")
    print("")


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    lettersGuessed = []
    while not isGameOver(secretWord, lettersGuessed):
        getGuessedWord(secretWord, lettersGuessed)
        guessesLeft(secretWord, lettersGuessed)
        guess = getGuess(lettersGuessed)
        lettersGuessed.append(guess)
        getAvailableLetters(lettersGuessed)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = loadWord()
print(secretWebWord)
hangman(secretWebWord)

