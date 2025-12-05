from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from interfaces.admin.admin_manage_branch import Ui_Frame
from connection import get_connection

class AdminManageBranchController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.selected_branch_id = None

        # Load table
        self.load_branches()

        # Connect signals
        self.ui.tableView.clicked.connect(self.on_row_clicked)
        self.ui.admin_add_button.clicked.connect(self.add_branch)
        self.ui.admin_update_button.clicked.connect(self.update_branch)

    # -----------------------------------------
    # Load branches into table
    # -----------------------------------------
    def load_branches(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("EXEC GetBranches")
            rows = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(
                ["ID", "Name", "Contact", "Created At", "Deleted"]
            )

            for row in rows:
                branch_id, name, contact, created_at, deleted = row

                model.appendRow([
                    QStandardItem(str(branch_id)),
                    QStandardItem(name),
                    QStandardItem(contact),
                    QStandardItem(str(created_at)),
                    QStandardItem("YES" if deleted else "NO")
                ])

            self.ui.tableView.setModel(model)
            self.ui.tableView.resizeColumnsToContents()
            self.ui.tableView.verticalHeader().setVisible(False)

        except Exception as e:
            self.ui.admin_message_label.setText(f"Error loading branches: {e}")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    # -----------------------------------------
    # Table row clicked → fill inputs
    # -----------------------------------------
    def on_row_clicked(self, index):
        model = self.ui.tableView.model()
        row = index.row()

        self.selected_branch_id = int(model.item(row, 0).text())
        name = model.item(row, 1).text()
        contact = model.item(row, 2).text()
        deleted = model.item(row, 4).text()  # YES / NO

        self.ui.admin_branch_name_input.setText(name)
        self.ui.admin_contact_number_input.setText(contact)
        self.ui.comboBox.setCurrentText(deleted)

        self.ui.admin_message_label.setText("")

    # -----------------------------------------
    # Add new branch
    # -----------------------------------------
    def add_branch(self):
        name = self.ui.admin_branch_name_input.text().strip()
        contact = self.ui.admin_contact_number_input.text().strip()
        deleted = 1 if self.ui.comboBox.currentText() == "YES" else 0

        if name == "":
            self.ui.admin_message_label.setText("Branch name required!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("EXEC InsertBranch ?, ?, ?", name, contact, deleted)
            conn.commit()
            self.ui.admin_message_label.setText("Branch added successfully!")

        except Exception as e:
            self.ui.admin_message_label.setText(f"DUPLICATE BRANCH NAME FOUND")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

        self.load_branches()
        self.clear_fields()


    # -----------------------------------------
    # Update branch
    # -----------------------------------------
    def update_branch(self):
        if not self.selected_branch_id:
            self.ui.admin_message_label.setText("Select a branch first!")
            return

        name = self.ui.admin_branch_name_input.text().strip()
        contact = self.ui.admin_contact_number_input.text().strip()
        deleted = 1 if self.ui.comboBox.currentText() == "YES" else 0

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "EXEC UpdateBranch ?, ?, ?, ?",
                self.selected_branch_id, name, contact, deleted
            )
            conn.commit()
            self.ui.admin_message_label.setText("Branch updated successfully!")

        except Exception as e:
            self.ui.admin_message_label.setText(f"DUPLICATE BRANCH NAME FOUND")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

        self.load_branches()
        self.clear_fields()

    # -----------------------------------------
    # Clear inputs
    # -----------------------------------------
    def clear_fields(self):
        self.ui.admin_branch_name_input.clear()
        self.ui.admin_contact_number_input.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.selected_branch_id = None
