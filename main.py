import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from urllib.request import urlopen

class DogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("dog.dog.dog")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        url = "https://avatars.githubusercontent.com/u/171740024?v=4&size=64"

        try:
            data = urlopen(url).read()
            image = QPixmap()
            image.loadFromData(data)

            label = QLabel()
            label.setPixmap(image)
            label.setAlignment(Qt.AlignCenter)
        except Exception as e:
            label = QLabel(f"Failed to load image.\n{e}")
            label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)
        self.resize(image.width(), image.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DogWindow()
    window.show()
    sys.exit(app.exec_())
