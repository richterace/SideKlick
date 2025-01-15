from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget, QGridLayout, QScrollArea, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5 import uic
import sys
from foodCalorie.assets import calories
import os

class Calorie(QMainWindow):
    
    def __init__(self):
        super( Calorie, self).__init__()
        
        # Load the UI file
        uic.loadUi("foodCalorie\Calorie.ui", self)
        
        self.stackedwidget = self.findChild(QStackedWidget, "stackedWidget")
        self.widget1 = self.findChild(QWidget, "page")
        self.widget2 = self.findChild(QWidget, "page_2")
        self.widget3 = self.findChild(QWidget, "page_3")
        self.widget4 = self.findChild(QWidget, "page_4")
        self.widget5 = self.findChild(QWidget, "page_5")
        self.widget6 = self.findChild(QWidget, "page_6")
        self.widget7 = self.findChild(QWidget, "page_7")
        self.widget8 = self.findChild(QWidget, "page_8")
        self.widget9 = self.findChild(QWidget, "page_9")
        
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.button11 = self.findChild(QPushButton, "pushButton_11")
        self.button12 = self.findChild(QPushButton, "pushButton_12")
        self.button13 = self.findChild(QPushButton, "pushButton_13")
        self.button14 = self.findChild(QPushButton, "pushButton_14")
        self.button15 = self.findChild(QPushButton, "pushButton_15")
        self.button16 = self.findChild(QPushButton, "pushButton_16")
        self.backButton2 = self.findChild(QPushButton, "backButton2")   
   
        
        self.button1.clicked.connect(self.go_to_vegetables)
        self.button2.clicked.connect(self.go_to_fruits)
        self.button3.clicked.connect(self.go_to_grains)
        self.button4.clicked.connect(self.go_to_proteins)
        self.button5.clicked.connect(self.go_to_dairy)
        self.button6.clicked.connect(self.go_to_nuts)
        self.button7.clicked.connect(self.go_to_sweets)
        self.button8.clicked.connect(self.go_to_beverages)
        self.button9.clicked.connect(self.back)
        self.button10.clicked.connect(self.back)
        self.button11.clicked.connect(self.back)
        self.button12.clicked.connect(self.back)
        self.button13.clicked.connect(self.back)
        self.button14.clicked.connect(self.back)
        self.button15.clicked.connect(self.back)
        self.button16.clicked.connect(self.back)
        
    def back(self):
        self.stackedwidget.setCurrentIndex(0)
    def go_to_vegetables(self):
        self.stackedwidget.setCurrentIndex(1)
    def go_to_fruits(self):
        self.stackedwidget.setCurrentIndex(2)
    def go_to_grains(self):
        self.stackedwidget.setCurrentIndex(3)
    def go_to_proteins(self):
        self.stackedwidget.setCurrentIndex(4)
    def go_to_dairy(self):
        self.stackedwidget.setCurrentIndex(5)
    def go_to_nuts(self):
        self.stackedwidget.setCurrentIndex(6)
    def go_to_sweets(self):
        self.stackedwidget.setCurrentIndex(7)
    def go_to_beverages(self):
        self.stackedwidget.setCurrentIndex(8)
        
        
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =  Calorie()
    window.show()
    sys.exit(app.exec_())