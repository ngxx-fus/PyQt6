import sys
import time
import numpy as np

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize

from resources.components.Ui_ControlCenter import Ui_MainWindow
from resources.announcements import announcements

class ControlCenter(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent);
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Global variables
        self.Dev1_Ctl=0 # only 1 or 0
        self.Dev2_Ctl=0 # only 1 or 0
        self.Dev3_Ctl=0 # in range [0->100]
        self.Chart_Len=10
        self.Chart_Data_1=np.zeros(self.Chart_Len)
        self.Chart_Data_2=np.zeros(self.Chart_Len)
        self.Chart_Data_3=np.zeros(self.Chart_Len)
        # Fixed size of windows
        self.setMaximumSize(QSize(1180, 750))
        # Set-up indicator
        self.Set_Indicator_Dev_1()
        self.Set_Indicator_Dev_2()
        self.Set_Indicator_Dev_3()
        # Set-up copyright
        self.Set_Copyright()
        # Set-up dev2 switch
        size=self.ui.IndicatorDev_2.size()
        pixmap=QPixmap("./resources/images/switch-off.png")
        self.ui.Dev2_Switch_1.setPixmap(pixmap.scaled(size))
        # Connect signal
        self.ui.Dev1_Start_1.clicked.connect(self.Set_Dev1_state_ON)
        self.ui.Dev1_Stop_1.clicked.connect(self.Set_Dev1_state_OFF)
        self.ui.Dev2_Switch_1.mousePressEvent = self.Toggle_Dev2
        self.ui.Dev3_Slider_1.valueChanged.connect(self.Update_Dev3)

    def Set_Indicator_Dev_1(self):
        size=self.ui.IndicatorDev_1.size()
        if self.Dev1_Ctl == 1:
            pixmap=QPixmap("./resources/images/shield.png")
            self.ui.IndicatorDev_1.setPixmap(pixmap.scaled(size))
        else:
            pixmap=QPixmap("./resources/images/warning.png")
            self.ui.IndicatorDev_1.setPixmap(pixmap.scaled(size))

    def Set_Indicator_Dev_2(self):
        size=self.ui.IndicatorDev_2.size()
        if self.Dev2_Ctl == 0:
            pixmap=QPixmap("./resources/images/fire-extinguisher.png")
            self.ui.IndicatorDev_2.setPixmap(pixmap.scaled(size))
        else:
            pixmap=QPixmap("./resources/images/fire-extinguisher_action.png")
            self.ui.IndicatorDev_2.setPixmap(pixmap.scaled(size))

    def Set_Indicator_Dev_3(self):
        size=self.ui.IndicatorDev_3.size()
        if self.Dev3_Ctl < 34:
            pixmap=QPixmap("./resources/images/sprinkler_off.png")
            self.ui.IndicatorDev_3.setPixmap(pixmap.scaled(size))
        elif self.Dev3_Ctl < 67:
            pixmap=QPixmap("./resources/images/sprinkler_half_on.png")
            self.ui.IndicatorDev_3.setPixmap(pixmap.scaled(size))
        else:
            pixmap=QPixmap("./resources/images/sprinkler_full_on.png")
            self.ui.IndicatorDev_3.setPixmap(pixmap.scaled(size))

    def Set_Dev1_state_ON(self):
        self.Dev1_Ctl=1
        self.Set_Indicator_Dev_1()

    def Set_Dev1_state_OFF(self):
        self.Dev1_Ctl=0
        self.Set_Indicator_Dev_1()

    def Toggle_Dev2(self, param):
        if self.Dev2_Ctl == 0:
            self.Dev2_Ctl = 1
            size=self.ui.IndicatorDev_2.size()
            pixmap=QPixmap("./resources/images/switch-on.png")
            self.ui.Dev2_Switch_1.setPixmap(pixmap.scaled(size))
        else:
            self.Dev2_Ctl = 0
            size=self.ui.IndicatorDev_2.size()
            pixmap=QPixmap("./resources/images/switch-off.png")
            self.ui.Dev2_Switch_1.setPixmap(pixmap.scaled(size))
        self.Set_Indicator_Dev_2()

    def Update_Dev3(self, param):
        self.Dev3_Ctl = self.ui.Dev3_Slider_1.value()
        self.Set_Indicator_Dev_3()            

    def Set_Copyright(self):
        size=self.ui.Copyright_3.size()
        pixmap=QPixmap("./resources/images/logo-boot.png")
        self.ui.Copyright_3.setPixmap(pixmap)

    # def Set_Dev_state_2(self):
    # def Set_Dev_state_3(self):


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    MYAPP = ControlCenter()
    MYAPP.show()
    sys.exit(APP.exec())