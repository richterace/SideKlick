import os
import mysql.connector
from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox, QListWidgetItem, QMainWindow, QPushButton, QTextEdit, QLabel, QRadioButton, QComboBox, QWidget, QStackedWidget, QVBoxLayout, QLineEdit, QCheckBox
from PyQt5.QtCore import QFile, Qt, QSize, QDateTime, QDate
from PyQt5 import uic

from Calendar.calendar_assets import resource_rc

ui_file_path = os.path.join(os.path.dirname(__file__), "WithRadio.ui")

class Calendar(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the ui file
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self) 
        ui_file.close()

        # Connect to the database
        self.db = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="123456",
                database="health"
)
        # Check if the connection is successful
        if self.db.is_connected():
            print("Connected to MySQL database")
        # Find the stacked widget in the UI
        self.stacked_widget = self.findChild(QStackedWidget, "stackedWidget")

         # Find the label widget in the UI
        self.label = self.findChild(QLabel, "TodayPage1")
        # self.label_page3 = self.findChild(QLabel, "DatePage3")

        # Find the DescriptionText and Save button widgets in the UI
        self.title_text = self.findChild(QTextEdit, "TitleText")
  
        self.description = self.findChild(QTextEdit, "DescriptionText")
        self.save_button = self.findChild(QPushButton, "Save")

        # Find the radio button widget in the UI
        self.radio_button_page3 = self.findChild(QRadioButton, "radioButton")
        # Find the QComboBox widgets in the UI
        self.month_box = self.findChild(QComboBox, "MonthBox")
        self.day_box = self.findChild(QComboBox, "DayBox")
        self.year_box = self.findChild(QComboBox, "YearBox")

        # Initialize month, day, and year values in the QComboBoxes
        self.initialize_date_comboboxes()

        # Connect the buttons to their respective functions
        self.Save.clicked.connect(self.save_tasks)
        self.doneTask.clicked.connect(self.doneTasks)
        self.pushButton.clicked.connect(self.go_to_add_widget)
        self.BackButtonPage2.clicked.connect(self.go_to_home_widget)
        self.BackButtonPage3.clicked.connect(self.go_to_home_widget)
        # self.taskListWidget.itemClicked.connect(self.handleTaskItemClick)
        # Grab the calendar's date when clicked
        self.CalendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.logged_in_user_id = None  # Initialize to None
        
        # Set default widget to the first one
        self.stacked_widget.setCurrentIndex(0)


    def initialize_date_comboboxes(self):
        # Initialize month, day, and year values in the QComboBoxes
        self.MonthBox.addItems(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.DayBox.addItems([str(i) for i in range(1, 32)])  # Days 1 to 31
        self.YearBox.addItems([str(i) for i in range(2022, 2030)])  # Years 2022 to 2029
    
    def calendarDateChanged(self):
        dateSelected = self.CalendarWidget.selectedDate()
        full_date = dateSelected.toString("MMMM dd, yyyy")
        day_of_week = dateSelected.toString("dddd")
        formatted_text = f"<span style='font-family: sans-serif; font-size: 14px;'>{full_date}<br>{day_of_week}</span>"
        self.label.setTextFormat(Qt.RichText)
        self.label.setText(formatted_text)
        print("The calendar date was changed.")
        dateSelected = self.CalendarWidget.selectedDate().toPyDate()
        print("Date selencted: ", dateSelected)
        self.updateTaskList(dateSelected)
    
    def updateTaskList(self, date):
        # Create a cursor object
        self.taskListWidget.clear()
        cursor = self.db.cursor()

        # Execute your SQL query here
        query = "SELECT task, completed FROM taskdb WHERE DATE(date) = %s"  # Ensure date format matches database
        cursor.execute(query, (date,))  # Pass date as a tuple

        # Fetch the results
        results = cursor.fetchall()

        # Process the results
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            if result[1] == "Yes":
                item.setCheckState(Qt.Checked)
            elif result[1] == "No":
                item.setCheckState(Qt.Unchecked)
            self.taskListWidget.addItem(item)

        # Close the cursor
        cursor.close()

        
    def get_logged_in_user_id(self):
        # Implement logic to retrieve the user_id of the currently logged-in user
        # This could involve querying the database or accessing user session data
        # For demonstration purposes, let's assume you have a method to retrieve it
        # For example, if you have a variable storing the logged-in user's ID:
        return self.logged_in_user_id
    
    def doneTasks(self):
        # Prompt the user for confirmation
        confirmation = QMessageBox.question(self, "Confirm", "Are you sure you want to mark this task as completed?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            cursor = self.db.cursor()
            date = self.CalendarWidget.selectedDate().toPyDate()

            # Iterate over the task items in reverse order
            for i in range(self.taskListWidget.count() - 1, -1, -1):
                item = self.taskListWidget.item(i)
                task = item.text()
                if item.checkState() == Qt.Checked:
                    # Delete the task from the database
                    query_delete = "DELETE FROM taskdb WHERE task = %s AND DATE(date) = %s"
                    cursor.execute(query_delete, (task, date,))

                    # Remove the task from the UI
                    self.taskListWidget.takeItem(i)

            self.db.commit()

            # Create a styled message box
            messageBox = QMessageBox()
            messageBox.setStyleSheet("QMessageBox {background-color: #f7f7f7; color: #333;} \
                                    QMessageBox QPushButton {background-color: #007BFF; color: #fff; border-radius: 5px; min-width: 80px;} \
                                    QMessageBox QPushButton:hover {background-color: #0056b3;}")
            messageBox.setIcon(QMessageBox.Information)
            messageBox.setText("Changes saved.")
            
            # Increase the size of the buttons
            ok_button = messageBox.addButton("OK", QMessageBox.AcceptRole)
            ok_button.setMaximumWidth(100)  # Set the maximum width of the button
            
            messageBox.exec()



    def save_tasks(self):
        cursor = self.db.cursor()

        newTask = str(self.title_text.toPlainText())
        # Retrieve selected values from QComboBoxes
        selected_month = self.MonthBox.currentText()
        selected_day = int(self.DayBox.currentText())
        selected_year = int(self.YearBox.currentText())
        # Construct QDate object from selected values
        selected_date = QDate(int(selected_year), self.MonthBox.findText(selected_month) + 1, selected_day)

        # Retrieve the user ID of the currently logged-in user
        # You need to implement this logic based on your application
        user_id = self.get_logged_in_user_id()

        if user_id is not None:  # Check if user_id is not None
            query = "INSERT INTO taskdb (user_id, task, completed, date) VALUES (%s, %s, %s, %s)"
            row = (user_id, newTask, "NO", selected_date.toString(Qt.ISODate))

            cursor.execute(query, row)
            self.db.commit()
            # self.updateTaskList(selected_date.toPyDate())  # Pass the Python date instead of the QDate
            self.title_text.clear()
            self.stacked_widget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Warning", "User not logged in. Cannot save task without a valid user.")



    def go_to_home_widget(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_add_widget(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_edit_widget(self):
        self.stacked_widget.setCurrentIndex(2)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = Calendar()
    main_window.show()

    # Center the main window
    desktop = QApplication.desktop()
    rect = desktop.availableGeometry(desktop.primaryScreen())
    center = rect.center()
    main_window.move(center - main_window.rect().center())

    sys.exit(app.exec_())