import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.setGeometry(100,100,500,500)

        hlayout1 = QtWidgets.QHBoxLayout()        
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('green'))
        hlayout1.addWidget(Color('blue'))
        #hlayout1.setContentsMargins(50,0,0,0)   #bosluk birakiyor
        hlayout1.setContentsMargins(30,20,0,30)   #bosluk birakiyor
        hlayout1.setSpacing(50)  #her bir eleman arasinda bosluk olusturuluyor

        hlayout2 = QtWidgets.QHBoxLayout()        
        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('blue'))
        hlayout2.setSpacing(20)  #her bir eleman arasinda bosluk olusturuluyor

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()