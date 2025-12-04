from PySide6.QtWidgets import QWidget
from interfaces.patient.patient_main_interface import Ui_Frame
from global_file import global_value


class PatientMainInterfaceController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        print("In Patient", global_value.current_user)


    def show_interface(self):
        self.show()
