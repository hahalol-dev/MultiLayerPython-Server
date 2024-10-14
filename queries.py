import sqlite3

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('test_db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

def handle_queries(query_type, user_input=None):
    conn = get_db_connection()
    query = ''

    if query_type == 'vulnerable':
        # Vulnerable query - SQL Injection (due to direct user input in the query)
        query = f"SELECT * FROM users WHERE username = '{user_input}'"
    
    elif query_type == 'safe-int':
        # Safe query - the external input is an integer
        query = f"SELECT * FROM users WHERE id = {user_input}"
    
    elif query_type == 'safe-constant':
        # Safe query - the value is constant
        fixed_username = 'admin'
        query = f"SELECT * FROM users WHERE username = '{fixed_username}'"
    
    else:
        return None

    result = conn.execute(query).fetchall()
    conn.close()
    return result
