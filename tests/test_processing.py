from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter(test_filter_card):
    assert filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], state='CANCELED') == test_filter_card


def test_sort(test_sort_card):
    assert sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], sort_order=False) == test_sort_card