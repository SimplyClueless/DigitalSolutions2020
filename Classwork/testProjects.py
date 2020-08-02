import statistics

stats = statistics

numbers = []
continueInput = "y"

while continueInput == "y" or continueInput == "Y":
    numberInput = int(input("Enter a number: "))
    numbers.append(numberInput)

    continueInput = str(input("Continue adding numbers: "))

numbers.sort()
print(numbers)
print("Length is:", len(numbers))
print("Mean is:", stats.mean(numbers))
print("Median is:", stats.median(numbers))
print("Mode is:", stats.mode(numbers))