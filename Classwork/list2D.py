# Create 2D list with 3 items in list
list2D = [['Sarah', 4156, 23], ['Sam', 4000, 21], ['Terry', 4123, 17],
          ['Michael', 4100, 3], ['Frank', 4003, 12], ['Warren', 4300, 11],
          ['Samantha', 4165, 24], ['Will', 4034, 43], ['Ben', 4025, 54],
          ['Hudini', 4010, 19], ['Zach', 4540, 20], ['Sam', 4045, 45]]

print(list2D)
# Printing list 5 and sublist 3
print(list2D[4][2])
# Printing list 2 and sublist 2
print(list2D[1][1])
print(len(list2D))
# Printing length of the sub list
print(len(list2D[4]))

name = input("Who are you looking for: ")

# iterating through a list
for i in range(len(list2D)):
    #print(list2D[i])
    if list2D[i][0] == name:
        print(list2D[i])

        #print(list2D[i][j])


