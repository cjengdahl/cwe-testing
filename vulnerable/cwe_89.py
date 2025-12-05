import sqlite3

def find_user_by_name(db_path, name):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # VULNERABLE: building SQL by concatenating user input directly
    query = f"SELECT id, username FROM users WHERE username = '{name}';"
    cur.execute(query)  # if `name` contains SQL, it can change the query meaning
    result = cur.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Suppose user supplies name from a web form or CLI
    user_input = input("Enter username to look up: ")
    print(find_user_by_name("example.db", user_input))

