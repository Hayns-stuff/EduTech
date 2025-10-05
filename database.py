"""
Lightweight database helpers.

This module now delegates insertion to `data_handler.save_student_data` so there
is a single canonical insert implementation. Other helpers (fetch/update)
remain available for the rest of the app.
"""
from typing import Any, Dict, List, Optional, Tuple

from data_handler import get_connection as dh_get_connection, save_student_data


def get_connection():
    """Return a DB connection (delegates to data_handler.get_connection)."""
    return dh_get_connection()


def insert_student(data: Dict[str, Any]) -> Tuple[bool, str, Optional[int]]:
    """Insert student data using the centralized handler.

    Returns a tuple (success, message, last_id).
    """
    return save_student_data(data)


def fetch_students() -> List[Dict[str, Any]]:
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT id, lrn, last_name, first_name, strand, status FROM students ORDER BY id DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Exception:
        return []
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass


def fetch_student_by_id(student_id: int) -> Optional[Dict[str, Any]]:
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        row = cursor.fetchone()
        return row
    except Exception:
        return None
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass


def update_student_status(student_id: int, new_status: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE students SET status = %s WHERE id = %s"
        cursor.execute(sql, (new_status, student_id))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass
