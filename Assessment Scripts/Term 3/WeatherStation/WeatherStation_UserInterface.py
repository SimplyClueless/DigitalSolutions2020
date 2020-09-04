import sqlite3
from guizero import App, Window, Box, Text, TextBox, PushButton, Picture, ListBox
from sense_hat import SenseHat
import matplotlib.pyplot as plt
import time
from time import strftime, gmtime

app = App()
app.hide()
sense = SenseHat()
database = "Weather.db"
connection = sqlite3.connect(database)

def MainPage():
    global mainWindow
    
    mainWindow = Window(app, title="S.W.I.G.G.S", layout="grid")
    mainWindow.width = 900; mainWindow.height = 850; mainWindow.bg = "Grey"
    
    titleText = Text(mainWindow, text="Sheldon Weather Information & Graph Generating Software", grid=[0, 0], align="top")
    titleText.text_size = 25
    abbreviationText = Text(mainWindow, text="---S.W.I.G.G.S---", grid=[0, 1], align="top")
    abbreviationText.text_size = 20
    
    spacerText = Text(mainWindow, text="", grid=[0, 2], align="top")
    spacerText.text_size = 20
    
    savedText = Text(mainWindow, text="---Display Stored Data---", grid=[0, 3], align="top")
    savedText.text_size = 25
    
    standardButtonContainer = Box(mainWindow, layout="grid", grid=[0, 4], align="top", border=True)
    standardButtonContainer.set_border(10, "Grey")
    dataButton = PushButton(standardButtonContainer, text="Display Data", grid=[0, 0], align="top", command=SQLQuerySelection)
    dataButton.width = 20; dataButton.height = 5; dataButton.bg = "White"
    graphButtonContainer = Box(standardButtonContainer, layout="grid", grid=[0, 1], align="top", border=True)
    graphButtonContainer.set_border(10, "Grey")
    tempGraphButton = PushButton(graphButtonContainer, text="Temperature Graph", grid=[0, 1], align="top", command=CreateTempGraph)
    tempGraphButton.width = 20; tempGraphButton.height = 5; tempGraphButton.bg = "White"
    humidGraphButton = PushButton(graphButtonContainer, text="Humidity Graph", grid=[1, 1], align="top", command=CreateHumidGraph)
    humidGraphButton.width = 20; humidGraphButton.height = 5; humidGraphButton.bg = "White"
    pressGraphButton = PushButton(graphButtonContainer, text="Pressure Graph", grid=[2, 1], align="top", command=CreatePressGraph)
    pressGraphButton.width = 20; pressGraphButton.height = 5; pressGraphButton.bg = "White"
    
    liveText = Text(mainWindow, text="---Live Data Collection---", grid=[0, 5], align="top")
    liveText.text_size = 25
    informationText = Text(mainWindow, text="Collect Data for...", grid=[0, 6], align="top")
    informationText.text_size = 15
    liveContainer = Box(mainWindow, layout="grid", grid=[0, 7], align="top", border=True)
    liveContainer.set_border(10, "Grey")

    '''
    Runs LiveCollection function passing through the number of cycles to complete the displayed time on the button
    Doesn't get any return variables
    '''
    hrs48Button = PushButton(liveContainer, text="48 Hours...", grid=[0, 0], align="top", command=lambda: LiveCollection(17280))
    hrs48Button.width = 10; hrs48Button.height = 5; hrs48Button.bg = "White"
    hrs24Button = PushButton(liveContainer, text="24 Hours...", grid=[1, 0], align="top", command=lambda: LiveCollection(8640))
    hrs24Button.width = 10; hrs24Button.height = 5; hrs24Button.bg = "White"
    hrs12Button = PushButton(liveContainer, text="12 Hours...", grid=[3, 0], align="top", command=lambda: LiveCollection(4320))
    hrs12Button.width = 10; hrs12Button.height = 5; hrs12Button.bg = "White"
    hrs1Button = PushButton(liveContainer, text="1 Hours...", grid=[4, 0], align="top", command=lambda: LiveCollection(360))
    hrs1Button.width = 10; hrs1Button.height = 5; hrs1Button.bg = "White"
    customButton = PushButton(mainWindow, text="Custom Time...", grid=[0, 8], align="top", command=CustomLiveCollection)
    customButton.width = 15; customButton.height = 5; customButton.bg = "White"
        
    warningContainer = Box(mainWindow, layout="grid", grid=[0, 9], align="top", border=True)
    warningContainer.set_border(30, "Grey")
    databaseButton = PushButton(warningContainer, text="!Create New Database!", grid=[0, 0], align="top", command=CreateNewDatabase)
    databaseButton.width = 20; databaseButton.height = 2; databaseButton.bg = "Red"

