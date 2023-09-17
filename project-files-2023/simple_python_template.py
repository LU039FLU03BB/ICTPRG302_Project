"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 6

# TODO: select target word at random from TARGET_WORDS

# Stand-in (until function works:
target_word = 'hello'

def select_random_word(TARGET_WORDS):
    """Selects target word at random from TARGET_WORDS.
    Returns a string: target_word
    Examples:
    >>> select_random_word()
    'ficus'
    >>> select_random_word()
    'mango'
    >>> select_random_word()
    'holly'
    """

    return target_word
# Uncomment to run when function works
# target_word = select_random_word()


# TODO: repeat for MAX_TRIES valid attempts
# (start loop)
print("Please enter a 5-letter word")
guess = input("Enter guess? ")


def valid_guess_checker(guess):
    """Checks whether a guess is in  the VALID_WORDS list.
    Takes user input "guess" and returns boolean "in_list"

    Example:
    >>> valid_guess_checker('12345')
    False
    >>> valid_guess_checker('ficus')
    True
    >>> valid_guess_checker('    ')
    False
    >>> valid_guess_checker('zzzzzzzzzzzzzz')
    False

    """
    in_list = False

    return in_list


def guess_scorer(target_word, guess):
    """Compares guess to target_word and checks each letter to see if correct,
    incorrect, or misplaced.

    Returns 2 for correct, 1 for misplaced, & 0 for incorrect

    Examples:
    >>> guess_scorer('mango', 'ficus')
    (0, 0, 0, 0, 0)
    >>> guess_scorer('mango', 'mango')
    (2, 2, 2, 2, 2)
    >>> guess_scorer('mango', 'manga')
    (2, 2, 2, 2, 0)
    """

    return 0, 0, 0, 0, 0



# TODO: provide clues for each character in the guess using your scoring algorithm
if guess == target_word:
    print("Your guess is correct!")
else:
    print("Your guess is wrong!")

# (end loop)
print("Game Over")


# NOTES:
# ======
# - Add your own flair to the project
# - You will be required to add and refine features based on changing requirements
# - Ensure your code passes any tests you have defined for it.

# SNIPPETS
# ========
# A set of helpful snippets that may help you meet the project requirements.

def pick_target_word(words=None):
    """returns a random item from the list"""
    words = ['a', 'b', 'c']
    return random.choice(words)


def display_matching_characters(guess='hello', target_word='world'):
    """Get characters in guess that correspond to characters in the target_word"""
    i = 0
    for char in guess:
        print(char, target_word[i])
        i += 1

# Uncomment to run:


display_matching_characters()
print(pick_target_word())
