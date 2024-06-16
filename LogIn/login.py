from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStackedWidget, QMessageBox, QLineEdit, QScrollArea, QWidget, QGridLayout
from PyQt5.QtCore import QFile
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5 import uic
from LogIn.assets import login_resource
import os
import mysql.connector

ui_file_path = os.path.join(os.path.dirname(__file__), "login.ui")

class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        # Load the ui file
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self)  # Load the UI file directly into the QMainWindow
        ui_file.close()

        self.stacked_widget = self.findChild(QStackedWidget, "stackedWidget")
       

        #creating placeholder texts for login
        self.userLogin.setPlaceholderText("Username")
        self.passwordLogin.setPlaceholderText("Password")
        self.passwordLogin.setEchoMode(QLineEdit.Password)

        #creating placeholder texts for signup
        self.userSignup.setPlaceholderText("Username")
        self.passwordSignup.setPlaceholderText("Password")
        self.passwordSignup.setEchoMode(QLineEdit.Password)
        self.passwordConfirm.setPlaceholderText("Confirm Password")
        self.passwordConfirm.setEchoMode(QLineEdit.Password)

        
        self.signUpButton.clicked.connect(self.go_to_signup)
        self.stacked_widget.setCurrentIndex(0)

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_signup(self):
        self.stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = login()
    main_window.show()
    sys.exit(app.exec_())