from functools import wraps
import os


def log(filename=None):
    """выводит имя функции и тип ошибки(при наличии) в файл(или консоль, если файл не указан)"""
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:

                if filename is None:
                    result = func(*args, **kwargs)
                    print(f'{func.__name__} все ок \nРезультат: {result}')
                    return result
                elif filename is not None:
                    result = func(args, kwargs)
                    with open(os.path.abspath(filename), "a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} все ок \nРезультат: {result}')
                        return result

            except Exception as err:

                if filename is None:
                    return print(f'{func.__name__} Ошибка {err}\nВходные параметры {args}, {kwargs}')
                elif filename is not None:
                    with open(os.path.abspath(filename), "a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} Ошибка {err}\nВходные параметры {args}, {kwargs}')

        return wrapper
    return inner
