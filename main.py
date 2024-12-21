from src.file_readers import get_csv_file, get_excel_file
from src.generators import filter_by_currency
from src.oper_finder import find_operation
from src.processing import filter_by_state, sort_by_date
from src.utils import get_json_data
from src.widget import get_date, mask_account_card


def main() -> any:
    """основная функция отвечающая за логику проекта"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. ')
    while True:
        print('Выберите необходимый пункт меню:')
        print('1. Получить информацию о транзакциях из JSON-файла'
          '\n2. Получить информацию о транзакциях из CSV-файла'
          '\n3. Получить информацию о транзакциях из XLSX-файла')

        user_choose_extension = str(input())

        if user_choose_extension == "1":
            print('Для обработки выбран JSON-файл.')
            transaction_dict = get_json_data()
            break

        elif user_choose_extension == "2":
            print('Для обработки выбран CSV-файл.')
            transaction_dict = get_csv_file()
            break

        elif user_choose_extension == "3":
            print('Для обработки выбран XLSX-файл.')
            transaction_dict = get_excel_file()
            break

        else:
            print('Введен некоректный номер пункта')

    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию.'
           'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

        user_choose_filter = str(input().upper())

        if user_choose_filter == "EXECUTED" or user_choose_filter == 'CANCELED' or user_choose_filter == 'PENDING':
            print(f'Операции отфильтрованы по статусу {user_choose_filter}')
            filter_by_state(transaction_dict,state=user_choose_filter)
            break

        else:
            print(f'Статус операции {user_choose_filter} недоступен.')

    while True:
        print('Отсортировать операции по дате? Да/Нет')

        user_choose_sort_date = str(input().lower())

        if user_choose_sort_date == "да" or 'yes':
             while True:
                 print('Отсортировать по возрастанию или по убыванию? ')

                 user_choose_sort = str(input().lower())

                 if 'возраст' in user_choose_sort:
                     sort_by_date(transaction_dict,sort_order=False)
                     break
                 elif 'убыван' in  user_choose_sort:
                     sort_by_date(transaction_dict)
                     break
                 else:
                     print('Ответ введен некоректно')
                     continue
             break
        elif user_choose_sort_date == 'нет' or 'no':
            break
        else:
            print('Ответ введен некоректно')

    while True:
        print('Выводить только рублевые тразакции? Да/Нет')

        user_choose_rub =str(input().lower())

        if user_choose_rub == 'да' or 'yes':
            filter_by_currency(transaction_dict,"RUB")
            break
        elif user_choose_rub == 'нет' or 'no':
            break
        else:
            print('Ответ введен некоректно')
            continue

    while True:
        print('Отфильтровать список транзакций по определенному слову' 
               ' в описании? Да/Нет')

        user_choose_word_filter = input().lower()

        if user_choose_word_filter == 'да' or 'yes':
            print('Введите слово')
            transaction_dict = find_operation(transaction_dict, search_string=input())
            break
        elif user_choose_word_filter == 'нет' or 'no':
            break
        else:
            print('Ответ введен некоректно')
            continue

    print('Распечатываю итоговый список транзакций...')
    if len(transaction_dict) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши'
              'условия фильтрации')
    elif len(transaction_dict) > 0:

        print(f'Всего банковских операций в выборке:{len(transaction_dict)}')
        if user_choose_extension == "1":
            for transaction in transaction_dict:
                if transaction.get("description") == "Открытие вклада":
                    print(f"{get_date(transaction)} {transaction.get("description")}\n"
                          f"{mask_account_card(transaction.get("to"))}\nСумма: {transaction.get("operationAmount")["amount"]} "
                          f"{transaction.get("operationAmount")["currency"]["name"]}")

                else:
                    print(f"{get_date(transaction)}{transaction.get("description")}\n"
                          f"{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}\n"
                          f"Сумма: {transaction.get("operationAmount")["amount"]} "
                          f"{transaction.get("operationAmount")["currency"]["name"]}")

        else:
            for transaction in transaction_dict:
                if transaction.get("currency_name") == 'Rub':
                    transaction["currency_name"] = "руб."
                if transaction.get("description") == "Открытие вклада":
                    print(f"{get_date(transaction)} {transaction.get("description")}\n"
                          f"{mask_account_card(transaction.get("to"))}\nСумма: {transaction.get("amount")} "
                          f"{transaction["currency_name"]}")

                else:
                    print(f"{get_date(transaction)} {transaction.get("description")}\n"
                          f"{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}\n"
                          f"Сумма: {transaction.get("amount")} {transaction.get("currency_name")}")
