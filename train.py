from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
import tkinter as tk
from tkinter import Message, Text
import cv2, os
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as font


class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image 
        bg1 = Image.open(r"Images_GUI\t_bg1.jpg")
        bg1 = bg1.resize((1366, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Training Pannel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.train_classifier, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.train_classifier, text="Train Dataset", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        window = tk.Tk()
        window.title("F.Y. B.Tech - Group G4")
        window.configure(background='black')
        window.geometry('1280x670')

        lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white", fg="black", width=50,
                       height=3, font=('times', 30, 'italic bold'))
        lbl.place(x=100, y=20)

        lbl1 = tk.Label(window, text="Enter ID", width=20, height=2, fg="black", bg="white",
                        font=('times', 15, ' bold '))
        lbl1.place(x=200, y=200)

        txt1 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        txt1.place(x=550, y=215)

        lbl2 = tk.Label(window, text="Enter Name", width=20, fg="black", bg="white", height=2,
                        font=('times', 15, ' bold '))
        lbl2.place(x=200, y=300)

        txt2 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        txt2.place(x=550, y=315)

        lbl3 = tk.Label(window, text="Notification →", width=20, fg="black", bg="white", height=2,
                        font=('times', 15, ' bold '))
        lbl3.place(x=200, y=400)

        message = tk.Label(window, text="", bg="white", fg="black", width=30, height=2, font=('times', 15, ' bold '))
        message.place(x=550, y=400)

        def clearId():
            txt1.delete(0, 'end')

        def clearName():
            txt2.delete(0, 'end')

        def isNumber(s):
            try:
                float(s)
                return True
            except ValueError:
                pass

        def takeImages():
            Id = (txt1.get())
            name = (txt2.get())
            if (isNumber(Id) and name.isalpha()):
                cam = cv2.VideoCapture(0)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        sampleNum = sampleNum + 1
                        cv2.imwrite("SampleImages\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        cv2.imshow('Face Detecting', img)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    elif sampleNum > 60:
                        break
                cam.release()
                cv2.destroyAllWindows()
                res = "Images Saved for ID : " + Id + " Name : " + name
                row = [Id, name]
                with open('StudentRecord.csv', 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                message.configure(text=res)
            else:
                if (isNumber(name)):
                    res = "Enter Alphabetical Name"
                    message.configure(text=res)
                if (Id.isalpha()):
                    res = "Enter Numeric Id"
                    message.configure(text=res)

        def trainImages():
            recognizer = cv2.face_LBPHFaceRecognizer.create()
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            faces, Id = getImagesAndLabels("SampleImages")
            recognizer.train(faces, np.array(Id))
            recognizer.save("DataSet\Trainner.yml")
            res = "Image Trained"
            message.configure(text=res)

        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            Ids = []
            for imagePath in imagePaths:
                pilImage = Image.open(imagePath).convert('L')
                imageNp = np.array(pilImage, 'uint8')
                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces.append(imageNp)
                Ids.append(Id)
            return faces, Ids

        clearButton1 = tk.Button(window, text="Clear", command=clearId, fg="black", bg="white", width=20, height=2,
                                 activebackground="Red", font=('times', 15, ' bold '))
        clearButton1.place(x=850, y=200)

        clearButton2 = tk.Button(window, text="Clear", command=clearName, fg="black", bg="white", width=20, height=2,
                                 activebackground="Red", font=('times', 15, ' bold '))
        clearButton2.place(x=850, y=300)

        takeImg = tk.Button(window, text="Take Images", command=takeImages, fg="black", bg="white", width=20, height=3,
                            activebackground="Green", font=('times', 15, ' bold '))
        takeImg.place(x=200, y=500)

        trainImg = tk.Button(window, text="Train Images", command=trainImages, fg="black", bg="white", width=20,
                             height=3, activebackground="Green", font=('times', 15, ' bold '))
        trainImg.place(x=500, y=500)

        quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black", bg="white", width=20, height=3,
                               activebackground="Red", font=('times', 15, ' bold '))
        quitWindow.place(x=800, y=500)

        lbl4 = tk.Label(window, text="DESIGN BY VIT PUNE F.Y B.TECH, GROUP : G4", width=80, fg="white", bg="black",
                        font=('times', 15, ' bold'))
        lbl4.place(x=200, y=620)

        window.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
