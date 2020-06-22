import matplotlib.pyplot as plt
import sqlite3

names = []
life = []

# create name of database
database = "world.db"

# create connection to the database
connection = sqlite3.connect(database)

# query database
record = connection.execute("SELECT Name, Lifeexpectancy FROM Country "
                            "WHERE Lifeexpectancy > 70 AND Region = 'Eastern Europe'")

# print records
for row in record:
    names.append(row[0])
    life.append(row[1])

plt.bar(names, life)
plt.title("Countries in Eastern Europe with a Life Expenctancy Above 70 years")
plt.ylabel("Life Expectancy")
plt.xlabel("Country Name")
plt.show()

# close connection
connection.close()