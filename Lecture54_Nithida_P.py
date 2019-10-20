def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234":
        showMenu()
    else:
        print("Sorry. Wrong username or password. Please try again")
        login()

def showMenu():
    print("------------------------------------------------------------------------")
    print("                           Welcome to my shop                           ")
    print("------------------------------------------------------------------------")
    print("Please choose option below")
    print("Option 1 : Find total price (vat included)")
    print("Option 2 : Put price for 2 products and find total price (vat included)")
    print("------------------------------------------------------------------------")
    selectOption()

def selectOption():
    option = int(input("Option : "))
    if option == 1:
        print("Total price (vat included) :",vatCal(int(input("Price : "))))
        con1()
    elif option == 2:
        print("Total price (vat included) :",priceCal())
        con1()
    else:
        print("Please select either option 1 or 2")
        selectOption()

def con1():
    print("----------------------------------------------------")
    conOp1 = int(input("Do you wish to continue calculation? 1) Yes 2)No : "))
    print("----------------------------------------------------")
    if conOp1 == 1:
        selectOption()
    elif conOp1 == 2:
        print("Thank you :)")
    else:
        print("Please select either option 1 or 2")
        con1()

def vatCal(totalPrice):
    result = totalPrice + totalPrice*7/100
    return result

def priceCal():
    product1 = int(input("Product 1 = "))
    product2 = int(input("Product 2 = "))
    totalPrice = product1+product2
    print("Total price : ",float(totalPrice))
    print("VAT 7% :",totalPrice*7/100)
    return vatCal(totalPrice)

login()