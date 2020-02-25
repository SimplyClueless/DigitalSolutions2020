people = int(input("How many people do you need to feed: "))
hotdogs = int(input("How many hot dogs will each person eat: "))

total = people * hotdogs
HPackets = total // 10
HRemainder = total % 10
BPackets = total // 8
BRemainder = total % 8

print("Total =", total)
print("Hotdog packets =", HPackets)
print("Remaining Hotdogs =", HRemainder)
print("Bun pakcets =", BPackets)
print("Remaining Buns =", BRemainder )
