import random

RandomNumber = random.randint(1, 101)
CorrectNumber = False

while CorrectNumber != True:
    UserNumber = int(input("I have picked a number between 1 and 100, guess what it is: "))
    if UserNumber > RandomNumber:
        print("That number is too high, try again!")
    if UserNumber < RandomNumber:
        print("That number is too low, try again!")
    if UserNumber == RandomNumber:
        print("Congratulations! You guessed the number correct!")
        CorrectNumber = True