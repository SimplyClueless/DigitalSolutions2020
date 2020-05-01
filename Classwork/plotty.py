import random
from guizero import App, Picture, PushButton

app = App()

mylist = list(range(1, 53)) #Creates list of 52 integers

def RandomiseCard():
    random.shuffle(mylist) #Randomly shuffles list
    CardNumber = mylist[0] #Select item zero from list
    RandomCard = "PlayingCards/" + str(CardNumber) + ".png"
    CardImage = Picture(app, image=RandomCard)

button = PushButton(app, text="Push for a new card!", command=RandomiseCard)

CardImage = Picture(app)
app.display()
