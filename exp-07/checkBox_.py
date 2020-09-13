import sys
from PyQt5 import QtWidgets
from CheckBoxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitap.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnGoster.clicked.connect(self.getAllHobiler)
        self.ui.btnGoster_dersler.clicked.connect(self.getAllDersler)

    def getAllHobiler(self):
        sonuc = ''
        # items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) #form uzerindeki tum chckbx larin bilgileri toplaniyor
        
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox) #form uzerindeki tum chckbx larin bilgileri toplaniyor
        for cb in items:
            if cb.isChecked(): 
                sonuc += cb.text() + '\n'
        self.ui.lblSonuc.setText(sonuc)

    def getAllDersler(self):
        sonuc = ''
        # items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) #form uzerindeki tum chckbx larin bilgileri toplaniyor
        
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox) #form uzerindeki tum chckbx larin bilgileri toplaniyor
        for cb in items:
            if cb.isChecked(): 
                sonuc += cb.text() + '\n'
        self.ui.lblSonuc_dersler.setText(sonuc)

    def show_state(self, value):
        #print(value)
        #print(self.ui.cbSinema.isChecked())
        #print(self.ui.cbSinema.text())
        cb = self.sender() 
        #print(value)
        #print(cb.text())
        #print(cb.isChecked()) 

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app() 