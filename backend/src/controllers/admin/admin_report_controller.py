from PySide6.QtWidgets import QWidget
from interfaces.admin.admin_report_interface import Ui_Frame
from connection import get_connection
from global_file import global_value


class AdminrReportController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_appointment_id = None
        self.current_row = None
