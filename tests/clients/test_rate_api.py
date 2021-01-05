from lib.quotation.clients.rate_api import RateAPI

import requests
import requests_mock
import responses


def test_requests_get():
    currency_from = "USD"
    currency_to = "BRL"
    url = (
        f"https://api.ratesapi.io/api/latest?base={currency_from}&symbols={currency_to}"
    )
    response = {"base": "USD", "rates": {"BRL": 5.1432173064}, "date": "2021-01-04"}

    with requests_mock.Mocker() as mock:
        mock.get(url, json=response)
        assert requests.get(url).json() == response


@responses.activate
def test_rate_api_get():
    currency_to = "BRL"
    currency_from = "USD"
    url = (
        f"https://api.ratesapi.io/api/latest?base={currency_from}&symbols={currency_to}"
    )
    response = {"base": "USD", "rates": {"BRL": 5.1432173064}, "date": "2021-01-04"}

    rate_api = RateAPI(currency_from, currency_to)

    responses.add(responses.GET, url, json=response, status=200)

    assert rate_api.get() == "5.14"
