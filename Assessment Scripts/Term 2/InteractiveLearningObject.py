import random
from PIL import Image
from guizero import App, Picture, PushButton, Window, Text, TextBox, Box

app = App()
app.hide()

isOnePlayer = None
isGameAddition = None

'''
This function is executed at the start of the code and creates startWindow, the main menu for the game.
buttonOnePlayer and buttonTwoPlayer both call the same function SetPlayerNumber, but passes through a boolean and a- 
string to set global variables. Doesn't return any values.
buttonAddition and buttonSubtraction both call the same function SetGameMode, but passes through a boolean and a string- 
to set global variables. Doesn't return any values.
Doesn't return any variables.
'''
def Run():
    global startWindow
    global finalCheck
    global startButton

    startWindow = Window(app, title="Starting Screen", layout="grid")
    startWindow.width = 360; startWindow.height = 630; startWindow.bg = "Lime"

    playersQuestionText = Text(startWindow, text="How Many Players?", grid=[0, 0], align="top")
    playersQuestionText.text_size = 25
    playerButtonContainer = Box(startWindow, layout="grid", grid=[0, 1], align="top", border=True)
    playerButtonContainer.set_border(10, "Lime")
    buttonOnePlayer = PushButton(playerButtonContainer, text="1 Player", grid=[1, 0], command=lambda: SetPlayerNumber(True, "1 Player"))
    buttonOnePlayer.width = 20; buttonOnePlayer.height = 10; buttonOnePlayer.bg = "White";
    buttonTwoPlayer = PushButton(playerButtonContainer, text="2 Player", grid=[2, 0], command=lambda: SetPlayerNumber(False, "2 Player"))
    buttonTwoPlayer.width = 20; buttonTwoPlayer.height = 10; buttonTwoPlayer.bg = "White"

    gameModeQuestionText = Text(startWindow, text="What Game Mode?", grid=[0, 2], align="top")
    gameModeQuestionText.text_size = 25
    gameModeButtonContainer = Box(startWindow, layout="grid", grid=[0, 3], align="top", border=True)
    gameModeButtonContainer.set_border(10, "Lime")
    buttonAddition = PushButton(gameModeButtonContainer, text="Addition", grid=[1, 0], command=lambda: SetGameMode(True, "Addition"))
    buttonAddition.width = 20; buttonAddition.height = 10; buttonAddition.bg = "White"
    buttonSubtraction = PushButton(gameModeButtonContainer, text="Subtraction", grid=[2, 0], command=lambda: SetGameMode(False, "Subtraction"))
    buttonSubtraction.width = 20; buttonSubtraction.height = 10; buttonSubtraction.bg = "White"

    finalCheck = Box(startWindow, layout="grid", grid=[0, 4], align="top", border=True)
    finalCheck.set_border(10, "Lime")
    startButton = PushButton(finalCheck, text="Start!", grid=[0, 2], align="top", command=StartGame)
    startButton.width = 20; startButton.height = 5; startButton.bg = "White"; startButton.disable()

'''
Takes passed through variables playerBool & playerString and sets a global variable and string depending on the passed- 
through variables.
Calls function EnableStartButton.
Doesn't return any variables.
'''
def SetPlayerNumber(playerBool, playerString):
    global isOnePlayer

    isOnePlayer = playerBool
    playerText = Text(finalCheck, text=playerString, grid=[0, 1])

    EnableStartButton()

'''
Takes passed through variables gameModeBool & gameModeString and sets a global variable and string depending on the-
passed through variables.
Calls function EnableStartButton.
Doesn't return any variables.
'''
def SetGameMode(gameModeBool, gameModeString):
    global isGameAddition

    isGameAddition = gameModeBool
    gameModeText = Text(finalCheck, text=gameModeString, grid=[1, 1])

    EnableStartButton()

'''
Check if the variables isOnePlayer & isGameAddition are equal to nothing and if they have a value then activate a-
button created in the Run function.
Doesn't return any variables.
'''
def EnableStartButton():
    global startButton
    global isOnePlayer
    global isGameAddition

    if (isOnePlayer == None or isGameAddition == None):
        startButton.disable()
    else:
        startButton.enable()

