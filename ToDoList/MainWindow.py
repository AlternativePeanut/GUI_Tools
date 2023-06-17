# Simple to do list with a selected due date. Items can be added and removed and will be stored in sqlite3 db for future use
#
#Created by: AlternativePeanut
#
# TODO: - Complete functionality for completed goals
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PopUp1 import Ui_PopUp1
import sqlite3


class Ui_MainWindow(object):
    #Opens the window that will add a new item
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PopUp1()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.addItem)
        self.window.show()

    #Adds a new item
    def addItem(self):
        connection = sqlite3.connect('ToDoList\\list.db')
        c = connection.cursor()
        item_desc = self.ui.textEdit.toPlainText()
        date = self.ui.dateEdit.dateTime().toString('MM-dd-yyyy')
        c.execute(f'INSERT INTO ToDo_List (item_desc, due_date) VALUES ("{item_desc}","{date}")')
        connection.commit()
        connection.close()
        self.refreshList()
    
    #removes an item
    def removeItem(self):
        recordValues = self.listWidget.selectedItems()[0].text().split('    ')
        connection = sqlite3.connect('ToDoList\\list.db')
        c = connection.cursor()
        c.execute(f"DELETE FROM ToDo_List WHERE item_desc = '{recordValues[0]}' and due_date = '{recordValues[1]}'")
        connection.commit()
        connection.close()
        self.refreshList()
    
    #refreshes list by checking for updates in the db
    def refreshList(self):
        connection = sqlite3.connect('ToDoList\\list.db')
        c = connection.cursor()
        c.execute("SELECT * FROM ToDo_List")
        allRecords = c.fetchall()
        self.listWidget.clear()
        for record in allRecords:
            self.listWidget.addItem(record[0]+"    "+record[1])
        connection.commit()
        connection.close()

    
    #Initialized UI for the main window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 371, 301))
        self.listWidget.setObjectName("listWidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openWindow())
        self.addButton.setGeometry(QtCore.QRect(20, 30, 111, 61))
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.removeItem())
        self.deleteButton.setGeometry(QtCore.QRect(150, 30, 111, 61))
        self.deleteButton.setObjectName("deleteButton")
        self.completed = QtWidgets.QPushButton(self.centralwidget)
        self.completed.setGeometry(QtCore.QRect(280, 30, 111, 61))
        self.completed.setObjectName("completed")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
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
        self.addButton.setText(_translate("MainWindow", "Add Goal"))
        self.deleteButton.setText(_translate("MainWindow", "Remove Goal"))
        self.completed.setText(_translate("MainWindow", "Completed Goals"))


if __name__ == "__main__":
    import sys
    sys.path.append('GUI_Tools/ToDoList')
    
    #Connects or adds db
    connection = sqlite3.connect('ToDoList\\list.db')
    c = connection.cursor()

    #add to do list table if it doesn't exist
    c.execute("""CREATE TABLE if not exists ToDo_List(item_desc text, due_date date)""")
    connection.commit()
    connection.close()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshList()
    MainWindow.show()
    sys.exit(app.exec_())
