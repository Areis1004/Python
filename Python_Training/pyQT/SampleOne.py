import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

b2 = None
b1 = None
b3 = None

def window():
   app = QApplication([])
   window = QWidget()
   window.setGeometry(200,200,400,400)
   b = QLabel(window)
   b.setText("Hello World!")

   global b2
   b2 = QPushButton(window)
   b2.setText("Button2")
   b2.move(100,100)
   b2.clicked.connect(b1_clicked)
   
   window.setWindowTitle("PyQt")

   global b3
   b3 = QLineEdit(window)
   b3.setText("Button2")
   b3.move(20,200)

   global b1
   b1 = QLineEdit(window)
   b1.setText("Button1")
   b1.move(200,200)

   window.show()
   sys.exit(app.exec_())

def b1_clicked():
    b2.setText(str(int(b1.text()) + int(b3.text())))
	
window()




#   from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#app = QApplication([])
#window = QWidget()
#layout = QVBoxLayout()
#layout.addWidget(QPushButton('Top'))
#layout.addWidget(QPushButton('Bottom'))
#window.setLayout(layout)
#window.show()
#app.exec_()