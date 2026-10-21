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
import dnd_widget as dw


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.resize(1280, 720)

        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()

        Layout1, reset1  = self.DragNDrop()
        Layout2, reset2 = self.DragNDrop()


        btn1 = self.btn("frist button")
        btn1.clicked.connect(reset1.rm_image)
        btn2 = self.btn("second button")
        btn2.clicked.connect(reset2.rm_image)


        layoutV.addWidget(btn1)
        layoutH.addLayout(Layout1)
        layoutH.addLayout(Layout2)
        layoutV.addLayout(layoutH)
        layoutV.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

    def DragNDrop(self):
            DnDWidget = dw.DnDWidget()
            DnD = QVBoxLayout()
            DnD.addWidget(DnDWidget)
            return DnD, DnDWidget

    def InputArea(self, size=(20,20)):
        pass


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