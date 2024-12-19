import re
from collections import Counter


def operations_count(dicts: list[dict], descriptions: list[any] = None) -> dict:
    keys_list = []
    for some_dict in dicts:
        for keys in some_dict.keys():
            match = re.match(fr'{descriptions}',str(keys), re.I)
            if match:
                keys_list.append(keys)
            else:
                continue
    counted = Counter(keys_list)
    return counted
