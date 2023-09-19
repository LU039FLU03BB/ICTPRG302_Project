"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO
# items below in the order you specified in the journal

import random

TARGET_WORDS = 'project-files-2023/word-bank/target_words.txt'
VALID_WORDS = 'project-files-2023/word-bank/all_words.txt'


def select_random_word(file_path=TARGET_WORDS):
    """Selects target word at random from TARGET_WORDS.
    Returns a string: target
    Examples:
    >>> select_random_word()
    'ficus'
    >>> select_random_word()
    'mango'
    >>> select_random_word()
    'holly'
    """
    word_list = []
    handle = open(TARGET_WORDS)

    for line in handle:
        line_list = line.rstrip().split("\n")
        for item in line_list:
            if item not in word_list:
                word_list.append(item)
    target = random.choice(word_list)

    return target


def is_valid_guess(guess):
    """Checks whether a guess is in  the VALID_WORDS list.
    Takes user input "guess" and returns boolean "in_list"

    Example:
    >>> is_valid_guess('12345')
    False
    >>> is_valid_guess('ficus')
    True
    >>> is_valid_guess('    ')
    False
    >>> is_valid_guess('zzzzzzzzzzzzzz')
    False

    """
    in_list = False
    guess = guess.lower()

    handle = open(VALID_WORDS)
    for line in handle:
        line = line.rstrip()
        if guess == line:
            in_list = True
        else:
            continue

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


def play():
    """Starts the game and goes through the flow chart"""
    TARGET_WORD = select_random_word(TARGET_WORDS)
    print(TARGET_WORD)
    MAX_TRIES = 6

    while MAX_TRIES > 0:

        print("Please enter a 5-letter word")
        guess = input("Enter guess: ")

        while not is_valid_guess(guess):
            print("That is not a valid guess. Please enter a 5-letter word")
            guess = input("Enter guess: ")

        if guess == TARGET_WORD:
            print("Your guess is correct!")
        else:
            print("Your guess is wrong!")

# TODO: provide clues for each character
# in the guess using your scoring algorithm
        MAX_TRIES = MAX_TRIES - 1
        if MAX_TRIES != 0:
            print("You have ", MAX_TRIES, "tries left. Please guess again")

    print("Game Over")


play()
