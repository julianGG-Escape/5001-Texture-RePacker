# the gui for the texture packer

import sys

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.resize(1280, 720)

        layoutV = QVBoxLayout()

        #wgt1 = self.InputArea()

        btn1 = self.btn("frist button")
        btn2 = self.btn("second button")

        layoutV.addWidget(btn1)
        #layoutV.addWidget(wgt1)
        layoutV.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

    def InputArea(self, size=(20,20)):
        widget = QWidget()
        widget.setAcceptDrops(True)
        self.lbl = imageLabel()

        self.setCentralWidget(lbl)
        return widget


    def btn(self, msg="button", command = None):

        def cmd(command=command):
            if command != None:
                print("Error, button has no output")
            else:
                command()

        button = QPushButton(msg)
        button.clicked.connect(cmd)
        return button

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()