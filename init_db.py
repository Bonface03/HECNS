import sqlite3

connection = sqlite3.connect('database.db')


with open('backend.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username,password) VALUES (?, ?)",
            ('test', 'test')
            )

connection.commit()
connection.close()
