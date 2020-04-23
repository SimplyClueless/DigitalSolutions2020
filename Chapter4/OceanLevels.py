RiseLevel = 1.6
WaterLevel = 0
Year = 1
while Year < 25:
    WaterLevel += RiseLevel
    print("In year", Year, "the water will rise to", WaterLevel, "mm high")
    Year += 1