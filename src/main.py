from src.file_readers import get_csv_file, get_excel_file
from src.processing import filter_by_state
from src.utils import get_json_data


if __name__ == '__main__':
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. ')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла'
          '\n2. Получить информацию о транзакциях из CSV-файла'
          '\n3. Получить информацию о транзакциях из XLSX-файла')

user_choose_extension = str(input())

if user_choose_extension == "1":
    print('Для обработки выбран JSON-файл.')
    get_json_data()
elif user_choose_extension == "2":
    print('Для обработки выбран CSV-файл.')
    get_csv_file()
elif user_choose_extension == "3":
    print('Для обработки выбран XLSX-файл.')
    get_excel_file()

print('Введите статус, по которому необходимо выполнить фильтрацию.' 
         'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

user_choose_filter = str(input())

print(filter_by_state(get_json_data()))





