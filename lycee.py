# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lycee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 671, 471))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 161, 23))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 59, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(220, 40, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(30, 160, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 59, 15))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 60, 91, 23))
        self.comboBox_2.setObjectName("comboBox_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(140, 60, 131, 191))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(290, 60, 141, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(470, 20, 59, 15))
        self.label_4.setObjectName("label_4")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_4.setGeometry(QtCore.QRect(450, 60, 141, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 60, 111, 23))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 59, 15))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(170, 20, 59, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(300, 20, 59, 15))
        self.label_14.setObjectName("label_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 60, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget_8 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_8.setGeometry(QtCore.QRect(280, 60, 151, 91))
        self.listWidget_8.setObjectName("listWidget_8")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(480, 20, 59, 15))
        self.label_15.setObjectName("label_15")
        self.listWidget_9 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_9.setGeometry(QtCore.QRect(470, 60, 161, 351))
        self.listWidget_9.setObjectName("listWidget_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 59, 15))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 50, 101, 23))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(180, 20, 59, 15))
        self.label_9.setObjectName("label_9")
        self.listWidget_5 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_5.setGeometry(QtCore.QRect(150, 50, 221, 351))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(480, 30, 71, 16))
        self.label_10.setObjectName("label_10")
        self.listWidget_6 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_6.setGeometry(QtCore.QRect(400, 60, 256, 111))
        self.listWidget_6.setObjectName("listWidget_6")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(490, 200, 71, 16))
        self.label_11.setObjectName("label_11")
        self.listWidget_7 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_7.setGeometry(QtCore.QRect(400, 220, 256, 181))
        self.listWidget_7.setObjectName("listWidget_7")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 30, 101, 23))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_6.setGeometry(QtCore.QRect(110, 80, 151, 23))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_7.setGeometry(QtCore.QRect(110, 130, 151, 23))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(20, 30, 59, 15))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(20, 80, 59, 15))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(20, 130, 59, 15))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setGeometry(QtCore.QRect(20, 180, 59, 15))
        self.label_19.setObjectName("label_19")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_8.setGeometry(QtCore.QRect(110, 180, 151, 23))
        self.comboBox_8.setObjectName("comboBox_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 230, 113, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setGeometry(QtCore.QRect(20, 230, 59, 15))
        self.label_20.setObjectName("label_20")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.comboBox.currentTextChanged['QString'].connect(MainWindow.profs_par_discipline)
        self.pushButton.clicked.connect(MainWindow.add_discipline)
        self.comboBox_2.currentTextChanged['QString'].connect(MainWindow.prof)
        self.comboBox_3.currentTextChanged['QString'].connect(MainWindow.classe)
        self.comboBox_4.currentTextChanged['QString'].connect(MainWindow.eleve)
        self.comboBox_5.currentTextChanged['QString'].connect(MainWindow.notes_classes)
        self.comboBox_6.currentTextChanged['QString'].connect(MainWindow.update_note)
        self.comboBox_7.currentTextChanged['QString'].connect(MainWindow.update_note)
        self.comboBox_8.currentTextChanged['QString'].connect(MainWindow.update_note)
        self.comboBox_7.currentTextChanged['QString'].connect(MainWindow.update_devoirs)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Disciplines"))
        self.label_3.setText(_translate("MainWindow", "Ajouter"))
        self.lineEdit.setText(_translate("MainWindow", "Nom ?"))
        self.label_7.setText(_translate("MainWindow", "Professeurs"))
        self.pushButton.setText(_translate("MainWindow", "Ajouter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Disciplines"))
        self.label_5.setText(_translate("MainWindow", "Professeur"))
        self.label_6.setText(_translate("MainWindow", "Disciplines"))
        self.label_2.setText(_translate("MainWindow", "Classes"))
        self.label_4.setText(_translate("MainWindow", "Cours"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Professeurs"))
        self.label_12.setText(_translate("MainWindow", "Elève"))
        self.label_13.setText(_translate("MainWindow", "Classe"))
        self.label_14.setText(_translate("MainWindow", "Cours"))
        self.label_15.setText(_translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Elèves"))
        self.label_8.setText(_translate("MainWindow", "Classe"))
        self.label_9.setText(_translate("MainWindow", "Elèves"))
        self.label_10.setText(_translate("MainWindow", "Professeurs"))
        self.label_11.setText(_translate("MainWindow", "Disciplines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Classes"))
        self.label_16.setText(_translate("MainWindow", "Classe"))
        self.label_17.setText(_translate("MainWindow", "Elève"))
        self.label_18.setText(_translate("MainWindow", "Cours"))
        self.label_19.setText(_translate("MainWindow", "Devoir"))
        self.label_20.setText(_translate("MainWindow", "Note"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Statistiques"))
