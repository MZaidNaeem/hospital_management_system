from PySide6.QtWidgets import QWidget
from interfaces.doctor.doctor_mange_appointment import Ui_Frame
from global_file import global_value   
from connection import get_connection



class DoctorManageAppointmentController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("Manage Appointments")

        

    