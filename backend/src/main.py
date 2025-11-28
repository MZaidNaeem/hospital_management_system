from PySide6.QtWidgets import QApplication, QWidget
from interfaces.login_ui import Ui_Frame  
import sys
from connection import get_connection
from interfaces.admin.admin_ui import Ui_Frame as AdminUI
from interfaces.doctor.doctor_ui import Ui_Frame as DoctorUI
from interfaces.patient.patient_ui import Ui_Frame as PatientUI
from interfaces.staff.staff_ui import Ui_Frame as StaffUI


class MyApp(QWidget):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.handle_login)
        
    def handle_login(self):
        cnic = self.ui.cnic_input.text()
        password = self.ui.password_input.text()
        role = self.ui.login_as_input.currentText()

        conn = get_connection()

        if not conn:
            self.ui.error_label.setText("Database connection failed")
            self.ui.error_label.setStyleSheet("color: red;")
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

            self.ui.error_label.setText(f"Login successful as {role.lower()}")
            self.ui.error_label.setStyleSheet("color: green;")

            print(f"\n--- {role} Data ---")
            for key, value in user_data.items():
                print(f"{key}: {value}")
            
            self.open_role_window(role)


        else:
            self.ui.error_label.setText("Invalid CNIC or password")
            self.ui.error_label.setStyleSheet("color: red;")

        cursor.close()
        conn.close()

    def open_role_window(self, role):
        if role == "ADMIN":
            self.role_window = QWidget()
            self.role_ui = AdminUI()
            self.role_ui.setupUi(self.role_window)
        elif role == "DOCTOR":
            self.role_window = QWidget()
            self.role_ui = DoctorUI()
            self.role_ui.setupUi(self.role_window)
        elif role == "PATIENT":
            self.role_window = QWidget()
            self.role_ui = PatientUI()
            self.role_ui.setupUi(self.role_window)
        elif role == "STAFF":
            self.role_window = QWidget()
            self.role_ui = StaffUI()
            self.role_ui.setupUi(self.role_window)

        self.role_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
