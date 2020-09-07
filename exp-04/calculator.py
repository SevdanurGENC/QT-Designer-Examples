import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Hesap makinesi')
        self.setGeometry(200,200,500,500)
        self.initUI()
    
    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Birinci Sayiyi Giriniz : ')
        self.lbl_sayi1.move(50,30)
        self.lbl_sayi1.resize(200,32)

        self.txt_sayi1 = QtWidgets.QLineEdit(self) 
        self.txt_sayi1.move(250,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Ikinci Sayiyi Giriniz : ')
        self.lbl_sayi2.move(50,80)
        self.lbl_sayi2.resize(200,32)
       
        self.txt_sayi2 = QtWidgets.QLineEdit(self) 
        self.txt_sayi2.move(250,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150, 130)
        #self.btn_topla.clicked.connect(self.toplama)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Cikar')
        self.btn_cikar.move(150, 170)
        #self.btn_cikar.clicked.connect(self.cikarma) 
        self.btn_cikar.clicked.connect(self.hesapla)
 
        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText('Carpma')
        self.btn_carpma.move(150, 210)
        #self.btn_carpma.clicked.connect(self.carpma)
        self.btn_carpma.clicked.connect(self.hesapla)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText('Bolme')
        self.btn_bolme.move(150, 250)
        #self.btn_bolme.clicked.connect(self.bolme)
        self.btn_bolme.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuc : ')  
        self.lbl_sonuc.resize(300,32)
        self.lbl_sonuc.move(150,290) 

    def toplama(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuc : ' + str(result) )

    def cikarma(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuc : ' + str(result) )

    def carpma(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuc : ' + str(result) )

    def bolme(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('Sonuc : ' + str(result) )
    
    def hesapla(self):
        sender = self.sender().text()
        #print(sender.text())
        result=0

        if sender=='Topla':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender=='Cikar':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender=='Carpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender=='Bolme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        
        self.lbl_sonuc.setText('Sonuc : ' + str(result) )








def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()
