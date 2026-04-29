
import sqlite3

conn = sqlite3.connect("biliwaka.db", check_same_thread=False)
c = conn.cursor()

def init_db():
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        password TEXT,
        is_subscriber INTEGER DEFAULT 0
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS ads(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT,
        description TEXT,
        media TEXT,
        is_featured INTEGER,
        created_at TEXT,
        expires_at TEXT,
        clicks INTEGER DEFAULT 0
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS banner_ads(
        id INTEGER PRIMARY KEY,
        media TEXT,
        link TEXT,
        expires_at TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS ratings(
        id INTEGER PRIMARY KEY,
        vendor_id INTEGER,
        rating INTEGER
    )""")

    conn.commit()
