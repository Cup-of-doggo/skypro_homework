from decorators import log


@log()
def add_numbers(x, y):
    """функция для теста"""
    return x + y


result = add_numbers(3, 5)
assert result == 8


@log()
def hello_world():
    """функция для теста"""
    print("Hello, world!")


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!\nhello_world все ок \nРезультат: None\n'
