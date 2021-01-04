from lib.quotation.clients.rate_api import RateAPI

@responses.activate
def test_get():
    currency_to = "USD"
    currency_from = "BRL"
    rate_api = RateAPI(currency_from, currency_to)

    assert rate_api.get() == 2
