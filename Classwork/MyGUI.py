from guizero import App, Text, Picture, PushButton, MenuBar, Slider, TextBox, CheckBox, Combo

app = App()

def DoSomething():
    print("You have pushed my button")

def SliderChanged(value):
    textbox.value = value

def CheckBoxChanger():
    textbox1 = TextBox(app, text="Gays Burnt!")

menubar = MenuBar(app,
                  toplevel=["File", "Edit", "Settings"],
                  options=[
                      [["File option 1", DoSomething], ["File option 2", DoSomething]],
                      [["Edit option 1", DoSomething], ["Edit option 2", DoSomething]],
                      [["Settings option 1", DoSomething], ["Settings option 1", DoSomething]]
                  ])

textbox = TextBox(app, align="bottom")

text = Text(app, align="top", text="Hello GUI", color="blue", font="Times New Roman", size="30")
text1 = Text(app, align="bottom", text="General Kenobi")

picture = Picture(app, image="picture1.png", width=300, height=300)
picture1 = Picture(app, image="picture2.png", width=300, height=300)

slider = Slider(app, align="bottom", command=SliderChanged)

checkbox = CheckBox(app, text="Burn the Gays!", command=CheckBoxChanger)

button = PushButton(app, text="Push me!", command=DoSomething)
button.bg = "green"
# text_color
# text_size
# width
# font

app.display()