def SQLQuerySelection():    
    queryWindow = Window(app, title="SQL Query Selection", layout="grid")
    queryWindow.width = 800; queryWindow.bg = "Grey"
    
    dataButtonContainer = Box(queryWindow, layout="grid", grid=[0, 0], align="top", border=True)
    dataButtonContainer.set_border(10, "Grey")

    allDataButton = PushButton(dataButtonContainer, text="Show All Data", grid=[0, 0], align="top",
                               command=lambda: SQLQueriesExecution("SELECT Date, Time, Temp, Humid, Press FROM WeatherData", "Date, Time, Temperature, Humidity, Pressure"))
    allDataButton.width = 10; allDataButton.height = 5; allDataButton.bg = "White"

    '''
    Request all the fields from the database and orders then ascending by a specifc field
    Doesn't get any return variables
    '''
    sortingText = Text(dataButtonContainer, text="Sort By:", grid=[0, 1], align="top")
    tempSortButton = PushButton(dataButtonContainer, text="Temperature (min - max)", grid=[0, 2], align="top",
                                 command=lambda: SQLQueriesExecution("SELECT Date, Time, Temp, Humid, Press FROM WeatherData ORDER BY Temp ASC", 
                                                                    "Date, Time, Temperature, Humidity, Pressure"))
    tempSortButton.width = 20; tempSortButton.height = 5; tempSortButton.bg = "White"
    humidSortButton = PushButton(dataButtonContainer, text="Humidity (min - max)", grid=[1, 2], align="top",
                                 command=lambda: SQLQueriesExecution("SELECT Date, Time, Temp, Humid, Press FROM WeatherData ORDER BY Humid ASC", 
                                                                     "Date, Time, Temperature, Humidity, Pressure"))
    humidSortButton.width = 20; humidSortButton.height = 5; humidSortButton.bg = "White"
    pressSortButton = PushButton(dataButtonContainer, text="Pressure (min - max)", grid=[2, 2], align="top",
                                 command=lambda: SQLQueriesExecution("SELECT Date, Time, Temp, Humid, Press FROM WeatherData ORDER BY Press ASC",
                                                                     "Date, Time, Temperature, Humidity, Pressure"))
    pressSortButton.width = 20; pressSortButton.height = 5; pressSortButton.bg = "White"
    # dateInput = TextBox(dataButtonContainer, grid=[1, 1], align="top")
    # dateInput.bg = "White"
    # dateDataButton = PushButton(dataButtonContainer, text="Show Data From Date (YYYYMMDD)", grid=[1, 0], align="top",
    #                             command=lambda: SQLQueriesExecution("""SELECT Date, Time, Temp, Humid, Press FROM WeatherData
    #                                                                 WHERE Date = ({0});""".format(dateInput), "Date, Time, Temp"))
    # dateDataButton.width = 30; dateDataButton.height = 5; dateDataButton.bg = "White"
    #
    # timeInput = TextBox(dataButtonContainer, grid=[2, 1], align="top")
    # timeInput.bg = "White"
    # timeDataButton = PushButton(dataButtonContainer, text="Show Data from Time (HHMMSS)", grid=[2, 0], align="top",
    #                             command=lambda: SQLQueriesExecution("""SELECT Date, Time, Temp, Humid, Press FROM WeatherData
    #                                                                 WHERE Date = ({0});""".format(timeInput), "Date, Time, Temp"))
    # timeDataButton.width = 30; timeDataButton.height = 5; timeDataButton.bg = "White

'''
Executes the passed through SQL Query (queryString) and add the output to a list
Print list onto a GUIZero listbox and displays data on a new window
Doesn't return any variables
'''
def SQLQueriesExecution(queryString, informationData):
    printData = []
    
    dataWindow = Window(app, title="Query Display", layout="grid")
    dataWindow.height = 1080; dataWindow.width = 400; dataWindow.bg = "Grey"
    
    dataRecord = connection.execute(queryString)
    printData.append(informationData)
    for row in dataRecord:
        printData.append(row)
        
    dataList = ListBox(dataWindow, items=printData, scrollbar=True, grid=[0, 0], align="top")
    dataList.height = 1080; dataList.width = 400; dataList.bg = "White"

