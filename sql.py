import sqlite3
conn = sqlite3.connect('Data/usersdata.db')
c = conn.cursor()

c.execute("SELECT * FROM users WHERE permission_level = 4")

# Fetch all rows from the query
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()