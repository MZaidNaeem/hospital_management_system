from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_profile import Ui_Frame
from global_file import global_value   
from connection import get_connection
import re
from PySide6.QtWidgets import QMessageBox



class AdminProfileController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("My Profile")

        self.load_admin_data()
        self.ui.admin_update_button.clicked.connect(self.update_admin_profile)
        self.ui.admin_delete_button.clicked.connect(self.delete_admin_profile)

        

    def load_admin_data(self):
        user = global_value.current_user
        
        self.ui.admin_first_name_input.setText(user["first_name"])
        self.ui.admin_last_name_input.setText(user["last_name"])
        self.ui.admin_email_input.setText(user["email"])
        self.ui.admin_cnic_input.setText(user["cnic"])
        self.ui.admin_password_input.setText(user["password"])


    def update_admin_profile(self):
        user = global_value.current_user

        # Fetch updated values from inputs
        first_name = self.ui.admin_first_name_input.text()
        last_name = self.ui.admin_last_name_input.text()
        email = self.ui.admin_email_input.text()
        cnic = self.ui.admin_cnic_input.text()
        password = self.ui.admin_password_input.text()


# ----- Validations -----
        # ----- Validations -----
        name_pattern = r"^[A-Za-z ]+$"  # letters and spaces
        if not re.match(name_pattern, first_name):
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("First name can contain only letters and spaces.")
            return

        if not re.match(name_pattern, last_name):
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("Last name can contain only letters and spaces.")
            return

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, email):
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("Email must be valid (e.g., user@example.com).")
            return
        
        cnic_pattern = r"^\d{13}$"  # exactly 13 digits
        if not re.match(cnic_pattern, cnic):
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("CNIC must be exactly 13 digits.")
            return
        
        password_pattern = r"^.{8,}$"

        if not re.match(password_pattern, password):
            self.ui.admin_message_label.setText("Password must be at least 8 characters long!")
            return
        
      
        if not first_name or not last_name or not email or not cnic or not password:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("All fields are required.")
            return






        admin_id = user["user_id"]  

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC UpdateAdminProfile 
                    @admin_id = ?, 
                    @first_name = ?, 
                    @last_name = ?, 
                    @email = ?, 
                    @cnic = ?, 
                    @password = ?
            """, (admin_id, first_name, last_name, email, cnic, password))
            conn.commit()
            cursor.close()
            conn.close()

            global_value.current_user["first_name"] = first_name
            global_value.current_user["last_name"] = last_name
            global_value.current_user["email"] = email
            global_value.current_user["cnic"] = cnic
            global_value.current_user["password"] = password

            self.ui.admin_message_label.setStyleSheet("color: green;")
            self.ui.admin_message_label.setText("Profile updated successfully!")

        except Exception as e:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText(f"Failed to update profile due to duplicate cnic or email")




    def delete_admin_profile(self):
        user = global_value.current_user
        admin_id = user["user_id"]

        # Show confirmation dialog
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

                # Call the delete procedure (trigger handles soft delete)
                cursor.execute("EXEC DeleteAdminProfile @admin_id = ?", (admin_id,))
                conn.commit()
                cursor.close()
                conn.close()

                # Clear global user info
                global_value.current_user = {}

                # Show success message
                self.ui.admin_message_label.setStyleSheet("color: green;")
                self.ui.admin_message_label.setText("Profile deleted successfully!")

                # Close the profile window
                self.close()
                global_value.current_user_window.close()

            except Exception as e:
                self.ui.admin_message_label.setStyleSheet("color: red;")
                self.ui.admin_message_label.setText(f"Failed to delete profile: {e}")
        else:
            # User clicked No
            self.ui.admin_message_label.setStyleSheet("color: black;")
            self.ui.admin_message_label.setText("Profile deletion cancelled.")




