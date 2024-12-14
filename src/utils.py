import json
import os
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_json_data(file_path=None) -> any:
    """возвращает список словарей из json файла"""
    try:
        file_path = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        logger.info('превращаем json файл в python обьект')
        with open(file_path, 'r', encoding="utf-8") as f:
            transactions = json.load(f)
            return transactions
    except Exception as err:
        logger.error(f'Произошла ошибка {err}')
        return f'Произошла ошибка {err}'
