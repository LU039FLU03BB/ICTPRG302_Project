"""Tests for simple_python_template"""
import pytest

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'
"""pytest Tests for simple_python_template.py"""

# Once function is written,
# from simple_python_template import select_target_word, guess_scorer
from simple_python_template import is_valid_guess

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


@pytest.mark.parametrize("guess", [
    "ficus",
    "Ficus",
    "FICUS",
    "FiCuS",
    "mango",
])
def test_is_valid_guess(guess):
    assert is_valid_guess(guess)


@pytest.mark.parametrize("invalid_guess", [
    "",
    "ficu5",
    "mangooooooooo",
    "12345",
])
def test_is_valid_guess_invalid(invalid_guess):
    assert not is_valid_guess(invalid_guess)


# Learned how to use parametrize from
# https://www.datacamp.com/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing


@pytest.mark.parametrize("test_input1, test_input2, expected_output",
                         [('mango', 'mango', '2, 2, 2, 2, 2'),
                          ('mango', 'ficus', '0, 0, 0, 0, 0'),
                          ('mango', 'manga', '2, 2, 2, 2, 0')])
def test_guess_scorer(test_input1, test_input2, expected_output):
    """Test for guess_scorer()"""
    assert guess_scorer(test_input1, test_input2) == expected_output
