from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_main_interface import Ui_Frame

from controllers.admin.admin_mange_patient_controller import AdminManagePatientController
from controllers.admin.admin_manage_doctor_controller import AdminManageDoctorController
from controllers.admin.admin_manage_rooms_controller import AdminManageRoomsController
from controllers.admin.admin_manage_branch_controller import AdminManageBranchController
from controllers.admin.admin_manage_appointment_controller import AdminManageAppointmentController
from controllers.admin.admin_profile_controller import AdminProfileController
from controllers.admin.admin_mange_controller import AdminManageAdminsController
from controllers.admin.admin_report_controller import AdminrReportController
from global_file import global_value   



class AdminMainInterfaceController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        print("In Admin", global_value.current_user)

        self.ui.admin_manage_patients.clicked.connect(self.open_manage_patients)
        self.ui.admin_manage_doctors.clicked.connect(self.open_manage_doctors)
        self.ui.admin_manage_rooms.clicked.connect(self.open_manage_rooms)
        self.ui.admin_manage_branches.clicked.connect(self.open_manage_branches)
        self.ui.admin_manage_appointments.clicked.connect(self.open_manage_appointments)
        self.ui.admin_my_profile.clicked.connect(self.open_profile)
        self.ui.admin_mange_admins.clicked.connect(self.open_manage_admins)
        self.ui.report_button.clicked.connect(self.open_report_admins)


    def open_manage_patients(self):
        self.window = AdminManagePatientController()
        self.window.show()

    def open_manage_doctors(self):
        self.window = AdminManageDoctorController()
        self.window.show()

    def open_manage_rooms(self):
        self.window = AdminManageRoomsController()
        self.window.show()

    def open_manage_branches(self):
        self.window = AdminManageBranchController()
        self.window.show()

    def open_manage_appointments(self):
        self.window = AdminManageAppointmentController()
        self.window.show()


    def open_profile(self):
        self.window = AdminProfileController()
        self.window.show()

    def open_manage_admins(self):
        self.window = AdminManageAdminsController()
        self.window.show()


    def open_report_admins(self):
        self.window = AdminrReportController()
        self.window.show()