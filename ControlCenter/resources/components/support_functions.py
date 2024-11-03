import numpy
import time
import numpy as np
import pyqtgraph as pg
from random import randint
from datetime import datetime
from PyQt6.QtCore import QObject, pyqtSignal

class UpdateSensor_ClassWorker(QObject):
    finished = pyqtSignal()
 
    def __init__(self):
        super().__init__()
        # myapp = myapp

    def Load_Chart_x(self, chart, XValues=None, YValues=None, YLabel=None, YUnit=None, Color=None):
        chart.setBackground('white')
        layout = pg.GraphicsLayout()
        chart.setCentralItem(layout)
        chart.show()
        plot = layout.addPlot(0, 0)
        if XValues is not None \
            and YValues is not None \
            and Color is not None:
            plot.plot(XValues, YValues, Color)
        if XValues is not None \
            and YValues is not None:
            plot.plot(XValues, YValues)
        plot.showGrid(x = True, y = True, alpha = 0.5)
        plot.setLabel('left', YLabel, YUnit)
        X_axis = plot.getAxis('bottom')
        X_axis.setStyle(showValues=False)

    def Update_Sensor_1(self, myapp):
        data = np.append(myapp.Chart_Data_1[1:], randint(78, 82)*1000)
        self.Load_Chart_x(
            myapp.ui.Chart_1,
            XValues=myapp.Chart_XAxis_Data,
            YValues=data,
            YLabel="Power Generated",
            YUnit="VAh"
        )

    # def Update_Sensor_2(self):
    #     data = randint(78, 82)
    #     myappmyapp.Chart_Data_2 = np.append(myapp.Chart_Data_2[1:], data)
    #     myapp.Load_Chart_2()

    # def Update_Sensor_3(self):
    #     data = randint(78, 82)*1000
    #     myapp.Chart_Data_3 = np.append(myapp.Chart_Data_3[1:], data)
    #     myapp.Load_Chart_3()


    def UpdateData(self, myapp):
        while True:
            print("HEHEHE")
            self.Update_Sensor_1(myapp)
            # Update_Sensor_2()
            # Update_Sensor_3()
            time.sleep(1)
