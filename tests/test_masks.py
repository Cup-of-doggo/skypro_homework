import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 5999414228426353", "Maestro 5999 41** **** 6353"),
    ("MasterCard 5999414228426353", "MasterCard 5999 41** **** 6353"),
    ("Visa Classic 5999414228426353", "Visa Classic 5999 41** **** 6353"),
    ("Visa Platinum 5999414228426353", "Visa Platinum 5999 41** **** 6353"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
])
def test_mask_card(string, expected_result):
    assert get_mask_card_number(string) == expected_result


def test_mask_acc():
    assert get_mask_account('Счет 64686473678894779589') == 'Счет **9589'
