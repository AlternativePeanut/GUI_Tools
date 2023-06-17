# Pop up window for adding items to main window
#
# Created by: AlternativePeanut



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp1(object):
    
    #Initialize UI for pop up window
    def setupUi(self, PopUp1):
        PopUp1.setObjectName("PopUp1")
        PopUp1.resize(485, 297)
        self.centralwidget = QtWidgets.QWidget(PopUp1)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(260, 60, 151, 41))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 6, 12), QtCore.QTime(0, 0, 0)))
        currentDay = QtCore.QDate.currentDate().day()
        currentMonth = QtCore.QDate.currentDate().month()
        currentYear =  QtCore.QDate.currentDate().year()
        self.dateEdit.setDate(QtCore.QDate(currentYear, currentMonth, currentDay))
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 201, 81))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 131, 41))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        PopUp1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PopUp1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        PopUp1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PopUp1)
        self.statusbar.setObjectName("statusbar")
        PopUp1.setStatusBar(self.statusbar)

        self.retranslateUi(PopUp1)
        QtCore.QMetaObject.connectSlotsByName(PopUp1)

    def retranslateUi(self, PopUp1):
        _translate = QtCore.QCoreApplication.translate
        PopUp1.setWindowTitle(_translate("PopUp1", "MainWindow"))
        self.label.setText(_translate("PopUp1", "Goal:"))
        self.label_2.setText(_translate("PopUp1", "Due Date:"))
        self.pushButton.setText(_translate("PopUp1", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp1 = QtWidgets.QMainWindow()
    ui = Ui_PopUp1()
    ui.setupUi(PopUp1)
    PopUp1.show()
    sys.exit(app.exec_())
