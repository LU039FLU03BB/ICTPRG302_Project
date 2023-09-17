"""Tests for simple_python_template"""
import pytest

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'
"""pytest Tests for simple_python_template.py"""

# Once function is written,
# from simple_python_template import select_target_word, guess_scorer


def test_select_random_word():
    """Test for select_random_word()"""
    target_word = 'mango'
    # target_word = select_random_word() once function is written
    is_from_file = False

    handle = open(TARGET_WORDS)
    for line in handle:
        line = line.rstrip()
        if target_word == line:
            is_from_file = True
        else:
            continue

    assert is_from_file


def test_valid_guess_checker(guess):
    """Test for valid_guess_checker()

    If guess is in VALID_WORDS, it is a valid guess.
    To run test:
    pytest --guess guessgoeshere test_simple_python_template.py
    """
    in_list = False

    handle = open(VALID_WORDS)
    for line in handle:
        line = line.rstrip()
        if guess == line:
            in_list = True
        else:
            continue

    assert in_list

# Learned how to use parametrize from
# https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing


@pytest.mark.parametrize("test_input1, test_input2, expected_output",
                         [('mango', 'mango', '2, 2, 2, 2, 2'),
                          ('mango', 'ficus', '0, 0, 0, 0, 0'),
                          ('mango', 'manga', '2, 2, 2, 2, 0')])
def test_guess_scorer(test_input1, test_input2, expected_output):
    """Test for guess_scorer()"""
    assert guess_scorer(test_input1, test_input2) == expected_output
