import sqlite3

# Create cursor/database & make tables if they don't exist yet
def initialize_database():
    global c
    global conn
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # entries table (id, name, link)
    c.execute('''CREATE TABLE IF NOT EXISTS entries( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        link TEXT
        )''')
    # items table (id, name)
    c.execute('''CREATE TABLE IF NOT EXISTS items(
        id INT,
        name TEXT
        )''')
    conn.commit()
    return True, "OK"

# Adds entry/photo to entries table and all the items to the items table
def add_item(name, items, link):
    c.execute("INSERT INTO entries(name, link) VALUES(?,?)", (name, link))
    entry_id = c.lastrowid
    for item in items:
        c.execute("INSERT INTO items VALUES(?,?)", (entry_id, item))
    conn.commit()

# returns every item in a list
def query_entries(table):
    c.execute(f"SELECT * FROM {table}")
    return c.fetchall()

initialize_database()
print(query_entries("entries"))