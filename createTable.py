import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table with columns for studentid, firstname, and lastname
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    studentid INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
