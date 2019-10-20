number = int(input("Number : "))
for x in range(number):
    y = x+1
    print(" "*(number-y),end='')
    print("*"*((x*2)+1))