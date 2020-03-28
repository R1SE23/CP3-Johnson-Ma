def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
totalprice = float(input('Price: '))
print(vatCalculate(totalprice))sss