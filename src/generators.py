def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """ Фильтрует список транзакций по заданной валюте. """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> str:
    """ Возвращает выполненные операции """
    try:
        for i in transactions:
            yield i["description"]
    except StopIteration:
        pass


def card_number_generator(a: int, b: int) -> str:
    """ Создает случайный номер для карты в заданном диапазоне """
    for number in range(a, b):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        generated_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
    yield generated_card_number
