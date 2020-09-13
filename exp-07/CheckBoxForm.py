# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckBoxForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGoster = QtWidgets.QPushButton(self.centralwidget)
        self.btnGoster.setGeometry(QtCore.QRect(20, 200, 221, 41))
        self.btnGoster.setObjectName("btnGoster")
        self.lblSonuc = QtWidgets.QLabel(self.centralwidget)
        self.lblSonuc.setGeometry(QtCore.QRect(20, 280, 291, 91))
        self.lblSonuc.setObjectName("lblSonuc")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(10, 20, 251, 161))
        self.groupHobiler.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.groupHobiler)
        self.widget.setGeometry(QtCore.QRect(10, 30, 221, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitap = QtWidgets.QCheckBox(self.widget)
        self.cbKitap.setObjectName("cbKitap")
        self.verticalLayout.addWidget(self.cbKitap)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(300, 20, 311, 161))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cbProgramlama)
        self.cbGorsel = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbGorsel.setObjectName("cbGorsel")
        self.verticalLayout_2.addWidget(self.cbGorsel)
        self.cbVeritabani = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbVeritabani.setObjectName("cbVeritabani")
        self.verticalLayout_2.addWidget(self.cbVeritabani)
        self.btnGoster_dersler = QtWidgets.QPushButton(self.centralwidget)
        self.btnGoster_dersler.setGeometry(QtCore.QRect(310, 200, 221, 41))
        self.btnGoster_dersler.setObjectName("btnGoster_dersler")
        self.lblSonuc_dersler = QtWidgets.QLabel(self.centralwidget)
        self.lblSonuc_dersler.setGeometry(QtCore.QRect(310, 280, 291, 91))
        self.lblSonuc_dersler.setObjectName("lblSonuc_dersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGoster.setText(_translate("MainWindow", "Secilenleri Goster"))
        self.lblSonuc.setText(_translate("MainWindow", "TextLabel"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinemaya gitmek"))
        self.cbKitap.setText(_translate("MainWindow", "Kitap okumak"))
        self.cbSpor.setText(_translate("MainWindow", "Spor yapmak"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama Temelleri"))
        self.cbGorsel.setText(_translate("MainWindow", "Gorsel Programlama"))
        self.cbVeritabani.setText(_translate("MainWindow", "Veri Tabani"))
        self.btnGoster_dersler.setText(_translate("MainWindow", "Secilenleri Goster"))
        self.lblSonuc_dersler.setText(_translate("MainWindow", "TextLabel"))
