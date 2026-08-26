import sqlite3


DATABASE = "users.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

)
""")


connection.commit()

connection.close()


print("Database created successfully!")
print("Users table is ready.")