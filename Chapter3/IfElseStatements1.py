length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

Area1 = length1 * width1
Area2 = length2 * width2

print("The area of your first rectangle is:", Area1)
print("The area of your second rectangle is:", Area2)

if (Area1 > Area2):
    print(Area1,"Is greater than", Area2)

elif (Area2 > Area1):
    print(Area2,"Is greater than", Area1)

