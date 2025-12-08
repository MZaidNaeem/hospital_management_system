from PySide6.QtWidgets import QWidget
from interfaces.doctor.doctor_profile import Ui_Frame
from global_file import global_value
from connection import get_connection
from PySide6.QtWidgets import QMessageBox


class DoctorProfileController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("My Profile")

        # Load profile
        self.load_doctor_data()

        # Button connections
        self.ui.admin_update_button.clicked.connect(self.update_doctor_data)
        self.ui.admin_delete_button.clicked.connect(self.delete_doctor_account)

    # ---------------------------------------------------
    # LOAD DOCTOR DATA
    # ---------------------------------------------------
    def load_doctor_data(self):
        user = global_value.current_user

        self.ui.first_name_input.setText(user["first_name"])
        self.ui.last_name_input.setText(user["last_name"])
        self.ui.email_input.setText(user["email"])
        self.ui.cnic_input.setText(user["cnic"])
        self.ui.password_input.setText(user["password"])
        self.ui.speciality_input.setText(user["specialty"])
        self.ui.contact_number_input.setText(user["contact_number"])

    # ---------------------------------------------------
    # UPDATE DOCTOR PROFILE USING PROCEDURE
    # ---------------------------------------------------
    def update_doctor_data(self):

        # Fetch current input values
        first_name = self.ui.first_name_input.text()
        last_name = self.ui.last_name_input.text()
        email = self.ui.email_input.text()
        cnic = self.ui.cnic_input.text()
        password = self.ui.password_input.text()
        specialty = self.ui.speciality_input.toPlainText()
        contact_number = self.ui.contact_number_input.toPlainText()

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                EXEC UpdateDoctorProfile 
                    ?, ?, ?, ?, ?, ?, ?, ?
            """, (
                global_value.current_user["user_id"],
                first_name,
                last_name,
                email,
                cnic,
                password,
                specialty,
                contact_number
            ))

            conn.commit()
            cursor.close()
            conn.close()

            # Update global stored user data
            global_value.current_user["first_name"] = first_name
            global_value.current_user["last_name"] = last_name
            global_value.current_user["email"] = email
            global_value.current_user["cnic"] = cnic
            global_value.current_user["password"] = password
            global_value.current_user["specialty"] = specialty
            global_value.current_user["contact_number"] = contact_number

            print(global_value.current_user)

            self.ui.admin_message_label.setText("Profile Updated Successfully")

        except Exception as e:
            msg = global_value.extract_sql_error(e)
            self.ui.admin_message_label.setText(msg)

    # ---------------------------------------------------
    # DELETE ACCOUNT USING PROCEDURE
    # ---------------------------------------------------
    def delete_doctor_account(self):


        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete your profile?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    EXEC DeleteDoctorAccount ?
                """, (global_value.current_user["user_id"],))

                conn.commit()
                cursor.close()
                conn.close()

                global_value.current_user = {}

                self.ui.admin_message_label.setText("Account Deleted Successfully")
                global_value.current_user_window.close()
                self.close()

            except Exception as e:
                msg = global_value.extract_sql_error(e)
                self.ui.admin_message_label.setText(msg)

        else:
            self.ui.admin_message_label.setStyleSheet("color: black;")
            self.ui.admin_message_label.setText("Profile deletion cancelled.")