'''
Create a list for storing the stored temperature, time and date values from the databse for local use
Will append the values from the database into its respective list using a for loop
Creates a graph with matplotlib using the list data and saves it as an image which will be displayed using GUIZero
Doesn't return any variables
'''
def CreateTempGraph():
    tempArray = []
    timeArray = []
    dateArray = []
    
    plt.clf()
    
    graphWindow = Window(app, title="Temperature Graph")
    graphWindow.width = 650; graphWindow.height = 500
    
    record = connection.execute("SELECT * FROM WeatherData")
    for row in record:
        tempArray.append(row[1])
        timeArray.append(row[4])
        dateArray.append(row[5])

    endDate = len(dateArray) - 1

    plt.plot(timeArray, tempArray)
    plt.ylabel("Temperature")
    plt.xlabel("Time (HHMMSS) from " + str(dateArray[0]) + " to " + str(dateArray[endDate - 1]) + " (YYYYMMDD)")
    plt.savefig("tempGraph.png")
    
    graphImage = Picture(graphWindow, image="tempGraph.png")

'''
Create a list for storing the stored temperature, time and date values from the databse for local use
Will append the values from the database into its respective list using a for loop
Creates a graph with matplotlib using the list data and saves it as an image which will be displayed using GUIZero
Doesn't return any variables
'''
def CreateHumidGraph():
    humidArray = []
    timeArray = []
    dateArray = []
    
    plt.clf()
    
    graphWindow = Window(app, title="Humidity Graph")
    graphWindow.width = 650; graphWindow.height = 500
    
    record = connection.execute("SELECT * FROM WeatherData")
    for row in record:
        humidArray.append(row[2])
        timeArray.append(row[4])
        dateArray.append(row[5])
        
    endDate = len(dateArray) - 1
    
    plt.plot(timeArray, humidArray)
    plt.ylabel("Humidity")
    plt.xlabel("Time (HHMMSS) from " + str(dateArray[0]) + " to " + str(dateArray[endDate - 1]) + " (YYYYMMDD)")
    plt.savefig("humidGraph.png")
    
    graphImage = Picture(graphWindow, image="humidGraph.png")

'''
Create a list for storing the stored temperature, time and date values from the databse for local use
Will append the values from the database into its respective list using a for loop
Creates a graph with matplotlib using the list data and saves it as an image which will be displayed using GUIZero
Doesn't return any variables
'''
def CreatePressGraph():
    pressArray = []
    timeArray = []
    dateArray = []
    
    plt.clf()
    
    graphWindow = Window(app, title="Pressure Graph")
    graphWindow.width = 650; graphWindow.height = 500
    
    record = connection.execute("SELECT * FROM WeatherData")
    for row in record:
        pressArray.append(row[3])
        timeArray.append(row[4])
        dateArray.append(row[5])
        
    endDate = len(dateArray) - 1
    
    plt.plot(timeArray, pressArray)
    plt.ylabel("Pressure")
    plt.xlabel("Time (HHMMSS) from " + str(dateArray[0]) + " to " + str(dateArray[endDate - 1]) + " (YYYYMMDD)")
    plt.savefig("pressGraph.png")
    
    graphImage = Picture(graphWindow, image="pressGraph.png")

