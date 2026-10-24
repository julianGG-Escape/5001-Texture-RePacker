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
import outputWidget


global size
size = 150

save_path = "./Output/Save.png"
arrow_img = "./Assets/Arrow.png"

color_matrix = {
    "R":"Red",
    "G":"Green",
    "B":"Blue",
    "A":"Alpha"
}

class DnDLabel(QLabel):
    def __init__(self):
        super().__init__()
        def SetLayout(self=self):
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setText("Drop here")
            self.setStyleSheet("""
                QLabel{
                    border: 4px dashed #aaa
                }
            """)
        SetLayout()



                ############
                #MainWindow#
                ############



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Texture Packer")
        self.resize(1280, 720)
        #self.setFixedSize(1280, 720)




  

        l_dnd_widgetR, DnDWidgetR = self.DragNDrop("R")
        l_dnd_widgetG, DnDWidgetG = self.DragNDrop("G")
        l_dnd_widgetB, DnDWidgetB = self.DragNDrop("B")
        l_dnd_widgetA, DnDWidgetA = self.DragNDrop("A",100)


        btn1 = self.btn()
        btn1.clicked.connect(DnDWidgetR.rm_image)
        btn2 = self.btn()
        btn2.clicked.connect(DnDWidgetG.rm_image)
        btn3 = self.btn()
        btn3.clicked.connect(DnDWidgetB.rm_image)
        btn4 = self.btn()
        btn4.clicked.connect(DnDWidgetA.rm_image)


        arrow_label = QLabel()#.setPixmap(QPixmap(arrow_img).scaled(size,size))
        arrow_label.setPixmap(QPixmap(arrow_img).scaled(100,100))
        arrow_label.setFixedSize(100,100)
        #arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.outputWidgetinst = outputWidget.outputWidget(save_path=save_path)
        self.outputWidgetinst.setFixedSize(300,300)

        l_outputWidget = QHBoxLayout()
        #l_outputWidget.setAlignment(Qt.AlignmentFlag.AlignLeft)
        l_outputWidget.addWidget(arrow_label)
        l_outputWidget.addWidget(self.outputWidgetinst)
        #l_outputWidget.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # ----------
        #  LAYOUTS!
        # ----------

        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()
        layoutV3 = QHBoxLayout()
        layoutV4 = QHBoxLayout()

        layoutR = QHBoxLayout()
        layoutG = QHBoxLayout()
        layoutB = QHBoxLayout()

        layoutR.addLayout(l_dnd_widgetR)
        layoutR.addWidget(btn1)
        layoutR.setAlignment(Qt.AlignmentFlag.AlignRight)



        layoutG.addLayout(l_dnd_widgetG)
        layoutG.addWidget(btn2)
        layoutG.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #layoutG.addSpacing(200)
        # play around with setAlignment()


        layoutB.addLayout(l_dnd_widgetB)
        layoutB.addWidget(btn3)
        layoutB.setAlignment(Qt.AlignmentFlag.AlignRight)


        layoutV1.addLayout(layoutR)
        layoutV1.addLayout(layoutG)
        layoutV1.addLayout(layoutB)

        WidgetV1 = QWidget()
        WidgetV1.setFixedWidth(300)
        WidgetV1.setLayout(layoutV1)

        layoutA = QHBoxLayout()

        layoutA.addLayout(l_dnd_widgetA)
        layoutA.addWidget(btn4)
        layoutA.setAlignment(Qt.AlignmentFlag.AlignLeft)
        



        layoutV2.addLayout(layoutA)
        #layoutV2.addWidget(arrow_label)
        layoutV2.addSpacing(200)

        layoutV3.addWidget(arrow_label)
        layoutV3.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layoutV4.addSpacing(250)
        layoutV4.addLayout(l_outputWidget) # this image here officer!WidgetV1 = QWidget()
        #layoutV4.setAlignment(Qt.AlignmentFlag.AlignLeft)


        layoutH.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layoutH.addSpacing(50)
        layoutH.addWidget(WidgetV1)
        layoutH.addSpacing(50)
        layoutH.addLayout(layoutV2)
        #layoutH.addSpacing(150)
        layoutH.addLayout(layoutV3)
        #layoutH.addSpacing(150)
        layoutH.addLayout(layoutV4)
        layoutH.addSpacing(50)

        # ----------
        #  Create Widget
        # ----------

        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)

    def UpdateOutputImage(self):
        self.outputWidgetinst.updateImage(save_path)


    def DragNDrop(self,channel, size = size):                # import drag and drop widget
            DnDWidgetinst = self.DnDWidget(channel, size)
            #DnDWidgetinst.channel = channel
            layout = QVBoxLayout()
            layout.addWidget(DnDWidgetinst)
            return layout, DnDWidgetinst


    def btn(self, msg="remove", button_length = 65):
        button = QPushButton(msg)
        button.setFixedSize(button_length,30)
        return button


    class DnDWidget(QWidget):
        def __init__(self, channel, size):
            super().__init__()
            self.setWindowTitle("window title")
            self.setAcceptDrops(True)
            self.channel = channel
            channel_text = f"[{color_matrix[channel]}]"


            mainLayout = QVBoxLayout()
            text_label = QLabel(channel_text)
            text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            mainLayout.addWidget(text_label)

            #dnd_layout = QVBoxLayout()

            self.IMG = DnDLabel()
            self.IMG.setFixedSize(size,size)
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
                # "C/:file"
                # "<number>"
                self.set_image(file_path)

                event.accept()
            else:
                event.ignore()

        def set_image(self,file_path):
            print(f"image file path = {file_path}")
            self.isLinear = tph.handler(file_path,self.channel, save_path)
            self.IMG.setPixmap(QPixmap(file_path).scaled(size,size))
            #tph.updateOutput()
            self.MainWindow = window
            self.MainWindow.UpdateOutputImage()

            



        def rm_image(self):
            print("resetting img")
            #self.IMG.setPixmap(None)
            if self.isLinear:
                tph.input_chan_lst.pop(self.channel)
            print(f"new tph input chan list: {list(tph.input_chan_lst.keys())}")
            self.IMG.setPixmap(QPixmap())
            self.IMG.setText("Drop here")
            tph.updateOutput(save_path)
            self.MainWindow.UpdateOutputImage()


app = QApplication(sys.argv)
window = MainWindow()


window.show()
app.exec()