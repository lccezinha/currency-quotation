import requests


class RateAPI:
    """
    Wrapper for RateAPI get endpoint.
    """
    __base_url = "https://api.ratesapi.io/api/latest"

    def __init__(self, currency_from, currency_to):
        self.currency_from = currency_from
        self.currency_to = currency_to

    def get(self) -> str:
        """
        Gets the currency currency_from -> currency_to
        """
        url = f"{self.__base_url}?base={self.currency_from}&symbols={self.currency_to}"
        rates = requests.get(url).json()["rates"][self.currency_to]

        return f"%.2f" % rates
