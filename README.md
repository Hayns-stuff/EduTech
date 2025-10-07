# EduTech
EduTech is an online enrollment system developed and presented at the University of Mindanao. It provides students with an easy way to register for courses, view schedules, and manage enrollment records. 


## SHS Enrollment System (Desktop)

A desktop enrollment management suite featuring a Staff Dashboard and Admin Panel. Staff can view, search, sort, and update student statuses with analytics; Admins can add, edit, and delete students. MySQL-backed with resilient helpers.

### Features
- Staff Dashboard (Tkinter)
  - Sortable table (click headers)
  - Live search by name or LRN
  - Update status: Completed / Incomplete
  - Analytics: status and strand breakdowns + bar chart
- Admin Panel (Tkinter)
  - Creative dark-themed UI
  - Full CRUD (Add, Edit, Delete) with validation
  - Sort/search/refresh
- Login (PyQt6)
  - Roles: staff/admin
  - Launches Dashboard or Admin Panel in separate processes
- Main app (PyQt6)
  - Global shortcut Ctrl+Alt+W to open Login
  - Smooth fade transition between PyQt windows
- Database Helpers
  - Fetch, create, update, delete student records

### Requirements
- Python 3.11+ (tested on 3.13)
- MySQL Server
- Python packages:
```bash
pip install PyQt6 mysql-connector-python
```

### Database Setup
- Configure DB connection in `data_handler.py` (default):
  - host: 127.0.0.1
  - user: root
  - password: "" (empty)
  - database: enrollment_db
- Table `students` must include at least:
  - id INT AUTO_INCREMENT PRIMARY KEY
  - lrn VARCHAR(255)
  - last_name VARCHAR(255)
  - first_name VARCHAR(255)
  - strand VARCHAR(255)
  - status VARCHAR(255)

Example SQL:
```sql
CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  lrn VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  strand VARCHAR(255),
  status VARCHAR(255)
);
```

### Run the Apps

- Main application (PyQt6, with global shortcut):
```bash
python Main.py
```
- Press Ctrl+Alt+W to open the login window.

- Login (PyQt6) credentials:
  - staff / staffpass → opens Staff Dashboard
  - admin / adminpass → opens Admin Panel

- Staff Dashboard (Tkinter) directly:
```bash
python Dashboard.py
```
- Admin Panel (Tkinter) directly:
```bash
python admin.py
```

### Usage

- Staff Dashboard
  - Search: type name or LRN to filter
  - Sort: click a column header, click again to reverse
  - Update status: select a row → Mark Complete / Mark Incomplete
  - Analytics: click Analytics for status/strand breakdowns and bar chart
  - Refresh: reloads from DB

- Admin Panel
  - Add: click Add, fill in fields (LRN, Last Name, First Name required), Save
  - Edit: select row → Edit → adjust fields → Save
  - Delete: select row → Delete → confirm
  - Search/Sort/Refresh available at the top

### Troubleshooting
- No data in tables:
  - Ensure MySQL is running and `students` table exists
  - Verify `data_handler.get_connection()` credentials
- CRUD or status updates fail:
  - Confirm your MySQL user has INSERT/UPDATE/DELETE permissions
- Images not showing:
  - Ensure `EduTech.jpg` and `EduTechSchool.jpg` are present in the project root

### Project Structure
- `Main.py`: PyQt6 main window, global shortcut, fade transitions
- `Login.py`: PyQt6 login; starts Dashboard/Admin in separate processes
- `Dashboard.py`: Tkinter staff dashboard with analytics and status updates
- `admin.py`: Tkinter admin panel with full CRUD
- `database.py`: DB helpers (`fetch/create/update/delete`)
- `data_handler.py`: connection factory (`get_connection`)

### Notes
- Credentials are hardcoded for demo purposes in `Login.py`.
- Ensure the database columns align with the code’s usage.