'''
Creates 4 lists with integers going from 1 - 13 and then places then in a seperate multidimensional list along with a- 
string based on the different suits.
Shuffles the seperate indexes of the list so the cards are drawn randomly.
Returns the list variable cardList.
'''
def ShuffleCards():
    global cardList

    clubs = list(range(1, 14)); diamonds = list(range(1, 14)); hearts = list(range(1, 14)); spades = list(range(1, 14))
    cardList = [["Clubs", clubs], ["Diamonds", diamonds], ["Hearts", hearts], ["Spades", spades]]
    for i in range(len(cardList)):
        random.shuffle(cardList[i][1])
    # print(cardList)
    return cardList

'''
Checks to see if the cardList index is empty. If it is empty then try and find a different suit that isn't empty.
Sets the cardNumber variables and suit variables then deletes the index so that duplicates cannot occur.
Returns cardNumber & suit.
'''
def RandomCard(suit):
    global cardList

    if (len(cardList[suit][1]) == 0):
        while (len(cardList[suit][1]) == 0):
            suit = random.randint(0, 3)
    cardNumber = cardList[suit][1][0]
    del cardList[suit][1][0]
    # print(cardList)
    return cardNumber, suit

'''
Closes the startWindow created in the Run function.
Sets the variables to their starting values and a function depending on how many players have been chosen-
(StartOnePlayer & StartTwoPlayer).
Doesn't return any variables.
'''
def StartGame():
    global gameRun
    global playerOnePoints
    global playerTwoPoints
    global addedScoresPlayerOne
    global addedScoresPlayerTwo
    global cardList

    startWindow.hide()

    gameRun = 0
    playerOnePoints = 0
    playerTwoPoints = 0
    addedScoresPlayerOne = 0
    addedScoresPlayerTwo = 0

    ShuffleCards()

    if isOnePlayer == True:
        StartOnePlayer()
    elif isOnePlayer != True:
        StartTwoPlayer()

#---Begin One Player---#
'''
Creates onePlayerWindow.
drawButtonOnePlayer calls function ButtonSwapOnePlayer which doesn't have any parameters.
guessCheckButtonOnePlayer calls function CheckValuesOnePlayer which doesn't have any parameters.
Doesn't return any variables.
'''
def StartOnePlayer():
    global onePlayerWindow
    global drawButtonOnePlayer
    global cardImagesOnePlayer
    global guessContainerOnePlayer
    global guessCheckButtonOnePlayer
    global guessTextBoxOnePlayer
    global correctOnePlayer
    global errorTextOnePlayer

    onePlayerWindow = Window(app, title="One Player Game", layout="grid")
    onePlayerWindow.width = 320; onePlayerWindow.height = 560; onePlayerWindow.bg = "Lime"

    drawButtonOnePlayer = PushButton(onePlayerWindow, text="Draw!", grid=[0, 0], align="top", command=ButtonSwapOnePlayer)
    drawButtonOnePlayer.width = 20; drawButtonOnePlayer.height = 5; drawButtonOnePlayer.bg = "White"
    cardImagesOnePlayer = Box(onePlayerWindow, layout="grid", grid=[0, 1], align="top", border=True)
    cardImagesOnePlayer.set_border(10, "Lime")

    guessContainerOnePlayer = Box(onePlayerWindow, layout="grid", grid=[0, 2], align="top", border=True)
    guessContainerOnePlayer.set_border(10, "Lime")
    guessTextBoxOnePlayer = TextBox(guessContainerOnePlayer, grid=[0, 0], align="top")
    guessTextBoxOnePlayer.text_size = 20; guessTextBoxOnePlayer.bg = "White"; guessTextBoxOnePlayer.disable();
    guessCheckButtonOnePlayer = PushButton(guessContainerOnePlayer, text="Check!", grid=[0, 1], align="top", command=CheckValuesOnePlayer)
    guessCheckButtonOnePlayer.width = 20; guessCheckButtonOnePlayer.height = 5; guessCheckButtonOnePlayer.bg = "White"; guessCheckButtonOnePlayer.disable();
    pointsTextOnePlayer = Text(guessContainerOnePlayer, text="Score: ", grid=[0, 2], align="top")

    correctOnePlayer = Text(onePlayerWindow, text="", grid=[0, 3])
    errorTextOnePlayer = Text(onePlayerWindow, text="Please enter a number!", grid=[0, 4])
    errorTextOnePlayer.hide()

