from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDateTime
from interfaces.admin.admin_manage_appointment import Ui_Frame
from connection import get_connection
from global_file import global_value


class AdminManageAppointmentController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_appointment_id = None
        self.current_row = None

        self.load_branches()

        self.load_appointments()

        self.ui.ap_search_doctor_cnic_input.textChanged.connect(self.load_appointments)
        self.ui.ap_search_patient_cnic_input.textChanged.connect(self.load_appointments)
        self.ui.ap_search_room_id_input.textChanged.connect(self.load_appointments)
        self.ui.search_status_dropbox.currentIndexChanged.connect(self.load_appointments)
        self.ui.admin_add_button.clicked.connect(self.add_appointment)
        self.ui.admin_delete_button.clicked.connect(self.delete_appointment)
        self.ui.admin_update_button.clicked.connect(self.update_appointment)
        

        self.ui.tableView.clicked.connect(self.populate_fields_from_table)


    def load_branches(self):
        self.ui.appointment_branch.clear()
        branches = global_value.fetch_branches()  
        for name, branch_id in branches.items():
            self.ui.appointment_branch.addItem(name, branch_id)


    def load_appointments(self):
        doctor_cnic = self.ui.ap_search_doctor_cnic_input.text().strip() or None
        patient_cnic = self.ui.ap_search_patient_cnic_input.text().strip() or None
        room_id_text = self.ui.ap_search_room_id_input.text().strip()
        status_text = self.ui.search_status_dropbox.currentText()

        room_id_param = int(room_id_text) if room_id_text.isdigit() else None
        status_param = None if status_text == "All" else status_text

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            EXEC GetAppointments
                @doctor_cnic = ?,
                @patient_cnic = ?,
                @room_id = ?,
                @status = ?
        """, (
            doctor_cnic,
            patient_cnic,
            room_id_param,
            status_param
        ))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        headers = [
            "Appointment ID", "Patient Name", "Patient CNIC",
            "Doctor Name", "Doctor CNIC", "Status",
            "Room ID", "Start Time", "End Time", "Branch Name"
        ]

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)
        for row in rows:
            model.appendRow([QStandardItem(str(col)) for col in row])

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.verticalHeader().setVisible(False)



    def populate_fields_from_table(self, index):
        model = self.ui.tableView.model()
        row_idx = index.row()

        headers = [
            "appointment_id", "patient_name", "patient_cnic", "doctor_name",
            "doctor_cnic", "status", "room_id", "start_time",
            "end_time", "branch_name"
        ]

        self.current_row = {header: model.index(row_idx, col).data() for col, header in enumerate(headers)}
        self.selected_appointment_id = self.current_row["appointment_id"]

        self.ui.ap_patient_cnic_input.setText(self.current_row["patient_cnic"])
        self.ui.ap_doctor_cnic_input.setText(self.current_row["doctor_cnic"])
        self.ui.ap_status_dropbox.setCurrentText(self.current_row["status"])
        self.ui.ap_room_id_input.setText(str(self.current_row["room_id"]))

        branch_name = self.current_row["branch_name"]
        index = self.ui.appointment_branch.findText(branch_name)
        if index != -1:
            self.ui.appointment_branch.setCurrentIndex(index)

        start_dt = QDateTime.fromString(self.current_row["start_time"], "yyyy-MM-dd hh:mm AP")
        end_dt = QDateTime.fromString(self.current_row["end_time"], "yyyy-MM-dd hh:mm AP")
        self.ui.ap_assignment_start_input.setDateTime(start_dt)
        self.ui.ap_assignment_end_input.setDateTime(end_dt)


    def add_appointment(self):
        # Read values from UI
        patient_cnic = self.ui.ap_patient_cnic_input.text().strip()
        doctor_cnic = self.ui.ap_doctor_cnic_input.text().strip()
        status = self.ui.ap_status_dropbox.currentText()
        room_id_text = self.ui.ap_room_id_input.text().strip()
        branch_index = self.ui.appointment_branch.currentIndex()
        branch_id = self.ui.appointment_branch.itemData(branch_index)
        start_dt = self.ui.ap_assignment_start_input.dateTime().toPython()
        end_dt = self.ui.ap_assignment_end_input.dateTime().toPython()

        if not patient_cnic:
            self.ui.admin_message_label.setText("Patient CNIC is required!")
            return
        if not doctor_cnic:
            self.ui.admin_message_label.setText("Doctor CNIC is required!")
            return
        if not room_id_text.isdigit():
            self.ui.admin_message_label.setText("Room ID must be a number!")
            return
        if not branch_id:
            self.ui.admin_message_label.setText("Select a branch!")
            return
        if start_dt >= end_dt:
            self.ui.admin_message_label.setText("End time must be after start time!")
            return

        room_id = int(room_id_text)

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC AddAppointment
                    @branch_id = ?,
                    @patient_cnic = ?,
                    @doctor_cnic = ?,
                    @status = ?,
                    @room_id = ?,
                    @assignment_start = ?,
                    @assignment_end = ?
            """, (branch_id, patient_cnic, doctor_cnic, status, room_id, start_dt, end_dt))
            conn.commit()
            self.ui.admin_message_label.setText("Appointment added successfully!")
            self.clear_appointment_fields()


        except Exception as e:
            self.ui.admin_message_label.setText(global_value.throw_exception(e))

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

        self.load_appointments()


    def delete_appointment(self):
        if not self.selected_appointment_id:
            self.ui.admin_message_label.setText("Select an appointment first!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC DeleteAppointment @appointment_id = ?
            """, (self.selected_appointment_id,))
            conn.commit()
            self.ui.admin_message_label.setText("Appointment deleted successfully!")

        except Exception as e:
            msg = global_value.throw_exception(e)
            self.ui.admin_message_label.setText(msg)

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

        self.load_appointments()
        self.clear_appointment_fields()
        self.selected_appointment_id = None


    def update_appointment(self):
        if not self.selected_appointment_id:
            self.ui.admin_message_label.setText("Select an appointment first!")
            return

        try:
            patient_cnic = self.ui.ap_patient_cnic_input.text().strip()
            doctor_cnic = self.ui.ap_doctor_cnic_input.text().strip()
            status = self.ui.ap_status_dropbox.currentText()
            room_id_text = self.ui.ap_room_id_input.text().strip()
            branch_id = self.ui.appointment_branch.currentData()
            assignment_start = self.ui.ap_assignment_start_input.dateTime().toPython()
            assignment_end = self.ui.ap_assignment_end_input.dateTime().toPython()

            if not room_id_text.isdigit():
                self.ui.admin_message_label.setText("Room ID must be a number")
                return

            room_id = int(room_id_text)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC UpdateAppointment
                    @appointment_id = ?,
                    @branch_id = ?,
                    @patient_cnic = ?,
                    @doctor_cnic = ?,
                    @status = ?,
                    @room_id = ?,
                    @assignment_start = ?,
                    @assignment_end = ?
            """, (
                self.selected_appointment_id,
                branch_id,
                patient_cnic,
                doctor_cnic,
                status,
                room_id,
                assignment_start,
                assignment_end
            ))
            conn.commit()
            cursor.close()
            conn.close()

            self.ui.admin_message_label.setText("Appointment updated successfully!")
            self.load_appointments() 
            self.clear_appointment_fields()

        except Exception as e:
            msg = global_value.throw_exception(e)
            self.ui.admin_message_label.setText(msg)




    def clear_appointment_fields(self):
        self.ui.ap_patient_cnic_input.clear()
        self.ui.ap_doctor_cnic_input.clear()
        self.ui.ap_status_dropbox.setCurrentIndex(0)
        self.ui.ap_room_id_input.clear()
        self.ui.ap_assignment_start_input.setDateTime(self.ui.ap_assignment_start_input.minimumDateTime())
        self.ui.ap_assignment_end_input.setDateTime(self.ui.ap_assignment_end_input.minimumDateTime())
        self.ui.appointment_branch.setCurrentIndex(0)


