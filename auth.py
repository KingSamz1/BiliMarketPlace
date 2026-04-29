
from passlib.hash import pbkdf2_sha256
from database import c, conn

def register(name, phone, password):
    hashed = pbkdf2_sha256.hash(password)
    c.execute("INSERT INTO users(name, phone, password) VALUES(?,?,?)",
              (name, phone, hashed))
    conn.commit()

def login(phone, password):
    user = c.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
    if user and pbkdf2_sha256.verify(password, user[3]):
        return user
    return None
