import random

print("Rock = 1")
print("Paper = 2")
print("Scissors = 3")
PlayerInput = int(input("Enter your choice: "))
AIInput = random.randint(1, 4)

def Scoring(Player, AI):
    if Player == 1:
        if AI == 1:
            print("Game tied!")
        if AI == 2:
            print("Player wins!")
        if AI == 3:
            print("AI wins!")
    if Player == 2:
        if AI == 0:
            print("AI wins!")
        if AI == 1:
            print("Game tied!")
        if AI == 2:
            print("Player wins!")
    if Player == 3:
        if AI == 0:
            print("Player wins!")
        if AI == 1:
            print("AI wins!")
        if AI == 2:
            print("Game tied!")