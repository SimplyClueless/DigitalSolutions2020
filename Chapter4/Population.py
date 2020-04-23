Organisms = float(input("Enter how many organisms there are: "))
Increase = float(input("Enter the percentage of increase these organisms have: "))
Days = float(input("Enter how many days you want to approximate: "))
Day = 0

while Day < Days :
    Day += 1
    if Day == 1:
        print("Day", Day, "-", "Population =", Organisms)
    else:
        Organisms = Organisms + (Increase/100)
        print("Day", Day, "-", "Population =", Organisms)