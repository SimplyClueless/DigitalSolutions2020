laps = int(input("Enter how many laps you completed: "))
run = set()
loop1 = 0
loop2 = 0
while loop1 < laps:
    seconds = int(input("Time for the lap (in seconds): "))
    run.add(seconds)
    loop1 += 1
run = list(run)
run.sort()
while loop2 < laps:
    loop2 += run[loop2]
average = loop2/laps
print("Your fastest lap was: ", run[0], "seconds")
print("Your Slowest Lap was: ", run[loop1-1], "seconds")
print ("Your average lap time was: ", average, "seconds")