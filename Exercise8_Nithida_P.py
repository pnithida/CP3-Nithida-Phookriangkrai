username = input("Username : ")
password = input("Password : ")

if username == "customer" and password == "xyz1":
    print("----------Welcome to My Shop----------")
    print("Menu")
    print("--------------------------------------")
    print("Pencil              ", 5, " THB/pc")
    print("Blue Pen            ", 10, "THB/pc")
    print("Red Pen             ", 10, "THB/pc")
    print("Black Pen           ", 10, "THB/pc")
    print("Eraser              ", 8, " THB/pc")
    print("Ruler               ", 12, "THB/pc")
    print("--------------------------------------")
    print("How many quantity do you want?")
    pencil = int(input(  "Pencil        : "))
    bluePen = int(input( "Blue Pen      : "))
    redPen = int(input(  "Red Pen       : "))
    blackPen = int(input("Black Pen     : "))
    eraser = int(input(  "Eraser        : "))
    ruler = int(input(   "Ruler         : "))
    print("--------------------------------------")
    total = pencil*5 + bluePen*10 + redPen*10 + blackPen*10 + eraser*8 + ruler*12
    print("Total                        :", total, "THB")
    vat = total*7/100
    print("VAT 7%                       :", vat, "THB")
    print("Total (VAT included)         :", total+vat, "THB")
    print("--------------------------------------")
    print("Thank you very much.")

else:
    print("Wrong username or password. Please try again.")



