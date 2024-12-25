from src.oper_counter import operations_count


def test_operations_count():
    operations_count([{
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
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 7305799447374042",
    "to": "Maestro 3364923093037194"
  }],["to"])
    assert {'operationAmount': 2, 'to': 2}