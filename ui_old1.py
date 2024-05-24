# import .py
import client
#import camera


# import package
import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QPainter, QImage
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5 import uic


# UI파일 연결
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("summary.ui")
form_class = uic.loadUiType(form)[0]

scan_cnt = 0

#화면을 띄우는데 사용되는 Class 선언
class MainWindow(QMainWindow, form_class) :

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
        self.initBTN()
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


    def initBTN(self):
        self.btn_scan.clicked.connect(lambda: self.initbtnscan())
        self.btn_summary.clicked.connect(lambda: self.initbtnssummary())
        self.btn_reset.clicked.connect(lambda: self.initbtnreset())

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

        settingAction = QAction('Settings', self)



        # Menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(settingAction)
        filemenu.addAction(exitAction)
        helpmenu = menubar.addMenu('&Help')
        helpmenu.addAction(aboutAction)


    def initbtnscan(self):
        #camera.
        client.send_file()

        global scan_cnt
        scan_cnt = scan_cnt + 1
        self.statusBar().showMessage('현재까지 스캔된 페이지 : ' + str(scan_cnt) + '장')

    #     camera.cameracapture()


    def initbtnssummary(self):
        response = ''
        response = client.send_summary_signal()
        self.label_summary.setFont(QFont('Arial', 12))
        self.label_summary.setText(str(response))

        self.statusBar().showMessage('요약 완료')
        global scan_cnt
        scan_cnt = 0


    def initbtnreset(self):
        client.send_delete_signal()
        self.label_summary.setText('')
        self.statusBar().showMessage('Ready')
        global scan_cnt
        scan_cnt = 0


    def closeEvent(self, event,):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure to exit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



# class SettingsWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Settings')
#         self.setWindowIcon(QIcon('.ico/icon.png'))
#         self.ui = uic.loadUi('settings.ui', self)
#