'''
Takes the number of cycles and adds the collected data to the database in a while loop until the number of cycles is matched by the counter
Uses a try catch to make sure that the passed through cycles variable is a valid interger
Takes the data and adds it to local lists which will be printed on a GUIZero listbox
Creates graphs based ONLY on the data being collected and save them as image which will be displayed by GUIZero
Doesn't return any variables
'''
def LiveCollection(cycles):
    printedData = []
    liveTime = []
    liveTemp = []
    liveHumid = []
    livePress = []
    
    liveWindow = Window(app, title="Data Collection Window", layout="grid")
    liveWindow.width = 620; liveWindow.height = 920
    
    try:
        localCycles = int(cycles)
    except:
        print("invalid variable")
        liveWindow.error("Error", "Invalid Variable")
    else:
        x = 0
        localCycles = int(cycles)
        liveDataList = ListBox(liveWindow)
        imageContainer = Box(liveWindow, layout="grid", grid=[1, 0], align="top", border=True)
        imageContainer.border = 10
        liveTempImage = Picture(imageContainer)
        liveHumidImage = Picture(imageContainer)
        livePressImage = Picture(imageContainer)
        
        while x < (localCycles):
            currentTemperature = (round(sense.get_temperature(), 2))
            currentHumidity = round(sense.get_humidity(), 2)
            currentPressure = round(sense.get_pressure(), 2)
            currentTime = time.strftime("%H%M%S", time.localtime())
            currentDate = time.strftime("%Y%m%d", gmtime())
            ID = str(currentTime) + str(currentDate)

            liveTime.append(currentTime)
            liveTemp.append(currentTemperature)
            liveHumid.append(currentHumidity)
            livePress.append(currentPressure)

            printedData.append(("ID:", ID))
            printedData.append(("Temp:", currentTemperature))
            printedData.append(("Humidity:", currentHumidity))
            printedData.append(("Pressure:", currentPressure))
            printedData.append(("Time:", currentTime))
            printedData.append(("Date:", currentDate))
            printedData.append(("Entry: {0} Out of: {1}".format(x+1, localCycles)))
            printedData.append("")
            
            connection.execute("INSERT INTO WeatherData (ID, Temp, Humid, Press, Time, Date) Values ({0}, {1}, {2}, {3}, {4}, {5});"
                               .format(ID, currentTemperature, currentHumidity, currentPressure, currentTime, currentDate))
            connection.commit()
            
            plt.clf()
            plt.plot(liveTime, liveTemp)
            plt.ylabel("Temperature")
            plt.xlabel("Time")
            plt.savefig("liveTemp.png")
            plt.clf()
            plt.plot(liveTime, liveHumid)
            plt.ylabel("Pressure")
            plt.xlabel("Time")
            plt.savefig("liveHumid.png")
            plt.clf()
            plt.plot(liveTime, livePress)
            plt.ylabel("Humidity")
            plt.xlabel("Time")
            plt.savefig("livePress.png")
            plt.clf()
            
            liveDataList.destroy()
            liveDataList = ListBox(liveWindow, items=printedData, grid=[0, 0], scrollbar=True)
            liveDataList.width = 200; liveDataList.height = 920
            liveTempImage.destroy()
            liveTempImage = Picture(imageContainer, image="liveTemp.png", grid=[0, 0])
            liveTempImage.width = 400; liveTempImage.height = 300
            liveHumidImage.destroy()
            liveHumidImage = Picture(imageContainer, image="liveHumid.png", grid=[0, 1])
            liveHumidImage.width = 400; liveHumidImage.height = 300
            livePressImage.destroy()
            livePressImage = Picture(imageContainer, image="livePress.png", grid=[0, 2])
            livePressImage.width = 400; livePressImage.height = 300
            
            liveWindow.update()
            time.sleep(10)
            x += 1
            liveWindow.focus()
            
def CustomLiveCollection():
    customInformationWindow = Window(app, title="Custom Information Entry", layout="grid")
    customInformationWindow.width = 450; customInformationWindow.height = 180; customInformationWindow.bg = "Grey"
    usageText = Text(customInformationWindow, text="Enter the number of cycles you wish to run for...", grid=[0, 0], align="top")
    usageText.text_size = 15
    informationText = Text(customInformationWindow, text="1 Cycle = 10 seconds", grid=[0, 1], align="top")
    valueTextBox = TextBox(customInformationWindow, grid=[0, 2], align="top")
    valueTextBox.width = 6; valueTextBox.bg = "White"
    beginButton = PushButton(customInformationWindow, text="Begin...", grid=[0, 3], align="top", command=lambda: LiveCollection(valueTextBox.value))
    beginButton.width = 15; beginButton.height = 5; beginButton.bg = "White"

'''
When called it will overwrite the currently existing database and create a new one with same variables
Commits the database and closes the connection
Doesn't return any variables
'''
def CreateNewDatabase():
    database = "Weather.db"

    connection = sqlite3.connect(database)
    
    connection.execute("DROP TABLE IF EXISTS WeatherData;")
    connection.execute("""CREATE TABLE WeatherData
                    (ID INT PRIMARY KEY NOT NULL,
                    Temp DECIMAL,
                    Humid DECIMAL,
                    Press DECIMAL,
                    Time INT NOT NULL,
                    Date DATE NOT NULL);""")

    connection.commit()
    connection.close()

MainPage()
    
app.display()