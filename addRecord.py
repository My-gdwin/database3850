import sqlite3

# Function to add students to the database
def add_students():
    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # List of students to add (studentid, firstname, lastname)
    students = [
        (1, 'John', 'Doe'),
        (2, 'Jane', 'Smith'),
        (3, 'Michael', 'Brown'),
        (4, 'Emily', 'Davis')
    ]

    try:
        # Insert students into the students table
        cursor.executemany('''
        INSERT INTO students (studentid, firstname, lastname) VALUES (?, ?, ?)
        ''', students)
        conn.commit()
        print("Students added successfully!")

    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}. A student with this ID may already exist.")

    finally:
        # Close the connection
        conn.close()

# Call the function
if __name__ == "__main__":
    add_students()
