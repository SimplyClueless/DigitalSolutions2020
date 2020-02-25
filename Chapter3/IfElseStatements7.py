people = int(input("How many people do you need to feed: "))
hotdogs = int(input("How many hot dogs will each person eat: "))

total = people * hotdogs
HPackets = total // 10
HRemainder = total % 10
BPackets = total // 8
BRemainder = total % 8