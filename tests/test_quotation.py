import pytest
from lib.quotation.quotation import Quotation


def test_valid_quotation_instance():
    assert Quotation("BRL", "USD")
    assert Quotation("BRL", "USD", 1.0)
    assert Quotation("USD", "BRL")
    assert Quotation("USD", "BRL", 1.0)


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
        assert Quotation("BRL", "USD", -1.1)
    assert str(error.value) == "amount must not be negative"


# other tests


def test_currencies_must_not_be_equal():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "BRL")
    assert str(error.value) == "currencies must not be equals"


# get() tests


def test_get_with_valid_data_must_return_quotation():
    assert Quotation("USD", "BRL").get() == "1 USD is equal to 5.2 BRL"
