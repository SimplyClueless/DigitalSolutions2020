import random
from guizero import App, Picture, PushButton, Window, Text, TextBox, Box

cardList = [
    ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1],
    ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1], ["Diamonds", 1],
    ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1],
    ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1], ["Hearts", 1],
    ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1],
    ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1], ["Clubs", 1],
    ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1],
    ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1], ["Spades", 1],
    ]
isGameAddition = True

app = App()
app.hide()

#---Start Opening Window---#
startWindow = Window(app, title="Start Window", layout="grid")
startWindow.width = 1280
startWindow.height = 720
startWindow.bg = "Lime"

playerButtonContainer = Box(startWindow, layout="grid", grid=[0, 0], align="top", border=True)
playerButtonContainer.set_border(10, "Lime")
buttonOnePlayer = PushButton(playerButtonContainer, text="1 Player", grid=[1, 0])
buttonOnePlayer.width = 20
buttonOnePlayer.height = 10
buttonOnePlayer.bg = "White"
buttonTwoPlayer = PushButton(playerButtonContainer, text="2 Player", grid=[2, 0])
buttonTwoPlayer.width = 20
buttonTwoPlayer.height = 10
buttonTwoPlayer.bg = "White"

gamemodeButtonContainer = Box(startWindow, layout="grid", grid=[0, 1], align="top", border=True)
gamemodeButtonContainer.set_border(10, "Lime")
buttonAddition = PushButton(gamemodeButtonContainer, text="Addition", grid=[1, 0])
buttonAddition.width = 20
buttonAddition.height = 10
buttonAddition.bg = "White"
buttonSubtraction = PushButton(gamemodeButtonContainer, text="Subtraction", grid=[2, 0])
buttonSubtraction.width = 20
buttonSubtraction.height = 10
buttonSubtraction.bg = "White"

finalCheck = Box(startWindow, layout="grid", grid=[0, 2], align="top", border=True)
finalCheck.set_border(10, "Lime")
gameInformation = Text(finalCheck, text="Game Information Here", grid=[0, 1])
buttonStart = PushButton(finalCheck, text="Start!", grid=[0, 2])
buttonStart.width = 20
buttonStart.height = 5
buttonStart.bg = "White"
#---End Opening Window---#

#---Start One Player Addition---#
#---End One Player Addition---#

#---Start Two Player Addition---#
#---End Two Player Addition---#

#---Start One Player Subtraction---#
#---End One Player Subtraction---#

#---Start Two Player Subtraction---#
#---End Two Player Subtraction---#

app.display()
