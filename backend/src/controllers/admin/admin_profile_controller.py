from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_profile import Ui_Frame


class AdminProfileController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("My Profile")


    def show_interface(self):
        self.show()
