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

        l_dnd_widgetR, DnDWidgetR  = self.DragNDrop()
        l_dnd_widgetG, DnDWidgetG = self.DragNDrop()
        l_dnd_widgetB, DnDWidgetB = self.DragNDrop()
        l_dnd_widgetA, DnDWidgetA = self.DragNDrop()
        



        btn1 = self.btn()
        btn1.clicked.connect(DnDWidgetR.rm_image)
        btn2 = self.btn()
        btn2.clicked.connect(DnDWidgetG.rm_image)
        btn3 = self.btn()
        btn3.clicked.connect(DnDWidgetB.rm_image)
        btn4 = self.btn()
        btn4.clicked.connect(DnDWidgetA.rm_image)


        # ----------
        #  LAYOUTS!
        # ----------

        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()

        layoutR = QHBoxLayout()
        layoutG = QHBoxLayout()
        layoutB = QHBoxLayout()

        layoutR.addLayout(l_dnd_widgetR)
        layoutR.addWidget(btn1)


        layoutG.addLayout(l_dnd_widgetG)
        layoutG.addWidget(btn2)

        layoutB.addLayout(l_dnd_widgetB)
        layoutB.addWidget(btn3)

        layoutV1.addLayout(layoutR)
        layoutV1.addLayout(layoutG)
        layoutV1.addLayout(layoutB)

        layoutA = QHBoxLayout()

        layoutA.addLayout(l_dnd_widgetA)
        layoutA.addWidget(btn4)

        layoutV2.addLayout(layoutA)

        layoutH.addLayout(layoutV1)
        layoutH.addLayout(layoutV2)

        # ----------
        #  Create Widget
        # ----------

        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)

    def DragNDrop(self):                # import drag and drop widget
            DnDWidget = dw.DnDWidget()
            layout = QVBoxLayout()
            layout.addWidget(DnDWidget)
            return layout, DnDWidget

    def InputArea(self, size=(20,20)):
        pass


    def btn(self, msg="X"):
        button = QPushButton(msg)
        button.setFixedSize(30,30)
        return button

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()