'''
Disables drawButtonOnePlayer so the player cannot continually draw cards from the deck.
Enables guessTextBoxOnePlayer and clears any values previously in it so players can input their answer.
Enables guessCheckButtonOnePlayer so they can run the function to check their answers.
Doesn't return any variables.
'''
def ButtonSwapOnePlayer():
    OnePlayer()
    drawButtonOnePlayer.disable()
    guessTextBoxOnePlayer.enable()
    guessTextBoxOnePlayer.clear()
    guessCheckButtonOnePlayer.enable()

'''
Assigns a random number ranging from 0 - 3 to the variables suit1 and suit2.
Assigns the return value of the function RandomCard to cardNumber1 and suit1 with the passed parameter of suit1.
Assigns the return value of the function RandomCard to cardNumber2 and suit2 with the passed parameter or suit2.
Checks if the gameMode is addition or subtraction and does the required equation to the 2 cardNumber variables.
Displays cardImage1 and cardImage2 depending on the suit string from the cardList and the cardNumber variables.
Doesn't return any variables.
'''
def OnePlayer():
    global suit1
    global suit2
    global isGameAddition
    global addedScoresPlayerOne

    suit1 = random.randint(0, 3); suit2 = random.randint(0, 3)
    # print("First suit is " + str(suit1)); print("Second suit is " + str(suit2))

    cardNumber1, suit1 = RandomCard(suit1); cardNumber2, suit2 = RandomCard(suit2)
    # print("first card is " + str(cardNumber1)); print("second card is " + str(cardNumber2))
    # print("CardnNumber1 suit number is " + str(suit1)); print("CardNumber2 suit number is " + str(suit2))

    if (isGameAddition == True):
        addedScoresPlayerOne = cardNumber1 + cardNumber2
    elif (isGameAddition != True):
        addedScoresPlayerOne = cardNumber1 - cardNumber2
    # print(addedScoresPlayerOne)

    cardImage1 = Picture(cardImagesOnePlayer, image="PlayingCards/" + str(cardList[suit1][0]) + "/" + str(cardNumber1) + ".png", grid=[0, 0])
    cardImage1.width = 144; cardImage1.height = 192
    cardImage2 = Picture(cardImagesOnePlayer, image="PlayingCards/" + str(cardList[suit2][0]) + "/" + str(cardNumber2) + ".png", grid=[1, 0])
    cardImage2.width = 144; cardImage2.height = 192

'''
Checks if the guessTextBoxOnePlayer value is empty or not a number. If true then display and error message.
Checks if the addedScoresPlayerOne variable is or isn't equal to the guessTextBoxOnePlayer value and then calls the- 
ScoresOnePlayer function with a different string and integer parameter.
If the variables gameRun is equal to 26 then run the function EndScreens as 26 is the maximum number of times the- 
player should be allowed to draw.
Doesn't return any variables.
'''
def CheckValuesOnePlayer():
    global playerOnePoints
    global gameRun

    if (guessTextBoxOnePlayer.value == "" or guessTextBoxOnePlayer.value.lstrip("-").isdigit() != True):
        errorTextOnePlayer.show()
        correctOnePlayer.hide()
    else:
        if (guessTextBoxOnePlayer.value == str(addedScoresPlayerOne)):
            ScoresOnePlayer("Correct!", 1)
        elif (guessTextBoxOnePlayer.value != str(addedScoresPlayerOne)):
            ScoresOnePlayer("Incorrect! Draw some more cards!", 0)

    if (gameRun == 26):
        EndScreens()

'''
Enables drawButtonOnePlayer so the player can draw another hand of cards from the deck.
Disables guessCheckButtonOnePlayer so the player can't continually gain points from the same answer.
Displays correctOnePlayer with the string parameter passed when calling the function.
Adds the passed through integer to the playerOnePoints variable then displays playerOnePointsText showing the-
playerOnePoints variable.
Increments the variables gameRun by 1.
Doesn't return any variables.
'''
def ScoresOnePlayer(outcome, addedPoints):
    global correctOnePlayer
    global playerOnePoints
    global gameRun

    drawButtonOnePlayer.enable()
    guessCheckButtonOnePlayer.disable()
    errorTextOnePlayer.hide()
    correctOnePlayer.hide()
    correctOnePlayer = Text(guessContainerOnePlayer, text=outcome, grid=[0, 4])
    playerOnePoints += addedPoints
    gameRun += 1
    playerOnePointsText = Text(guessContainerOnePlayer, text=playerOnePoints, grid=[1, 2])

