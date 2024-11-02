import numpy
import time
import numpy as np
from random import randint
from datetime import datetime
from PySide6 import QtGui
from PySide6.QtCore import QSize
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class UpdateSensor_ClassWorker(QObject):
    finished = pyqtSignal()
 
    def __init__(self, myapp):
        super().__init__()
        self.myapp = myapp

    def Update_Sensor_1(self):
        data = randint(78, 82)*1000
        myapp.Chart_Data_1 = np.append(myapp.Chart_Data_1[1:], data)
        myapp.Load_Chart_1()

    def Update_Sensor_2(self):
        data = randint(78, 82)
        myapp.Chart_Data_2 = np.append(myapp.Chart_Data_2[1:], data)
        myapp.Load_Chart_2()

    def Update_Sensor_3(self):
        data = randint(78, 82)*1000
        myapp.Chart_Data_3 = np.append(myapp.Chart_Data_3[1:], data)
        myapp.Load_Chart_3()


    def UpdateData(self):
        while True:
            Update_Sensor_1()
            Update_Sensor_2()
            Update_Sensor_3()
