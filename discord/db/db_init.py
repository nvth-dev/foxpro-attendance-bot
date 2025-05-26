import sqlite3

def init_db():
    conn = sqlite3.connect('jwt.db')
    cursor = conn.cursor()

    # check if the 'users' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # if the table does not exist, create it and insert initial data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                app_authorization TEXT
            )
        ''')

        cursor.execute("INSERT INTO users (user_id, app_authorization) VALUES (1, 'sample_app_authorization')")

        conn.commit()
        print("Database created and initialized successfully.")
    else:
        print("Database already exists. No need to create.")

    conn.close()
