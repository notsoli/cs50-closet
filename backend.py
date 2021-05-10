import sqlite3
import random

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
    return c, conn
    conn.commit()
    conn.close()

# Adds entry/photo to entries table and all the items to the items table
def add_item(name, items, link):
    c, conn = initialize_database()
    c.execute("INSERT INTO entries(name, link) VALUES(?,?)", (name, link))
    entry_id = c.lastrowid
    for item in items:
        c.execute("INSERT INTO items VALUES(?,?)", (entry_id, item))
    conn.commit()
    conn.close()

def query_entries(sort):
    c, conn = initialize_database()
    c.execute("SELECT * FROM entries")
    entries = c.fetchall()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    entry_list = []
    for entry in entries:
        entry = list(entry)
        entry_id = entry[0]
        item_list = []
        for item in items:
            if item[0] == entry_id:
                item = list(item)
                item_list.append(item[1])
        entry.append(item_list)
        entry_list.append(entry)
    
    if sort == "none":
        return entry_list
    elif sort == "earliest":
        return entry_list[0]
    elif sort == "latest":
        return entry_list[-1]
    elif sort == "random":
        random.shuffle(entry_list)
        return entry_list
    else:
        return "yes"
    conn.commit()
    conn.close()

# Populates database
# for i in range(10):
#    add_item(str(i),[f"shirt{i}", f"pants{i}"], f"link{i}")