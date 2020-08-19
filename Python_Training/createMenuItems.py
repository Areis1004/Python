import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class App(QMainWindow):
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

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        mainMenu.addMenu("Selection")

        self.show()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())