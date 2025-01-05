import sqlite3

def create_db():
    conn = sqlite3.connect('jwt.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            jwt_token TEXT,
            refresh_token TEXT
        )
    ''')

    cursor.execute("INSERT INTO users (user_id, jwt_token, 'refresh_token') VALUES (1, 'sample_jwt_token','sample_refresh_token')")

    conn.commit()
    conn.close()

create_db()