from functools import wraps
import os


def log(filename = None):
    """выводит имя функции и тип ошибки(при наличии) в файл(или консоль, если файл не указан)"""
    def inner(func):
        @wraps(func)
        def wrapper(arg,kwarg=None):
            try:

                if filename is None:
                    result = func(arg,kwarg)
                    print(f'{func.__name__} все ок \nРезультат: {result}')
                    return result
                elif filename is not None:
                    result = func(arg,kwarg)
                    with open(os.path.abspath(filename),"a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} все ок \nРезультат: {result}')
                        return result

            except Exception as err:

                if filename is None:
                    return print(f'{func.__name__} Ошибка {err}\nВходные параметры {arg,kwarg}')
                elif filename is not None:
                    with open(os.path.abspath(filename),"a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} Ошибка {err}\nВходные параметры {arg,kwarg}')

        return wrapper
    return inner
