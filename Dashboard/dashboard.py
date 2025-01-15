import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStackedWidget, QMessageBox, QLineEdit, QScrollArea, QWidget, QGridLayout, QVBoxLayout,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QFile, pyqtSignal
from PyQt5 import uic
from Dashboard.assets import resources_dash1
from Calendar.WithRadio import Calendar
import mysql.connector
from mysql.connector import Error

ui_file_path = os.path.join(os.path.dirname(__file__), "dashboard.ui")

class DashboardMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the ui file
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self)
        ui_file.close()
        # Connect to MySQL database with error handling
        try:
            self.db_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="123456",
                database="health"
            )
            self.db_cursor = self.db_connection.cursor()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Connection Error", f"Failed to connect to database: {err}")
            sys.exit(1)

        # Find the stacked widget in the UI
        self.stacked_widget = self.findChild(QStackedWidget, "stackedWidget")
        
        # HomeDashboard Buttons
        self.profile_button = self.findChild(QPushButton, "ProfileButton_5")
        # HomeDashboard Buttons
        self.profile_button2 = self.findChild(QPushButton, "ProfileButton_2")
        self.profile_button6 = self.findChild(QPushButton, "ProfileButton_6")
        self.setting_button = self.findChild(QPushButton, "SettingButton")
        self.feature_button = self.findChild(QPushButton, "FeatureButton")
        self.go_to_task_button = self.findChild(QPushButton, "pushButton")
        self.save = self.findChild(QPushButton, "save")
        
          # Find the scroll area in the UI
        self.scroll = self.findChild(QScrollArea, "scrollAreaWidgetContents_2")

        # Configure the scroll area if found
        if self.scroll:
            self.scroll.setWidgetResizable(True)
            self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll.setStyleSheet("""
                QScrollArea {
                    background: transparent;
                }
                QScrollBar:vertical {
                    border: none;
                    background: #f0f0f0;
                    width: 8px;
                    margin: 10px 0 10px 0;
                    border-radius: 4px;
                }
                QScrollBar::handle:vertical {
                    background: #a0a0a0;
                    min-height: 20px;
                    border-radius: 4px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }
            """)

        else:
            print("Scroll area not found in UI.")

        # Ensure scrollWidgetContents has a layout
        if self.scrollAreaWidgetContents_2.layout() is None:
            layout = QGridLayout(self.scrollAreaWidgetContents_2)
            layout.setVerticalSpacing(25)
            layout.setHorizontalSpacing(25)
            self.scrollAreaWidgetContents_2.setLayout(layout)

        # Back Buttons
        self.back_button1 = self.findChild(QPushButton, "BackButton")
        self.back_button2 = self.findChild(QPushButton, "BackButton_2")
        self.back_button3 = self.findChild(QPushButton, "BackButton_3")
        self.change_button = self.findChild(QPushButton, "pushButton")
        self.userName = self.findChild(QLabel, "userName")
        
        # Functionality of homedashboard buttons
        self.profile_button.clicked.connect(self.go_to_profile_widget)
        self.setting_button.clicked.connect(self.go_to_setting_widget)
        self.feature_button.clicked.connect(self.go_to_feature_widget)

        # Functionality of back buttons
        self.back_button1.clicked.connect(self.go_to_home_widget)
        self.back_button2.clicked.connect(self.go_to_home_widget)
        self.back_button3.clicked.connect(self.go_to_home_widget)
        
        self.profile_button2.clicked.connect(self.choose_image)
        self.load_profile_image()

        # Set default widget to the first one
        self.stacked_widget.setCurrentIndex(1)
        
        self.image_file_path = ""

        # QLineEdit and QLabel
        self.personinfo = self.findChild(QLineEdit, "personinfo")
        self.personinfo_2 = self.findChild(QLineEdit, "personinfo_2")
        self.personinfo_3 = self.findChild(QLineEdit, "personinfo_3")
        self.personinfo_4 = self.findChild(QLineEdit, "personinfo_4")
        self.personinfo_5 = self.findChild(QLineEdit, "personinfo_5")
        self.personinfo_6 = self.findChild(QLineEdit, "personinfo_6")
        self.personinfo_7 = self.findChild(QLineEdit, "personinfo_7")
        self.personinfo_8 = self.findChild(QLineEdit, "personinfo_8")
        self.personinfo_9 = self.findChild(QLineEdit, "personinfo_9")
        self.personinfo_10 = self.findChild(QLineEdit, "personinfo_10")
        self.personinfo_11 = self.findChild(QLineEdit, "personinfo_11")
        self.label = self.findChild(QLabel, "label")
        self.label_2 = self.findChild(QLabel, "label_2")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_4 = self.findChild(QLabel, "label_4")
        self.label_5 = self.findChild(QLabel, "label_5")
        self.label_6 = self.findChild(QLabel, "label_6")
        self.label_7 = self.findChild(QLabel, "label_7")
        self.label_8 = self.findChild(QLabel, "label_8")
        self.label_9 = self.findChild(QLabel, "label_9")
        self.label_10 = self.findChild(QLabel, "label_10")
        
        # Connect the save button to the custom slot
        self.save.clicked.connect(self.save_person_info)
        
       
    def save_person_info(self):
        # Set the text of the label to the text from the QLineEdit
        self.label.setText(self.personinfo.text())
        self.label_2.setText(self.personinfo_4.text())
        self.label_4.setText(self.personinfo_5.text())
        self.label_3.setText(self.personinfo_6.text())

    def update_profile_name(self):
        if self.logged_in_user_id is None:
            self.userName.setText("Unknown User")
            return
        
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor(dictionary=True)
                cursor.execute("SELECT username FROM users WHERE user_id = %s", (self.logged_in_user_id,))
                user = cursor.fetchone()
                if user:
                    self.userName.setText(f"@{user['username']}")
                    self.userName2.setText(f"{user['username']}")
                else:
                    self.userName.setText("Unknown User")
                
                # Set the font to Arial and font size to 14
                self.userName.setStyleSheet("font-family: Arial; font-size: 14px; font-weight:bold; background-color: transparent; background: none;")
                self.userName2.setStyleSheet("color:white; font-family: Verdana; font-size: 29px; font-weight:bold; background-color: transparent; background: none;")
                
            except Error as e:
                print(f"Error retrieving username from MySQL: {e}")


    def choose_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Image Files (*.jpg *.png)", options=options)
        if fileName:
            self.profile_button2.setStyleSheet(f"border-image: url({fileName}); background-repeat: no-repeat; background-position: center;border-radius: 65px; border: 3px solid white; background-size: cover;")
            self.profile_button6.setStyleSheet(f"border-image: url({fileName}); background-repeat: no-repeat; background-position: center;border-radius: 65px; border: 3px solid white; background-size: cover;")
            self.image_file_path = fileName  # Save the file path
            self.save_profile_image(fileName)
            self.load_profile_image()

    def save_profile_image(self, file_path):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="123456",
                database="health"
            )
            cursor = conn.cursor()
            username = "your_username"
            cursor.execute("UPDATE user_profiles SET profile_image = %s WHERE username = %s", (self.image_file_path, username))  # Use the instance variable
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error saving profile image: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def load_profile_image(self):
        try:
            conn = mysql.connector.connect(
               host="127.0.0.1",
                user="root",
                password="123456",
                database="health"
            )
            cursor = conn.cursor()
            username = "your_username"
            cursor.execute("SELECT profile_image FROM user_profiles WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result:
                file_path = result[0]
                self.profile_button2.setStyleSheet(f"border-image: url({file_path}); background-repeat: no-repeat; background-position: center;border-radius: 65px; border: 3px solid white; background-size: cover;")
        except mysql.connector.Error as e:
            print(f"Error loading profile image: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
            
    def go_to_profile_widget(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_home_widget(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_setting_widget(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_feature_widget(self):
        self.stacked_widget.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = DashboardMain()
    main_window.show()
    sys.exit(app.exec_())
    