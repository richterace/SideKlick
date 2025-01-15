from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget, QGridLayout, QScrollArea, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5 import uic
import sys
from foodGuide.image import food
import os

class FoodHand(QMainWindow):
    
    def __init__(self):
        super( FoodHand, self).__init__()
        
        # Load the UI file
        uic.loadUi("foodGuide\hfoodguide.ui", self)
        
        self.stackedwidget = self.findChild(QStackedWidget, "stackedWidget")
        self.widget1 = self.findChild(QWidget, "page")     
        self.backButton = self.findChild(QPushButton, "backButton")   
        #self.button1.clicked.connect(self.go_to_vegetables)
       # self.button9.clicked.connect(self.back)
 
        
        
              

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =  FoodHand()
    window.show()
    sys.exit(app.exec_())