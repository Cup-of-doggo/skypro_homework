
from time import strftime
from functools import wraps


def log(func):
    #def inner(func):
        @wraps(func)
        def wrapper(arg):
            try:
                time_1 = strftime('%H:%M:%S')
                print(f'Начало работы фунции {time_1}')
                result = func(arg)
                time_2 = strftime('%H:%M:%S')
                print(f'Конец работы функции {time_2}')
                print(f'{func.__name__} все ок \nРезультат: {result}')
                return result
            except Exception as err:
                return print(f'{func.__name__} Ошибка {err}\nВходные параметры {arg}')
        return wrapper
    #return inner



