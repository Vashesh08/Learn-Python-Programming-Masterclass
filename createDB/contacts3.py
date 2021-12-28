import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please Enter Your Name:")

cursor = db.cursor()

# for row in cursor.execute("SELECT * FROM contacts WHERE name=?", (name,)):
for row in cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)
cursor.close()
# for row in cursor:
#     print(row)
#     print("-"*20)
db.close()