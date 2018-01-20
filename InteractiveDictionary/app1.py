"""
This file is the demonstration of the how the dictionary works
The user inputs a word and the program gives the meaning of the word
The data.json file contains a collection of words(around 50000) and their meanings
(all in lowercase)
The program returns the meaning of a similar word if the exact match
is not found after user confirmation
"""

import json
from difflib import get_close_matches

# Loading the json file
data = json.load(open("data.json"))

# Constants
# Error message for word doesn't exist
WORD_NON_EXISTENCE = "The word doesn't exist"

def meaning_of_word(word):
    """
    Function that returns the meaning of a word
    :param word: Input from the user
    :return: a string, which is the meaning of the given word
    """
    # Converting the user input to lower case
    word_lower_case = word.lower()

    # Variable to hold proper nouns(Start with capital letter)
    proper_nouns = word[0] + word[1:]

    # Checking if the word actually exists in the dictionary

    # Checking for proper nouns
    if proper_nouns in data:
        return data[proper_nouns]
    # Checking after converting the word to all lower case
    elif word_lower_case in data:
        return data[word]
    else:
        # Checking for non-existence and similarity of the word
        return check_for_similar_word(word)


def check_for_similar_word(word):
    """
    This function checks if the given word passed as argument
    doesn't really exist in the dictionary or if there is a similar word
    in the dictionary
    :param word: the word input by the user
    :return: meaning of the word iff it exists, error message otherwise
    """
    # Checking if the user-input word is similar to one
    # of the words in the dictionary
    close_matches_list = get_close_matches(word, data.keys())
    if len(close_matches_list):
        # There exists a close match to the word with cutoff 0.6
        # refer difflib module

        # Accepting user confirmation
        yes_no = input("Did you mean to type %s instead. Enter Y or N: " % \
                       get_close_matches(word, data.keys())[0])

        # Parsing the user input
        if yes_no == "Y":
            return data[close_matches_list[0]]
        elif yes_no == "N":
            return WORD_NON_EXISTENCE
        else:
            return "Please enter Y or N only"

    else:
        return WORD_NON_EXISTENCE


# Accepting input from user
word = input("Enter the word:")

# The result is a list
result = meaning_of_word(word)

# Displaying the elements in a list
if type(result) == list:
    for meaning in result:
        print(meaning)
else:
    print(result)

