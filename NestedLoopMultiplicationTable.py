number = int(input("Multiplication table for number : "))
time = int(input("How many times? "))

for i in range(time):
    print(number,"x",i+1,"=",number*(i+1))