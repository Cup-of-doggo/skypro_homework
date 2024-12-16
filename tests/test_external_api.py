from unittest.mock import patch
from src.external_api import convert

trans = [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


@patch('requests.request')
def test_convert(mock_get):
    mock_get.return_value.json.return_value = {'info': {'rate': "8221.37"}}
    assert convert(trans) == "8221.37"
