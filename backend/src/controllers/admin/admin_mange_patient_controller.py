from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_mange_patient import Ui_Frame
from global_file import global_value   


class AdminManagePatientController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

