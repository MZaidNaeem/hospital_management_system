from connection import get_connection

def handle_login(ui):
    """
    Handles login for all roles.
    `ui` is the Ui_Frame instance from your QWidget.
    """
    cnic = ui.cnic_input.text()
    password = ui.password_input.text()
    role = ui.login_as_input.currentText()

    conn = get_connection()
    if not conn:
        ui.error_label.setText("Database connection failed")
        ui.error_label.setStyleSheet("color: red;")
        return

    cursor = conn.cursor()

    role_table_map = {
        "ADMIN": "Admin",
        "DOCTOR": "Doctors",
        "PATIENT": "Patients",
        "STAFF": "Staff"
    }

    table = role_table_map.get(role)
    query = f"SELECT * FROM {table} WHERE cnic = ? AND password = ?"
    cursor.execute(query, (cnic, password))
    row = cursor.fetchone()

    if row:
        columns = [column[0] for column in cursor.description]
        user_data = dict(zip(columns, row))

        ui.error_label.setText(f"Login successful as {role.lower()}")
        ui.error_label.setStyleSheet("color: green;")

        print(f"\n--- {role} Data ---")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        ui.error_label.setText("Invalid CNIC or password")
        ui.error_label.setStyleSheet("color: red;")

    cursor.close()
    conn.close()
