import sqlite3

database = "Company.db"

connection = sqlite3.connect(database)

connection.execute("DROP TABLE IF EXISTS Customers;")

connection.execute("""CREATE TABLE Customers
                    (Id INT PRIMARY KEY NOT NULL,
                    FirstName VARCHAR(255),
                    LastName VARCHAR(255),
                    Dob VARCHAR(255));""")

connection.commit()

connection.close()