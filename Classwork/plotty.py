import matplotlib.pyplot as plt
import random


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
averageMoney = []
explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(12):
    averageMoney.append(random.randint(1, 101))
    print(averageMoney)

largestValue = max(averageMoney)

for i in range(12):
    if (averageMoney[i] == largestValue):
        listIndex = i
        explode[i] = 0.2


fig1, ax1 = plt.subplots()
ax1.pie(averageMoney, explode=explode, labels=months, autopct='%1.1f%%', shadow=False, startangle=90)
plt.legend(title="Months")
plt.show()