'''
Creates endOnePlayerWindow.
Displays how many points the player got out of the maximum points that could have gotten.
restartButton calls the function RestartGame which... restarts the game.
Doesn't return any variables.
'''
def EndScreenOnePlayer():
    global endOnePlayerWindow
    global playerOnePoints

    endOnePlayerWindow = Window(app, title="One Player End Screen", layout="grid")
    endOnePlayerWindow.width = 300; endOnePlayerWindow.height = 300; endOnePlayerWindow.bg = "Lime"

    gameOverOnePlayer = Text(endOnePlayerWindow, text="Game Over!", grid=[0, 0], align="top")
    gameOverOnePlayer.text_size = 40
    yourScoreTextOnePlayer = Text(endOnePlayerWindow, text="Your Score", grid=[0, 1], align="top")
    yourScoreTextOnePlayer.text_size = 20
    displayedScoreOnePlayer = Text(endOnePlayerWindow, text=playerOnePoints, grid=[0, 2], align="top")
    displayedScoreOnePlayer.text_size = 30
    outOfOnePlayer = Text(endOnePlayerWindow, text="Out Of", grid=[0, 3], align="top")
    outOfOnePlayer.text_size = 20
    onePlayerMaxScore = Text(endOnePlayerWindow, text="26", grid=[0, 4], align="top")
    onePlayerMaxScore.text_size = 30

    restartButton = PushButton(endOnePlayerWindow, grid=[0, 5], text="Play Again", align="top", command=RestartGame)
    restartButton.bg = "White"

#---End One Player---#

#---Begin Two Player---#

'''
Creates twoPlayerWindow
drawButtonTwoPlayer calls function ButtonSwapTwoPlayer which doesn't have any parameters.
guessCheckButtonTwoPlayer calls the function CheckValuesTwoPlayer which doesn't have any parameters.
Doesn't return any variables.
'''
def StartTwoPlayer():
    global twoPlayerWindow
    global drawButtonTwoPlayer
    global cardImagesTwoPlayer1
    global cardImagesTwoPlayer2
    global guessContainerTwoPlayer1
    global guessContainerTwoPlayer2
    global guessTextBoxTwoPlayer1
    global guessTextBoxTwoPlayer2
    global guessCheckButtonTwoPlayer
    global correctTwoPlayer1
    global correctTwoPlayer2
    global errorTextTwoPlayer

    twoPlayerWindow = Window(app, title="Two Player Game", layout="grid")
    twoPlayerWindow.width = 660; twoPlayerWindow.height = 570; twoPlayerWindow.bg = "Lime"

    drawButtonTwoPlayer = PushButton(twoPlayerWindow, text="Draw!", grid=[0, 0], align="top", padx=20, command=ButtonSwapTwoPlayer)
    drawButtonTwoPlayer.width = 20; drawButtonTwoPlayer.height = 5; drawButtonTwoPlayer.bg = "White"
    cardImagesTwoPlayer1 = Box(twoPlayerWindow, layout="grid", grid=[0, 1], align="top", border=True)
    cardImagesTwoPlayer1.set_border(5, "Lime")
    cardImagesTwoPlayer2 = Box(twoPlayerWindow, layout="grid", grid=[1, 1], align="top", border=True)
    cardImagesTwoPlayer2.set_border(5, "Lime")

    guessContainerTwoPlayer1 = Box(twoPlayerWindow, layout="grid", grid=[0, 2], align="top", border=True)
    guessContainerTwoPlayer1.set_border(10, "Lime")
    guessTextBoxTwoPlayer1 = TextBox(guessContainerTwoPlayer1, grid=[0, 0], align="top")
    guessTextBoxTwoPlayer1.text_size = 20; guessTextBoxTwoPlayer1.bg = "White"; guessTextBoxTwoPlayer1.disable()
    guessContainerTwoPlayer2 = Box(twoPlayerWindow, layout="grid", grid=[1, 2], align="top", border=True)
    guessContainerTwoPlayer2.set_border(10, "Lime")
    guessTextBoxTwoPlayer2 = TextBox(guessContainerTwoPlayer2, grid=[0, 0], align="top")
    guessTextBoxTwoPlayer2.text_size = 20; guessTextBoxTwoPlayer2.bg = "White"; guessTextBoxTwoPlayer2.disable()

    pointsTextTwoPlayer1 = Text(guessContainerTwoPlayer1, text="Player One Score: ", grid=[0, 2], align="top")
    pointsTextTwoPlayer2 = Text(guessContainerTwoPlayer2, text="Player Two Score: ", grid=[0, 2], align="top")

    guessCheckButtonTwoPlayer = PushButton(twoPlayerWindow, text="Check!", grid=[0, 3], align="top", command=CheckValuesTwoPlayer)
    guessCheckButtonTwoPlayer.width = 20; guessCheckButtonTwoPlayer.height = 5; guessCheckButtonTwoPlayer.bg = "White"; guessCheckButtonTwoPlayer.disable()

    correctTwoPlayer1 = Text(guessContainerTwoPlayer1, text="", grid=[0, 3])
    correctTwoPlayer2 = Text(guessContainerTwoPlayer2, text="", grid=[0, 3])
    errorTextTwoPlayer = Text(twoPlayerWindow, text="Please Enter a Number!", grid=[0, 4])
    errorTextTwoPlayer.hide()

