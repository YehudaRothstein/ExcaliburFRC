import sqlite3
conn = sqlite3.connect('usersdata.db')
c = conn.cursor()

# Execute the SQL query
c.execute("SELECT * FROM users WHERE permission_level = 4")

# Fetch all rows from the query
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()