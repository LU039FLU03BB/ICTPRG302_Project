"""Config file for pytest, to add parameter to tests. Code below taken from:

   https://stackoverflow.com/questions/40880259/how-to-pass-arguments-in-pytest-by-command-line
"""
import pytest


def pytest_addoption(parser):
    """To add guess parameter to parser"""
    parser.addoption("--guess", action="store")


@pytest.fixture(scope='session')
def guess(request):
    """Pytest request fixture"""
    guess_value = request.config.option.guess
    if guess_value is None:
        pytest.skip()
    return guess_value
