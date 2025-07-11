pkr = float(input("Enter amount in PKR: "))
currency = input("Convert to (usd / eur / sar): ")
if currency == "usd":
    print("In USD:", pkr / 278)
elif currency == "eur":
    print("In EUR:", pkr / 300)
elif currency == "sar":
    print("In SAR:", pkr / 74)
else:
    print("Currency not supported.")