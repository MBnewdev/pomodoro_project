Pomodoro Timer
A simple Pomodoro timer application built with Python using the Tkinter library for the graphical user interface (GUI) and the Pillow library for handling images. The app helps users manage their time efficiently using the Pomodoro technique, which involves working for 25 minutes followed by a short break, and after four cycles, a long break is taken.

Features
Pomodoro Timer: Works in cycles of 25 minutes of work followed by a 5-minute short break.

Long Break: After completing four Pomodoro cycles, a long break of 20 minutes is taken.

Customizable Background: The app displays random images from a specified folder as the background during each session.


UI Components:
Displays the timer countdown.
Shows the current session type (work or break).
Buttons to start and reset the timer.
A checkmark is displayed after completing each Pomodoro session.


Requirements
Make sure you have Python 3.6+ installed

then run 

pip install pillow
Pillow for image handling.

pip install tk
Tkinter for the GUI.

Add images to the Assets folder.

Make sure to place any images you want to use as backgrounds in the Assets folder. The app will select a random image from this folder to display as the background.

To start the Pomodoro timer, run the main.py script:

python3 main.py
