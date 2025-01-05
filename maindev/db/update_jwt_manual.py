import sqlite3

def update_tokens_in_db(user_id, access_token, refresh_token):
    conn = sqlite3.connect('jwt.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET jwt_token = ?, refresh_token = ? WHERE user_id = ?", (access_token, refresh_token, user_id))

    conn.commit()
    conn.close()

access_token= "insert_valid_token_here"
refresh_token="insert_valid_refresh_token_here"
update_tokens_in_db(1, access_token, refresh_token)