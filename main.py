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
def get_next_char(seed, book):
    # initialize the list of characters
    chars = []
    book_copy = book
    # initialize the current index (where we begin to look in the book)
    index = 0
    # continually find the seed in the book
    while index != -1:
        # find the index of the seed in the book beginning at the current index
        index = book_copy.find(seed, index)
        # abort if the seed is not found (or it's at the end of the book)
        if index == -1:
            break

        # otherwise, add the next character to the list
        chars.append(book_copy[index + len(seed)])

        #remove everything up to and including the current seed
        book_copy = book_copy[index + len(seed):]

    # if there is at least one next character in the list of characters, return a randomly chosen one
    if len(chars) > 0:
        return choice(chars)
    # otherwise, return some appropriate trigger (e.g., None)
    return None

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
level = 10
length = 300
<<<<<<< Updated upstream
filename = "books\\hg-wells_the-time-machine.txt"
=======
filename = "books\\jules-verne_the-mysterious-island.txt"
>>>>>>> Stashed changes

# grab the book
with open(filename, "r") as f:
    book = f.read()

# initialize the output
output = ""


# pick a random seed of length level (or k)
seed = get_seed(level, book)


# repeat as long as there isn't enough output yet
while(len(output) != length):
    # get a random next character
    next_char = get_next_char(seed, book)
    # if one exists
    if next_char is not None:
        # add it to the output
        output += next_char

        # and recalculate the seed
        seed = seed[1:] + next_char
    # otherwise, pick another random seed
    else:
        seed = get_seed(level, book)

# display the output
# OUTPUT
print(output)