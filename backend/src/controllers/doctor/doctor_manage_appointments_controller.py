from PySide6.QtWidgets import QWidget, QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem

from interfaces.doctor.doctor_mange_appointment import Ui_Frame
from global_file import global_value
from connection import get_connection


class DoctorManageAppointmentController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("Manage Appointments")

        # Logged-in doctor
        self.doctor_id = global_value.current_user['user_id']
        print("Logged-in doctor ID =", self.doctor_id)

        # Setup model for QTableView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            "Appointment ID", "Patient Name", "Patient CNIC",
            "Status", "Room", "Start Time", "End Time"
        ])

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Connect signals
        self.ui.search_patient_cnic.textChanged.connect(self.load_appointments)
        self.ui.search_status.currentTextChanged.connect(self.load_appointments)
        self.ui.update_button.clicked.connect(self.complete_appointment)

        # Load data initially
        self.load_appointments()

    # ---------------------------------------------------------------------
    # Load Appointments for THIS doctor only
    # ---------------------------------------------------------------------
    def load_appointments(self):
        patient_cnic = self.ui.search_patient_cnic.toPlainText().strip()
        status = self.ui.search_status.currentText()

        if status == "":
            status = None

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                EXEC GetDoctorAppointments
                    @doctor_id=?,
                    @patient_cnic=?, 
                    @status=?
            """, (self.doctor_id, patient_cnic if patient_cnic else None, status))

            rows = cursor.fetchall()

            self.model.removeRows(0, self.model.rowCount())

            for row in rows:
                items = [QStandardItem(str(col)) for col in row]
                self.model.appendRow(items)

            cursor.close()
            conn.close()

        except Exception as e:
            print("Error loading appointments:", str(e))
            self.ui.message_label.setText("Error loading appointments!")

    def complete_appointment(self):
        selected = self.ui.tableView.currentIndex().row()

        if selected == -1:
            self.ui.message_label.setText("Please select an appointment!")
            return

        appointment_id = self.model.item(selected, 0).text()
        current_status = self.model.item(selected, 3).text()

        if current_status != "Scheduled":
            self.ui.message_label.setText("Only scheduled appointments can be completed!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""EXEC CompleteAppointment ?, ? """, (appointment_id, self.doctor_id))

            result = cursor.fetchone()
            rows_updated = result[0]

            conn.commit()
            cursor.close()
            conn.close()

            if rows_updated == 0:
                self.ui.message_label.setText("Failed: Appointment is not scheduled!")
                return
            elif (rows_updated == 1):
                self.ui.message_label.setText("Appointment marked as Completed.")
                self.load_appointments()
                print(appointment_id,self.doctor_id)

        except Exception as e:
            print("Error completing appointment:", str(e))
            self.ui.message_label.setText("Error completing appointment!")

