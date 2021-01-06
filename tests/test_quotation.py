import pytest
from lib.quotation.quotation import Quotation


class ClientMock:
    def __init__(self, currency_from, currency_to):
        self.currency_from = currency_from
        self.currency_to = currency_to

    def get(self):
        return "3.33"


@pytest.fixture
def api_client():
    return ClientMock


def test_quotation_with_client(api_client):
    quotation = Quotation("BRL", "USD", client=api_client)
    assert quotation.get() == "1.0 BRL is equal to 3.33 USD"


def test_valid_quotation_instance():
    assert Quotation("BRL", "USD")
    assert Quotation("BRL", "USD", amount=1.0)
    assert Quotation("USD", "BRL")
    assert Quotation("USD", "BRL", amount=1.0)


# current_from tests


def test_currency_from_must_be_string():
    with pytest.raises(AttributeError) as error:
        assert Quotation(1, "")
    assert str(error.value) == "currency_from must be a string"


def test_currency_from_must_valid():
    with pytest.raises(AttributeError) as error:
        assert Quotation("XPTO", "USD")
    assert (
        str(error.value)
        == "the given XPTO currency is not available, available_currencies are ['BRL', 'USD']"
    )


def test_currency_from_must_not_be_blank():
    with pytest.raises(AttributeError) as error:
        assert Quotation("", "BRL")
    assert str(error.value) == "currency_from must not be blank"


# currency_to tests


def test_currency_to_must_be_string():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", 1)
    assert str(error.value) == "currency_to must be a string"


def test_currency_from_must_valid():
    with pytest.raises(AttributeError) as error:
        assert Quotation("USD", "XXX")
    assert (
        str(error.value)
        == "the given XXX currency is not available, available_currencies are ['BRL', 'USD']"
    )


def test_currency_to_must_not_be_blank():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "")
    assert str(error.value) == "currency_to must not be blank"


# amount tests


def test_amount_must_be_positive_float():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "USD", amount=-1.1)
    assert str(error.value) == "amount must not be negative"


# other tests


def test_currencies_must_not_be_equal():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "BRL")
    assert str(error.value) == "currencies must not be equals"


# get() tests


def test_get_with_valid_data_must_return_quotation(api_client):
    assert (
        Quotation("USD", "BRL", client=api_client).get()
        == "1.0 USD is equal to 3.33 BRL"
    )
