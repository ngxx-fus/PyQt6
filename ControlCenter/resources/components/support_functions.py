import numpy
import time
import numpy as np
import pyqtgraph as pg
from random import randint
from datetime import datetime
from PyQt6.QtCore import QObject, pyqtSignal

class UpdateSensor_ClassWorker(QObject):
    finished = pyqtSignal()
    update_chart_1 = pyqtSignal()
    update_chart_2 = pyqtSignal()
    update_chart_3 = pyqtSignal()

    def __init__(self, myapp):
        super().__init__(parent=None)
        self.myapp=myapp

    def Update_Sensor_1(self):
        data = np.append(self.myapp.Chart_Data_1[1:], randint(30, 82)*1000)
        self.myapp.Chart_Data_1 = data
        #------------------------------------#
        self.update_chart_1.emit()

    def Update_Sensor_2(self):
        data = randint(68, 82)
        self.myapp.Chart_Data_2 = np.append(self.myapp.Chart_Data_2[1:], data)
        #------------------------------------#
        self.update_chart_2.emit()

    def Update_Sensor_3(self):
        data = randint(68, 82)
        self.myapp.Chart_Data_3 = np.append(self.myapp.Chart_Data_3[1:], data)
        #------------------------------------#
        self.update_chart_3.emit()


    def UpdateData(self):
        while True:
            self.Update_Sensor_1()
            self.Update_Sensor_2()
            self.Update_Sensor_3()
            time.sleep(5)
        self.finished.emit()
