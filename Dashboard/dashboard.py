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
        self.nameBox = self.findChild(QLineEdit, "nameBox")
        self.contactBox = self.findChild(QLineEdit, "contactBox")
        self.ageBox = self.findChild(QLineEdit, "ageBox")
        self.sexBox = self.findChild(QLineEdit, "sexBox")
        self.weightBox = self.findChild(QLineEdit, "weightBox")
        self.heightBox = self.findChild(QLineEdit, "heightBox")
        self.bmiBox = self.findChild(QLineEdit, "bmiBox")
        self.bloodBox = self.findChild(QLineEdit, "bloodBox")
        self.heartBox = self.findChild(QLineEdit, "heartBox")
        self.cholesterolBox = self.findChild(QLineEdit, "cholesterolBox")
        self.usernameBox = self.findChild(QLineEdit, "usernameBox")
        self.ageLabel = self.findChild(QLabel, "ageLabel")
        self.sexLabel = self.findChild(QLabel, "sexLabel")
        self.heightLabel = self.findChild(QLabel, "heightLabel")
        self.weightLabel = self.findChild(QLabel, "weightLabel")
        self.dateLabel = self.findChild(QLabel, "dateLabel")
        self.contactLabel = self.findChild(QLabel, "contactLabel")
        self.bmiLabel = self.findChild(QLabel, "bmiLabel")
        self.bpLabel = self.findChild(QLabel, "bpLabel")
        self.heartLabel = self.findChild(QLabel, "heartLabel")
        self.cholesterolLabel = self.findChild(QLabel, "cholesterolLabel")
        
        # Connect the save button to the custom slot
        # Inside __init__()
        # self.load_profile_data()
        self.logged_in_user_id = None  # Initialize to None
        # Save button click saves data and reloads it
        self.save.clicked.connect(lambda: [self.save_person_info(), self.load_profile_data()])
        # self.save.clicked.connect(self.save_person_info)

    
    def save_person_info(self):
        cursor = self.db_connection.cursor()
        
        # Retrieve selected values from QComboBoxes
        name = str(self.nameBox.text())
        age = str(self.ageBox.text())
        contact = str(self.contactBox.text())
        height = str(self.heightBox.text())
        sex = str(self.sexBox.text())
        weight = str(self.weightBox.text())
        bmi = str(self.bmiBox.text())
        bp = str(self.bloodBox.text())
        hrate = str(self.heartBox.text())
        clevel = str(self.cholesterolBox.text())

        # You need to implement this logic based on your application
        user_id = self.logged_in_user_id

        if user_id is not None:  # Check if user_id is not None
            # Get the username from the QLineEdit widget
            username_input = self.findChild(QLineEdit, "usernameBox")
            username = username_input.text() if username_input else None

            if not username:  # Check if username is empty
                QMessageBox.warning(self, "Warning", "Username is required.")
                return

            query = "INSERT INTO user_profiles_info (user_id, name, age, contact, sex, username, height, weight, bmi, blood_pressure, heart_rate, cholesterol_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            row = (user_id, name, age, contact, sex, username, height, weight, bmi, bp, hrate,clevel)

            cursor.execute(query, row)
            self.db_connection.commit()

            # clear the input boxes
            self.nameBox.clear()
            self.usernameBox.clear()
            self.ageBox.clear()
            self.contactBox.clear()
            self.sexBox.clear()
            self.heightBox.clear()
            self.weightBox.clear()

            self.bmiBox.clear()
            self.bloodBox.clear()
            self.heartBox.clear()
            self.cholesterolBox.clear()
            self.stacked_widget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Warning", "User not logged in. Cannot save task without a valid user.")

    def load_profile_data(self):
        if self.logged_in_user_id is None:
            QMessageBox.warning(self, "Warning", "User not logged in. Cannot load profile data without a valid user.")
            return

        cursor = self.db_connection.cursor()

        # Query to fetch user data based on logged-in user ID
        query = "SELECT age, contact, sex, height,   weight, bmi, blood_pressure, heart_rate, cholesterol_level FROM user_profiles_info WHERE user_id = %s"
        cursor.execute(query, (self.logged_in_user_id,))
        result = cursor.fetchone()

        if result:
            age, contact, sex, height, weight, bmi, bp, hr, cl = result

            # Set QLabel text with the fetched data
            # self.label.setText(f"Name: {name}")
            self.ageLabel.setText(f"{int(age)}")
            self.contactLabel.setText(f"{contact}")
            self.sexLabel.setText(f"{sex}")
            self.heightLabel.setText(f"{int(height)} cm")
            self.weightLabel.setText(f"{int(weight)} kg")
            self.bmiLabel.setText(f"{int(bmi)}")
            self.bpLabel.setText(f"{bp}")
            self.heartLabel.setText(f"{hr}")
            self.cholesterolLabel.setText(f"{cl}")
        else:
            QMessageBox.information(self, "Info", "No profile data found for the logged-in user.")

        cursor.close()
        

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
            cursor.execute("UPDATE user_profiles_info SET profile_image = %s WHERE username = %s", (self.image_file_path, username))  # Use the instance variable
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
            cursor.execute("SELECT profile_image FROM user_profiles_info WHERE username = %s", (username,))
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
    