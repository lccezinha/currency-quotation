class Quotation:
    available_currencies = ["BRL", "USD"]

    def __init__(self, currency_from, currency_to, amount=1.0) -> str:
        self.__check_validations(currency_from, currency_to, amount)

        self.currency_from = currency_from
        self.currency_to = currency_to
        self.amount = amount

    def get(self):
        return f"1 {self.currency_from} is equal to 5.2 {self.currency_to}"

    def __check_validations(self, currency_from, currency_to, amount):
        if not type(currency_from) is str:
            raise AttributeError("currency_from must be a string")

        if not type(currency_to) is str:
            raise AttributeError("currency_to must be a string")

        if not currency_from:
            raise AttributeError("currency_from must not be blank")

        if not currency_to:
            raise AttributeError("currency_to must not be blank")

        if amount < 0:
            raise AttributeError("amount must not be negative")

        if not currency_from in self.available_currencies:
            raise AttributeError(
                f"the given {currency_from} currency is not available, available_currencies are {self.available_currencies}"
            )

        if not currency_to in self.available_currencies:
            raise AttributeError(
                f"the given {currency_to} currency is not available, available_currencies are {self.available_currencies}"
            )

        if currency_from == currency_to:
            raise AttributeError("currencies must not be equals")
