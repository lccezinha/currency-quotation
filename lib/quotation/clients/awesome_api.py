import requests
from decimal import Decimal


class AwesomeAPI:
    __base_url = "https://economia.awesomeapi.com.br/all/"

    def __init__(self, currency_from, currency_to):
        self.currency_from = currency_from
        self.currency_to = currency_to

    def get(self):
        url = f"{self.__base_url}{self.currency_from}-{self.currency_to}"
        rates = requests.get(url).json()[self.currency_from]["bid"]

        return f"%.2f" % Decimal(rates)
