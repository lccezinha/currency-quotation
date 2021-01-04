import pytest
from lib.quotation.quotation import Quotation


def test_valid_quotation_instance():
    assert Quotation("BRL", "USD")
    assert Quotation("BRL", "USD", 1.0)
    assert Quotation("USD", "BRL")
    assert Quotation("USD", "BRL", 1.0)


def test_currency_from_must_be_string():
    with pytest.raises(AttributeError) as error:
        assert Quotation(1, "")
    assert str(error.value) == "currency_from must be a string"


def test_currency_to_must_be_string():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", 1)
    assert str(error.value) == "currency_to must be a string"


def test_currency_from_must_not_be_blank():
    with pytest.raises(AttributeError) as error:
        assert Quotation("", "BRL")
    assert str(error.value) == "currency_from must not be blank"


def test_currency_to_must_not_be_blank():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "")
    assert str(error.value) == "currency_to must not be blank"


def test_amount_must_be_positive_floart():
    with pytest.raises(AttributeError) as error:
        assert Quotation("BRL", "USD", -1.1)
    assert str(error.value) == "amount must not be negative"
