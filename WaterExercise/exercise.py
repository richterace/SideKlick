from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget
from PyQt5.QtCore import QTimer, QUrl, QFile
from PyQt5.QtGui import QFont,  QMovie, QPixmap
from PyQt5 import uic
import sys
import os  
from WaterExercise import exerciseimg

ui_file_path = os.path.join(os.path.dirname(__file__), "exercise.ui")

class UIexercise(QMainWindow):
    
    def __init__(self):
        super(UIexercise, self).__init__()
        
        # Load the UI file
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self)  # Load the UI file directly into the QMainWindow
        ui_file.close()
        
        # Buttons Widgets
        self.waterbutton = self.findChild(QPushButton, "waterButton")
        self.a1 = self.findChild(QPushButton, "a1")
        self.a2 = self.findChild(QPushButton, "a2")
        self.a3 = self.findChild(QPushButton, "a3")
        self.a4 = self.findChild(QPushButton, "a4")
        self.a5 = self.findChild(QPushButton, "a5")
        self.start = self.findChild(QPushButton, "start")
        self.start_2 = self.findChild(QPushButton, "start_2")
        self.start_3 = self.findChild(QPushButton, "start_3")
        self.start_4 = self.findChild(QPushButton, "start_4")
        self.start_5 = self.findChild(QPushButton, "start_5")
        
        self.back2main = self.findChild(QPushButton, "back2main")
        self.back2main_2 = self.findChild(QPushButton, "back2main_2")
        self.back2main_3 = self.findChild(QPushButton, "back2main_3")
        self.back2main_4 = self.findChild(QPushButton, "back2main_4")
        self.back2main_5 = self.findChild(QPushButton, "back2main_5")
        
        self.cardioduration = self.findChild(QPushButton, "cardioduration")
        self.cardiorepitition = self.findChild(QPushButton, "cardiorepitition")
        self.cardioresttime = self.findChild(QPushButton, "cardioresttime")
        
        self.classicduration = self.findChild(QPushButton, "classicduration")
        self.classicrepitition = self.findChild(QPushButton, "classicrepitition")
        self.classicresttime = self.findChild(QPushButton, "classicresttime")
        
        self.strengthduration = self.findChild(QPushButton, "strengthduration")
        self.strengthrepitition = self.findChild(QPushButton, "strengthrepitition")
        self.strengthresttime = self.findChild(QPushButton, "strengthresttime")
        
        self.flexibleduration = self.findChild(QPushButton, "flexibleduration")
        self.flexiblerepitition = self.findChild(QPushButton, "flexiblerepitition")
        self.flexibleresttime = self.findChild(QPushButton, "flexibleresttime")
        
        self.intensityduration = self.findChild(QPushButton, "intensityduration")
        self.intensityrepitition = self.findChild(QPushButton, "intensityrepitition")
        self.intensityresttime = self.findChild(QPushButton, "intensityresttime")
        
        self.durationback = self.findChild(QPushButton, "durationback")
        self.durationback_2 = self.findChild(QPushButton, "durationback_2")
        self.durationback_3 = self.findChild(QPushButton, "durationback_3")
        self.durationback_4 = self.findChild(QPushButton, "durationback_4")
        self.durationback_5 = self.findChild(QPushButton, "durationback_5")
        self.backButton = self.findChild(QPushButton, "backButton")
        
        self.time1 = self.findChild(QPushButton, "time1")
        self.time2 = self.findChild(QPushButton, "time2")
        self.time3 = self.findChild(QPushButton, "time3")
        self.time4 = self.findChild(QPushButton, "time4")
        self.time5 = self.findChild(QPushButton, "time5")
        self.savetime = self.findChild(QPushButton, "savetime")
        
        self.repeat1 = self.findChild(QPushButton, "repeat1")
        self.repeat2 = self.findChild(QPushButton, "repeat2")
        self.repeat3 = self.findChild(QPushButton, "repeat3")
        self.repeat4 = self.findChild(QPushButton, "repeat4")
        self.repeat5 = self.findChild(QPushButton, "repeat5")
        self.saverepetition = self.findChild(QPushButton, "saverepetition")
        
        self.rest1 = self.findChild(QPushButton, "rest1")
        self.rest2 = self.findChild(QPushButton, "rest2")
        self.rest3 = self.findChild(QPushButton, "rest3")
        self.rest4 = self.findChild(QPushButton, "rest4")
        self.rest5 = self.findChild(QPushButton, "rest5")
        self.saverest = self.findChild(QPushButton, "saverest")
        
        self.labelduration1 = self.findChild(QLabel, "labelduration1")
        self.labelduration1_2 = self.findChild(QLabel, "labelduration1_2")
        self.labelduration1_3 = self.findChild(QLabel, "labelduration1_3")
        self.labelduration1_4 = self.findChild(QLabel, "labelduration1_4")
        self.labelduration1_5 = self.findChild(QLabel, "labelduration1_5")
        
        self.classiclabelduration1 = self.findChild(QLabel, "classiclabelduration1")
        self.classiclabelduration1_2 = self.findChild(QLabel, "classiclabelduration1_2")
        self.classiclabelduration1_3 = self.findChild(QLabel, "classiclabelduration1_3")
        self.classiclabelduration1_4 = self.findChild(QLabel, "classiclabelduration1_4")
        self.classiclabelduration1_5 = self.findChild(QLabel, "classiclabelduration1_5")
        
        self.strengthlabelduration1 = self.findChild(QLabel, "strengthlabelduration1")
        self.strengthlabelduration1_2 = self.findChild(QLabel, "strengthlabelduration1_2")
        self.strengthlabelduration1_3 = self.findChild(QLabel, "strengthlabelduration1_3")
        self.strengthlabelduration1_4 = self.findChild(QLabel, "strengthlabelduration1_4")
        self.strengthlabelduration1_5 = self.findChild(QLabel, "strengthlabelduration1_5")
        
        self.flexiblelabelduration1 = self.findChild(QLabel, "flexiblelabelduration1")
        self.flexiblelabelduration1_2 = self.findChild(QLabel, "flexiblelabelduration1_2")
        self.flexiblelabelduration1_3 = self.findChild(QLabel, "flexiblelabelduration1_3")
        self.flexiblelabelduration1_4 = self.findChild(QLabel, "flexiblelabelduration1_4")
        self.flexiblelabelduration1_5 = self.findChild(QLabel, "flexiblelabelduration1_5")
        
        self.intensitylabelduration1 = self.findChild(QLabel, "intensitylabelduration1")
        self.intensitylabelduration1_2 = self.findChild(QLabel, "intensitylabelduration1_2")
        self.intensitylabelduration1_3 = self.findChild(QLabel, "intensitylabelduration1_3")
        self.intensitylabelduration1_4 = self.findChild(QLabel, "intensitylabelduration1_4")
        self.intensitylabelduration1_5 = self.findChild(QLabel, "intensitylabelduration1_5")
        
        self.labelrest = self.findChild(QLabel, "labelrest")
        self.labelrest_2 = self.findChild(QLabel, "labelrest_2")
        self.labelrest_3 = self.findChild(QLabel, "labelrest_3")
        self.labelrest_4 = self.findChild(QLabel, "labelrest_4")
        
        self.strengthlabelrest = self.findChild(QLabel, "strengthlabelrest")
        self.strengthlabelrest_2 = self.findChild(QLabel, "strengthlabelrest_2")
        self.strengthlabelrest_3 = self.findChild(QLabel, "strengthlabelrest_3")
        self.strengthlabelrest_4 = self.findChild(QLabel, "strengthlabelrest_4")
        
        self.classiclabelrest = self.findChild(QLabel, "classiclabelrest")
        self.classiclabelrest_2 = self.findChild(QLabel, "classiclabelrest_2")
        self.classiclabelrest_3 = self.findChild(QLabel, "classiclabelrest_3")
        self.classiclabelrest_4 = self.findChild(QLabel, "classiclabelrest_4")
        
        self.flexiblelabelrest = self.findChild(QLabel, "flexiblelabelrest")
        self.flexiblelabelrest_2 = self.findChild(QLabel, "flexiblelabelrest_2")
        self.flexiblelabelrest_3 = self.findChild(QLabel, "flexiblelabelrest_3")
        self.flexiblelabelrest_4 = self.findChild(QLabel, "flexiblelabelrest_4")
        
        self.intensitylabelrest = self.findChild(QLabel, "intensitylabelrest")
        self.intensitylabelrest_2 = self.findChild(QLabel, "intensitylabelrest_2")
        self.intensitylabelrest_3 = self.findChild(QLabel, "intensitylabelrest_3")
        self.intensitylabelrest_4 = self.findChild(QLabel, "intensitylabelrest_4")
        
        # Label Widgets
        self.c3 = self.findChild(QLabel, "c3_2")
        self.headerbg = self.findChild(QLabel, "headerbg")
        self.headerbg_2 = self.findChild(QLabel, "headerbg_2")
        self.headerbg_3 = self.findChild(QLabel, "headerbg_3")
        self.countnum = self.findChild(QLabel, "countnum")
        self.restcount = self.findChild(QLabel, "restcount")
        
        self.cardioshow = self.findChild(QLabel, "cardioshow")
        self.cardiopreview = self.findChild(QLabel, "cardiopreview")
        self.cardiopreview3 = self.findChild(QLabel, "cardiopreview_3")
        self.cardiopreview2 = self.findChild(QLabel, "cardiopreview_2")
        
        
        self.repeatbg = self.findChild(QLabel, "repeatbg")
        self.durationbg = self.findChild(QLabel, "durationbg")
        self.resettimebg = self.findChild(QLabel, "resettimebg")
 
        # Stacked Widgets
        self.exercisestackedWidget = self.findChild(QStackedWidget, "exercisestackedWidget")
        self.exercisemain = self.findChild(QWidget, "exercisemain")
        self.cardio = self.findChild(QWidget, "cardio")
        self.cardioexercise = self.findChild(QWidget, "cardioexercise")
        self.classic = self.findChild(QWidget, "classic")
        self.flexible = self.findChild(QWidget, "flexible")
        self.strength = self.findChild(QWidget, "strength")
        self.intensity = self.findChild(QWidget, "intensity")
        self.classicexercise = self.findChild(QWidget, "classicexercise")
        self.centralWidget1 = self.findChild(QWidget, "centralWidget")
        
        self.repeat = self.findChild(QWidget, "repeat")
        self.duration = self.findChild(QWidget, "duration")
        self.resettime = self.findChild(QWidget, "resettime")
        self.count = self.findChild(QWidget, "count")
      
        # Media player for playing the sound
        mp3_1 = os.path.join(os.path.dirname(__file__),"exerciseimg/music.mp3")
        mp3_2 = os.path.join(os.path.dirname(__file__),"exerciseimg/music2.mp3")
        mp3_3 = os.path.join(os.path.dirname(__file__),"exerciseimg/music3.mp3")
        mp3_4 = os.path.join(os.path.dirname(__file__),"exerciseimg/music4.mp3")
        mp3_5 = os.path.join(os.path.dirname(__file__),"exerciseimg/music5.mp3")
        
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_1)))

        self.media_player1 = QMediaPlayer()
        self.media_player1.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_1)))
        
        self.media_player2 = QMediaPlayer()
        self.media_player2.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_2)))
        
        self.media_player3 = QMediaPlayer()
        self.media_player3.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_3)))
        
        self.media_player4 = QMediaPlayer()
        self.media_player4.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_4)))
        
        self.media_player5 = QMediaPlayer()
        self.media_player5.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_5)))
        
        # Counter for the animation
        self.counter = 0
        
   
        
        # Define the list of image paths
        self.cardio_images = [
            os.path.join(os.path.dirname(__file__),"exerciseimg/cardio1.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/cardio2.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/cardio3.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/cardio4.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/cardio5.png")
        ]
        
        self.classic_images = [
            os.path.join(os.path.dirname(__file__),"exerciseimg/classic1.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/classic2.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/classic3.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/classic4.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/classic5.png")
        ]
        
        self.strength_images = [
            os.path.join(os.path.dirname(__file__),"exerciseimg/strength1.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/strength2.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/strength3.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/strength4.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/strength5.png")
        ]
        
        self.flexible_images = [
            os.path.join(os.path.dirname(__file__),"exerciseimg/flexible1.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/flexible2.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/flexible3.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/flexible4.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/flexible5.png")
        ]
        
        self.intensity_images = [
            os.path.join(os.path.dirname(__file__),"exerciseimg/intensity1.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/intensity2.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/intensity3.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/intensity4.png"),
            os.path.join(os.path.dirname(__file__),"exerciseimg/intensity5.png")
        ]
        
        
        
        self.current_image_index = 0  # Initialize the current image index
        
        self.is_resting = False  # Flag to track rest mode
        self.rest_counter = 0     # Counter for rest countdown
        self.general_countdown = 30  # General countdown value (modifiable by the user)
        self.rest_duration = 10   # Rest duration (fixed at 10 seconds)
        # Connect start button click to show_labels
        self.start.clicked.connect(self.show_labels)
        self.start_2.clicked.connect(self.show_labels)
        self.start_3.clicked.connect(self.show_labels)
        self.start_4.clicked.connect(self.show_labels)
        self.start_5.clicked.connect(self.show_labels)
        
        # Connect a1 button click to switch to cardio widget
        self.a1.clicked.connect(self.switch_to_cardio)
        self.a2.clicked.connect(self.switch_to_classic)
        self.a3.clicked.connect(self.switch_to_strength)
        self.a4.clicked.connect(self.switch_to_flexible)
        self.a5.clicked.connect(self.switch_to_intensity)
        
        self.cardioduration.clicked.connect(self.open_duration)
        self.cardiorepitition.clicked.connect(self.open_repitition)
        self.cardioresttime.clicked.connect(self.open_rest)
        
        self.classicduration.clicked.connect(self.open_duration)
        self.classicrepitition.clicked.connect(self.open_repitition)
        self.classicresttime.clicked.connect(self.open_rest)
        
        self.flexibleduration.clicked.connect(self.open_duration)
        self.flexiblerepitition.clicked.connect(self.open_repitition)
        self.flexibleresttime.clicked.connect(self.open_rest)
        
        self.strengthduration.clicked.connect(self.open_duration)
        self.strengthrepitition.clicked.connect(self.open_repitition)
        self.strengthresttime.clicked.connect(self.open_rest)
        
        self.intensityduration.clicked.connect(self.open_duration)
        self.intensityrepitition.clicked.connect(self.open_repitition)
        self.intensityresttime.clicked.connect(self.open_rest)
        
        self.durationback.clicked.connect(self.close_duration)
        self.durationback_2.clicked.connect(self.close_duration)
        self.durationback_3.clicked.connect(self.close_duration)
        
        
        
        # Button click connections
        self.time1.clicked.connect(lambda: self.highlight_button(self.time1))
        self.time2.clicked.connect(lambda: self.highlight_button(self.time2))
        self.time3.clicked.connect(lambda: self.highlight_button(self.time3))
        self.time4.clicked.connect(lambda: self.highlight_button(self.time4))
        self.time5.clicked.connect(lambda: self.highlight_button(self.time5))
        self.savetime.clicked.connect(self.set_countnum_value)
        
        # Button click connections
        self.rest1.clicked.connect(lambda: self.resthighlight_button(self.rest1))
        self.rest2.clicked.connect(lambda: self.resthighlight_button(self.rest2))
        self.rest3.clicked.connect(lambda: self.resthighlight_button(self.rest3))
        self.rest4.clicked.connect(lambda: self.resthighlight_button(self.rest4))
        self.rest5.clicked.connect(lambda: self.resthighlight_button(self.rest5))
        self.saverest.clicked.connect(self.update_rest_count)
        
         # Button click connections
        self.repeat1.clicked.connect(lambda: self.repeathighlight_button(self.repeat1))
        self.repeat2.clicked.connect(lambda: self.repeathighlight_button(self.repeat2))
        self.repeat3.clicked.connect(lambda: self.repeathighlight_button(self.repeat3))
        self.repeat4.clicked.connect(lambda: self.repeathighlight_button(self.repeat4))
        self.repeat5.clicked.connect(lambda: self.repeathighlight_button(self.repeat5))
        self.saverepetition.clicked.connect(self.set_repeat_value)
        
         # Set default highlighted buttons
        self.highlight_button(self.time1)  # Default highlighted button for set_countnum_value
        self.repeathighlight_button(self.repeat1)  # Default highlighted button for set_repeat_value
        self.resthighlight_button(self.rest1) 
        
        self.repeat_count = 1 
        self.backButton.clicked.connect(self.back_button_clicked)
        self.back2main.clicked.connect(self.back_main)
        self.back2main_2.clicked.connect(self.back_main)
        self.back2main_3.clicked.connect(self.back_main)
        self.back2main_4.clicked.connect(self.back_main)
        self.back2main_5.clicked.connect(self.back_main)
        
        self.current_workout_type = None

        
    def back_main(self):      
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisemain"))
        if self.sender() == self.back2main:
            self.media_player.stop()  # Stop the music
        elif self.sender() == self.back2main_2:
            self.media_player2.stop()  # Stop the music
        elif self.sender() == self.back2main_3:
            self.media_player3.stop()  # Stop the music
        elif self.sender() == self.back2main_4:
            self.media_player4.stop()  # Stop the music
        elif self.sender() == self.back2main_5:
            self.media_player5.stop()  # Stop the music

        
    def back_button_clicked(self):
        # Stop all timers
        self.timer.stop()
        self.countdown_timer.stop()      
        # Stop the music
        self.media_player.stop() 
        self.media_player2.stop()  # Stop the music
        self.media_player3.stop()  # Stop the music
        self.media_player4.stop()  # Stop the music
        self.media_player5.stop()  # Stop the music       
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisemain"))
    
    def close_duration(self):
        self.exercisestackedWidget.raise_() 
    
    def open_rest(self):
        self.resettime.raise_()  
    
    def open_repitition(self):
        self.repeat.raise_()   
          
    def open_duration(self):
        self.duration.raise_()   
        
    def switch_to_cardio(self):
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "cardio"))
    def switch_to_classic(self):
        self.exercisestackedWidget.setCurrentWidget(self.classic)
        self.exercisestackedWidget.raise_()
    def switch_to_strength(self):
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "strength"))
        
    def switch_to_flexible(self):
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "flexible"))
        
    def switch_to_intensity(self):
        self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "intensity"))


        
  
    def show_labels(self):
        self.count.raise_()
        # Stop the timer if it's running
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
            self.media_player.stop()  # Stop the music
            self.media_player2.stop()  # Stop the music
            self.media_player3.stop()  # Stop the music
            self.media_player4.stop()  # Stop the music
            self.media_player5.stop()  # Stop the music

        if self.sender() == self.start:
            self.current_workout_type = "cardio"
            self.update_cardio_image()
            self.headerbg_3.setText("Cardio Workout")
            self.media_player.play()  # Play the audio
        elif self.sender() == self.start_2:
            self.current_workout_type = "classic"
            self.update_classic_image()
            self.headerbg_3.setText("Classic Workout")
            self.media_player2.play()  # Play the audio
        elif self.sender() == self.start_3:
            self.current_workout_type = "strength"
            self.update_strength_image()
            self.headerbg_3.setText("Strength Workout")
            self.media_player3.play()  # Play the audio
        elif self.sender() == self.start_4:
            self.current_workout_type = "flexible"
            self.update_flexible_image()
            self.headerbg_3.setText("Flexibility Workout")
            self.media_player4.play()  # Play the audio
        elif self.sender() == self.start_5:
            self.current_workout_type = "intensity"
            self.update_intensity_image()
            self.headerbg_3.setText("High-Intensity Workout")
            self.media_player5.play()  # Play the audio
        # Reset the countdown label to 3
        self.counter = 0
        self.c3_2.setText("3")

        # Timer for the animation
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 second interval
        self.timer.timeout.connect(self.update_c3_label)

        # Start the timer
        self.timer.start()

    def update_c3_label(self):
        count = int(self.c3_2.text())
        if count > 1:
            self.c3_2.setText(str(count - 1))
        else:
            # Stop the timer when countdown finishes
            self.timer.stop()
            # Proceed to the cardio_exercise method
            self.cardio_exercise()

    def cardio_exercise(self):   
            self.exercisestackedWidget.setCurrentWidget(self.cardioexercise)
            self.exercisestackedWidget.raise_()
            self.countdown_timer = QTimer()
            self.countdown_timer.setInterval(1000)  # 1 second interval
            self.countdown_timer.timeout.connect(self.update_countdown)
            self.countdown_timer.start()
            
    def update_countdown(self):
        try:           
            if self.is_resting:
                rest_count = int(self.restcount.text())
                if rest_count > 0:
                    self.restcount.setText(str(rest_count - 1))
                else:
                    self.is_resting = False
                    self.restcount.hide()
                    self.countnum.show()
                    self.set_countnum_value()
                    getattr(self, f"switch_to_next_{self.current_workout_type}_image")()
                    self.repeat_count = self.set_repeat_value()
            else:
                count = int(self.countnum.text())
                if count > 0:
                    self.countnum.setText(str(count - 1))
                else:
                    if self.repeat_count == 1:
                        self.is_resting = True
                        self.countnum.hide()
                        self.restcount.show()
                        self.update_rest_count()
                        self.cardioshow.setText("REST")
                    else:
                        self.set_countnum_value()
                        self.repeat_count -= 1
        except Exception as e:
            print("Error in update_countdown:", e)
                           
    def switch_to_next_cardio_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.cardio_images)
        self.update_cardio_image()
        
    def switch_to_next_classic_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.classic_images)
        self.update_classic_image()
        
    def switch_to_next_strength_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.strength_images)
        self.update_strength_image()
        
    def switch_to_next_flexible_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.flexible_images)
        self.update_flexible_image()
        
    def switch_to_next_intensity_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.intensity_images)
        self.update_intensity_image()

    def update_cardio_image(self):
        pixmap = QPixmap(self.cardio_images[self.current_image_index])
        self.cardioshow.setPixmap(pixmap)
        
        # Get the size of the labels
        size_current = self.cardiopreview.size()
        size_next = self.cardiopreview2.size()
        size_prev = self.cardiopreview3.size()

        # Show the current image in cardiopreview (scaled to label size)
        pixmap_current = QPixmap(self.cardio_images[self.current_image_index]).scaled(size_current)
        self.cardiopreview.setPixmap(pixmap_current)

        # Calculate the indices for the next and previous images
        next_index = (self.current_image_index + 1) % len(self.cardio_images)
        prev_index = (self.current_image_index - 1) % len(self.cardio_images)

        # Show the next image in cardiopreview2 (scaled to label size)
        pixmap_next = QPixmap(self.cardio_images[next_index]).scaled(size_next)
        self.cardiopreview2.setPixmap(pixmap_next)

        # Show the previous image in cardiopreview3 (scaled to label size)
        pixmap_prev = QPixmap(self.cardio_images[prev_index]).scaled(size_prev)
        self.cardiopreview3.setPixmap(pixmap_prev)
        
        # Check if it's the last image and switch back to the main widget
        if self.current_image_index == len(self.cardio_images) - 1:
            self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisestackedWidget"))
            
    def update_classic_image(self):
        pixmap = QPixmap(self.classic_images[self.current_image_index])
        self.cardioshow.setPixmap(pixmap)
        
        # Get the size of the labels
        size_current = self.cardiopreview.size()
        size_next = self.cardiopreview2.size()
        size_prev = self.cardiopreview3.size()

        # Show the current image in cardiopreview (scaled to label size)
        pixmap_current = QPixmap(self.classic_images[self.current_image_index]).scaled(size_current)
        self.cardiopreview.setPixmap(pixmap_current)

        # Calculate the indices for the next and previous images
        next_index = (self.current_image_index + 1) % len(self.classic_images)
        prev_index = (self.current_image_index - 1) % len(self.classic_images)

        # Show the next image in cardiopreview2 (scaled to label size)
        pixmap_next = QPixmap(self.classic_images[next_index]).scaled(size_next)
        self.cardiopreview2.setPixmap(pixmap_next)

        # Show the previous image in cardiopreview3 (scaled to label size)
        pixmap_prev = QPixmap(self.classic_images[prev_index]).scaled(size_prev)
        self.cardiopreview3.setPixmap(pixmap_prev)
        
        # Check if it's the last image and switch back to the main widget
        if self.current_image_index == len(self.classic_images) - 1:
            self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisestackedWidget"))
            
    def update_strength_image(self):
        pixmap = QPixmap(self.strength_images[self.current_image_index])
        self.cardioshow.setPixmap(pixmap)
        
        # Get the size of the labels
        size_current = self.cardiopreview.size()
        size_next = self.cardiopreview2.size()
        size_prev = self.cardiopreview3.size()

        # Show the current image in cardiopreview (scaled to label size)
        pixmap_current = QPixmap(self.strength_images[self.current_image_index]).scaled(size_current)
        self.cardiopreview.setPixmap(pixmap_current)

        # Calculate the indices for the next and previous images
        next_index = (self.current_image_index + 1) % len(self.strength_images)
        prev_index = (self.current_image_index - 1) % len(self.strength_images)

        # Show the next image in cardiopreview2 (scaled to label size)
        pixmap_next = QPixmap(self.strength_images[next_index]).scaled(size_next)
        self.cardiopreview2.setPixmap(pixmap_next)

        # Show the previous image in cardiopreview3 (scaled to label size)
        pixmap_prev = QPixmap(self.strength_images[prev_index]).scaled(size_prev)
        self.cardiopreview3.setPixmap(pixmap_prev)
        
        # Check if it's the last image and switch back to the main widget
        if self.current_image_index == len(self.strength_images) - 1:
            self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisestackedWidget"))
            
    def update_flexible_image(self):
        pixmap = QPixmap(self.flexible_images[self.current_image_index])
        self.cardioshow.setPixmap(pixmap)
        
        # Get the size of the labels
        size_current = self.cardiopreview.size()
        size_next = self.cardiopreview2.size()
        size_prev = self.cardiopreview3.size()

        # Show the current image in cardiopreview (scaled to label size)
        pixmap_current = QPixmap(self.flexible_images[self.current_image_index]).scaled(size_current)
        self.cardiopreview.setPixmap(pixmap_current)

        # Calculate the indices for the next and previous images
        next_index = (self.current_image_index + 1) % len(self.flexible_images)
        prev_index = (self.current_image_index - 1) % len(self.flexible_images)

        # Show the next image in cardiopreview2 (scaled to label size)
        pixmap_next = QPixmap(self.flexible_images[next_index]).scaled(size_next)
        self.cardiopreview2.setPixmap(pixmap_next)

        # Show the previous image in cardiopreview3 (scaled to label size)
        pixmap_prev = QPixmap(self.flexible_images[prev_index]).scaled(size_prev)
        self.cardiopreview3.setPixmap(pixmap_prev)
        
        # Check if it's the last image and switch back to the main widget
        if self.current_image_index == len(self.flexible_images) - 1:
            self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisestackedWidget"))
    
    def update_intensity_image(self):
        pixmap = QPixmap(self.intensity_images[self.current_image_index])
        self.cardioshow.setPixmap(pixmap)
        
        # Get the size of the labels
        size_current = self.cardiopreview.size()
        size_next = self.cardiopreview2.size()
        size_prev = self.cardiopreview3.size()

        # Show the current image in cardiopreview (scaled to label size)
        pixmap_current = QPixmap(self.intensity_images[self.current_image_index]).scaled(size_current)
        self.cardiopreview.setPixmap(pixmap_current)

        # Calculate the indices for the next and previous images
        next_index = (self.current_image_index + 1) % len(self.intensity_images)
        prev_index = (self.current_image_index - 1) % len(self.intensity_images)

        # Show the next image in cardiopreview2 (scaled to label size)
        pixmap_next = QPixmap(self.intensity_images[next_index]).scaled(size_next)
        self.cardiopreview2.setPixmap(pixmap_next)

        # Show the previous image in cardiopreview3 (scaled to label size)
        pixmap_prev = QPixmap(self.intensity_images[prev_index]).scaled(size_prev)
        self.cardiopreview3.setPixmap(pixmap_prev)
        
        # Check if it's the last image and switch back to the main widget
        if self.current_image_index == len(self.intensity_images) - 1:
            self.exercisestackedWidget.setCurrentWidget(self.exercisestackedWidget.findChild(QWidget, "exercisestackedWidget"))
       
    def highlight_button(self, button):
        # Reset all buttons to normal
        for time_button in [self.time1, self.time2, self.time3, self.time4, self.time5]:
            time_button.setStyleSheet("border-radius:25px;background-color: white;")
        # Highlight the clicked button
        button.setStyleSheet("background-color: black; color: white;border-radius:25px")
    
    def resthighlight_button(self, button):
        # Reset all buttons to normal
        for rest_button in [self.rest1, self.rest2, self.rest3, self.rest4, self.rest5]:
            rest_button.setStyleSheet("border-radius:25px;background-color: white;")
        # Highlight the clicked button
        button.setStyleSheet("background-color: black; color: white;border-radius:25px")
    
    def repeathighlight_button(self, button):
        # Reset all buttons to normal
        for time_button in [self.repeat1, self.repeat2, self.repeat3, self.repeat4, self.repeat5]:
            time_button.setStyleSheet("border-radius:25px;background-color: white;")
        # Highlight the clicked button
        button.setStyleSheet("background-color: black; color: white;border-radius:25px")

    def set_countnum_value(self):
        self.exercisestackedWidget.raise_()
        button_values = {
            self.time1: 20,
            self.time2: 30,
            self.time3: 40,
            self.time4: 50,
            self.time5: 60
        }
        for time_button in [self.time1, self.time2, self.time3, self.time4, self.time5]:
            if time_button.styleSheet() == "background-color: black; color: white;border-radius:25px":
                count_value = button_values[time_button]
                self.countnum.setText(str(count_value))
 
                self.labelduration1.setText(str(count_value))
                self.labelduration1_2.setText(str(count_value))
                self.labelduration1_3.setText(str(count_value))
                self.labelduration1_4.setText(str(count_value))
                self.labelduration1_5.setText(str(count_value))
                
                self.classiclabelduration1.setText(str(count_value))
                self.classiclabelduration1_2.setText(str(count_value))
                self.classiclabelduration1_3.setText(str(count_value))
                self.classiclabelduration1_4.setText(str(count_value))
                self.classiclabelduration1_5.setText(str(count_value))
           
                self.strengthlabelduration1.setText(str(count_value))
                self.strengthlabelduration1_2.setText(str(count_value))
                self.strengthlabelduration1_3.setText(str(count_value))
                self.strengthlabelduration1_4.setText(str(count_value))
                self.strengthlabelduration1_5.setText(str(count_value))
          
                self.flexiblelabelduration1.setText(str(count_value))
                self.flexiblelabelduration1_2.setText(str(count_value))
                self.flexiblelabelduration1_3.setText(str(count_value))
                self.flexiblelabelduration1_4.setText(str(count_value))
                self.flexiblelabelduration1_5.setText(str(count_value))
         
                self.intensitylabelduration1.setText(str(count_value))
                self.intensitylabelduration1_2.setText(str(count_value))
                self.intensitylabelduration1_3.setText(str(count_value))
                self.intensitylabelduration1_4.setText(str(count_value))
                self.intensitylabelduration1_5.setText(str(count_value))

                break
            
    def set_repeat_value(self):
        self.exercisestackedWidget.raise_()
        button_values = {
            self.repeat1: 1,
            self.repeat2: 2,
            self.repeat3: 3,
            self.repeat4: 4,
            self.repeat5: 5
        }
        for time_button in [self.repeat1, self.repeat2, self.repeat3, self.repeat4, self.repeat5]:
            if time_button.styleSheet() == "background-color: black; color: white;border-radius:25px":
                self.repeat_count = button_values[time_button]
   
                break
        return self.repeat_count
                
    def update_rest_count(self):
        self.exercisestackedWidget.raise_()
        self.rest_values = {
            self.rest1: 5,
            self.rest2: 10,
            self.rest3: 15,
            self.rest4: 20,
            self.rest5: 30
        }
        for rest_button in self.rest_values:
            rest_value = self.rest_values[rest_button]
            if rest_button.styleSheet() == "background-color: black; color: white;border-radius:25px":
                self.restcount.setText(str(rest_value))
                self.labelrest.setText(str(rest_value))
                self.labelrest_2.setText(str(rest_value))
                self.labelrest_3.setText(str(rest_value))
                self.labelrest_4.setText(str(rest_value))  
                self.classiclabelrest.setText(str(rest_value))
                self.classiclabelrest_2.setText(str(rest_value))
                self.classiclabelrest_3.setText(str(rest_value))
                self.classiclabelrest_4.setText(str(rest_value))
                self.strengthlabelrest.setText(str(rest_value))
                self.strengthlabelrest_2.setText(str(rest_value))
                self.strengthlabelrest_3.setText(str(rest_value))
                self.strengthlabelrest_4.setText(str(rest_value))    
                self.flexiblelabelrest.setText(str(rest_value))
                self.flexiblelabelrest_2.setText(str(rest_value))
                self.flexiblelabelrest_3.setText(str(rest_value))
                self.flexiblelabelrest_4.setText(str(rest_value))
                self.intensitylabelrest.setText(str(rest_value))
                self.intensitylabelrest_2.setText(str(rest_value))
                self.intensitylabelrest_3.setText(str(rest_value))
                self.intensitylabelrest_4.setText(str(rest_value))  
                break
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UIexercise()
    window.show()
    sys.exit(app.exec_())
