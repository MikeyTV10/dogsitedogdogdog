import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("dog.dog.dog")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Load the image
        image_path = os.path.join(os.path.dirname(__file__), "dog.png")
        if not os.path.exists(image_path):
            label = QLabel("dog.png not found.")
            label.setAlignment(Qt.AlignCenter)
        else:
            pixmap = QPixmap(image_path)
            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)
        self.resize(pixmap.width() if 'pixmap' in locals() else 300,
                    pixmap.height() if 'pixmap' in locals() else 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DogWindow()
    window.show()
    sys.exit(app.exec_())
