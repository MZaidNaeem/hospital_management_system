from PySide6.QtWidgets import QWidget
from interfaces.doctor.doctor_main_interface import Ui_Frame
from controllers.patient.patient_mange_appointments_controller import PatientManageAppointmentController
from controllers.patient.patient_profile_edit_controller import PatientProfileController
from global_file import global_value


class PatientMainInterfaceController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        print(global_value.current_user)

        self.ui.edit_profile_button.clicked.connect(self.open_profile_edit)
        self.ui.appointment_button.clicked.connect(self.open_manage_appointments)


    def open_profile_edit(self):
        self.window = PatientProfileController()
        self.window.show()

    def open_manage_appointments(self):
        self.window = PatientManageAppointmentController()
        self.window.show()

