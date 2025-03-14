import tkinter                     
import cv2                        #pip install opencv-python
import PIL.Image, PIL.ImageTk     #pip install Pillow
from functools import partial
import threading
import imutils                    #pip install imutils
import time

'''
Tkinter is the simplest way in Python to create Graphical User interfaces (GUIs) and is included in all standard Python Distributions. In fact, it’s the only framework built into the Python standard library.

Opencv is an open source library which is very useful for computer vision applications such as video analysis, CCTV footage analysis and image analysis.When we create applications for computer vision that we don't want to build from scratch we can use this library to start focusing on real world problems. 

'''

stream = cv2.VideoCapture("video3.mp4")                                                            #it is used to sst the stream to capture the video
def play(speed):
    print(f"The screen plays at speed of {speed}.")

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    
    if not grabbed:
        return  # Instead of exit(), return to prevent abrupt program termination

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    frame = imutils.resize(frame, width=805, height=452)  
    # frame = imutils.resize(frame, width = 1000,height=592)
    #Here as the video is having the differnt frame size than the SET_WIDTH and SET_HEIGHT so we change the width and height of the fram as per requirement such that the video plays on full screen 
    #here do trial and error to find the perfect frame requirement of the video in line 32
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    canvas.create_text(140, 35, fill="black", font="Times 26 bold", text="Decision Pending")

    
def pending(decision):
    #1. display the decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)                             #To resize the fram if the fram is not resized
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    #2. wait for 1 second
    time.sleep(1)

    #3. display the sponser image
    frame = cv2.cvtColor(cv2.imread("sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)                             #To resize the fram if the fram is not resized
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    
    #4. wait for 1.5 second
    time.sleep(1.5)
    
    #5. disply the decision image(out/not out)
    if decision == "out":
        decisionImg = "out.png"
    else:
        decisionImg = "notout.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)                            #To resize the fram if the fram is not resized
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("The player is out.")

def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("The player is not out.")

#Width and Height of the screen
SET_WIDTH = 630
SET_HEIGHT = 452
# SET_WIDTH = 1000
# SET_HEIGHT = 592

#Tkinter GUI starts here 
window = tkinter.Tk()                                                                    #To create a main window
window.title("DHS Third Umpire Decision Review System")                                  #To give Title to the Tkinter window

cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)                      #cv2.COLOR_BGR2RGB is used so that the image is read in the original coclour 
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)                  #to set the canvas frame
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))                        #to take the photo that is to be displayed
img_on_canvas = canvas.create_image(0,0, anchor=tkinter.NW, image=photo)                 #to display image on canavs canvas.create_image(start position, start position, postion, image)
canvas.pack()

#buttoms on window
btn = tkinter.Button(window, text="<< previous(fast)", width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< previous(slow)", width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next(fast) >>", width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next(slow) >>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width = 50, command = out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width = 50, command = not_out)
btn.pack()

window.mainloop()                                                                      
#There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.