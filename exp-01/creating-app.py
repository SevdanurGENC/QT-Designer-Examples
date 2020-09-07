import sys   
from PyQt5 import QtWidgets 
#komut satirini kullanacagimiz icin sys kullaniliyor
#qtwidgets ile qt designer'in toollarini aktiflestiriyoruz
from PyQt5.QtWidgets import QApplication, QMainWindow

def window(): #pencere olusturuyoruz ve nesnelerle baglantisini yapiyoruz.
    # app = QtWidgets.QApplication egerki from PyQt5.QtWidgets import QApplication, QMainWindow
    # yazilmayacaksa bu kod yazilabilir. yazilacaksa asagidaki gibi kullanilir
    app = QApplication(sys.argv)
    win = QMainWindow()  #pencere nesnesi aktif hale getiriliyor ve bir degiskene aktariliyor

    win.show()  #pencere gosteriliyor
    sys.exit(app.exec_())  #pencere kapatmak icin x iconu ekleniyor


window()