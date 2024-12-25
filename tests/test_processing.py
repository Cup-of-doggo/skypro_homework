from src.processing import filter_by_state, sort_by_date


def test_filter(test_filter_card):
    assert filter_by_state([
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
          state='CANCELED') == test_filter_card

New_list = [{"date": "2018-11-23T17:47:33.127140"},{"date": "2019-12-30T23:10:35.459698"}]


def test_sort(test_sort_card):
    assert (sort_by_date
    ([{"date": "2019-12-30T23:10:35.459698"},{"date": "2018-11-23T17:47:33.127140"},],
     sort_order=False) == New_list)
