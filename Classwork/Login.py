from guizero import App, Window, TextBox, Text, PushButton

app = App(title="Login Screen", layout="grid")
window = Window(app, title="GUI", layout="grid")
window.hide()

Username = "bristow"
Password = "password"

UsernameText = TextBox(app, grid=[0, 0], width="50", align="top")
PasswordText = TextBox(app, grid=[0, 1], width="50", align="top", hide_text=True)

def CheckCredentials():
    text = Text(app, grid=[0, 2])
    text.clear()
    if UsernameText.value == Username and PasswordText.value == Password:
        app.hide()
        window.show()
    else:
        text = Text(app, text="Incorrect Credentials", grid=[0, 3], align="top")

SubmitLoginDetails = PushButton(app, text="Login", grid=[0, 4], align="top", command=CheckCredentials)
app.display()
