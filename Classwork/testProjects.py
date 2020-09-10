num1Entered = False
num2Entered = False

if not num1Entered or not num2Entered:
    while not num1Entered:
        try:
            num1 = int(input("Enter first number: "))
        except:
            print("Invalid Variable!")
        else:
            num1Entered = True

    while not num2Entered:
        try:
            num2 = int(input("Enter second number: "))
        except:
            print("Invalid Variable!")
        else:
            num2Entered = True

print(num1 + num2)