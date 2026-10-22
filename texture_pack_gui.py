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

def refreshOutputPath():
    global save_path
    save_path = "./Output/Save.png"

refreshOutputPath()

global size
size = 150

class imageLabel(QLabel):
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
"""
Stupid helper function(class) that doesn't fix the issue
"""
class Outputwigi():
    def __init__(self):
        super().__init__()    
        self.outputWidgetinst = outputWidget.outputWidget(image_path=save_path, cow_name="Alexandra")
        l_outputWidget = QVBoxLayout()
        l_outputWidget.addWidget(self.outputWidgetinst)

    def update(self):
        refreshOutputPath()
        self.outputWidgetinst.updateImage(save_path)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.resize(1280, 720)

        """
        I'm not actually using the "outputWigi"
        """
        self.outputWidgetinst = outputWidget.outputWidget(image_path=save_path, cow_name="Alexandra")
        l_outputWidget = QVBoxLayout()
        l_outputWidget.addWidget(self.outputWidgetinst)

  

        l_dnd_widgetR, DnDWidgetR = self.DragNDrop("R")
        l_dnd_widgetG, DnDWidgetG = self.DragNDrop("G")
        l_dnd_widgetB, DnDWidgetB = self.DragNDrop("B")
        l_dnd_widgetA, DnDWidgetA = self.DragNDrop("A")

        
        """ OLD method
        #l_placeholder, Placeholder = self.DragNDrop("A")
        #outputWidgetinst = outputWidget.outputWidget()

        #print(f"DnDWidgetA: {DnDWidgetA}")
        #print(f"outputWidgetInst: {outputWidgetinst}")

        #l_outputWidget = QVBoxLayout()
        #l_outputWidget.addWidget()
        """



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
        layoutV3 = QVBoxLayout()

        layoutR = QHBoxLayout()
        layoutG = QHBoxLayout()
        layoutB = QHBoxLayout()

        layoutR.addLayout(l_dnd_widgetR)
        layoutR.addWidget(btn1)


        layoutG.addLayout(l_dnd_widgetG)
        layoutG.addWidget(btn2)
        layoutG.addSpacing(200)
        # play around with setAlignment()


        layoutB.addLayout(l_dnd_widgetB)
        layoutB.addWidget(btn3)

        layoutV1.addLayout(layoutR)
        layoutV1.addLayout(layoutG)
        layoutV1.addLayout(layoutB)

        layoutA = QHBoxLayout()

        layoutA.addLayout(l_dnd_widgetA)
        layoutA.addWidget(btn4)


        layoutV2.addLayout(layoutA)
        layoutV2.addSpacing(500)

        layoutV3.addLayout(l_outputWidget) # this is going to break the code


        layoutH.addLayout(layoutV1)
        layoutH.addLayout(layoutV2)
        layoutH.addLayout(layoutV3)

        # ----------
        #  Create Widget
        # ----------

        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)


    def DragNDrop(self,channel):                # import drag and drop widget
            DnDWidgetinst = self.DnDWidget()
            DnDWidgetinst.channel = channel
            layout = QVBoxLayout()
            layout.addWidget(DnDWidgetinst)
            return layout, DnDWidgetinst


    def btn(self, msg="X"):
        button = QPushButton(msg)
        button.setFixedSize(30,30)
        return button


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
            OutputwigiInst.update() # not working
            



        def rm_image(self):
            print("resetting img")
            #self.IMG.setPixmap(None)
            if self.isLinear:
                tph.input_chan_lst.pop(self.channel)
            print(f"new tph input chan list: {list(tph.input_chan_lst.keys())}")
            self.IMG.setPixmap(QPixmap())
            self.IMG.setText("Drop here")
            tph.updateOutput()


app = QApplication(sys.argv)
window = MainWindow()

OutputwigiInst = Outputwigi()
window.show()
app.exec()