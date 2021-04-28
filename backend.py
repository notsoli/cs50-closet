import sqlite3

def initialize_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.exeute('''CREATE TABLE IF NOT EXISTS entries(
        
        )''')