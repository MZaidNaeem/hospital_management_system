from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_manage_rooms import Ui_Frame

class AdminManageRoomsController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

