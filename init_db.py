import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ("Пост 1", 'контент пост 1')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ("Пост 2", 'контент пост 2')
            )


connection.commit()
connection.close()