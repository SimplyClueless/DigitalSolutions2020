num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def NumberChecker(x, y):
    if (x > y):
        print(x, "is greater than", y)
    if (y > x):
        print(y, "is greater than", x)
    if (x == y):
        print("They are the same number")

NumberChecker(num1, num2)