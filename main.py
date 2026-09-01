"""
Charles Kahlenberg 
Date Created: 9/1/2026
Last edit: 9/1/2026

Random Writer: Collects information from a provided text and creates a predictive model based on it to create an output.
Built off of provided template
"""

# INPUTS
from random import randint, choice

# SUBROUTINES

# returns a random seed of length level (or k) from the book
def get_seed(level, book):
    # pick a random index, prevent the seed going out of bounds
    index = randint(0, len(book) - level)
    # return the random seed of length level (or k)
    return book[index:index + level]

# returns a random next character given a seed from the book
def get_next_char():
    # initialize the list of characters
    pass
    # initialize the current index (where we begin to look in the book)

    # continually find the seed in the book
        # find the index of the seed in the book beginning at the current index

        # abort if the seed is not found (or it's at the end of the book)

        # otherwise, add the next character to the list

        # and update the index in the book

    # if there is at least one next character in the list of characters, return a randomly chosen one

    # otherwise, return some appropriate trigger (e.g., None)

# VARIABLES
level = 0
length = 0
filename = 0
book = None
output = None
seed = None
###### MAIN ######

# grab command line arguments (or manually set the parameters)
#  k (or level) -> the level of analysis performed on the book
#  length -> the length of output to generate
#  filename -> the filename that contains the text of the book
level = 2
length = 150
filename = "books\\hg-wells_the-time-machine.txt"

# grab the book
with open(filename, "r") as f:
    book = f.read()

# initialize the output
output = ""


# pick a random seed of length level (or k)
#seed = get_seed(level, book)

# repeat as long as there isn't enough output yet
    # get a random next character

    # if one exists
        # add it to the output

        # and recalculate the seed

    # otherwise, pick another random seed

# display the output
# OUTPUT