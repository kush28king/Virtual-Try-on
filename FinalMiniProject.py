from tkinter import *
#Using Tkinter for the GUI
import PIL.ImageTk
import PIL.Image

background="#f00f0f"
background2="#ff9000"
text="black"
width="200c"

top = Tk()
top.geometry(newGeometry="600x650")
top.title("Welcome to Your Own Virtual DressChecker !!!!!")




Message(top,text="DEVELOPED BY Kushagra Gupta") 

def webcam():
    import cv2
    #Using cv2 i.e OpenCV for all the color related operations

    import numpy as np
    #Using numpy for all grouping of numerals

    # capturing video through webcam
    cap = cv2.VideoCapture(0)

    while (1):
        _, img = cap.read()

        # converting frame(img i.e BGR) to HSV (hue-saturation-value)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # defining the range of red color
        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)

        # defining the Range of Blue color
        blue_lower = np.array([99, 115, 150], np.uint8)
        blue_upper = np.array([110, 255, 255], np.uint8)

        # defining the Range of yellow color
        yellow_lower = np.array([22, 60, 200], np.uint8)
        yellow_upper = np.array([60, 255, 255], np.uint8)

        # finding the range of red,blue and yellow color in the image
        red = cv2.inRange(hsv, red_lower, red_upper)
        blue = cv2.inRange(hsv, blue_lower, blue_upper)
        yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

        # Morphological transformation, Dilation
        kernal = np.ones((5, 5), "uint8")

        red = cv2.dilate(red, kernal)
        res = cv2.bitwise_and(img, img, mask=red)

        blue = cv2.dilate(blue, kernal)
        res1 = cv2.bitwise_and(img, img, mask=blue)

        yellow = cv2.dilate(yellow, kernal)
        res2 = cv2.bitwise_and(img, img, mask=yellow)

        # Tracking the Red Color
        #Hex value is assumed to be 0,0,255
        (_, contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, "RED color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

        # Tracking the Blue Color
        #Hex value is assumed to be 255,0,0
        (_, contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "Blue color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

        # Tracking the yellow Color
        #Hex value for HSV is assumed to be 0,255,0
        (_, contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "yellow  color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

        cv2.imshow("Press Esc To Exit", img)
        k=cv2.waitKey(10) & 0xFF
        if k==27:
            cap.release()
            cv2.destroyAllWindows()
            break
#End of webcam module


#Defining callbacks for each of the 8 buttons

def match1():
     w1=Toplevel()
     w1.config(padx=10, pady=10)
     w1.title("Match 1 !!!!!")
     w1.geometry(newGeometry="800x800")
     C = Canvas(w1,bg="white" , height=1000, width=1000)
     top.img=img=PIL.ImageTk.PhotoImage(PIL.Image.open("match1.jpg"))
     Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
         x=600, y=700)
     image = C.create_image(500, 500,  image=img)
     C.pack()



def match2():
    w1 = Toplevel()
    w1.config(padx=10, pady=10)
    w1.geometry(newGeometry="800x800")
    w1.title("Match 2 !!!!!")

    C = Canvas(w1, bg="white", height=1000, width=1000)
    top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match2.jpg"))

    Button(w1, text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=600, y=700)

    image = C.create_image(500, 500, image=img)
    C.pack()


def match3():

        w1 = Toplevel()
        w1.config(padx=10, pady=10)
        w1.title("Match 3 !!!!!")
        w1.geometry(newGeometry="800x800")
        C = Canvas(w1, bg="white", height=1000, width=1000)
        top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match3.jpg"))

        Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
            x=600, y=700)
        image = C.create_image(500, 500, image=img)
        C.pack()


def match4():
    w1 = Toplevel()
    w1.config(padx=10, pady=10)
    w1.title("Match 4 !!!!!")
    w1.geometry(newGeometry="800x800")
    C = Canvas(w1, bg="white", height=1000, width=1000)
    top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match4.jpg"))

    Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=600, y=700)
    image = C.create_image(500, 500, image=img)
    C.pack()


def match5():
        w1 = Toplevel()
        w1.config(padx=10, pady=10)
        w1.title("Match 5 !!!!!")
        w1.geometry(newGeometry="800x800")
        C = Canvas(w1, bg="white", height=1000, width=1000)
        top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match5.jpg"))

        Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
            x=600, y=700)
        image = C.create_image(500, 500, image=img)
        C.pack()


def match6():
    w1 = Toplevel()
    w1.config(padx=10, pady=10)
    w1.title("Match 6 !!!!!")
    w1.geometry(newGeometry="800x800")
    C = Canvas(w1, bg="white", height=1000, width=1000)
    top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match6.jpg"))

    Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=600, y=700)
    image = C.create_image(500, 500, image=img)
    C.pack()


def match7():
    w1 = Toplevel()
    w1.config(padx=10, pady=10)
    w1.title("Match 7 !!!!!")
    w1.geometry(newGeometry="800x800")
    C = Canvas(w1, bg="white", height=1000, width=1000)
    top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match7.jpg"))
    Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=600, y=700)
    image = C.create_image(500, 500, image=img)
    C.pack()


def match8():
    w1 = Toplevel()
    w1.config(padx=10, pady=10)
    w1.title("Match 8 !!!!!")
    w1.geometry(newGeometry="800x800")
    C = Canvas(w1, bg="white", height=1000, width=1000)
    top.img = img = PIL.ImageTk.PhotoImage(PIL.Image.open("match8.jpg"))
    Button(w1,text="Quit", command=quitting, padx=10, pady=10, activebackground=background, fg="BLACK").place(
        x=600, y=700)
    image = C.create_image(500, 500, image=img)
    C.pack()

#Defining a main screen GUI Window which pops up when the user wants the module to show the suggestions from the clothes that the program matches
#We have ensured that the user gets satisfied with all the available outputs


def callback():
    top.withdraw()
    w = Toplevel()
    w.geometry(newGeometry="800x500")
    w.title("Let's Get You Dressed Up")
    Frame(w, width=50, height=250).place(x=800,y=600)
    Label(w, text="Found Some Matches  Here They Are!!",font=("Times New Roman", 16)).pack()
    Button(w, text="Match 1", command=match1 ,activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 2", command=match2, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 3", command=match3, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 4", command=match4, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Match 5", command=match5, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()
    Button(w, text="Match 6", command=match6, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()
    Button(w, text="Match 7", command=match7, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()
    Button(w, text="Match 8", command=match8, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()
    Button(w, text="Go Back", command=initiate, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()
    Button(w, text="Quit", command=quitting, activebackground=background, fg=text,font=("Comic Sans", 16)).pack()


#When the user selects quit

def quitting():
    exit(0)

#First Window on Screen


def initiate():
    top.deiconify()
    top.tkraise() #To raise the method
    Button(top,text="Start Webcam",command=webcam, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=200)
    Button(top,text="Suggest Clothes", command=callback, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=250)
    Button(top,text="Quit", command=quitting, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200,y=300)


if __name__ == '__main__':
    # Calling the main display method to show up all the available options
    initiate()

top.mainloop()