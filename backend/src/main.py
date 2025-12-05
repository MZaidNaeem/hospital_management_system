from PySide6.QtWidgets import QApplication, QWidget
from connection import get_connection
import sys

from interfaces.login_ui import Ui_Frame
from controllers.admin.admin_main_interface_controller import AdminMainInterfaceController
from controllers.doctor.doctor_main_interface_controller import DoctorMainInterfaceController
from controllers.patient.patient_main_interface_controller import PatientMainInterfaceController
from global_file import global_value


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.current_window = None
        self.ui.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        cnic = self.ui.cnic_input.text()
        password = self.ui.password_input.text()
        role = self.ui.login_as_input.currentText()

        conn = get_connection()
        
        if not conn:
            self.ui.error_label.setText("Database connection failed!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("EXEC LoginUser ?, ?, ?", cnic, password, role)
            row = cursor.fetchone()

            if row:
                global_value.current_user = self.row_to_dict(cursor, row)
                global_value.current_user['role'] = role

                if role == "ADMIN":
                    self.open_admin_main_interface()

                elif role == "DOCTOR":
                    self.open_doctor_main_interface()

                elif role == "PATIENT":
                    self.open_patient_main_interface()

                self.ui.cnic_input.setText("")
                self.ui.password_input.setText("")

            
            else:
                self.ui.error_label.setText("Invalid CNIC, password, or role!")
            
        finally:
            cursor.close()
            conn.close()

                    
    def row_to_dict(self,cursor, row):
        """Convert a pyodbc row tuple into a dictionary using cursor.description."""
        return {column[0]: row[idx] for idx, column in enumerate(cursor.description)}
                    

    def open_admin_main_interface(self):
        global_value.current_user_window = AdminMainInterfaceController()
        global_value.current_user_window.show()

    def open_doctor_main_interface(self):
        global_value.current_user_window = DoctorMainInterfaceController()
        global_value.current_user_window.show()
    
    def open_patient_main_interface(self):
        global_value.current_user_window = PatientMainInterfaceController()
        global_value.current_user_window.show()


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
