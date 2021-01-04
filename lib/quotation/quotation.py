class Quotation:
    available_currencies = ["USD", "BRL"]

    def __init__(self, currency_from, currency_to, amount=0.0) -> str:
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

        self.currency_from = currency_from
        self.currency_to = currency_to
        self.amount = amount
