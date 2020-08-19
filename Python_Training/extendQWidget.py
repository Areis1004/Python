import sys
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Working with PyQt"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.initialize()

    def initialize(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
