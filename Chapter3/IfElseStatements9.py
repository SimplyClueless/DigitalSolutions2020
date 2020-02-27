Pennies = int(input("Enter an amount of pennies: "))
Nickles = int(input("Enter an amount of nickles: "))
Dimes = int(input("Enter an amount of dimes: "))
Quarters = int(input("Enter an amount of quarters: "))

TotalMoney = Pennies + (Nickles * 5) + (Dimes * 10) + (Quarters * 25)

if TotalMoney > 100:
    print("Your total amount of money is over $1")
elif TotalMoney < 100:
    print("Your total amount of money is less that $1")
elif TotalMoney == 100:
    print("Congratulations! Your total amount of money equals $1")