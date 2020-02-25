month: int = int(input("Enter your number: "))

if month >= 0:
    print("First Quarter")

if month >= 3:
    print("Second Quarter")

if month >= 6:
    print("Third Quarter")

if month >= 9:
    print("Fourth Quarter")

else:
    print("ERROR")