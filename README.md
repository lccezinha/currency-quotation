### Currency Quotations

Just to study Python lang.

### How to use with RateAPI?

```python
quotation = Quotation("USD", "BRL", amount=3.10).get()
print(quotation) # 3.1 USD is equal to 16.55 BRL

quotation = Quotation("EUR", "BRL").get()
print(quotation) # 1.0 EUR is equal to 6.55 BRL

quotation = Quotation("EUR", "USD", amount=2.0).get()
print(quotation) # 2.0 EUR is equal to 2.46 USD
```

### How to use with AwesomeAPI?

```python
quotation = Quotation("USD", "BRL", client=AwesomeAPI, amount=5.1).get()
print(quotation) # 5.1 USD is equal to 26.98 BRL

quotation = Quotation("EUR", "BRL", client=AwesomeAPI).get()
print(quotation) # 1.0 EUR is equal to 6.53 BRL

quotation = Quotation("CAD", "BRL", client=AwesomeAPI).get()
print(quotation) # 1.0 CAD is equal to 4.17 BRL
```
