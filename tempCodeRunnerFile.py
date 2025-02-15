from tkinter import *
import cv2
import numpy as np
import PIL.Image
import PIL.ImageTk

background = "#f00f0f"
text = "black"

top = Tk()
top.geometry("600x650")
top.title("Welcome to Your Own Virtual DressChecker !!!!!")

Label(top, text="DEVELOPED BY Kushagra Gupta", 
      justify=LEFT, fg="#c9210a").place(height=120, width=600)

def webcam():
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define color ranges
        colors = {
            "Red": ([136, 87, 111], [180, 255, 255], (0, 0, 255)),
            "Blue": ([99, 115, 150], [110, 255, 255], (255, 0, 0)),
            "Yellow": ([22, 60, 200], [60, 255, 255], (0, 255, 0))
        }

        kernal = np.ones((5, 5), "uint8")

        for color_name, (lower, upper, bgr) in colors.items():
            mask = cv2.inRange(hsv, np.array(lower, np.uint8), np.array(upper, np.uint8))
            mask = cv2.dilate(mask, kernal)
            res = cv2.bitwise_and(img, img, mask=mask)

            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 300:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(img, (x, y), (x + w, y + h), bgr, 2)
                    cv2.putText(img, f"{color_name} Color", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, bgr, 2)

        cv2.imshow("Press Esc To Exit", img)
        if cv2.waitKey(10) & 0xFF == 27:  # Exit on pressing ESC
            break

    cap.release()
    cv2.destroyAllWindows()

def quitting():
    top.quit()

def show_match(image_path, title):
    w1 = Toplevel()
    w1.title(title)
    w1.geometry("800x800")
    C = Canvas(w1, bg="white", height=800, width=800)
    
    img = PIL.Image.open(image_path)
    img = img.resize((500, 500), PIL.Image.ANTIALIAS)
    w1.img = PIL.ImageTk.PhotoImage(img)

    C.create_image(250, 250, image=w1.img)
    C.pack()

    Button(w1, text="Quit", command=w1.destroy, padx=10, pady=10, activebackground=background, fg="BLACK").pack()

def callback():
    w = Toplevel()
    w.geometry("800x500")
    w.title("Let's Get You Dressed Up")

    Label(w, text="Found Some Matches! Here They Are:", font=("Times New Roman", 16)).pack()

    for i in range(1, 9):
        Button(w, text=f"Match {i}", command=lambda i=i: show_match(f"match{i}.jpg", f"Match {i}"), 
               activebackground=background, fg=text, font=("Comic Sans", 16)).pack()

    Button(w, text="Go Back", command=w.destroy, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()
    Button(w, text="Quit", command=quitting, activebackground=background, fg=text, font=("Comic Sans", 16)).pack()

def initiate():
    Button(top, text="Start Webcam", command=webcam, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200, y=200)
    Button(top, text="Suggest Clothes", command=callback, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200, y=250)
    Button(top, text="Quit", command=quitting, activebackground=background, fg=text, padx=10, pady=10, font=("Comic Sans", 16)).place(x=200, y=300)

initiate()
top.mainloop()
