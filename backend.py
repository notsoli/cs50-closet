import sqlite3

def initialize_database():
    global c
    global conn
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        link TEXT
        )''')
    c.execute('''CREATE TABLE IF NOT EXISTS items(
        id INT,
        name TEXT
        )''')
    conn.commit()
    return True, "OK"

def add_item(name, items, link):
    c.execute("INSERT INTO entries(name, link) VALUES(?,?)", (name, link))
    entry_id = c.lastrowid
    for item in items:
        c.execute("INSERT INTO items VALUES(?,?)", (entry_id, item))
    conn.commit()

def query_entries():
    c.execute("SELECT * FROM entries")
    print(c.fetchall())

initialize_database()
query_entries()