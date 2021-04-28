import sqlite3

def initialize_database():
    global c
    global conn
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.exeute('''CREATE TABLE IF NOT EXISTS entries(
        id INT PRIMARY AUTOINCREMENT,
        name TEXT,
        photo BLOB,
        )''')
    c.execute('''CREATE TABLE IF NOT EXISTS items(
        id INT PRIMARY
        name TEXT
        )''')
    conn.commit()

def add_item(name, items, photo):
    c.execute("INSERT INTO entries(name, photo) VALUES(?,?)", name, photo)
    response = c.execute("SELECT id FROM entries WHERE name=?", name)
    id = response[0]
    for item in items:
        c.execute("INSERT INTO items VALUES(?,?)", id, item)