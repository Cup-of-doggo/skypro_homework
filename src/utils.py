import json
import os

def get_date(file_path = None) -> any:
    """возвращает список словарей из json файла"""
    if file_path == None:
        file_path = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        with open(file_path, 'r', encoding= "utf-8") as f:
            transactions = json.load(f)
            return transactions
