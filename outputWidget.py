# file of only the widget to drag files out

import sys
from pathlib import Path

from PySide6.QtCore import Qt, QMimeData, QUrl
from PySide6.QtGui import QDrag, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# rename image_path -> save_path when working

class draggableOutput(QLabel):
    def __init__(self, image_path, parent = None):
        super().__init__(parent)
        self.image_path = Path(image_path).resolve()

        self.setImage(image_path)
        self.setCursor(Qt.CursorShape.OpenHandCursor)

    def setImage(self,image_path):
        self.setPixmap(
            QPixmap(str(self.image_path)).scaled(300,300)
        )
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        mime_data.setUrls([QUrl.fromLocalFile(str(self.image_path))])
        drag.setMimeData(mime_data)

        drag.exec(Qt.DropAction.CopyAction)


class outputWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.resize(200,200)
        layout = QVBoxLayout()
        # image_path = r"./Assets/Apples.webp" # test image
        
        self.image = draggableOutput(image_path, self)
        layout.addWidget(self.image)
        #self.setLayout(layout) # added this last second, dont think it will fix the code
    def updateImage(self, image_path):
        self.image.setImage(image_path)
        print("updating output image")

