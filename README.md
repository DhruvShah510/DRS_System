# DRS_System
This is the DRS system, which is used in Cricket to give the decision of out or not-out in a runout situation.

## Project Description
The DRS System (Decision Review System) is a cricket-based GUI application that simulates the third umpire's decision-making process. This application allows users to review video footage and make decisions regarding player dismissals.

Built using Python and Tkinter, it enables frame-by-frame video playback and displays decision images such as "Out" or "Not Out" based on user input.

## Features
Frame-by-Frame Video Control: Move forward or backward through the video in slow or fast motion.
Graphical User Interface (GUI): Built using Tkinter for an interactive experience.
Automated Decision Process: Displays a pending screen, sponsor screen, and then the final decision.
Multithreading Support: Ensures a smooth user experience while handling delays.
Image-Based Decision Display: Shows pre-defined images for "Out" and "Not Out" results.

## Installation & Requirements
Prerequisites
Ensure you have the following Python libraries installed:
- pip install opencv-python
- pip install pillow
- pip install imutils


## Project Files
The project consists of the following files:

- DRS_System.py → Main Python script for the application.
- video3.mp4,video2.mp4,video1.mp4 → The video file used for decision review.
- pending.png → Image displayed during the decision review process.
- sponser.png → Sponsor image displayed before the final decision.
- out.png → Image displayed if the decision is "Out".
- notout.png → Image displayed if the decision is "Not Out".
- welcome.png → Initial welcome screen image.

## How to Run
- Open a terminal or command prompt in the project directory.
- Run the script using:
- python DRS_System.py
- The application window will open, allowing you to interact with the decision review system.

## How to Use the Application
Video Navigation:
- << previous (fast): Move back 25 frames.
- << previous (slow): Move back 2 frames.
- Next (fast) >>: Move forward 25 frames.
- Next (slow) >>: Move forward 2 frames.

Decision Making:
- Give Out: Starts the decision review and displays the "Out" result.
- Give Not Out: Starts the decision review and displays the "Not Out" result.

## Project Workflow
- The user plays the video and navigates frame-by-frame.
- When a decision is made, a "Pending" screen appears.
- A sponsor screen is shown before displaying the final decision.
- The final decision (Out or Not Out) is displayed with an appropriate image.

## Technologies Used
- Python → Core programming language.
- Tkinter → GUI framework for user interaction.
- OpenCV → Video processing library.
- Pillow (PIL) → Image handling library.
- Imutils → Image processing utilities.
- Threading → Ensures smooth execution of the decision-making process.


## Acknowledgments
This project was created for **educational purposes** by learning from various online resources such as **YouTube and Google**.  
- Special thanks to **Code With Harry** for teaching this project and various python modules.
- Video clips taken from "Direct Hit! Some of the best run-outs in recent years"(https://youtu.be/zmiVWO7ab88?si=VsXEeDHXmTNoae3J) for educational and demonstration purpose only, credited to its original creator..

## Disclaimer 
This project is a **learning-based implementation** and is **not entirely an original idea**.  
It is **public for viewing**, but no explicit permission is given for commercial or large-scale use.  

This project includes **video clips from external sources**, used purely for **educational and demonstration purposes**.  
All rights to those clips remain with their original creators. If any content owners have concerns, they may contact me for removal.  



