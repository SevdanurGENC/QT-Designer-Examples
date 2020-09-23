from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from TelefonDefteriGUI import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    

        self.loadKullaniciListesi()

# Kullanicilar (id INT, isim TEXT, soyisim TEXT, sehir TEXT, telefon TEXT, email TEXT)

    def loadKullaniciListesi(self): 
        Kullanicilar = [
            {'id': 'Samsung S5', 'isim': 'Sevdanur', 'soyisim': 'GENC', 'sehir': 'Kastamonu', 'telefon': '05557777777', 'email': 'sgenc@kastamonu.edu.tr'},
            {'id': 'Samsung S6', 'isim': 3000, 'soyisim': 3000, 'sehir': 3000, 'telefon': 3000, 'email': 3000}
        ]

        self.ui.tblListele.setRowCount(len(Kullanicilar))

        self.ui.tblListele.setColumnCount(6)
        self.ui.tblListele.setHorizontalHeaderLabels(('ID','Isim','Soyisim','Sehir','Telefon','Email'))
        self.ui.tblListele.setColumnWidth(0,200)
        self.ui.tblListele.setColumnWidth(1,100)
        self.ui.tblListele.setColumnWidth(2,100)
        self.ui.tblListele.setColumnWidth(3,100)
        self.ui.tblListele.setColumnWidth(4,100)
        self.ui.tblListele.setColumnWidth(5,100)


        rowIndex = 0
        for user in Kullanicilar:
            self.ui.tblListele.setItem(rowIndex,0, QTableWidgetItem(user['id']))
            self.ui.tblListele.setItem(rowIndex,1, QTableWidgetItem(str(user['isim']))) 
            self.ui.tblListele.setItem(rowIndex,2, QTableWidgetItem(str(user['soyisim']))) 
            self.ui.tblListele.setItem(rowIndex,3, QTableWidgetItem(str(user['sehir']))) 
            self.ui.tblListele.setItem(rowIndex,4, QTableWidgetItem(str(user['telefon']))) 
            self.ui.tblListele.setItem(rowIndex,5, QTableWidgetItem(str(user['email']))) 

            rowIndex+=1

            
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
 