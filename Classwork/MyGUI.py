from guizero import App, Text, Picture, PushButton, MenuBar

app = App()

text = Text(app, align="top", text="Hello GUI", color="blue", font="Times New Roman", size="30")
text1 = Text(app, align="bottom", text="General Kenobi")

picture = Picture(app, image="picture1.png", width=100, height=100)
picture1 = Picture(app, image="picture2.png", width=100, height=100)


def DoSomething():
    print("You have pushed my button")


menubar = MenuBar(app,
                  toplevel=["File", "Edit", "Settings"],
                  options=[
                      [["File option 1", DoSomething], ["File option 2", DoSomething]],
                      [["Edit option 1", DoSomething], ["Edit option 2", DoSomething]],
                      [["Settings option 1", DoSomething], ["Settings option 1", DoSomething]]
                  ])

button = PushButton(app, text="Push me!", command=DoSomething)
button.bg = "green"
# text_color
# text_size
# width
# font

app.display()
