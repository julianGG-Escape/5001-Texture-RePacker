# file of only the widget to drag files out

import sys
from pathlib import Path

from PyQt6.QtCore import Qt, QMimeData, QUrl
from PyQt6.QtGui import QDrag, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout



class draggableOutput(QLabel):
    def __init__(self, image_path, parent = None):
        super().__init__(parent)
        self.image_path = Path(image_path).resolve()

        self.setPixmap(
            QPixmap(str(self.image_path)).scaled(300,300)
        )
        self.setCursor(Qt.CursorShape.OpenHandCursor)
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        mime_data.setUrls([QUrl.fromLocalFile(str(self.image_path))])
        drag.setMimeData(mime_data)

        drag.exec(Qt.DropAction.CopyAction)


class outputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)

        layout = QVBoxLayout()
        image_path = r"./Assets/Apples.webp" # place holder

        self.image = draggableOutput(image_path, self)
        layout.addWidget(self.image)

