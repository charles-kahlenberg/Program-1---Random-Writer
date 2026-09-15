"""
Charles Kahlenberg 
Date Created: 9/1/2026
Last edit: 9/15/2026

Random Writer: Collects information from a provided text and creates a predictive model based on it to create an output.
Built off of provided template

Sources: Used Claude (Anthropic) to check and debug this program, including fixing the search logic in
get_next_char, the seed update when level is 0, and the file encoding.
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
    # initialize the current index (where we begin to look in the book)
    index = 0
    # continually find the seed in the book
    while index != -1:
        # find the index of the seed in the book beginning at the current index
        index = book.find(seed, index)
        # abort if the seed is not found (or it's at the end of the book)
        if index == -1 or index + len(seed) >= len(book):
            break

        # otherwise, add the next character to the list
        chars.append(book[index + len(seed)])

        # move the current index one past this match (so overlapping seeds are still found)
        index += 1

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
filename = "books\\jules-verne_the-mysterious-island.txt"

# grab the book (Project Gutenberg files are UTF-8)
with open(filename, "r", encoding="utf-8") as f:
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

        # and recalculate the seed (add the new char, then drop the first one; keeps the seed empty when level is 0)
        seed = (seed + next_char)[1:]
    # otherwise, pick another random seed
    else:
        seed = get_seed(level, book)

# display the output
# OUTPUT
print(output)