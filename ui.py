# import .py


# import package
import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic




# UI파일 연결
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("summary.ui")
form_class = uic.loadUiType(form)[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    # Main initial
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()


    # AddUI initial
    def initUI(self):
        self.setWindowTitle('Summary King')
        icon_dir = resource_path("./.ico/icon.png")
        self.setWindowIcon(QIcon(icon_dir))
        self.initSTATUS()
        self.initMENU()
        #self.initBTN()
        self.initLOGO()

    # Logo initial
    def initLOGO(self):
        logo_dir = resource_path("./.ico/logo.png")
        logo = QPixmap(logo_dir)
        logo_img = logo.scaled(QSize(100, 100), aspectRatioMode=Qt.KeepAspectRatio)
        self.label_logo.setPixmap(logo_img)


    # StatusBar initial
    def initSTATUS(self):
        self.statusBar().showMessage('Ready')


    # MenuBar initial
    def initMENU(self):
        # Menu Action initial
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda : self.close())

        abouttext = "This program is a hands-on program for 융종설 in the first semester of 2024 and was produced by Team SUMMARYKING.\n" \
                    "It cannot be copied or used without permission and requires the consent of the manufacturer.\n\n " \
                    "Powerd by 오픈 소스 소프트웨어 기반\n" \
                    " Copyright ⓒ 2024 Team SUMMARYKING"
        aboutAction = QAction('About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.triggered.connect(lambda : QMessageBox.about(self, 'About', abouttext))


        # Menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        helpmenu = menubar.addMenu('&Help')
        helpmenu.addAction(aboutAction)










    def closeEvent(self, event,):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()