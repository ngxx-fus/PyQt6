import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize

from Ui_MYAPP import Ui_MainWindow

class MYAPP(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent);
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.address = r"./sample_image.png"
        self.light_state = 0
        self.image = QPixmap(self.address)
        self.image_viewer_size = self.ui.image_view.size()
        self.ui.image_view.setPixmap(self.image.scaled(self.image_viewer_size))
        self.ui.refresh_button.clicked.connect(self.refresh_button_action)
        

    def refresh_button_action(self):
        if self.light_state == 0:
            self.light_state = 1
            self.image = QPixmap("./ON.png")
            self.ui.image_view.setPixmap(self.image.scaled(self.image_viewer_size))
        else:
            self.light_state = 0
            self.image = QPixmap("./OFF.png")
            self.ui.image_view.setPixmap(self.image.scaled(self.image_viewer_size))

    def menuBar_open_action():
        print("Hehe!")

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    MYAPP = MYAPP()
    MYAPP.show()
    sys.exit(APP.exec())