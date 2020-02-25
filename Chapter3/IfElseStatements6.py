grade = int(input("Enter you grade number: "))

if grade >= 0 and grade <= 59:
    print("Pass")

elif grade >= 60 and grade <= 79:
    print("Credit")

elif grade >= 80 and grade <= 100:
    print("Distinction")

else:
    print("ERROR! Not a valid number!")