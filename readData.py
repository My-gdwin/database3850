import sqlite3

# Function to read and display students from the database
def read_students():
    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    try:
        # Query to select all students
        cursor.execute('SELECT * FROM students;')

        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Check if there are any students and print them
        if rows:
            print("Student ID | First Name | Last Name")
            print("-------------------------------------")
            for row in rows:
                print(f"{row[0]:<11} | {row[1]:<11} | {row[2]:<11}")
        else:
            print("No students found in the database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close the connection
        conn.close()

# Call the function
if __name__ == "__main__":
    read_students()
