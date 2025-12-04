from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from connection import get_connection
from interfaces.admin.admin_mange import Ui_Frame
from global_file import global_value

class AdminManageAdminsController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_admin_id = None

        # Connect buttons
        self.ui.admin_add_button.clicked.connect(self.insert_admin)
        self.ui.admin_update_button.clicked.connect(self.update_admin)
        self.ui.admin_search_button.clicked.connect(self.load_admins)

        # Connect row click separately
        self.ui.tableView.clicked.connect(self.admin_row_clicked)
        self.current_row = None

        # Load data
        self.load_admins()

    def load_admins(self):
        """Load all admins except current user into the table."""
        current_admin_id = global_value.current_user['user_id']
        filter_cnic = self.ui.admin_search_input.text().strip()
        conn = get_connection()
        cursor = conn.cursor()

        # Call stored procedure
        cursor.execute("EXEC GetAdminsExceptSelf ?,?", current_admin_id, filter_cnic)
        data = cursor.fetchall()
        conn.close()

        # Populate table
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "Admin ID", "First Name", "Last Name", "Email", "CNIC", "Password", "Created At", "Deleted",
        ])

        for row in data:
            items = [QStandardItem(str(col)) for col in row]
            model.appendRow(items)

        self.ui.tableView.setModel(model)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.resizeColumnsToContents()
    


    def admin_row_clicked(self, index):
        """Populate input fields and store row values in a dictionary."""
        row = index.row()
        model = self.ui.tableView.model()

        # Build dictionary of selected row
        self.current_row = {
            "admin_id": model.index(row, 0).data(),
            "first_name": model.index(row, 1).data(),
            "last_name": model.index(row, 2).data(),
            "email": model.index(row, 3).data(),
            "cnic": model.index(row, 4).data(),
            "password": model.index(row, 5).data(),
            "created_at": model.index(row, 6).data(),
            "deleted": model.index(row, 7).data(),
        }

        # Save selected admin ID
        self.selected_admin_id = self.current_row["admin_id"]

        # Fill inputs with dictionary values
        self.ui.admin_first_name_input.setText(self.current_row["first_name"])
        self.ui.admin_last_name_input.setText(self.current_row["last_name"])
        self.ui.admin_email_input.setText(self.current_row["email"])
        self.ui.admin_cnic_input.setText(self.current_row["cnic"])
        self.ui.admin_password_input.setText(self.current_row["password"])

        # Set deleted dropdown
        deleted_value = str(self.current_row["deleted"]).strip()
        if deleted_value == "1":
            self.ui.admin_deleted_dropbox.setCurrentText("YES")
        else:
            self.ui.admin_deleted_dropbox.setCurrentText("NO")

        print(self.current_row)





    def insert_admin(self):
        fname = self.ui.admin_first_name_input.text().strip()
        lname = self.ui.admin_last_name_input.text().strip()
        email = self.ui.admin_email_input.text().strip()
        cnic = self.ui.admin_cnic_input.text().strip()
        password = self.ui.admin_password_input.text().strip()

        # Convert YES/NO to 1/0
        deleted_value = self.ui.admin_deleted_dropbox.currentText()
        deleted = 1 if deleted_value == "YES" else 0

        if not fname or not lname or not email or not cnic or not password:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("All fields are required.")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                EXEC InsertAdmin ?, ?, ?, ?, ?, ?
            """, (fname, lname, email, cnic, password, deleted))
            print("done")
            conn.commit()
            cursor.close()
            conn.close()

            # SUCCESS MESSAGE
            self.ui.admin_message_label.setStyleSheet("color: green;")
            self.ui.admin_message_label.setText("Admin added successfully!")

            # REFRESH TABLE
            self.load_admins()

            # CLEAR INPUTS
            self.ui.admin_first_name_input.clear()
            self.ui.admin_last_name_input.clear()
            self.ui.admin_email_input.clear()
            self.ui.admin_cnic_input.clear()
            self.ui.admin_password_input.clear()
            self.ui.admin_deleted_dropbox.setCurrentText("NO")
            print("done")

        except Exception as e:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText(f"Cnic or Email duplicated")


    def update_admin(self):
        if not self.current_row:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("Please select a row first.")
            return

        admin_id = self.current_row["admin_id"]
        fname = self.ui.admin_first_name_input.text().strip()
        lname = self.ui.admin_last_name_input.text().strip()
        email = self.ui.admin_email_input.text().strip()
        cnic = self.ui.admin_cnic_input.text().strip()
        password = self.ui.admin_password_input.text().strip()

        deleted_value = self.ui.admin_deleted_dropbox.currentText()
        deleted = 1 if deleted_value == "YES" else 0

        # Validation
        if not fname or not lname or not email or not cnic or not password:
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("All fields are required.")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                EXEC UpdateAdmin ?, ?, ?, ?, ?, ?, ?
            """, (admin_id, fname, lname, email, cnic, password, deleted))

            conn.commit()
            cursor.close()
            conn.close()

            # SUCCESS MESSAGE
            self.ui.admin_message_label.setStyleSheet("color: green;")
            self.ui.admin_message_label.setText("Admin updated successfully!")

            # REFRESH TABLE
            self.load_admins()

            # CLEAR after update
            self.current_row = None
            self.selected_admin_id = None
            self.ui.admin_first_name_input.clear()
            self.ui.admin_last_name_input.clear()
            self.ui.admin_email_input.clear()
            self.ui.admin_cnic_input.clear()
            self.ui.admin_password_input.clear()
            self.ui.admin_deleted_dropbox.setCurrentText("NO")

        except Exception as e:
            print(e)
            self.ui.admin_message_label.setStyleSheet("color: red;")
            self.ui.admin_message_label.setText("Email or CNIC already exists!")

            

        
       