'''
Disables drawButtonTwoPlayer so the player cannot continually draw cards from the deck.
Enables guessTextBoxTwoPlayer1 and guessTextBoxTwoPlayer2 and clear any values previously in them so players can input-
their answers.
Enables guessCheckButtonTwoPlayer so they can run the function to check their answers.
Doesn't return any variables.
'''
def ButtonSwapTwoPlayer():
    TwoPlayer()
    drawButtonTwoPlayer.disable()
    guessTextBoxTwoPlayer1.enable()
    guessTextBoxTwoPlayer1.clear()
    guessTextBoxTwoPlayer2.enable()
    guessTextBoxTwoPlayer2.clear()
    guessCheckButtonTwoPlayer.enable()

'''
Assigns a random number ranging from 0 - 3 to the variables suit1, suit2, suit3 and suit4.
Assigns the return values of the function RandomCard to cardNumber1 and suit1 with the passed parameter of suit1.
Assigns the return values of the function RandomCard to cardNumber2 and suit2 with the passed parameter of suit2.
Assigns the return values of the function RandomCard to cardNumber3 and suit3 with the passed parameter of suit3.
Assigns the return values of the function RandomCard to cardNumber4 and suit4 with the passed parameter of suit4.
Checks if the gameMode is addition or subtraction and does the required equation to the 2 cardNumber variables assigned-
to each player.
Displays cardImage1, cardImage2, cardImage3 and cardImage4 depending on the suit string from the cardList and the- 
cardNumber variables.
Doesn't return any variables.
'''
def TwoPlayer():
    global suit1
    global suit2
    global suit3
    global suit4
    global isGameAddition
    global addedScoresPlayerOne
    global addedScoresPlayerTwo

    suit1 = random.randint(0, 3); suit2 = random.randint(0, 3);
    # print("First suit1 is " + str(suit1)); print("Second suit2 is " + str(suit2))
    suit3 = random.randint(0, 3); suit4 = random.randint(0, 3)
    # print("Third suit3 is " + str(suit3)); print("Fourth suit4 is " + str(suit4))

    cardNumber1, suit1 = RandomCard(suit1); cardNumber2, suit2 = RandomCard(suit2)
    # print("first card is " + str(cardNumber1)); print("second card is " + str(cardNumber2))
    # print("CardnNumber1 suit number is " + str(suit1)); print("CardNumber2 suit number is " + str(suit2))
    cardNumber3, suit3 = RandomCard(suit3); cardNumber4, suit4 = RandomCard(suit4)
    # print("third card is " + str(cardNumber3)); print("fourth card is " + str(cardNumber4))
    # print("CardnNumber3 suit number is " + str(suit3)); print("CardNumber4 suit number is " + str(suit4))

    if (isGameAddition == True):
        addedScoresPlayerOne = cardNumber1 + cardNumber2
        addedScoresPlayerTwo = cardNumber3 + cardNumber4
    elif (isGameAddition != True):
        addedScoresPlayerOne = cardNumber1 - cardNumber2
        addedScoresPlayerTwo = cardNumber3 - cardNumber4
    #print(addedScoresPlayerOne); print(addedScoresPlayerTwo)

    cardImage1 = Picture(cardImagesTwoPlayer1, image="PlayingCards/" + str(cardList[suit1][0]) + "/" + str(cardNumber1) + ".png", grid=[0, 0])
    cardImage1.width = 144; cardImage1.height = 192
    cardImage2 = Picture(cardImagesTwoPlayer1, image="PlayingCards/" + str(cardList[suit2][0]) + "/" + str(cardNumber2) + ".png", grid=[1, 0])
    cardImage2.width = 144; cardImage2.height = 192

    cardImage3 = Picture(cardImagesTwoPlayer2, image="PlayingCards/" + str(cardList[suit3][0]) + "/" + str(cardNumber3) + ".png", grid=[3, 0])
    cardImage3.width = 144; cardImage3.height = 192
    cardImage4 = Picture(cardImagesTwoPlayer2, image="PlayingCards/" + str(cardList[suit4][0]) + "/" + str(cardNumber4) + ".png", grid=[4, 0])
    cardImage4.width = 144; cardImage4.height = 192

