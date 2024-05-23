from libcamera import controls
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                             QPushButton, QVBoxLayout, QWidget)

from picamera2 import Picamera2
from picamera2.previews.qt import QGlPicamera2


def on_pic_button_clicked():
    # Send capture request
    if pic_tab.preview_check.isChecked() and rec_button.isEnabled():
        switch_config("still")
        picam2.capture_request(signal_function=qpicamera2.signal_done)
    else:
        picam2.capture_request(signal_function=qpicamera2.signal_done)
    rec_button.setEnabled(False)
    mode_tabs.setEnabled(False)


def capture_done(job):
    # Here's the request we captured. But we must always release it when we're done with it!
    if not pic_tab.hdr.isChecked():
        # Save the normal image
        request = picam2.wait(job)
        if pic_tab.filetype.currentText() == "raw":
            request.save_dng(
                f"{pic_tab.filename.text() if pic_tab.filename.text() else 'test'}.dng"
            )
        else:
            request.save(
                "main", f"{pic_tab.filename.text() if pic_tab.filename.text() else 'test'}.{pic_tab.filetype.currentText()}"
            )
        request.release()
        rec_button.setEnabled(True)
        mode_tabs.setEnabled(True)
        if pic_tab.preview_check.isChecked():
            switch_config("preview")



