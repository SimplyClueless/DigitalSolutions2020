import sqlite3
from guizero import App, Window, Text, TextBox, PushButton

# create name of database
database = "Company.db"

# create connection to database or create database
connection = sqlite3.connect(database)

connection.commit()

def CommitToTable():
    # enter values into table
    connection.execute("INSERT INTO Customers (Id, FirstName, LastName, Dob) VALUES ({0}, {1}, {2}, {3});".format(idInput.value, firstNameInput.value, lastNameInput.value, dateOfBirthInput.value))

    # commit changes to database
    connection.commit()

    # close connection
    connection.close()

def PrintTableData():
    tableData = connection.execute("SELECT * FROM Customers")
    dataText = Text(app, text=tableData, grid=[0, 6])

app = App(title="Login Page", layout="grid")

idText = Text(app, text="Enter your ID number: ", grid=[0, 0])
idInput = TextBox(app, grid=[1, 0])
firstNameText = Text(app, text="Enter your First Name: ", grid=[0, 1])
firstNameInput = TextBox(app, grid=[1, 1])
lastNameText = Text(app, text="Enter your Last Name: ", grid=[0, 2])
lastNameInput = TextBox(app, grid=[1, 2])
dobText = Text(app, text="Enter your Date Of Birth (YYYY-MM-DD): ", grid=[0, 3])
dateOfBirthInput = TextBox(app, grid=[1, 3])

loginButton = PushButton(app, text="Register User!", grid=[0, 4], command=CommitToTable)
dataButton = PushButton(app, text="Print Table Data!", grid=[0, 5], command=PrintTableData)

app.display()
