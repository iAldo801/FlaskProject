import psycopg2

def get_db_connection():
    return psycopg2.connect(database="flask_db", user="postgres", password="aldoshp07", host="localhost", port="5432")

def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT DEFAULT TO_CHAR(NOW(), 'Day, DD Month YYYY HH12:MI:SS AM'),
            last_login TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    
def get_user_info(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user