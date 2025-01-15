import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QMessageBox

# Importing your other modules (make sure these are correctly set up)
from Dashboard.dashboard import DashboardMain
from Calendar.WithRadio import Calendar
from Recipee.main import RecipeMain
from Grocery.grocery import UI
from LogIn.login import login
from WaterExercise.exercise import UIexercise
from WaterExercise.water import UIwater
from foodCalorie.calorie import Calorie
from foodGuide.foodHanling import FoodHand
from Skintip.skincare import Skin
from calorieIn.calorieIntake import Ui
from allergin.allergin import Ui

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SlideKick')
        self.setFixedSize(392, 852)  # Set fixed window size to 392 x 852

        # Create a stacked widget to manage pages
        self.stacked_widget = QStackedWidget()

        # Create pages (windows)
        self.login_window = login()
        self.dashboard_window = DashboardMain()
        self.calendar_window = Calendar()
        self.recipe_window = RecipeMain()
        self.grocery_window = UI()
        self.water_window = UIwater()
        self.exercise_window = UIexercise()
        self.foodcalorie_window = Calorie()
        self.foodcHandling_window = FoodHand()
        self.skintip_window = Skin()
        self.calorieIn_window = Ui()
        self.allergin_window = Ui()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.dashboard_window)
        self.stacked_widget.addWidget(self.calendar_window)
        self.stacked_widget.addWidget(self.recipe_window)
        self.stacked_widget.addWidget(self.grocery_window)
        self.stacked_widget.addWidget(self.water_window)
        self.stacked_widget.addWidget(self.exercise_window)
        self.stacked_widget.addWidget(self.foodcalorie_window)
        self.stacked_widget.addWidget(self.foodcHandling_window)
        self.stacked_widget.addWidget(self.skintip_window)
        self.stacked_widget.addWidget(self.calorieIn_window)
        self.stacked_widget.addWidget(self.allergin_window)

        # Use buttons within stacked widgets to switch between pages
        self.dashboard_window.pushButton.clicked.connect(self.show_calendar_page)
        self.dashboard_window.pushButton_6.clicked.connect(self.show_recipe_page)
        self.dashboard_window.pushButton_7.clicked.connect(self.show_grocery_page)
        self.dashboard_window.pushButton_2.clicked.connect(self.show_foodCalorie)
        self.dashboard_window.skincare.clicked.connect(self.show_skintip)
        self.dashboard_window.pushButton_9.clicked.connect(self.show_foodGuide)
        self.dashboard_window.pushButton_8.clicked.connect(self.show_allergin)
        # self.dashboard_window.calorieButton.clicked.connect(self.show_calorieIn)
        
        
        
        self.login_window.signFinish.clicked.connect(self.signup_and_goto_login)
        self.dashboard_window.logOut.clicked.connect(self.go_to_login)
        self.dashboard_window.calendarButton.clicked.connect(self.show_calendar_page)
        self.dashboard_window.recipeButton.clicked.connect(self.show_recipe_page)
        self.dashboard_window.waterButton.clicked.connect(self.show_water)
        self.dashboard_window.waterButton2.clicked.connect(self.show_water)
        self.dashboard_window.exerciseButton.clicked.connect(self.show_exercise)
        

        # Validate login when the login button is clicked
        self.login_window.pushButton.clicked.connect(self.validate_login)

        # Connect other buttons to switch between pages
        self.exercise_window.backDashboard.clicked.connect(self.show_dashboard_page)
        self.water_window.backtomain.clicked.connect(self.show_dashboard_page)
        self.water_window.backtomain2.clicked.connect(self.show_dashboard_page)
        self.calendar_window.BackButton.clicked.connect(self.show_dashboard_page)
        self.recipe_window.homeButton.clicked.connect(self.show_dashboard_page)
        self.grocery_window.grocerybackbutton_2.clicked.connect(self.show_dashboard_page)
        self.foodcHandling_window.backButton.clicked.connect(self.show_dashboard_page)
        self.foodcalorie_window.backButton2.clicked.connect(self.show_dashboard_page)
        self.skintip_window.backButton.clicked.connect(self.show_dashboard_page)
        self.calorieIn_window.backButton.clicked.connect(self.show_dashboard_page)
        self.allergin_window.backButton.clicked.connect(self.show_dashboard_page)
        

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

        # Set up main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.layout.addWidget(self.stacked_widget)
    
    def show_allergin(self):
        self.stacked_widget.setCurrentWidget(self.allergin_window)
           
    def show_calorieIn(self):
        self.stacked_widget.setCurrentWidget(self.calorieIn_window)
        
    def show_skintip(self):
        self.stacked_widget.setCurrentWidget(self.skintip_window)
           
    def show_foodGuide(self):
        self.stacked_widget.setCurrentWidget(self.foodcHandling_window)

    def show_calendar_page(self):
        self.stacked_widget.setCurrentWidget(self.calendar_window)

    def show_dashboard_page(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_window)

    def show_recipe_page(self):
        self.stacked_widget.setCurrentWidget(self.recipe_window)

    def show_grocery_page(self):
        self.stacked_widget.setCurrentWidget(self.grocery_window)
    
    def show_water(self):
        self.stacked_widget.setCurrentWidget(self.water_window)
    
    def show_exercise(self):
        self.stacked_widget.setCurrentWidget(self.exercise_window)
        
    def show_foodCalorie(self):
        self.stacked_widget.setCurrentWidget(self.foodcalorie_window)

    def signup_and_goto_login(self):
        username = self.login_window.userSignup.text()
        password = self.login_window.passwordSignup.text()
        confirm_password = self.login_window.passwordConfirm.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        # Insert user into the database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        user_data = (username, password)

        try:
            self.db_cursor.execute(query, user_data)
            self.db_connection.commit()
            QMessageBox.information(self, "Success", "User registered successfully!")
            self.go_to_login()  # Go to login widget after successful signup
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to register user: {err}")

    def validate_login(self):
        username = self.login_window.userLogin.text()
        password = self.login_window.passwordLogin.text()

        # Check if username and password exist in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        user_data = (username, password)

        self.db_cursor.execute(query, user_data)
        result = self.db_cursor.fetchone()

        if result:
           
            # Set the logged-in user ID in the RecipeMain instance
            logged_in_user_id = result[0]  # Assuming user_id is the first column in the result
            self.recipe_window.logged_in_user_id = logged_in_user_id
            self.calendar_window.logged_in_user_id = logged_in_user_id
            self.dashboard_window.logged_in_user_id = logged_in_user_id
            self.dashboard_window.update_profile_name()
            self.show_dashboard_page()
            # Proceed to dashboard or wherever needed
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")

    def go_to_login(self):
        self.login_window.go_to_login()
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()

    # Center the main window
    desktop = QApplication.desktop()
    rect = desktop.availableGeometry(desktop.primaryScreen())
    center = rect.center()
    main_page.move(center - main_page.rect().center())
    sys.exit(app.exec_())
