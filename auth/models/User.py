import psycopg2
from werkzeug.security import check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def add(self):
        conn = psycopg2.connect("dbname=auth user=auth password=auth")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (self.username, self.password))
        conn.commit()
        cur.close()
        conn.close()
    
    @staticmethod
    def authenticate(username, password):
        conn = psycopg2.connect("dbname=auth user=auth password=auth")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user and check_password_hash(user[2], password):
            return User(user[1], user[2])
            return None
        
    def get_by_username(username):
        conn = psycopg2.connect("dbname=auth user=auth password=auth")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            return User(user[1], user[2])
        return None
    