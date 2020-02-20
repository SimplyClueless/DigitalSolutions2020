mass = float(input("Enter the objects MASS in KG: "))
weight = mass * 9.81

print("Objects weight is", weight, "Newtons")

if (weight > 500):
    print("Weight is too heavy")

elif (weight < 100):
    print("Weight is too light")

else:
    print("")