from random import randint

MyList = list()
i = 0

while i < 50:
    Number = randint(1, 10)
    print(Number)
    MyList.append(Number) #add an item to the end of a list
    i += 1

print(MyList)

MyList.remove(3) # remove item from list
print(MyList)

MyList.sort() # sort list accending
print(MyList)

print(min(MyList))
print(max(MyList))

