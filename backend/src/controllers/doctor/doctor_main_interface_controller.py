from PySide6.QtWidgets import QWidget
from interfaces.doctor.doctor_main_interface import Ui_Frame
from global_file import global_value


class DoctorMainInterfaceController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        print("In Doctor", global_value.current_user)


    def show_interface(self):
        self.show()
