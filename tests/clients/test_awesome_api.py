from lib.quotation.clients.awesome_api import AwesomeAPI

import requests
import requests_mock
import responses


def test_requests_get():
    currency_from = "USD"
    currency_to = "BRL"
    url = f"https://economia.awesomeapi.com.br/all/{currency_from}-{currency_to}"
    response = {
        "USD": {
            "code": "USD",
            "codein": "BRL",
            "name": "Dólar Comercial",
            "high": "5.3543",
            "low": "5.2748",
            "varBid": "0.0104",
            "pctChange": "0.2",
            "bid": "5.3062",
            "ask": "5.3082",
            "timestamp": "1609865640",
            "create_date": "2021-01-05 13:54:59",
        }
    }

    with requests_mock.Mocker() as mock:
        mock.get(url, json=response)
        assert requests.get(url).json() == response


@responses.activate
def test_awesome_api_get():
    currency_to = "BRL"
    currency_from = "USD"
    url = f"https://economia.awesomeapi.com.br/all/{currency_from}-{currency_to}"
    response = {
        "USD": {
            "code": "USD",
            "codein": "BRL",
            "name": "Dólar Comercial",
            "high": "5.3543",
            "low": "5.2748",
            "varBid": "0.0104",
            "pctChange": "0.2",
            "bid": "5.3062",
            "ask": "5.3082",
            "timestamp": "1609865640",
            "create_date": "2021-01-05 13:54:59",
        }
    }

    awesome_api = AwesomeAPI(currency_from, currency_to)

    responses.add(responses.GET, url, json=response, status=200)

    assert awesome_api.get() == "5.31"
