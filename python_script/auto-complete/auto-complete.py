import sys

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Autocomplete(word, dictionary):
    for element in dictionary:
        if len(element) > len(word):
            if element[0:len(word)] == word:
                print (element)

    '''
    for i in range(len(ALPHABET)):  # loop through the alphabet
        possible = suggestion + ALPHABET[i]
        if (d.check(possible)):
            break
    return suggestion
    '''

if __name__ == '__main__':


    words = sys.argv
    words.pop(0)
    words = []
    with open("/usr/share/dict/words") as file:
        for word in file:
            words.append(word.rstrip())
            
    # test case
    Autocomplete("la", words)
    '''
    print("Press Ctrl+C to quit")
    current_input = 0
    try:
        while True:
            word_so_far = input("Enter a word: ")
            print(len(word_so_far))
            if len(word_so_far) > current_input:
                current_input = len(word_so_far)
                print(Autocomplete(word_so_far))
    except KeyboardInterrupt:
        pass
    '''

