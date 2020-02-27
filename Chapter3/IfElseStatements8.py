import random
RandomNumber = random.randint(0,36)
BinaryNumber = (RandomNumber % 2)

if RandomNumber <= 10:
    if BinaryNumber == 0:
        print("Black", RandomNumber)
    if BinaryNumber == 1:
        print("Red", RandomNumber)

elif RandomNumber <= 18:
    if BinaryNumber == 0:
        print("Red", RandomNumber)
    if BinaryNumber == 1:
        print("Black", RandomNumber)

elif RandomNumber <= 28:
    if BinaryNumber == 0:
        print("Black", RandomNumber)
    if BinaryNumber == 1:
        print("Red", RandomNumber)

elif RandonNumber <= 36:
    if BinaryNumber == 0:
        print("Red", RandomNumber)
    if BinaryNumber == 1:
        print("Black", RandomNumber)

else:
    print("Green", RandomNumber)