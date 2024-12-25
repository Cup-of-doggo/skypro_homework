import csv
import os
import pandas as pd


def get_csv_file(file_path=None) -> any:
    """возвращает список словарей с транзакциями из csv файла"""
    try:
        file_path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
        with open(file_path, 'r', encoding="utf-8") as file:
            transactions_reader = csv.DictReader(file, delimiter=';')
            transactions = []
            for transaction in transactions_reader:
                transactions.append(transaction)
        return transactions
    except Exception as err:
        return f'Произошла ошибка:{err}'


def get_excel_file(file_path=None) -> any:
    """возвращает список словарей с транзакциями из excel файла"""
    try:
        if file_path is None:
            filepath = (r"C:\Users\gorde\PycharmProjects\project_bank\project\src\data\transactions_excel.xlsx")
            transactions = pd.read_excel(filepath).to_dict('records')
            return transactions
        else:
            filepath = file_path
            transactions = pd.read_excel(filepath).to_dict('records')
            return transactions
    except Exception as err:
        return f'Произошла ошибка:{err}'
