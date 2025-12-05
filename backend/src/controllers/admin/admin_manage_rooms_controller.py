from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from interfaces.admin.admin_manage_rooms import Ui_Frame
from connection import get_connection
from global_file import global_value

class AdminManageRoomsController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        # Fetch branches and populate combo box
        self.branch_dict = global_value.fetch_branches()
        self.ui.admin_branch_dropbox.addItems(self.branch_dict.keys())
        self.ui.room_branch_search_dropbox.addItems(self.branch_dict.keys())

        self.selected_room_id = None

        # Load existing rooms
        self.load_rooms()

        # Connect UI buttons
        self.ui.tableView.clicked.connect(self.on_row_clicked)
        self.ui.admin_add_button.clicked.connect(self.add_room)
        self.ui.admin_update_button.clicked.connect(self.update_room)
        self.ui.room_search_button.clicked.connect(self.load_rooms)

    # ------------------------------
    # Load rooms into table
    # ------------------------------
    def load_rooms(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            search_branch = self.ui.room_branch_search_dropbox.currentText()
            if search_branch == 'ALL':
                cursor.execute("EXEC GetRooms")
            else :
                cursor.execute("EXEC GetRooms ? ", self.branch_dict[search_branch])
            rows = cursor.fetchall()

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["Room ID", "Branch", "Deleted"])
            for row in rows:
                room_id,branch_id,  branch_name, deleted = row
                model.appendRow([
                    QStandardItem(str(room_id)),
                    QStandardItem(branch_name),
                    QStandardItem("YES" if deleted else "NO")
                ])

            self.ui.tableView.setModel(model)
            self.ui.tableView.resizeColumnsToContents()
            self.ui.tableView.verticalHeader().setVisible(False)

        except Exception as e:
            self.ui.admin_message_label.setText(f"Failed to load rooms: {e}")
        finally:
            try: cursor.close(); conn.close()
            except: pass

    # ------------------------------
    # Populate fields when row clicked
    # ------------------------------
    def on_row_clicked(self, index):
        model = self.ui.tableView.model()
        row = index.row()

        self.selected_room_id = int(model.item(row, 0).text())
        branch_name = model.item(row, 1).text()
        deleted_text = model.item(row, 2).text()

        self.ui.admin_room_input.setText(str(self.selected_room_id))
        self.ui.admin_branch_dropbox.setCurrentText(branch_name)
        self.ui.room_delete_dropbox.setCurrentText(deleted_text)
        self.ui.admin_message_label.setText("")

    # ------------------------------
    # Add new room
    # ------------------------------
    def add_room(self):
        room_id_text = self.ui.admin_room_input.text()
        branch_name = self.ui.admin_branch_dropbox.currentText()
        deleted_text = self.ui.room_delete_dropbox.currentText()

        if not room_id_text.isdigit():
            self.ui.admin_message_label.setText("Error: Room ID must be a number!")
            return

        room_id = int(room_id_text)
        branch_id = self.branch_dict[branch_name]
        deleted = 1 if deleted_text == "YES" else 0

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("EXEC InsertRoom ?, ?, ?", room_id, branch_id, deleted)
            conn.commit()
            self.ui.admin_message_label.setText("Room added successfully!")
        except Exception as e:
            self.ui.admin_message_label.setText(f"duplicate room id found")
        finally:
            try: cursor.close(); conn.close()
            except: pass

        self.load_rooms()
        self.clear_fields()

    def update_room(self):
        if not self.selected_room_id:
            self.ui.admin_message_label.setText("Error: Please select a room first!")
            return

        branch_name = self.ui.admin_branch_dropbox.currentText()
        deleted_text = self.ui.room_delete_dropbox.currentText()
        branch_id = self.branch_dict[branch_name]
        deleted = 1 if deleted_text == "YES" else 0


        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("EXEC UpdateRoom ?, ?, ?", self.selected_room_id, branch_id, deleted)
            conn.commit()
            self.ui.admin_message_label.setText("Room updated successfully with previous ID")
        except Exception as e:
            self.ui.admin_message_label.setText(f"Error during updation")
        finally:
            try: cursor.close(); conn.close()
            except: pass

        self.load_rooms()
        self.clear_fields()


    # ------------------------------
    # Clear input fields
    # ------------------------------
    def clear_fields(self):
        self.ui.admin_room_input.clear()
        self.ui.admin_branch_dropbox.setCurrentIndex(0)
        self.ui.room_delete_dropbox.setCurrentIndex(0)
        self.selected_room_id = None
