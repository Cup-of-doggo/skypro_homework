import os
import requests
from dotenv import load_dotenv
load_dotenv()


def convert(transactions: list) -> float:
    """возвращает сумму транзакции(переводит транзакцию в рубли при необходимости)"""
    amount = transactions[0]["operationAmount"]["amount"]
    currency = transactions[0]["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        API_KEY = os.getenv('API_KEY')
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            response.json()
            rate = response.json()['info']['rate']
            return float(amount) * float(rate)
