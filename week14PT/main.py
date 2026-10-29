import sqlite3

DATABASE = "students.db"


def create_table():
    """Create the students table if it does not exist."""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                program TEXT NOT NULL
            )
        """)

    print("Students table is ready.")


def insert_student():
    """Coding Exercise 1: Insert a student safely."""
    name = "Angelito Cruz"
    program = "BSIS"

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "INSERT INTO students (name, program) VALUES (?, ?)",
            (name, program)
        )

        student_id = cursor.lastrowid

    print("\n--- Coding Exercise 1: Insert Student ---")
    print("Student saved")
    print("Student ID:", student_id)

    return student_id


def read_students():
    """Coding Exercise 1: Read and display student records."""
    with sqlite3.connect(DATABASE) as conn:
        rows = conn.execute(
            "SELECT id, name, program FROM students ORDER BY name"
        ).fetchall()

    print("\n--- Coding Exercise 1: Read Students ---")

    if not rows:
        print("No student records found.")
        return

    for row in rows:
        print(row)


def update_student(student_id, new_program):
    """Coding Exercise 2: Update a student record."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "UPDATE students SET program = ? WHERE id = ?",
            (new_program, student_id)
        )

        rows_updated = cursor.rowcount

        if rows_updated == 0:
            print("No student found with that ID")
        else:
            print("Student updated")
            print("Rows updated:", rows_updated)

            student = conn.execute(
                "SELECT id, name, program FROM students WHERE id = ?",
                (student_id,)
            ).fetchone()

            print("Updated record:", student)


def test_missing_record():
    """Exercise 2: Handle a record that does not exist."""
    missing_id = -1
    new_program = "BSIT"

    print("\n--- Handling a Missing Record ---")

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "UPDATE students SET program = ? WHERE id = ?",
            (new_program, missing_id)
        )

        if cursor.rowcount == 0:
            print("No student found with that ID")
        else:
            print("Student updated")


def delete_student(student_id):
    """Optional extension: Delete and verify a student record."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        if cursor.rowcount == 0:
            print("No student found to delete")
        else:
            print("Student deleted successfully")

        remaining = conn.execute(
            "SELECT id, name, program FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        if remaining is None:
            print("Confirmed: student record was removed")
        else:
            print("Student record still exists")


def main():
    print("IS306 WEEK 14 - CLOUD DATABASES")
    print("Coding Exercises 1 and 2")

    create_table()

    student_id = insert_student()
    read_students()

    print("\n--- Coding Exercise 2: Update Record ---")
    update_student(student_id, "BSIS")

    test_missing_record()

    print("\nAll required exercises completed.")


if __name__ == "__main__":
    main()