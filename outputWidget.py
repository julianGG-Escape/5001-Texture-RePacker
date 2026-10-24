# file of only the widget to drag files out

import sys
from pathlib import Path

from PySide6.QtCore import Qt, QMimeData, QUrl
from PySide6.QtGui import QDrag, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# rename save_path -> save_path when working

class draggableOutput(QLabel):
    def __init__(self, save_path, parent = None):
        super().__init__(parent)
        self.save_path = Path(save_path).resolve()

        self.setImage(save_path)
        self.setCursor(Qt.CursorShape.OpenHandCursor)

    def setImage(self,save_path):
        self.setPixmap(
            QPixmap(str(self.save_path)).scaled(300,300)
        )
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        mime_data.setUrls([QUrl.fromLocalFile(str(self.save_path))])
        drag.setMimeData(mime_data)

        drag.exec(Qt.DropAction.CopyAction)


class outputWidget(QWidget):
    def __init__(self, save_path):
        super().__init__()
        self.resize(200,200)
        layout = QVBoxLayout()
        # save_path = r"./Assets/Apples.webp" # test image
        
        self.image = draggableOutput(save_path, self)
        layout.addWidget(self.image)
        #self.setLayout(layout) # added this last second, dont think it will fix the code
    def updateImage(self, save_path):
        self.image.setImage(save_path)
        print("updating output image")

