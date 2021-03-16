from lib.quotation.quotation import Quotation
from lib.quotation.clients import RateAPI, AwesomeAPI

if "__main__" == __name__:
    print("RateAPI")

    quotation = Quotation("USD", "BRL").get()
    print(quotation)

    quotation = Quotation("USD", "BRL", amount=3.10).get()
    print(quotation)

    quotation = Quotation("EUR", "BRL").get()
    print(quotation)

    quotation = Quotation("EUR", "USD", amount=2.0).get()
    print(quotation)

    print("")

    print("AwesomeAPI")

    quotation = Quotation("USD", "BRL", client=AwesomeAPI).get()
    print(quotation)

    quotation = Quotation("USD", "BRL", client=AwesomeAPI, amount=5.1).get()
    print(quotation)

    quotation = Quotation("EUR", "BRL", client=AwesomeAPI).get()
    print(quotation)

    quotation = Quotation("CAD", "BRL", client=AwesomeAPI).get()
    print(quotation)
