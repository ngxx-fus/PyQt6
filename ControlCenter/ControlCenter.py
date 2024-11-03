import sys
import time
import datetime
import numpy as np
import pyqtgraph as pg
from random import randint

from pyqtgraph import AxisItem
from pyqtgraph import LabelItem

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, QTimer, QThread, QObject, pyqtSignal

from resources.components.support_functions import UpdateSensor_ClassWorker
from resources.components.Ui_ControlCenter import Ui_MainWindow
from resources.announcements import demo

class ControlCenter(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Global variables
        self.Notification_Buffer_Size=10000 #Chars
        self.Chart_Update="PAUSE"
        self.Preset_Mode_1={"Dev1":"ON", "Dev2":"OFF", "Dev3":"HALF"}
        self.Preset_Mode_2={"Dev1":"ON", "Dev2":"ON", "Dev3":"FULL"}
        self.Preset_Mode_3={"Dev1":"OFF", "Dev2":"OFF", "Dev3":"OFF"}
        self.Notification_Buffer=""
        self.Dev1_Ctl=0 # only 1 or 0
        self.Dev2_Ctl=0 # only 1 or 0
        self.Dev3_Ctl=0 # in range [0->100]
        self.Chart_Len=20
        self.Chart_XAxis_Data=range(1, self.Chart_Len+1)
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
        self.setWindowIcon(QIcon("./resources/images/LOGO - W.png"))
        # Set-up dev2 switch
        size=self.ui.IndicatorDev_2.size()
        pixmap=QPixmap("./resources/images/switch-off.png")
        self.ui.Dev2_Switch_1.setPixmap(pixmap.scaled(size))
        # Set-up chart
        self.Load_Chart_1()
        self.Load_Chart_2()
        self.Load_Chart_3()
        # Connect signal
        self.ui.Dev1_Start_1.clicked.connect(self.Set_Dev1_state_ON)
        self.ui.Dev1_Stop_1.clicked.connect(self.Set_Dev1_state_OFF)
        self.ui.Dev2_Switch_1.mousePressEvent = self.Toggle_Dev2
        self.ui.Dev3_Slider_1.valueChanged.connect(self.Update_Dev3)
        self.ui.Run_1.clicked.connect(self.Run_Mode_1)
        self.ui.Run_2.clicked.connect(self.Run_Mode_2)
        self.ui.Run_3.clicked.connect(self.Run_Mode_3)
        self.ui.Clear_Notification_1.clicked.connect(self.Clear_Notification)
        self.ui.Exit_1.clicked.connect(self.Exit)
        self.ui.Clear_Chart_2.clicked.connect(self.Clear_Chart)
        self.ui.Clear_1.clicked.connect(self.Reserve_Features)
        self.ui.Clear_2.clicked.connect(self.Reserve_Features)
        self.ui.Clear_3.clicked.connect(self.Reserve_Features)
        self.ui.Load_1.clicked.connect(self.Reserve_Features)
        self.ui.Load_2.clicked.connect(self.Reserve_Features)
        self.ui.Load_3.clicked.connect(self.Reserve_Features)
        self.ui.Save_Setting_1.clicked.connect(self.Reserve_Features)
        self.ui.Load_Setting_1.clicked.connect(self.Reserve_Features)
        #Update chart
        self.Start_Chart()
        # Hello 
        self.New_Notification(demo.noti__01)
        self.New_Notification(demo.noti__02)

    def Load_Chart_x(self, chart, YValues=None, YLabel=None, YUnit=None, Color=None):
        chart.setBackground('w')
        layout = pg.GraphicsLayout()
        chart.setCentralItem(layout)
        chart.show()
        plot = layout.addPlot(0, 0)
        if YValues is not None:
            if Color is not None:
                pen = pg.mkPen(color=Color)
                plot.plot(self.Chart_XAxis_Data, YValues, pen=pen, 
                            symbol="s", symbolSize=5, symbolBrush='k',
                            fillLevel=-0.3, brush=Color)
            else:
                plot.plot(self.Chart_XAxis_Data, YValues)
        plot.showGrid(x = True, y = True, alpha = 0.5)
        plot.setLabel('left', YLabel, YUnit)
        plot.legend 
        X_axis = plot.getAxis('bottom')
        X_axis.setStyle(showValues=False)
        
    def Start_Chart(self):
        # Create a new thread
        self.thread2 = QThread()
        # Set worker class (inherited from QObject)
        self.UpdateSensor_ClassWorker = UpdateSensor_ClassWorker(self)
        # Move worker class into thread2
        self.UpdateSensor_ClassWorker.moveToThread(self.thread2)
        # Connect finished signal to thread2.quit aka exit from thread2
        self.UpdateSensor_ClassWorker.finished.connect(self.thread2.quit) # Thoát luồng
        # Connect finished signal to deleteLater method of workerclass to delete worker class
        self.UpdateSensor_ClassWorker.finished.connect(self.UpdateSensor_ClassWorker.deleteLater)
        # Connect finished signal to deleteLater method of thread2 to delete thread2
        self.thread2.finished.connect(self.thread2.deleteLater)
        # Connect started signal to UpdateData method of worker class to start worker class
        self.thread2.started.connect(self.UpdateSensor_ClassWorker.UpdateData)
        # Starting thread2
        self.thread2.start()
        # Connect update_chart_1 signal to self.Load_Chart_1 
        self.UpdateSensor_ClassWorker.update_chart_1.connect(self.Load_Chart_1)
        # Connect update_chart_2 signal to self.Load_Chart_2 
        self.UpdateSensor_ClassWorker.update_chart_2.connect(self.Load_Chart_2)
        # Connect update_chart_3 signal to self.Load_Chart_3 
        self.UpdateSensor_ClassWorker.update_chart_3.connect(self.Load_Chart_3)
        # Connect warning signel to warning method
        self.UpdateSensor_ClassWorker.overheat_warning_chart_2.connect(self.Set_overheat_warning_chart_2)
        self.UpdateSensor_ClassWorker.overheat_warning_chart_3.connect(self.Set_overheat_warning_chart_3)

    def Load_Chart_1(self):
        self.Load_Chart_x(self.ui.Chart_1, YValues=self.Chart_Data_1, YLabel='Power Generation', YUnit='VAh', Color=(203, 96, 64, 70))

    def Load_Chart_2(self):
        self.Load_Chart_x(self.ui.Chart_2,  YValues=self.Chart_Data_2, YLabel='Solar Panel (Max)' , YUnit=' °C', Color=(19, 93, 102, 70))

    def Load_Chart_3(self):
        self.Load_Chart_x(self.ui.Chart_3,  YValues=self.Chart_Data_3, YLabel='Inverter (Max)' , YUnit=' °C', Color=(22, 66, 60, 70))

    def New_Notification(self, str_text):
        YEAR        = datetime.date.today().year     # the current year
        MONTH       = datetime.date.today().month    # the current month
        DATE        = datetime.date.today().day      # the current day
        HOUR        = datetime.datetime.now().hour   # the current hour
        MINUTE      = datetime.datetime.now().minute # the current minute
        SECONDS     = datetime.datetime.now().second #the current second
        Old_Notification=self.Notification_Buffer
        Time=f"[ {HOUR}:{MINUTE}:{SECONDS}   {YEAR}-{MONTH}-{DATE} ]\n"
        self.Notification_Buffer = "\n" + Time + str_text + "\n" + Old_Notification
        if len(self.Notification_Buffer) > self.Notification_Buffer_Size:
            self.Notification_Buffer = self.Notification_Buffer[:self.Notification_Buffer_Size]
        self.ui.Notification.setPlainText(self.Notification_Buffer)

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
            self.Set_Indicator_Dev_2()
        else:
            self.Dev2_Ctl = 0
            size=self.ui.IndicatorDev_2.size()
            pixmap=QPixmap("./resources/images/switch-off.png")
            self.ui.Dev2_Switch_1.setPixmap(pixmap.scaled(size))
            self.Set_Indicator_Dev_2()

    def Update_Dev3(self):
        self.Dev3_Ctl = self.ui.Dev3_Slider_1.value()
        self.Set_Indicator_Dev_3()

    def Set_Copyright(self):
        size=self.ui.Copyright_3.size()
        pixmap=QPixmap("./resources/images/logo-boot.png")
        self.ui.Copyright_3.setPixmap(pixmap)

    def Run_Mode_x(self, preset_mode):
        
        if preset_mode["Dev1"] == "ON":
            self.Set_Dev1_state_ON();
        elif preset_mode["Dev1"] == "OFF":
            self.Set_Dev1_state_OFF();
        
        if preset_mode["Dev2"] == "ON":
            if self.Dev2_Ctl == 0:
                self.Toggle_Dev2("param")
        elif preset_mode["Dev2"] == "OFF":
            if self.Dev2_Ctl == 1:
                self.Toggle_Dev2("param")
        
        if preset_mode["Dev3"] == "OFF":
            self.ui.Dev3_Slider_1.setValue(15)
            self.Update_Dev3()
        elif preset_mode["Dev3"] == "HALF":
            self.ui.Dev3_Slider_1.setValue(45)
            self.Update_Dev3()
        elif preset_mode["Dev3"] == "FULL":
            self.ui.Dev3_Slider_1.setValue(75)
            self.Update_Dev3()

    def Run_Mode_1(self):
        self.New_Notification("Run PRESET MODE-1")
        self.Run_Mode_x(self.Preset_Mode_1)

    def Run_Mode_2(self):
        self.New_Notification("Run PRESET MODE-2")
        self.Run_Mode_x(self.Preset_Mode_2)

    def Run_Mode_3(self):
        self.New_Notification("Run PRESET MODE-3")
        self.Run_Mode_x(self.Preset_Mode_3)

    def Clear_Notification(self):
        self.Notification_Buffer = ""
        self.ui.Notification.setPlainText("")

    def Clear_Chart(self):
        self.Chart_Data_1=np.zeros(self.Chart_Len)
        self.Chart_Data_2=np.zeros(self.Chart_Len)
        self.Chart_Data_3=np.zeros(self.Chart_Len)
        self.Load_Chart_1()
        self.Load_Chart_2()
        self.Load_Chart_3()

    def Exit(self):
        sys.exit(1)

    def Set_overheat_warning_chart_2(self):
        self.New_Notification(f"A panel is over-heat (at {self.Chart_Data_2[-1]}°C), please turn on Cooling System and walk around to fix it!")

    def Set_overheat_warning_chart_3(self):
        self.New_Notification(f"An inverter is over-heat (at {self.Chart_Data_3[-1]}°C), please turn on Cooling System and walk around to fix it!")

    def Reserve_Features(self):
        self.New_Notification("Reserve feature!")


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    MYAPP = ControlCenter()
    MYAPP.show()
    sys.exit(APP.exec())