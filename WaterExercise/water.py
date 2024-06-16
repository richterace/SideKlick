from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget, QGridLayout, QScrollArea, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont,  QMovie
from PyQt5.QtCore import QTimer, QUrl, QFile
from PyQt5 import uic
import sys
from WaterExercise import waterimg
from WaterExercise import water_rc
from WaterExercise import images
import os

ui_file_path = os.path.join(os.path.dirname(__file__), "water.ui")

class UIwater(QMainWindow):
    
    def __init__(self):
        super(UIwater, self).__init__()
        
        # Load the UI file
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self)  # Load the UI file directly into the QMainWindow
        ui_file.close()
        
        # Buttons Widgets
        self.waterbutton = self.findChild(QPushButton, "waterButton")
        self.female = self.findChild(QPushButton, "female")
        self.male = self.findChild(QPushButton, "male")
        self.nexttoweight = self.findChild(QPushButton, "nexttoweight")
        self.nexttoweather = self.findChild(QPushButton, "nexttoweather")
        self.nexttoreco = self.findChild(QPushButton, "nexttoreco")
        self.nexttodrink = self.findChild(QPushButton, "nextodrink")
        self.hot = self.findChild(QPushButton, "hot")
        self.temperate = self.findChild(QPushButton, "temperate")
        self.cold = self.findChild(QPushButton, "cold")
        
        self.backtomain = self.findChild(QPushButton, "backtomain")
        self.backtosex = self.findChild(QPushButton, "backtosex")
        self.backtoweight = self.findChild(QPushButton, "backtoweight")
        self.backtoweather = self.findChild(QPushButton, "backtoweather")
        self.backtomain2 = self.findChild(QPushButton, "backtomain2")
        
        # Label Widgets
        self.bgimg = self.findChild(QLabel, "bg")
        self.bgimg2 = self.findChild(QLabel, "bg2")
        self.label = self.findChild(QLabel, "label")
        self.label_2 = self.findChild(QLabel, "label_2")
        self.recommend = self.findChild(QLabel, "recommend")
        self.percent = self.findChild(QLabel, "percent")
        self.ml = self.findChild(QLineEdit, "ml")
        self.mlreco = self.findChild(QLineEdit, "mlreco")
        self.kg = self.findChild(QLineEdit, "kg")
        
        # Stacked Widgets
        self.waterstackedWidget = self.findChild(QStackedWidget, "waterstackedWidget")
        self.drinkwidget = self.findChild(QWidget, "drink")
        self.savewidget = self.findChild(QWidget, "save")
        self.sexwidget = self.findChild(QWidget, "sex")
        self.weightwidget = self.findChild(QWidget, "weight")
        self.weatherwidget = self.findChild(QWidget, "weather")
        self.recowidget = self.findChild(QWidget, "reco")
        self.drinkwaterwidget = self.findChild(QWidget, "drinkwaterwidget")
        self.recowidget = self.findChild(QWidget, "recowidget")

        # Set up the GIF
        gif_path = os.path.join(os.path.dirname(__file__), "waterimg/water1.gif")
        self.movie = QMovie(gif_path)
        
        # Verify QMovie is loaded
        if not self.movie.isValid():
            print("Failed to load GIF")
            return
        
        self.label.setMovie(self.movie)
        self.label.setMovie(self.movie)
        
        # Timer to move the GIF upwards
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_gif_up)
        
        # Timer to stop moving after 1.5 seconds
        self.stop_timer = QTimer()
        self.stop_timer.setSingleShot(True)
        self.stop_timer.timeout.connect(self.stop_moving)
        
        

        # Ensure GIF starts at the bottom with only the top part showing
        self.movie.start()
        self.show()

        # Path to the MP3 file
        mp3_path = os.path.join(os.path.dirname(__file__), "waterimg/drink.mp3")

        # Media player for playing the sound
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_path)))
        
        # Initialize total ml value
        self.total_ml = 0
        
        self.waterbutton.setStyleSheet("background-color: transparent; border: none; ")
        
        # Stacked Widgets
        self.waterbutton.clicked.connect(self.on_water_button_click)
        
        self.male.clicked.connect(self.male_button)
        self.female.clicked.connect(self.female_button)
        self.nexttoweight.clicked.connect(self.nexttoweight_button)
        self.nexttoweather.clicked.connect(self.nexttoweather_button)
        self.nexttoreco.clicked.connect(self.nexttoreco_button)
        self.nexttodrink.clicked.connect(self.nexttodrink_button)
        
        self.hot.clicked.connect(self.hot_button)
        self.temperate.clicked.connect(self.temperate_button)
        self.cold.clicked.connect(self.cold_button)
        
        # Disable nexttoweight button initially
        self.nexttoweight.setEnabled(False)
        self.ml.returnPressed.connect(self.on_ml_return_pressed)
        
        self.backtosex.clicked.connect(self.backtosex_button)
        self.backtoweight.clicked.connect(self.backtoweight_button)
        self.backtoweather.clicked.connect(self.backtoweather_button)
        
    def backtosex_button(self):
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "sex"))
        
    def backtoweight_button(self):
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "weight"))
        
    def backtoweather_button(self):
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "weather"))
        
        
    def on_ml_return_pressed(self):
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "save"))
    
    def hot_button(self):
        self.hot.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px;  text-align:left;")
        self.temperate.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px; text-align: left;color: rgb(0, 110, 156);")
        self.cold.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px; text-align: left;color: rgb(0, 110, 156);")
    
    def temperate_button(self):
        self.temperate.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px;text-align: left;")
        self.cold.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px;text-align: left;color: rgb(0, 110, 156);")
        self.hot.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px; text-align: left;color: rgb(0, 110, 156);")
    
    def cold_button(self):
        self.cold.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px;text-align: left;")
        self.temperate.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px; text-align: left;color: rgb(0, 110, 156);")
        self.hot.setStyleSheet("background-color:  rgb(235, 235, 235);   border-radius: 20px; text-align: left;color: rgb(0, 110, 156);")
    
        
    def male_button(self):
        self.male.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 50%;")
        self.female.setStyleSheet("background-color: transparent; color: black;  border-radius: 50%;")
        self.nexttoweight.setEnabled(True)

    def female_button(self):
        self.female.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 50%; padding: 10px;")
        self.male.setStyleSheet("background-color: transparent; color: black;  border-radius: 50%; padding: 10px;")
        self.nexttoweight.setEnabled(True)
        
    def nexttoweight_button(self):
        self.nexttoweight.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px; padding: 10px;")
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "weight"))
    
    def nexttoweather_button(self):
        self.nexttoweather.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px; padding: 10px;")
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "weather"))
        
        # Disable nexttoweather button if kg is empty
        self.nexttoweather.setEnabled(bool(self.kg.text()))

    
    def nexttoreco_button(self):
        self.nexttoreco.setStyleSheet("background-color: #006E9C; color: white; border-radius: 20px; padding: 10px;")
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "reco"))

        try:
            weight = int(self.kg.text())
            sex = "male" if self.male.isChecked() else "female"
            weather = "hot" if self.hot.isChecked() else ("temperate" if self.temperate.isChecked() else "cold")

            # Dictionary containing the recommended ml intake based on sex, weight ranges, and weather conditions
            recommended_ml = {
                "male": {
                    "hot": {60: 2100, 70: 2450, 80: 2800, 90: 3150, 100: 3500},
                    "temperate": {60: 1800, 70: 2100, 80: 2400, 90: 2700, 100: 3000},
                    "cold": {60: 1500, 70: 1750, 80: 2000, 90: 2250, 100: 2500}
                },
                "female": {
                    "hot": {45: 1575, 55: 1925, 65: 2275, 75: 2625, 85: 2975},
                    "temperate": {45: 1350, 55: 1650, 65: 1950, 75: 2250, 85: 2550},
                    "cold": {45: 1125, 55: 1375, 65: 1625, 75: 1875, 85: 2125}
                }
            }

            # Get the recommended ml intake based on the user's input weight
            if weight in recommended_ml[sex][weather]:
                recommended_ml_value = recommended_ml[sex][weather][weight]
            else:
                # Find the closest weight values in the dictionary
                closest_lower_weight = max([w for w in recommended_ml[sex][weather] if w < weight])
                closest_upper_weight = min([w for w in recommended_ml[sex][weather] if w > weight])

                # Interpolate the recommended ml intake based on the closest weight values
                recommended_ml_value = (
                    recommended_ml[sex][weather][closest_lower_weight]
                    + (recommended_ml[sex][weather][closest_upper_weight] - recommended_ml[sex][weather][closest_lower_weight])
                    * (weight - closest_lower_weight)
                    / (closest_upper_weight - closest_lower_weight)
                )

            # Update mlreco QLineEdit with the calculated recommendation as a whole number
            self.mlreco.setText(str(int(recommended_ml_value)))


        except Exception as e:
            print(f"An error occurred: {e}")



    
    def nexttodrink_button(self):
        self.nexttoweather.setStyleSheet("background-color: #006E9C; color: white;  border-radius: 20px; padding: 10px;background-color: transparent; border: none; ")
        self.waterstackedWidget.setCurrentWidget(self.waterstackedWidget.findChild(QWidget, "drink"))
        try:
            
            # Update mlreco QLineEdit with recommended_ml value
            self.recommend.setText(self.mlreco.text())

        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")




    def on_water_button_click(self):
        self.waterbutton.setStyleSheet("background-color: transparent; border: none; ")
        try:

            # Attempt to play the MP3 file
            self.media_player.play()
   
          

            
            # Get the ml value as an integer
            ml_value = int(self.ml.text())
            
            # Get the recommended goal as an integer
            recommended_goal = int(self.recommend.text())
            
            # Add ml value
            self.total_ml += ml_value
            
            # Calculate the current percentage
            current_percentage = (self.total_ml / recommended_goal) * 100
            
            # Limit percentage to 100%
            if current_percentage > 100:
                current_percentage = 100
                self.stop_moving()  # Stop moving the GIF if 100% is reached
            
            # Update the percent label
            self.percent.setText(f"{current_percentage:.1f}%")
            
            # Start moving the GIF only if under 100%
            if current_percentage < 100:
                self.start_moving()

            if current_percentage == 100:
                 self.show_completion_prompt()
            
        except Exception as e:
            # Print the exception
            print(f"An error occurred while playing the MP3 file: {e}")
            print(f"An error occurred: {e}")


    # for congratulations
    def show_completion_prompt(self):
        # Create a message box to display the message
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Congratulations!")
        msg_box.setText("Good job, you finished your goal water intake!")
        msg_box.setStandardButtons(QMessageBox.Ok)
        
        # Show the message box and wait for user interaction
        result = msg_box.exec_()
        
        if result == QMessageBox.Ok:
            # Set up a delay before calling backtosex_button
            QTimer.singleShot(2000, self.backtosex_button)  # 2000 milliseconds = 2 seconds delay

    def start_moving(self):
        # Start the animation and timer
        self.movie.start()
        self.move_timer.start(50)  # Update interval in milliseconds
        self.stop_timer.start(1500)  # Stop after 1.5 seconds

    def stop_moving(self):
        # Stop the animation and timer
        self.move_timer.stop()

    def move_gif_up(self):
        try:
            # Calculate the height of the widget
            widget_height = self.drinkwaterwidget.height()
            
            # Calculate the stop position based on the percentage and the widget's height
            stop_position = int((float(self.percent.text().replace("%", "")) / 100) * widget_height)
            # Limit the stop position to the widget's height
            stop_position = min(stop_position, widget_height)
            
            # Ensure the stop position does not exceed 567 pixels
            stop_position = min(stop_position, 567)
            
            # Calculate the new y-coordinate after moving
            new_y = self.drinkwaterwidget.pos().y() + widget_height - stop_position
            
            # Move the label upwards to the stop position
            self.label.move(self.label.pos().x(), new_y)
        except Exception as e:
            print(f"An error occurred while moving the GIF: {e}")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    

    
    window = UIwater()
    window.show()
    sys.exit(app.exec_())
