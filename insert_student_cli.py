import sys, json

# Use the same data handler used in the app
from data_handler import save_student_data

if __name__ == '__main__':
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        print(json.dumps({"success": False, "message": f"Failed to read input JSON: {e}", "last_id": None}))
        sys.exit(2)

    try:
        success, message, last_id = save_student_data(payload)
    except Exception as e:
        print(json.dumps({"success": False, "message": str(e), "last_id": None}))
        sys.exit(1)

    print(json.dumps({"success": success, "message": message, "last_id": last_id}))
    sys.exit(0 if success else 1)
