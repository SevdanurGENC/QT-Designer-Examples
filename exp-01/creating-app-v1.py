import sys   
from PyQt5 import QtWidgets 
#komut satirini kullanacagimiz icin sys kullaniliyor
#qtwidgets ile qt designer'in toollarini aktiflestiriyoruz
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window(): #pencere olusturuyoruz ve nesnelerle baglantisini yapiyoruz.
    # app = QtWidgets.QApplication egerki from PyQt5.QtWidgets import QApplication, QMainWindow
    # yazilmayacaksa bu kod yazilabilir. yazilacaksa asagidaki gibi kullanilir
    app = QApplication(sys.argv)
    win = QMainWindow()  #pencere nesnesi aktif hale getiriliyor ve bir degiskene aktariliyor

    win.setWindowTitle('Ilk Uygulama')  #pencereye title yazdiriliyor.
    win.setGeometry(200,200,500,500)  #pencerenin yatay ve dikeyde gorulen pixel boyutlariyla pencerenin yatay ve dikeydeki boyutlari
    win.setWindowIcon(QIcon('icon.png'))  #icon icin qicon kutuphanesinden qtgui eklentisi kullanilmaktadir.
    win.setToolTip('Tooltip Mesaji')  #tooltip mesaji yazilabilmektedir. bunun icin qtooltip kutuphanesi kullanilmaktadir.
        


    win.show()  #pencere gosteriliyor
    sys.exit(app.exec_())  #pencere kapatmak icin x iconu ekleniyor


window()