'''
Checks if the guessTextBoxTwoPlayer1 or guessTextBoxTwoPlayer2 values is empty or not equal to a number. If true then-
display an error message.
Checks if the addedScoresPlayerOne variable is or isn't equal to the guessTextBoxTwoPlayer1 values and then calls the-
ScoresTwoPlayer1 function with a different string and integer parameter.
Checks if the addedScoresPlayerTwo variable is or isn't equal to the guessTextBoxTwoPlayer2 values and then calls the-
ScoresTwoPlayer2 function with a different string and integer parameter.
If the variables gameRun is equal to 26 then run the function EndScreens as 26 is the maximum number of cards each-
player should be allowed to draw.
Doesn't return any variables.
'''
def CheckValuesTwoPlayer():
    global playerOnePoints
    global playerTwoPoints
    global gameRun

    if (guessTextBoxTwoPlayer1.value == "" or guessTextBoxTwoPlayer2.value == "" or guessTextBoxTwoPlayer1.value.lstrip("-").isdigit() != True or guessTextBoxTwoPlayer2.value.lstrip("-").isdigit() != True):
        errorTextTwoPlayer.show()
        correctTwoPlayer1.hide()
        correctTwoPlayer2.hide()
    else:
        for i in range(2):
            if (i == 0):
                if (guessTextBoxTwoPlayer1.value == str(addedScoresPlayerOne)):
                    ScoresTwoPlayer1("Correct!", 1)
                elif (guessTextBoxTwoPlayer1.value != str(addedScoresPlayerOne)):
                    ScoresTwoPlayer1("Incorrect!", 0)
            else:
                if (guessTextBoxTwoPlayer2.value == str(addedScoresPlayerTwo)):
                    ScoresTwoPlayer2("Correct!", 1)
                elif (guessTextBoxTwoPlayer2.value != str(addedScoresPlayerTwo)):
                    ScoresTwoPlayer2("Incorrect!", 0)

    if (gameRun == 26):
        EndScreens()

'''
Enables drawButtonTwoPlayer so the players can draw another hand of cards from the deck.
Disables guessCheckButtonTwoPlayer so the players can't continually gain points from the same answers.
Displays correctTwoPlayer1 with the string parameter passed when calling the function.
Adds the passed through integer to playerOnePoints variables then displays playerOnePointsText showing the-
playerOnePoints variable.
Increments the variable gameRun by 1
Doesn't return any variables.
'''
def ScoresTwoPlayer1(outcome, addedPoints):
    global correctTwoPlayer1
    global playerOnePoints
    global gameRun

    drawButtonTwoPlayer.enable()
    guessCheckButtonTwoPlayer.disable()
    errorTextTwoPlayer.hide()
    correctTwoPlayer1.hide()
    correctTwoPlayer1 = Text(guessContainerTwoPlayer1, text=outcome, grid=[0, 4])
    playerOnePoints += addedPoints
    gameRun += 1
    playerTwoPointsText1 = Text(guessContainerTwoPlayer1, text=playerOnePoints, grid=[1, 2])

'''
Enables drawButtonTwoPlayer so the players can draw another hand of cards from the deck.
Disables guessCheckButtonTwoPlayer so the players can't continually gain points from the same answers.
Displays correctTwoPlayer2 with the string parameter passed when calling the function.
Adds the passed through integer to playerTwoPoints variables then displays playerTwoPointsText showing the-
playerTwoPoints variable.
Increments the variable gameRun by 1.
Doesn't return any variables.
'''
def ScoresTwoPlayer2(outcome, addedPoints):
    global correctTwoPlayer2
    global playerTwoPoints
    global gameRun

    drawButtonTwoPlayer.enable()
    guessCheckButtonTwoPlayer.disable()
    errorTextTwoPlayer.hide()
    correctTwoPlayer2.hide()
    correctTwoPlayer2 = Text(guessContainerTwoPlayer2, text=outcome, grid=[0, 4])
    playerTwoPoints += addedPoints
    gameRun += 1
    playerTwoPointsText2 = Text(guessContainerTwoPlayer2, text=playerTwoPoints, grid=[1, 2])

