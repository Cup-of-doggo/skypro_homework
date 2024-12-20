import re


def find_operation(dicts: list[dict], search_string: any = None) -> list[dict]:
    """ищет операцию и возвращает список операций где строка есть"""
    founded_string =[]
    for some_dict in dicts:
        for keys,values in some_dict.items():
            match_value = re.match(fr'{search_string}',str(values),re.I)
            match_key = re.match(fr'{search_string}',str(keys),re.I)
            if match_value or match_key:
                founded_string.append(some_dict)
    return founded_string
