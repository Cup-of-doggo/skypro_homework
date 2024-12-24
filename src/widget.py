from src.masks import get_mask_account, get_mask_card_number



def mask_account_card(some_card_number: str) -> str:
    '''функция принимает счет или номер карты и возвращает его маску'''
    if "Счет" in str(some_card_number):
        return get_mask_account(some_card_number)
    else:
        return get_mask_card_number(some_card_number)


def get_date(transaction:dict) -> str:
    '''функция принимает дату и возвращает в читабельном формате'''
    date = str(transaction.get("date"))
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
