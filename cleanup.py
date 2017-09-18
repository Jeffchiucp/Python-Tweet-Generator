import re

# Takes: Freshly split list | Returns: Clean list of words
def clean_text(dirty_list):
    clean_list = []
    for word in dirty_list:
        word = re.sub('[.,:;!-[]?', '', word)
        clean_list.append(word)
    return clean_list
