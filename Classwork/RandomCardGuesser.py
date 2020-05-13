import random
from guizero import App, Picture, PushButton, Window, Text, TextBox

app = App(layout="grid")
window = Window(app, title="Second Window", layout="grid")
window2 = Window(app, title="Third Window", layout="grid")
window.hide()
window2.hide()

cardScore1 = 0
cardScore2 = 0
cardScore3 = 0
cardScore4 = 0

cardList = list(range(1, 53)) #Creates list of 52 integers

def RandomiseCard():
    checkButton = PushButton(app, text="Check Score...", grid=[0, 6], command=CheckScore)
    random.shuffle(cardList) #Randomly shuffles list
    cardNumber1 = cardList[0] #Select item zero from list
    cardNumber2 = cardList[1]
    cardNumber3 = cardList[2]
    cardNumber4 = cardList[3]
    cardList.remove(cardNumber1)
    cardList.remove(cardNumber2)
    cardList.remove(cardNumber3)
    cardList.remove(cardNumber4)

    # First card scores
    if cardNumber1 > 13 and cardNumber1 < 27:
        cardScore1 = cardNumber1 - 13
        print(cardScore1)
    if cardNumber1 > 26 and cardNumber1 < 40:
        cardScore1 = cardNumber1 - 26
        print(cardScore1)
    if cardNumber1 > 39:
        cardScore1 = cardNumber1 - 39
        print(cardScore1)
    if cardNumber1 <= 13:
        cardScore1 = cardNumber1
        print(cardScore1)

    # Second card scores
    if cardNumber2 > 13 and cardNumber2 < 27:
        cardScore2 = cardNumber2 - 13
        print(cardScore2)
    if cardNumber2 > 26 and cardNumber2 < 40:
        cardScore2 = cardNumber2 - 26
        print(cardScore2)
    if cardNumber2 > 39:
        cardScore2 = cardNumber2 - 39
        print(cardScore2)
    if cardNumber2 <= 13:
        cardScore2 = cardNumber2
        print(cardScore2)

    # Third card scores
    if cardNumber3 > 13 and cardNumber3 < 27:
        cardScore3 = cardNumber3 - 13
        print(cardScore3)
    if cardNumber3 > 26 and cardNumber3 < 40:
        cardScore3 = cardNumber3 - 26
        print(cardScore3)
    if cardNumber3 > 39:
        cardScore3 = cardNumber3 - 39
        print(cardScore3)
    if cardNumber3 <= 13:
        cardScore3 = cardNumber3
        print(cardScore3)

    # Fourth card scores
    if cardNumber4 > 13 and cardNumber4 < 27:
        cardScore4 = cardNumber4 - 13
        print(cardScore4)
    if cardNumber4 > 26 and cardNumber4 < 40:
        cardScore4 = cardNumber4 - 26
        print(cardScore4)
    if cardNumber4 > 39:
        cardScore4 = cardNumber4 - 39
        print(cardScore4)
    if cardNumber4 <= 14:
        cardScore4 = cardNumber4
        print(cardScore4)

    global addedScores
    addedScores = cardScore1 + cardScore2 + cardScore3 + cardScore4

    CardImage1 = Picture(app, image="PlayingCards/" + str(cardNumber1) + ".png", grid=[0, 1])
    CardImage2 = Picture(app, image="PlayingCards/" + str(cardNumber2) + ".png", grid=[0, 2])
    CardImage3 = Picture(app, image="PlayingCards/" + str(cardNumber3) + ".png", grid=[1, 1])
    CardImage4 = Picture(app, image="PlayingCards/" + str(cardNumber4) + ".png", grid=[1, 2])

    if len(cardList) == 0:
        window.show()
        window2.show()
        app.hide()

def CheckScore():
    if guess.value == "":
        errorText = Text(app, text="Enter a number in the text box!", grid=[0, 5])
    if guess.value == str(addedScores):
        score = Text(app, text="Score is " + str(addedScores), grid=[0, 3])
        answerText = Text(app, text="The guess was correct!", grid=[0, 5])
    if guess.value != str(addedScores):
        score = Text(app, text="Score is " + str(addedScores), grid=[0, 3])
        answerText = Text(app, text="Sorry, that guess was not correct!", grid=[0, 5])


button = PushButton(app, text="Draw!", command=RandomiseCard, grid=[0, 0])
global text
global guess
text = Text(app, text="Enter your score guess here: ", grid=[0, 4])
guess = TextBox(app, grid=[1, 4])
global errorText

app.display()
