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
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

import texture_pack_handler as tph

global size
size = 150

class imageLabel(QLabel):
    def __init__(self):
        super().__init__()
        def SetLayout(self=self):
            self.setAlignment(Qt.AlignCenter)
            self.setText("Drop here")
            self.setStyleSheet("""
                QLabel{
                    border: 4px dashed #aaa
                }
            """)
        SetLayout()

class DnDWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window title")
        self.setAcceptDrops(True)
        self.setFixedSize(size,size)
        self.channel = "G"

        mainLayout = QVBoxLayout()

        self.IMG = imageLabel()
        mainLayout.addWidget(self.IMG)


        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self,file_path):
        print(f"image file path = {file_path}")
        self.isLinear = tph.handler(file_path,self.channel)
        self.IMG.setPixmap(QPixmap(file_path).scaled(size,size))
        tph.updateOutput()


    def rm_image(self):
        print("resetting img")
        #self.IMG.setPixmap(None)
        if self.isLinear:
            tph.input_chan_lst.pop(self.channel)
        print(f"new tph input chan list: {list(tph.input_chan_lst.keys())}")
        self.IMG.setPixmap(QPixmap())
        self.IMG.setText("Drop here")
        tph.updateOutput()


                                    ############
                                    #MainWindow#
                                    ############

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.resize(1280, 720)

        l_dnd_widgetR, DnDWidgetR  = self.DragNDrop("R")
        l_dnd_widgetG, DnDWidgetG = self.DragNDrop("G")
        l_dnd_widgetB, DnDWidgetB = self.DragNDrop("B")
        l_dnd_widgetA, DnDWidgetA = self.DragNDrop("A")
        



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

    def DragNDrop(self,channel):                # import drag and drop widget
            DnDWidgetinst = DnDWidget()
            DnDWidgetinst.channel = channel
            layout = QVBoxLayout()
            layout.addWidget(DnDWidgetinst)
            return layout, DnDWidgetinst

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