'''
Creates endTwoPlayerWindow.
Displays how many points each player got out of the maximum points they could have gotten.
restartButton calls the function RestartGame which... restarts the game.
Doesn't return any variables.
'''
def EndScreenTwoPlayer():
    global endTwoPlayerWindow
    global playerOnePoints
    global playerTwoPoints

    endTwoPlayerWindow = Window(app, title="Two Player End Screen", layout="grid")
    endTwoPlayerWindow.width = 550; endTwoPlayerWindow.height = 350; endTwoPlayerWindow.bg = "Lime"

    gameOverTwoPlayer = Text(endTwoPlayerWindow, text="Game Over!", grid=[0, 0], align="top")
    gameOverTwoPlayer.text_size = 40
    yourScoreTextTwoPlayer1 = Text(endTwoPlayerWindow, text="Player One Score", grid=[0, 1], align="top")
    yourScoreTextTwoPlayer1.text_size = 20
    displayedScoreTwoPlayer1 = Text(endTwoPlayerWindow, text=playerOnePoints, grid=[0, 2], align="top")
    displayedScoreTwoPlayer1.text_size = 30
    outOfTwoPlayer1 = Text(endTwoPlayerWindow, text="Out of", grid=[0, 3], align="top")
    outOfTwoPlayer1.text_size = 20
    twoPlayerMaxScore1 = Text(endTwoPlayerWindow, text="13", grid=[0, 4], align="top")
    twoPlayerMaxScore1.text_size = 30

    yourScoreTextTwoPlayer2 = Text(endTwoPlayerWindow, text="Player Two Score", grid=[1, 1])
    yourScoreTextTwoPlayer2.text_size = 20
    displayedScoreTwoPlayer2 = Text(endTwoPlayerWindow, text=playerTwoPoints, grid=[1, 2], align="top")
    displayedScoreTwoPlayer2.text_size = 30
    outOfTwoPlayer2 = Text(endTwoPlayerWindow, text="Out of", grid=[1, 3], align="top")
    outOfTwoPlayer2.text_size = 20
    twoPlayerMaxScore2 = Text(endTwoPlayerWindow, text="13", grid=[1, 4], align="top")
    twoPlayerMaxScore2.text_size = 30

    competitionText = Text(endTwoPlayerWindow, text="", grid=[0, 5], align="top")
    competitionText.text_size = 20; competitionText.hide()

    if (playerOnePoints > playerTwoPoints):
        competitionText = Text(endTwoPlayerWindow, text="Player 1 Wins!", grid=[0, 5], align="top"); competitionText.text_size = 20;
    elif (playerOnePoints < playerTwoPoints):
        competitionText = Text(endTwoPlayerWindow, text="Player 2 Wins!", grid=[0, 5], align="top"); competitionText.text_size = 20;
    elif (playerOnePoints == playerTwoPoints):
        competitionText = Text(endTwoPlayerWindow, text="It's a Draw!", grid=[0, 5], align="top"); competitionText.text_size = 20;

    restartButton = PushButton(endTwoPlayerWindow, grid=[0, 6], text="Play Again!", align="top", command=RestartGame)
    restartButton.bg = "White"

#---End Two Player

'''
Checks how many players there are and calls the respective end game function.
Doesn't return any variables.
'''
def EndScreens():
    global isOnePlayer

    if (isOnePlayer == True):
        onePlayerWindow.hide()
        EndScreenOnePlayer()
    elif (isOnePlayer == False):
        twoPlayerWindow.hide()
        EndScreenTwoPlayer()

'''
Calls the function run to restart the game.
Checks how many players there are and closes the respective end game window.
Doesn't return any variables.
'''
def RestartGame():
    global endOnePlayerWindow
    global endTwoPlayerWindow
    global isOnePlayer

    Run()
    if (isOnePlayer == True):
        endOnePlayerWindow.hide()
    elif (isOnePlayer != True):
        endTwoPlayerWindow.hide()

Run()

app.display()