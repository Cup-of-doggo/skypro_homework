import pytest
from decorators import log

def add_numbers(x,y):
    return x + y


def test_log(capsys):
    @log()
        add_numbers(3,5)
        captured = capsys.readouterr()
        assert captured.out == 8


result = add_numbers(3,5)
assert result == 8


