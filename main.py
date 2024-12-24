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
            filtred_transaction_dict = filter_by_state(transaction_dict, state=user_choose_filter)
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
                     sorted_transaction_dict = sort_by_date(filtred_transaction_dict,sort_order=False)
                     break
                 elif 'убыван' in  user_choose_sort:
                     sorted_transaction_dict = sort_by_date(filtred_transaction_dict)
                     break
                 else:
                     print('Ответ введен некоректно')
                     continue
             break
        elif user_choose_sort_date == 'нет' or 'no':
            sorted_transaction_dict = filtred_transaction_dict
            break
        else:
            print('Ответ введен некоректно')

    while True:
        print('Выводить только рублевые тразакции? Да/Нет')

        user_choose_rub =str(input().lower())

        if user_choose_rub == 'да' or 'yes':
            sort_filtred_transaction_dict = filter_by_currency(sorted_transaction_dict,"RUB")
            break
        elif user_choose_rub == 'нет' or 'no':
            sort_filtred_transaction_dict = sorted_transaction_dict
            break
        else:
            print('Ответ введен некоректно')
            continue

    while True:
        print('Отфильтровать список транзакций по определенному слову'
              ' в описании? Да/Нет')

        user_choose_word_filter = input().lower()

        if user_choose_word_filter == 'нет' or 'no':
            word_filtred_transaction_dict = sort_filtred_transaction_dict
            break

        elif user_choose_word_filter == 'да' or 'yes':
            print('Введите слово')
            word_filtred_transaction_dict = find_operation(transaction_dict, search_string=input())
            break

        else:
            print('Ответ введен некоректно')
            continue

    print('Распечатываю итоговый список транзакций...')
    transaction_length = [*word_filtred_transaction_dict]
    if len(transaction_length) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши'
              'условия фильтрации')
    elif len(transaction_length) > 0:

        print(f'Всего банковских операций в выборке:{len(transaction_length)}')
        if user_choose_extension == "1":
            for transaction in transaction_length:
                if transaction.get("description") == "Открытие вклада":
                    print(f'{get_date(transaction)} {transaction.get("description")}\n'
                          f'{mask_account_card(transaction.get("to"))}'
                          f'\nСумма: {transaction["operationAmount"]["amount"]} '
                          f'{transaction["operationAmount"]["currency"]["name"]}')

                else:
                    print(f'{get_date(transaction)} {transaction.get("description")}\n'
                          f'{mask_account_card(transaction.get("from"))} -> '
                          f'{mask_account_card(transaction.get("to"))}\n'
                          f'Сумма: {transaction["operationAmount"]["amount"]} '
                          f'{transaction["operationAmount"]["currency"]["name"]}')

        else:
            for transaction in transaction_dict:
                if transaction.get("operationAmount")["currency"]["name"] == 'RUB':
                    transaction.get("operationAmount")["currency"]["name"] = "руб."
                if transaction.get("description") == "Открытие вклада":
                    print(f'{get_date(transaction)} {transaction.get("description")}\n'
                          f'{mask_account_card(transaction.get("to"))}\nСумма: {transaction.get("amount")} '
                          f'{transaction("operationAmount")["currency"]["name"]}')

                else:
                    print(f'{get_date(transaction)} {transaction.get("description")}\n'
                          f'{mask_account_card(transaction.get("from"))} -> '
                          f'{mask_account_card(transaction.get("to"))}\n'
                          f'Сумма: {transaction.get("operationAmount")["amount"]}'
                          f' {transaction.get("operationAmount")["currency"]["name"]}')

main()
