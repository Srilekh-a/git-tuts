import sqlite3

# Connect to SQLite database (or create it if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a table for students
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
""")
conn.commit()

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print(f"Student '{name}' added successfully!\n")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("\nStudent List:")
        print("ID  | Name        | Age | Grade")
        print("-" * 30)
        for student in students:
            print(f"{student[0]:<4} | {student[1]:<10} | {student[2]:<3} | {student[3]}")

# Function to search for a student
def search_student():
    name = input("Enter student name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    students = cursor.fetchall()

    if not students:
        print(f"No student found with name '{name}'.")
    else:
        print("\nSearch Results:")
        print("ID  | Name        | Age | Grade")
        print("-" * 30)
        for student in students:
            print(f"{student[0]:<4} | {student[1]:<10} | {student[2]:<3} | {student[3]}")

# Function to update a student
def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    grade = input("Enter new grade: ")

    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    print(f"Student ID {student_id} updated successfully!\n")

# Function to delete a student
def delete_student():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(f"Student ID {student_id} deleted successfully!\n")

# Main menu
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()