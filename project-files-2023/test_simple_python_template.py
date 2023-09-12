"""Tests for simple_python_template"""

TARGET_WORDS = './word-bank/target_words.txt'
# Once function is written,
# target_word = select_random_word()
target_word = 'mango'




def test_select_random_word():
    """Test for select_random_word()"""
    # target_word = select_random_word()
    is_from_file = False

    handle = open(TARGET_WORDS)
    for line in handle:
        line = line.rstrip()
        if target_word == line:
            is_from_file = True
        else:
            continue

    assert is_from_file
