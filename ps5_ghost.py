# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def player(player_num):
    """
    get player's input, check valid or not
    
    player_num: int
    """
    pass
    
def change_frag(fragment, input_letter):
    fragment.append(input_letter)
    return fragment

def check_frag(fragment, wordlist_to_change):
    lose_in_dict = False
    lose_illegal = False
    len_frag = len(fragment)
    wordlist_changed = []
    if len_frag>3 and fragment in wordlist_to_change:
        lose_in_dict = True
        return lose
    for word in wordlist_to_change:
        if word[len_frag-1] == fragment[-1]:
            wordlist_changed.append(word)
    if len_frag>3 and len(wordlist_changed) == 0:
        lose_illegal = True
        return lose_illegal
    return wordlist_changed

# test code
wordlist_changed = check_frag('z', wordlist)
print wordlist_changed
wordlist_changed = check_frag('za', wordlist_changed)
print wordlist_changed
# wordlist_changed = check_frag('zax', wordlist_changed)
# print wordlist_changed
# test code end