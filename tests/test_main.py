from unittest.mock import patch

import pytest

from main import main


@pytest.fixture
def test_main_list():
    return [{}]


@patch("main.input")
def test_main(mock_input,test_main_list):
    mock_input.side_effect = ["3","executed","да","возрастанию","да","да","Открытие вклада"]
    assert main() == None