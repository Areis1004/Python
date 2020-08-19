import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

textArea = None
inputOne = None
inputTwo = None

def button_Clicked():
    textArea.setText("Welcome Back to the Session...")

def salutation_Clicked():
    textArea.setText(str(int(inputOne.text()) + int(inputTwo.text())))

def window():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(200,200,400,400)

    global textArea
    textArea = QLabel(window)
    textArea.move(10, 10)
    textArea.setText("Hello World... This is Mayank....")

    textAreaOther = QLabel(window)
    textAreaOther.move(10, 30)
    textAreaOther.setText("Wlcome to session on PyQt..")

    pushButton = QPushButton(window)
    pushButton.move(10, 50)
    pushButton.setText("Click to Update the Salutation...")
    pushButton.clicked.connect(button_Clicked)

    global inputOne
    inputOne = QLineEdit(window)
    inputOne.move(10, 80)
    inputOne.setText("0")

    global inputTwo
    inputTwo = QLineEdit(window)
    inputTwo.move(10, 110)
    inputTwo.setText("0")

    pushButtonCommit = QPushButton(window)
    pushButtonCommit.move(10, 140)
    pushButtonCommit.setText("Click to Add...")
    pushButtonCommit.clicked.connect(salutation_Clicked)

    window.show()
    sys.exit(app.exec_())

window()