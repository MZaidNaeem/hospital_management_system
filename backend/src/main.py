from PySide6.QtWidgets import QApplication, QWidget
from interfaces.login_ui import Ui_Frame  
import sys
from connection import get_connection
from interfaces.admin.admin_ui import Ui_Frame as AdminUI
from interfaces.doctor.doctor_ui import Ui_Frame as DoctorUI
from interfaces.patient.patient_ui import Ui_Frame as PatientUI
from interfaces.staff.staff_ui import Ui_Frame as StaffUI

from interfaces.admin.manage_admin_ui import Ui_Frame as AdminsUI
from interfaces.admin.profile_ui import Ui_Frame as ProfileUI
from interfaces.admin.rooms_ui import Ui_Frame as RoomsUI
from interfaces.admin.assignments_ui import Ui_Frame as AssignmentsUI
from interfaces.admin.staff_ui import Ui_Frame as StaffUI
from interfaces.admin.billing_ui import Ui_Frame as BillingUI
from interfaces.admin.doctors_ui import Ui_Frame as DoctorsUI
from interfaces.admin.appointments_ui import Ui_Frame as AppointmentsUI
from interfaces.admin.patients_ui import Ui_Frame as PatientsUI
from interfaces.admin.medical_record_ui import Ui_Frame as MedicalRecordUI
from interfaces.admin.branches_ui import Ui_Frame as BranchesUI
from interfaces.admin.cleaning_service_ui import Ui_Frame as CleaningServiceUI



class MyApp(QWidget):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.handle_login)

        # Stores logged-in user
        self.logged_user = None

        # Stores current open admin window
        self.current_small_window = None

# ------------------------------------------------
#                  LOGIN HANDLER
# ------------------------------------------------
        
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

            self.logged_user = user_data

            self.ui.error_label.setText(f"Login successful as {role.lower()}")
            self.ui.error_label.setStyleSheet("color: green;")

            self.open_role_window(role)

        else:
            self.ui.error_label.setText("Invalid CNIC or password")
            self.ui.error_label.setStyleSheet("color: red;")

        cursor.close()
        conn.close()


# ------------------------------------------------
#        OPEN ROLE-SPECIFIC MAIN WINDOW
# ------------------------------------------------

    def open_role_window(self, role):

        # Close previous window if exists
        try:
            self.role_window.close()
            self.current_admin_window
            if self.current_small_window:
                self.current_small_window.close()
        except:
            pass

        if role == "ADMIN":
            self.role_window = QWidget()
            self.role_ui = AdminUI()
            self.role_ui.setupUi(self.role_window)

            # Connect admin options
            self.role_ui.admin_mange_admins.clicked.connect(self.open_manage_admins)
            self.role_ui.admin_my_profile.clicked.connect(self.open_my_profile)
            self.role_ui.admin_manage_rooms.clicked.connect(self.open_manage_rooms)
            self.role_ui.admin_manage_assignments.clicked.connect(self.open_assignments)
            self.role_ui.admin_manage_staff.clicked.connect(self.open_manage_staff)
            self.role_ui.admin_manage_billing.clicked.connect(self.open_billing)
            self.role_ui.admin_manage_doctors.clicked.connect(self.open_manage_doctors)
            self.role_ui.admin_manage_appointments.clicked.connect(self.open_appointments)
            self.role_ui.admin_manage_patients.clicked.connect(self.open_manage_patients)
            self.role_ui.admin_manage_medical_record.clicked.connect(self.open_medical_record)
            self.role_ui.admin_manage_branches.clicked.connect(self.open_manage_branches)
            self.role_ui.admin_manage_cleaning_service.clicked.connect(self.open_cleaning_service)

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


# ------------------------------------------------
#      SINGLE-WINDOW BEHAVIOR 
# ------------------------------------------------

    def open_single_window(self, ui_class):
        """Closes previous admin window and opens a new one."""
        if self.current_small_window:
            self.current_small_window.close()

        self.current_small_window = QWidget()
        ui = ui_class()
        ui.setupUi(self.current_small_window)
        self.current_small_window.show()

        return ui


# ------------------------------------------------
#             ADMIN PORTAL WINDOWS
# ------------------------------------------------

    def open_my_profile(self):
        self.profile_ui = self.open_single_window(ProfileUI)

        # Fill user data
        self.profile_ui.admin_first_name_input.setText(self.logged_user['first_name'])
        self.profile_ui.admin_last_name_input.setText(self.logged_user['last_name'])
        self.profile_ui.admin_email_input.setText(self.logged_user['email'])
        self.profile_ui.admin_cnic_input.setText(self.logged_user['cnic'])
        self.profile_ui.admin_password_input.setText(self.logged_user['password'])

        self.profile_ui.admin_update.clicked.connect(self.update_admin_profile)


    def update_admin_profile(self):
        first_name = self.profile_ui.admin_first_name_input.text()
        last_name = self.profile_ui.admin_last_name_input.text()
        email = self.profile_ui.admin_email_input.text()
        password = self.profile_ui.admin_password_input.text()
        cnic = self.profile_ui.admin_cnic_input.text()

        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    UPDATE Admin
                    SET first_name = ?, last_name = ?, email = ?, password = ?, cnic = ?
                    WHERE admin_id = ?
                """
                cursor.execute(query, (
                    first_name, last_name, email, password, cnic, 
                    self.logged_user['admin_id']
                ))
                conn.commit()

                # Update local memory
                self.logged_user['first_name'] = first_name
                self.logged_user['last_name'] = last_name
                self.logged_user['email'] = email
                self.logged_user['password'] = password
                self.logged_user['cnic'] = cnic

                self.profile_ui.message_label.setText("Profile updated successfully")
                self.profile_ui.message_label.setStyleSheet("color: green;")
            except Exception as e:
                self.profile_ui.message_label.setText(f"Error: {str(e)}")
                self.profile_ui.message_label.setStyleSheet("color: red;")
            finally:
                cursor.close()
                conn.close()


    def open_manage_admins(self):
        self.admins_ui = self.open_single_window(AdminsUI)

    def open_manage_rooms(self):
        self.rooms_ui = self.open_single_window(RoomsUI)

    def open_assignments(self):
        self.assign_ui = self.open_single_window(AssignmentsUI)

    def open_manage_staff(self):
        self.staff_ui = self.open_single_window(StaffUI)

    def open_billing(self):
        self.billing_ui = self.open_single_window(BillingUI)

    def open_manage_doctors(self):
        self.doctors_ui = self.open_single_window(DoctorsUI)

    def open_appointments(self):
        self.appt_ui = self.open_single_window(AppointmentsUI)

    def open_manage_patients(self):
        self.patients_ui = self.open_single_window(PatientsUI)

    def open_medical_record(self):
        self.medrec_ui = self.open_single_window(MedicalRecordUI)

    def open_manage_branches(self):
        self.branches_ui = self.open_single_window(BranchesUI)

    def open_cleaning_service(self):
        self.clean_ui = self.open_single_window(CleaningServiceUI)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
