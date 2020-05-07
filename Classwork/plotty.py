import random
from guizero import App, Picture, PushButton, Window

app = App(layout="grid")
window = Window(app, title="Second Window", layout="grid")
window2 = Window(app, title="Third Window", layout="grid")
window.hide()
window2.hide()

CardList = list(range(1, 53)) #Creates list of 52 integers

def RandomiseCard():
    random.shuffle(CardList) #Randomly shuffles list
    CardNumber1 = CardList[0] #Select item zero from list
    CardNumber2 = CardList[1]
    CardNumber3 = CardList[2]
    CardNumber4 = CardList[3]
    CardList.remove(CardNumber1)
    CardList.remove(CardNumber2)PYH
    CardList.remove(CardNumber3)
    CardList.remove(CardNumber4)

    CardImage1 = Picture(app, image="PlayingCards/" + str(CardNumber1) + ".png", grid=[0, 1])
    CardImage2 = Picture(app, image="PlayingCards/" + str(CardNumber2) + ".png", grid=[0, 2])
    CardImage3 = Picture(app, image="PlayingCards/" + str(CardNumber3) + ".png", grid=[1, 1])
    CardImage4 = Picture(app, image="PlayingCards/" + str(CardNumber4) + ".png", grid=[1, 2])

    if len(CardList) == 0:
        window.show()
        window2.show()
        app.hide()

button = PushButton(app, text="Push for a new card!", command=RandomiseCard, grid=[0, 0])

app.display()
