from PySide6.QtWidgets import QApplication, QWidget
from first_interface_ui import Ui_Frame  # Changed from Ui_MainWindow to Ui_Frame
import sys

class MyApp(QWidget):  # Changed from QMainWindow to QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        # Connect the button to the function
        self.ui.pushButton.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        print("Button clicked!")
        self.ui.label.setText("Button was clicked!")  # Changes the label text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())