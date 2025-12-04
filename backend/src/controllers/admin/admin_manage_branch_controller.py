from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_manage_branch import Ui_Frame

class AdminManageBranchController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

    def show_interface(self):
        self.show()
