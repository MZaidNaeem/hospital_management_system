from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from interfaces.admin.admin_mange_patient import Ui_Frame
from connection import get_connection


class AdminManagePatientController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_patient_id = None
        self.load_patients()

        self.ui.patient_add_button.clicked.connect(self.add_patient)
        self.ui.patient_update_button.clicked.connect(self.update_patient)
        self.ui.patinet_search_button.clicked.connect(self.load_patients)

        self.ui.tableView.clicked.connect(self.fill_fields_from_table)

    def load_patients(self):
        filter_cnic = self.ui.patinet_search_input.toPlainText().strip()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC GetPatients ?", filter_cnic if filter_cnic else None)
        data = cursor.fetchall()
        conn.close()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "Patient ID", "First Name", "Last Name", "Email",
            "CNIC", "Password", "Gender", "Contact",
            "Created At", "Deleted"
        ])

        for row in data:
            items = [QStandardItem(str(col)) for col in row]
            model.appendRow(items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.resizeColumnsToContents()


    def fill_fields_from_table(self, index):
        row = index.row()
        model = self.ui.tableView.model()

        self.selected_patient_id = model.index(row, 0).data()
        self.ui.patient_first_name_input.setText(model.index(row, 1).data())
        self.ui.patient_last_name_input.setPlainText(model.index(row, 2).data())
        self.ui.patient_email_input.setPlainText(model.index(row, 3).data())
        self.ui.patient_cnic_input.setText(model.index(row, 4).data())
        self.ui.patient_password_input.setText(model.index(row, 5).data())
        self.ui.patient_gender_dropbox.setCurrentText(model.index(row, 6).data())
        self.ui.patient_contact_input.setPlainText(model.index(row, 7).data())
        self.ui.patient_delete_input.setText(model.index(row, 9).data())

    # ----------------------------------------------------
    # ADD PATIENT
    # ----------------------------------------------------
    def add_patient(self):
        fname = self.ui.patient_first_name_input.text()
        lname = self.ui.patient_last_name_input.toPlainText()
        email = self.ui.patient_email_input.toPlainText()
        cnic = self.ui.patient_cnic_input.text()
        password = self.ui.patient_password_input.text()
        gender = self.ui.patient_gender_dropbox.currentText()
        contact = self.ui.patient_contact_input.toPlainText()

        deleted = 1 if self.ui.patient_delete_dropbox.currentText() == "YES" else 0

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                EXEC AddPatient 
                    @first_name=?, 
                    @last_name=?, 
                    @Email=?,
                    @CNIC=?, 
                    @Password=?, 
                    @Gender=?, 
                    @Contact=?, 
                    @Deleted=?
            """, (fname, lname, email, cnic, password, gender, contact, deleted))

            conn.commit()

            self.ui.patient_message_label.setStyleSheet("color: green;")
            self.ui.patient_message_label.setText("Patient added successfully!")
            self.load_patients()

        except Exception as e:
            self.ui.patient_message_label.setStyleSheet("color: red;")
            self.ui.patient_message_label.setText(f"Cnic and Email Must be unique")

        finally:
            conn.close()


    # ----------------------------------------------------
    # UPDATE PATIENT
    # ----------------------------------------------------
    def update_patient(self):
        if not self.selected_patient_id:
            self.ui.patient_message_label.setStyleSheet("color: red;")
            self.ui.patient_message_label.setText("Select a patient from the table first!")
            return

        fname = self.ui.patient_first_name_input.text().strip()
        lname = self.ui.patient_last_name_input.toPlainText().strip()
        email = self.ui.patient_email_input.toPlainText().strip()
        cnic = self.ui.patient_cnic_input.text().strip()
        password = self.ui.patient_password_input.text().strip()
        gender = self.ui.patient_gender_dropbox.currentText()
        contact = self.ui.patient_contact_input.toPlainText().strip()

        
        deleted = 1 if self.ui.patient_delete_dropbox.currentText() == "YES" else 0

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                EXEC UpdatePatient
                    @patient_id=?, 
                    @first_name=?, 
                    @last_name=?, 
                    @email=?,
                    @cnic=?, 
                    @password=?, 
                    @gender=?, 
                    @contact_number=?, 
                    @deleted=?
            """, (
                self.selected_patient_id, fname, lname, email, cnic, password, gender, contact, deleted
            ))

            conn.commit()

            self.ui.patient_message_label.setStyleSheet("color: green;")
            self.ui.patient_message_label.setText("Patient updated successfully!")
            self.load_patients()

        except Exception as e:
            self.ui.patient_message_label.setStyleSheet("color: red;")
            self.ui.patient_message_label.setText(f"Cnic or Email must be unique")

        finally:
            conn.close()
