import os

def get_db_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    db_path = os.path.join(current_dir, 'jwt.db')
    
    return db_path
