from PySide6.QtWidgets import QWidget
from interfaces.patient.patient_profile import Ui_Frame
from global_file import global_value   
from connection import get_connection



class PatientProfileController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("My Profile")

        

    