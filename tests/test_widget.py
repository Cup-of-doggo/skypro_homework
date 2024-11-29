from src.widget import get_date
from src.widget import mask_account_card

def test_mask_acc_card():
    assert mask_account_card('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'


def test_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'