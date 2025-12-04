from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from connection import get_connection
from interfaces.admin.admin_manage_doctor import Ui_Frame

class AdminManageDoctorController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_doctor_id = None
        self.current_row = None
        self.branch_dict = {}

        self.load_branches()

        self.ui.doctor_add_button.clicked.connect(self.insert_doctor)
        self.ui.doctor_update_button.clicked.connect(self.update_doctor)
        self.ui.doctor_search_button.clicked.connect(self.load_doctors)
        self.ui.tableView.clicked.connect(self.doctor_row_clicked)

        self.load_doctors()

    def load_branches(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, branch_name FROM Branches ORDER BY branch_name")
        branches = cursor.fetchall()
        conn.close()

        self.ui.doctor_branch_dropbox.clear()
        self.branch_dict = {}

        for index, (branch_id, branch_name) in enumerate(branches):
            self.ui.doctor_branch_dropbox.addItem(branch_name)
            self.branch_dict[branch_name] = (index, branch_id)

    def load_doctors(self):
        filter_cnic = self.ui.doctor_search_input.toPlainText().strip()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC GetDoctors ?", filter_cnic if filter_cnic else None)
        data = cursor.fetchall()
        conn.close()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "Doctor ID", "Branch ID", "Branch Name", "First Name", "Last Name",
            "Email", "CNIC", "Password", "Specialty", "Contact", "Created At", "Deleted"
        ])

        for row in data:
            items = [QStandardItem(str(col)) for col in row]
            model.appendRow(items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.resizeColumnsToContents()

    def doctor_row_clicked(self, index):
        row = index.row()
        model = self.ui.tableView.model()
        self.current_row = {
            "doctor_id": model.index(row, 0).data(),
            "branch_id": model.index(row, 1).data(),
            "branch_name": model.index(row, 2).data(),
            "first_name": model.index(row, 3).data(),
            "last_name": model.index(row, 4).data(),
            "email": model.index(row, 5).data(),
            "cnic": model.index(row, 6).data(),
            "password": model.index(row, 7).data(),
            "specialty": model.index(row, 8).data(),
            "contact": model.index(row, 9).data(),
            "created_at": model.index(row, 10).data(),
            "deleted": model.index(row, 11).data(),
        }
        self.selected_doctor_id = self.current_row["doctor_id"]

        self.ui.doctor_first_name_input.setText(self.current_row["first_name"])
        self.ui.doctor_last_name_input.setText(self.current_row["last_name"])
        self.ui.doctor_email_input.setText(self.current_row["email"])
        self.ui.doctor_cnic_input.setText(self.current_row["cnic"])
        self.ui.doctor_password_input.setText(self.current_row["password"])
        self.ui.doctor_speciality_input.setText(self.current_row["specialty"])
        self.ui.doctor_contact_input.setText(self.current_row["contact"])

        branch_name = self.current_row["branch_name"]
        if branch_name in self.branch_dict:
            index, _ = self.branch_dict[branch_name]
            self.ui.doctor_branch_dropbox.setCurrentIndex(index)

        self.ui.doctor_delete_dropbox.setCurrentText(self.current_row["deleted"])

    def insert_doctor(self):
        fname = self.ui.doctor_first_name_input.text().strip()
        lname = self.ui.doctor_last_name_input.toPlainText().strip()
        email = self.ui.doctor_email_input.toPlainText().strip()
        cnic = self.ui.doctor_cnic_input.text().strip()
        password = self.ui.doctor_password_input.text().strip()
        specialty = self.ui.doctor_speciality_input.text().strip()
        contact = self.ui.doctor_contact_input.toPlainText().strip()
        branch_name = self.ui.doctor_branch_dropbox.currentText()
        deleted = 1 if self.ui.doctor_delete_dropbox.currentText() == "YES" else 0

        if not all([fname, lname, email, cnic, password, specialty, contact, branch_name]):
            self.ui.doctor_message_label.setStyleSheet("color: red;")
            self.ui.doctor_message_label.setText("All fields are required.")
            return

        branch_id = self.branch_dict[branch_name][1]

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC InsertDoctor ?, ?, ?, ?, ?, ?, ?, ?, ?
            """, (fname, lname, email, cnic, password, specialty, contact, branch_id, deleted))
            conn.commit()
            cursor.close()
            conn.close()

            self.ui.doctor_message_label.setStyleSheet("color: green;")
            self.ui.doctor_message_label.setText("Doctor added successfully!")
            self.load_doctors()
            self.clear_inputs()

        except Exception as e:
            msg = str(e)
            if "CNIC already exists in this branch" in msg:
                self.ui.doctor_message_label.setText("Error: CNIC already exists in this branch.")
            elif "CNIC and Password combination already exists" in msg:
                self.ui.doctor_message_label.setText("Error: CNIC and Password combination already exists.")
            else:
                self.ui.doctor_message_label.setText("Error: " + msg)
            self.ui.doctor_message_label.setStyleSheet("color: red;")

    def update_doctor(self):
        if not self.current_row:
            self.ui.doctor_message_label.setStyleSheet("color: red;")
            self.ui.doctor_message_label.setText("Please select a doctor first.")
            return

        doctor_id = self.current_row["doctor_id"]
        fname = self.ui.doctor_first_name_input.text().strip()
        lname = self.ui.doctor_last_name_input.toPlainText().strip()
        email = self.ui.doctor_email_input.toPlainText().strip()
        cnic = self.ui.doctor_cnic_input.text().strip()
        password = self.ui.doctor_password_input.text().strip()
        specialty = self.ui.doctor_speciality_input.text().strip()
        contact = self.ui.doctor_contact_input.toPlainText().strip()
        branch_name = self.ui.doctor_branch_dropbox.currentText()
        deleted = 1 if self.ui.doctor_delete_dropbox.currentText() == "YES" else 0

        if not all([fname, lname, email, cnic, password, specialty, contact, branch_name]):
            self.ui.doctor_message_label.setStyleSheet("color: red;")
            self.ui.doctor_message_label.setText("All fields are required.")
            return

        branch_id = self.branch_dict[branch_name][1]

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                EXEC UpdateDoctor ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            """, (doctor_id, fname, lname, email, cnic, password, specialty, contact, branch_id, deleted))
            conn.commit()
            cursor.close()
            conn.close()

            self.ui.doctor_message_label.setStyleSheet("color: green;")
            self.ui.doctor_message_label.setText("Doctor updated successfully!")
            self.load_doctors()
            self.clear_inputs()

        except Exception as e:
            msg = str(e)
            if "CNIC already exists in this branch" in msg:
                self.ui.doctor_message_label.setText("Error: CNIC already exists in this branch.")
            elif "CNIC and Password combination already exists" in msg:
                self.ui.doctor_message_label.setText("Error: CNIC and Password combination already exists.")
            else:
                self.ui.doctor_message_label.setText("Error: " + msg)
            self.ui.doctor_message_label.setStyleSheet("color: red;")

    def clear_inputs(self):
        self.current_row = None
        self.selected_doctor_id = None
        self.ui.doctor_first_name_input.clear()
        self.ui.doctor_last_name_input.clear()
        self.ui.doctor_email_input.clear()
        self.ui.doctor_cnic_input.clear()
        self.ui.doctor_password_input.clear()
        self.ui.doctor_speciality_input.clear()
        self.ui.doctor_contact_input.clear()
        self.ui.doctor_branch_dropbox.setCurrentIndex(0)
        self.ui.doctor_delete_dropbox.setCurrentIndex(1)  # Default NO
        self.ui.doctor_message_label.setText("")
