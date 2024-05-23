from libcamera import controls
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                             QPushButton, QVBoxLayout, QWidget)

from picamera2 import Picamera2
from picamera2.previews.qt import QGlPicamera2


def cameracapture():
    global state
    button.setEnabled(False)
    continuous_checkbox.setEnabled(False)
    af_checkbox.setEnabled(False)
    state = STATE_AF if af_checkbox.isChecked() else STATE_CAPTURE
    if state == STATE_AF:
        picam2.autofocus_cycle(signal_function=qpicamera2.signal_done)
    else:
        do_capture()