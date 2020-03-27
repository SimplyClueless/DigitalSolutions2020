from guizero import App, Text, Picture

app = App()

text = Text(app, align="top", text="Hello GUI", color="blue", font="Times New Roman", size="30")
text1 = Text(app, align="bottom", text="General Kenobi")

picture = Picture(app, image="picture1.png", width=100, hieght=100)
picture1 = Picture(app, image="picture2.png")

app.display()
