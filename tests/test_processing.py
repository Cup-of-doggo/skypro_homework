from src.processing import filter_by_state, sort_by_date


def test_filter(test_filter_card):
    assert filter_by_state([
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
          state='CANCELED') == test_filter_card


def test_sort(test_sort_card):
    assert sort_by_date([
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        },
        {
            "id": 476991061,
            "state": "CANCELED",
            "date": "2018-11-23T17:47:33.127140",
            "operationAmount": {
                "amount": "26971.25",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }}
], sort_order=False) == None
