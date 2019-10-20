def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print("Total Price (vat included) :",vatCalculate(float(input("Please put the price here : "))))