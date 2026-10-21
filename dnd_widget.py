from PIL import Image

import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class imageLabel(QLabel):
    def __init__(self):
        super().__init__()


        self.setAlignment(Qt.AlignCenter)
        self.setText("Drop here")
        self.setStyleSheet("""
            QLabel{
                border: 4px dashed #aaa
            }
        """)

class DnDWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window title")
        self.setAcceptDrops(True)
        self.resize(40,40)
        #self.reset = self.rm_image()

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
        self.IMG.setPixmap(QPixmap(file_path))

    def rm_image(self):
        print("resetting img")
        #self.IMG.setPixmap(None)
        self.IMG.clear
        self.IMG = imageLabel()
"""
app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec())
"""




"""
openImg = Image.open

# 1. User provides image file
openImg = Image.open
img_orm = openImg(f"./Assets/sample_orm_tex.jpg")

R_img = openImg (f"./Assets/R.jpg")
G_img = openImg (f"./Assets/G.jpg")
B_img = openImg (f"./Assets/B.jpg")

channel_lst = { 
    # create empty so not have excessive channels
}
channel_lst.clear()

channel_lst["R"] = R_img
channel_lst["G"] = G_img
channel_lst["B"] = B_img


#pack_data = (R_img, G_img, B_img) # same as below
pack_data = tuple(channel_lst.values())

print(f"Pack data: {pack_data}")

pack = Image.merge("RGB",pack_data)

pack.show()
"""