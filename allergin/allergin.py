from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget, QGridLayout, QScrollArea, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5 import uic
import sys
from allergin.img import al
import os

class Ui(QMainWindow):
    
    def __init__(self):
        super( Ui, self).__init__()
        
        # Load the UI file
        uic.loadUi("allergin\ccal.ui", self)
        
        self.stackedwidget = self.findChild(QStackedWidget, "stackedWidget")
        self.widget1 = self.findChild(QWidget, "page")     
        self.backButton = self.findChild(QPushButton, "backButton")   
    
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =  Ui()
    window.show()
    sys.exit(app.exec_())