## Overview
Hello from ***ngxxfus***

This app was made for monitoring Solar Farm as a core monitor for quick activate/deactivate some cores system such as Security System, Fire Fighting System, Solar Panel Cooling System. 

Provide monitoring of:

    + Power (Generation)
    + temperature (Solar Panels)
    + temperature (Inverters)

In addition, this app also provide control of 03 devices:

    + Device 01: Currently assigned to control Security System
    + Device 02: Currently assigned to control Fire Fighting System
    + Device 03: Currently assigned to control Solar Panel Cooling System

Demo-Ui

![alt text](https://github.com/ngxx-fus/PyQt6/blob/main/ControlCenter/resources/demo.png?raw=true)

## Directory-Tree
```
PyQT6 (Reposistory)
├── ControlCenter (Current Project)
│   ├── ControlCenter.py
│   ├── readme.md
│   ├── resources
│   │   ├── announcements
│   │   │   ├── demo.py
│   │   │   └── __pycache__
│   │   │       └── demo.cpython-38.pyc
│   │   ├── components
│   │   │   ├── ControlCenter.ui
│   │   │   ├── __pycache__
│   │   │   │   ├── support_functions.cpython-38.pyc
│   │   │   │   └── Ui_ControlCenter.cpython-38.pyc
│   │   │   ├── support_functions.py
│   │   │   └── Ui_ControlCenter.py
│   │   ├── demo.png
│   │   └── images
│   │       ├── black-toggle-buttons-21539.png
│   │       ├── cyber-security.png
│   │       ├── fire-extinguisher_action.png
│   │       ├── fire-extinguisher.png
│   │       ├── logo-boot.png
│   │       ├── LOGO - W.png
│   │       ├── shield.png
│   │       ├── sprinkler_full_on.png
│   │       ├── sprinkler_half_on.png
│   │       ├── sprinkler_off.png
│   │       ├── switch-off.png
│   │       ├── switch-on.png
│   │       ├── toggle-switch-on-off-buttons-21542.png
│   │       └── warning.png
│   └── run
├── GettingStarted (Test Project)
└── README.md
```
## Dependencies and Environment

### Python-Environment
Requied a python-environment with **python=3.8.x**

Check your python-environment:

    python --version

Result:

    Python 3.8.20

### Virtual-Environment
To prevent (unwanted) bugs, you need run this source code in a virtual-environment. There is two ways to make your own environment.

1/ Install virtual-environment via [mini-conda](https://docs.anaconda.com/miniconda/)

    conda create -n python3.8 python=3.8
Note that "python3.8" just a name, it can be edited to whatever you want!


2/ Do that by using venv
To use this option, you need python3-venv package. It's able to be installed via pip:

    sudo apt install python3-venv

Create a venv (same version with global python-environment):

    python -m venv /path/to/where/you/want/to/store/your/venv/

Note that "venv" just a name, it can be edited to whatever you want!

### Dependencies
For easier when editing of this source, you need Qt Designer (standalone), pyuic6, PyQt6. Install them via the commands below:

    pip install PyQt6==6.4.2
    pip install PyQt6-Qt6==6.4.2
    pip install pyqt6-tools designer
    pip install pyqt6-tools==6.4.2.3.3
    pip install dvg-pyqtgraph-threadsafe


## References
| no. | Title  |
|:--:|:---|
| 1  | [Check if string is neither empty nor space in shell script](https://stackoverflow.com/questions/13509508/check-if-string-is-neither-empty-nor-space-in-shell-script)  |
| 2  | [Styling PyQt6 Applications - Default and Custom QSS Stylesheets](https://stackabuse.com/styling-pyqt6-applications-default-and-custom-qss-stylesheets/)  |
| 3  | [Plotting in pyqtgraph](https://pyqtgraph.readthedocs.io/en/latest/getting_started/plotting.html)  |
| 4  | [How can I extract hours and minutes from a datetime.datetime object?](https://stackoverflow.com/questions/25754405/how-can-i-extract-hours-and-minutes-from-a-datetime-datetime-object/25754481#25754481)  |
| 5  | [PyQt - Modify GUI from another thread](https://stackoverflow.com/questions/13420931/pyqt-modify-gui-from-another-thread)  |
| 6  | [Threads and QObjects](https://doc.qt.io/archives/qt-4.8/threads-qobject.html)  |
| 8  | [Threaded plotting with pyqtgraph](https://forum.qt.io/topic/125673/threaded-plotting-with-pyqtgraph)  |
| 9  | [Drawing and Displaying objects and labels over the Axis in pyqtgraph - How to do it effectively?](https://stackoverflow.com/questions/52410731/drawing-and-displaying-objects-and-labels-over-the-axis-in-pyqtgraph-how-to-do)  |
| 10  | [Install Qt Designer Standalone](https://www.pythonguis.com/installation/install-qt-designer-standalone/)  |
| 11 | [Plotting With PyQtGraph](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)  |
| 12  | [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph)  |
<!-- | 13  | []()  |
| 14  | []()  |
| 15  | []()  |
| 16  | []()  |
| 17  | []()  |
| 18  | []()  |
| 19  | []()  | -->