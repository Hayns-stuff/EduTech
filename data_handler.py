import mysql.connector
from PyQt6.QtWidgets import QMessageBox

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="enrollment_db",
            connect_timeout=5
        )
        return conn
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        return None

def save_student_data(student_data: dict):
    """
    Save student data to the database with error handling and validation
    """
    # basic validation
    # Validate required fields
    required_fields = ['last_name', 'first_name', 'lrn']
    for field in required_fields:
        if not student_data.get(field):
            error_msg = f"Missing required field: {field}"
            print(f"[ERROR] {error_msg}")
            return False, error_msg, None

    conn = get_connection()
    if not conn:
        return False, "Could not connect to database", None

    cursor = None
    try:
        cursor = conn.cursor()

        # Get actual column names from DB
        cursor.execute("SHOW COLUMNS FROM students")
        valid_columns = [row[0] for row in cursor.fetchall()]

        # Filter the data to only include valid columns
        filtered_data = {k: v for k, v in student_data.items() if k in valid_columns and k != 'id'}

        # Prepare SQL statement
        columns = ', '.join(filtered_data.keys())
        placeholders = ', '.join(['%s'] * len(filtered_data))
        sql = f"INSERT INTO students ({columns}) VALUES ({placeholders})"

        # Execute the query
        values = tuple(filtered_data.values())
        cursor.execute(sql, values)
        conn.commit()
        last_id = cursor.lastrowid
        return True, "Student data saved successfully", last_id

    except mysql.connector.Error as e:
        print(f"[ERROR] MySQL error: {e}")
        if conn:
            conn.rollback()
        return False, f"Database error: {str(e)}", None

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        if conn:
            conn.rollback()
        return False, f"Unexpected error: {str(e)}", None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("[DEBUG] Database connection closed")

def show_message(parent, title, message, icon=QMessageBox.Icon.Information):
    """
    Show a message box with the given title and message
    """
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(icon)
    msg.exec()