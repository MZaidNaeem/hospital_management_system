from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import pyodbc

from interfaces.admin.admin_report_interface import Ui_Frame
from connection import get_connection  # Your DB connection function


class AdminReportController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.data = None  

        # Connect signals
        self.ui.comboBox.currentTextChanged.connect(self.load_report)
        self.ui.comboBox_2.currentTextChanged.connect(self.load_report)
        self.ui.xlxs_button.clicked.connect(self.export_to_xlsx)

        self.load_report()

    def get_report(self, report_type: str, period: str):
        """
        Fetch report from SQL Server based on report_type and period.
        """
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if report_type == "BRANCH":
                cursor.execute("EXEC dbo.GetBranchLevelReport @filter_type=?", period)
            elif report_type == "ROOM":
                cursor.execute("EXEC dbo.GetRoomLevelReport @filter_type=?", period)
            elif report_type == "DOCTOR":
                cursor.execute("EXEC dbo.GetDoctorLevelReport @filter_type=?", period)
            elif report_type == "PATIENT":
                cursor.execute("EXEC dbo.GetPatientLevelReport @filter_type=?", period)
            else:
                return []

            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(columns, row)) for row in rows]

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch report:\n{str(e)}")
            return []
        finally:
            cursor.close()
            conn.close()

    def load_report(self):
        """
        Load report into QTableView based on selected type and period.
        """
        report_type = self.ui.comboBox.currentText()
        period = self.ui.comboBox_2.currentText()
        self.data = self.get_report(report_type, period)

        if not self.data:
            # Clear table
            self.ui.tableView.setModel(QStandardItemModel())
            return

        model = QStandardItemModel()
        headers = list(self.data[0].keys())
        model.setHorizontalHeaderLabels(headers)

        for row_data in self.data:
            row_items = [QStandardItem(str(row_data[col])) for col in headers]
            model.appendRow(row_items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

    def export_to_xlsx(self):
        """
        Export current report data to XLSX.
        """
        if not self.data:
            QMessageBox.warning(self, "No Data", "No report data to export!")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "Excel Files (*.xlsx)")
        if not path:
            return

        try:
            df = pd.DataFrame(self.data)
            df.to_excel(path, index=False)
            QMessageBox.information(self, "Success", f"Report exported successfully:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export report:\n{str(e)}")
