import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

conn.commit()
conn.close()