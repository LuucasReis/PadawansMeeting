# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 565)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_photo = QtWidgets.QLabel(self.centralwidget)
        self.label_photo.setGeometry(QtCore.QRect(10, 10, 551, 471))
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        self.label_estagio = QtWidgets.QLabel(self.centralwidget)
        self.label_estagio.setGeometry(QtCore.QRect(-125, 400, 535, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_estagio.setFont(font)
        self.label_estagio.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_estagio.setObjectName("label_estagio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pictures"))
        self.label_estagio.setText(_translate("MainWindow", "                                     O ESTÁGIO VEM HAHA!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
