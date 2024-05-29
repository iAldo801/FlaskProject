import psycopg2

def get_db_connection():
    return psycopg2.connect(database="db", user="postgres", password="pass", host="localhost", port="5432")

def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT DEFAULT TO_CHAR(NOW(), 'Day, DD Month YYYY HH12:MI:SS AM'),
            last_login TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    
def get_user_info(username):  # Ensure that get_user_info accepts the username parameter
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
