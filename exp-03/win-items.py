import sys   
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('Ilk Uygulama') 
        self.setGeometry(200,200,500,500) 
        self.setWindowIcon(QIcon('icon.png'))  
        self.setToolTip('Tooltip Mesaji') 
        self.initUI() 

    def initUI(self):
        self.lbl_isim = QtWidgets.QLabel(self)
        self.lbl_isim.setText('Isminiz : ')
        self.lbl_isim.move(50,30)

        self.lbl_soyisim = QtWidgets.QLabel(self)
        self.lbl_soyisim.setText('Soyisminiz : ')
        self.lbl_soyisim.move(50,70)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.move(150,150)
        self.lbl_sonuc.setText('Sonuc')
        self.lbl_sonuc.resize(300,50)

        self.txt_isim = QtWidgets.QLineEdit(self)
        self.txt_isim.move(250, 30)
        self.txt_isim.resize(200,32)

        self.txt_soyisim = QtWidgets.QLineEdit(self)
        self.txt_soyisim.move(250, 70)
        self.txt_soyisim.resize(200,32)
          
        self.btn_kaydet = QtWidgets.QPushButton(self)
        self.btn_kaydet.move(250, 110)
        self.btn_kaydet.setText('Kaydet')

        self.btn_kaydet.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_sonuc.setText(self.txt_isim.text() + ' ' + self.txt_soyisim.text() + ' kisisi sisteme kaydedilmistir')

 
def window(): 
    app = QApplication(sys.argv)
    win = MyWindow()    

    win.show()   
    sys.exit(app.exec_())    

window()
 
# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar