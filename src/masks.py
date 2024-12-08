import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и выдает засекреченный номер карты(маску)"""
    logger.info('накладываем маску на номер карты')
    try:
        if 'Maestro' in card_number:
            return f"{card_number[:12]} {card_number[12:14]}** **** {card_number[20:]}"
        if 'MasterCard' in card_number:
            return f"{card_number[:15]} {card_number[15:17]}** **** {card_number[23:]}"
        if 'Visa Classic' in card_number:
            return f"{card_number[:17]} {card_number[17:19]}** **** {card_number[25:]}"
        if 'Visa Platinum' in card_number:
            return f"{card_number[:18]} {card_number[18:20]}** **** {card_number[26:]}"
        if 'Visa Gold' in card_number:
            return f"{card_number[:14]} {card_number[14:16]}** **** {card_number[22:]}"
    except Exception as err:
        logger.error(f'Произошла ошибка {err}')
        return f'Произошла ошибка {err}'


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и выдает его маску"""
    logger.info('накладываем маску на номер счета')
    return f"{card_account[0:4]} **{card_account[-4:]}"
