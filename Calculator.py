
# Calculator using PyQt5. Includes basic funcationality for addition, subtraction, multiplication, division and modulus
#
# Created by: AlternativePeanut
# Last Updated: 6/10/2023
#
# TODO: -Add positive/negative button
#       -Add decimal button
#       -Address dividing by 0
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.currentOperation = None
        self.previousNumber = None
        
        #Remove this vairable once final buttons are added
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]

    def setupUi(self):
        #Configuration of main window for UI
        self.setObjectName("MainWindow")
        MainWindow.resize(370, 372)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 370, 350))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 40, 5, 40)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        
        #Creating all buttons and labels
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("1"))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("2"))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("3"))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("4"))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("5"))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("6"))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("7"))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("8"))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("9"))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("+"))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("-"))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1) 
        self.pushButton_times = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("X"))
        self.pushButton_times.setObjectName("pushButton_times")
        self.gridLayout.addWidget(self.pushButton_times, 2, 3, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_divide.sizePolicy().hasHeightForWidth())
        self.pushButton_divide.setSizePolicy(sizePolicy)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 1, 3, 1, 1)
        self.pushButton_modulo = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("%"))
        self.pushButton_modulo.setObjectName("pushButton_modulo")
        self.gridLayout.addWidget(self.pushButton_modulo, 1, 2, 1, 1)         
        self.pushButton_equals = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("="))
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.gridLayout.addWidget(self.pushButton_equals, 5, 3, 1, 1)  
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("C"))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 1, 0, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda : self.press("0"))
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        #Add arguments once button functionality is included
        self.pushButton_decimal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.gridLayout.addWidget(self.pushButton_decimal, 5, 2, 1, 1)   
        self.pushButton_PosNeg = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_PosNeg.setObjectName("pushButton_PosNeg")
        self.gridLayout.addWidget(self.pushButton_PosNeg, 1, 1, 1, 1) 

        #Set menu bar and status bar
        MainWindow.setCentralWidget(self.centralwidget)  
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    #UI element translation
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_times.setText(_translate("MainWindow", "X"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_modulo.setText(_translate("MainWindow", "%"))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.pushButton_PosNeg.setText(_translate("MainWindow", "+ / -"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_equals.setText(_translate("MainWindow", "="))

    #Function called to handle all press events
    def press(self, button):

        #Clears all number stored in calculator
        if button == "C":
            self.label.setText("0")
            self.previousNumber = None
         
        #Adds number input when current display isn't 0
        elif button in self.numbers and self.label.text() != "0":       
            self.label.setText(self.label.text()+button)

        #Adds number input when current display value is 0
        elif button in self.numbers and self.label.text() == "0":
            self.label.setText(button)

        #Handles addition when calculator is waitng for another number
        elif button == "+" and self.previousNumber == None:
            self.previousNumber = float(self.label.text())
            self.label.setText("0")
            self.currentOperation = "+"

        #Handles addition when multiple operations occur
        elif button == "+" and self.previousNumber != None:
            self.add()
            self.label.setText("0")
            self.currentOperation = "+"

        #Handles subtraction when calculator is waitng for another number
        elif button == "-" and self.previousNumber == None:
            self.previousNumber = float(self.label.text())
            self.label.setText("0")
            self.currentOperation = "-"

        #Handles subtraction when multiple operations occur
        elif button == "-" and self.previousNumber != None:
            self.subtract()
            self.label.setText("0")
            self.currentOperation = "-"

        #Handles multiplication when calculator is waitng for another number
        elif button == "X" and self.previousNumber == None:    
            self.previousNumber = float(self.label.text()) 
            self.label.setText("0")
            self.currentOperation = "X"

        #Handles multiplication when multiple operations occur
        elif button == "X" and self.previousNumber != None:
            self.multiply()
            self.label.setText("0")
            self.currentOperation = "X"

        #Handles division when calculator is waitng for another number
        elif button == "/" and self.previousNumber == None:
            self.previousNumber = float(self.label.text()) 
            self.label.setText("0")
            self.currentOperation = "/"

        #Handles division when multiple operations occur
        elif button == "/" and self.previousNumber != None:
            self.divide()
            self.label.setText("0")
            self.currentOperation = "/"

        #Handles modulus when calculator is waitng for another number
        elif button == "%" and self.previousNumber == None:
            self.previousNumber = float(self.label.text()) 
            self.label.setText("0")
            self.currentOperation = "%"

        #Handles division when multiple operations occur
        elif button == "%" and self.previousNumber != None:
            self.modulus()
            self.label.setText("0")
            self.currentOperation = "%"

        #Completes operations and displays final value
        elif button == "=" and self.previousNumber != None:
            self.equals()
            print(str(self.previousNumber))
            self.label.setText(str(self.previousNumber))
            self.previousNumber = None
            self.currentOperation = None

        
    #Function that handles all addition operations
    def add(self):
        self.previousNumber += float(self.label.text()) 
    
    #Function that handles all subtraction operations
    def subtract(self):
        self.previousNumber -= float(self.label.text()) 
    
    #Function that handles all multiplication operations
    def multiply(self):
        self.previousNumber *= float(self.label.text()) 

    #Function that handles all division operations     
    def divide(self):
        self.previousNumber /= float(self.label.text()) 
    
    #Function that handles all modulus operations
    def modulus(self):
        self.previousNumber %= float(self.label.text()) 

    #Function that calls the apporpriate operation for when the equals button is pressed
    def equals(self):
        if self.currentOperation == "+":
            self.add()
        elif self.currentOperation == "-":
            self.subtract()
        elif self.currentOperation == "X":
            self.multiply()
        elif self.currentOperation == "/":
            self.divide()
        elif self.currentOperation == "%":
            self.modulus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
