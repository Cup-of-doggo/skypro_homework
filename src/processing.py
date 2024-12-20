def filter_by_state(dict_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей, фильтрует по ключевому слову и возвращает новый список"""
    new_dict_list = []
    for some_dict in dict_list:
        if some_dict.get('state') == state:
            new_dict_list.append(some_dict)
    return new_dict_list



def sort_by_date(new_dict_list: list[dict], sort_order: bool = True) -> list[dict]:
    """Функция принимает список словарей и сортирует его(по умолчанию по убыванию) """
    for dict_list in new_dict_list:
        if dict_list.get('date') is True:
            if sort_order is True:
               sorted_list = sorted(new_dict_list, key=lambda index: index.get('date'), reverse=True)
            else:
                sorted_list = sorted(new_dict_list, key=lambda index: index.get('date'), reverse=False)
            return sorted_list
