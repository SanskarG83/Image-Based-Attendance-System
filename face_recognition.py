# import re
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import string


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image 
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Pannel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # =====================Attendance===================


    def face_recog(self):
        import datetime
        import time
        import tkinter as tk
        import cv2
        import os
        import pandas as pd

        window = Tk()
        window.title("F.Y. B.Tech - VIT Pune")
        window.configure(background='black')
        window.geometry('1280x670')

        lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white", fg="black", width=50,
                       height=3,
                       font=('times', 30, 'italic bold'))
        lbl.place(x=100, y=20)

        lbl1 = tk.Label(window, text="↓  List Of Present Students  ↓", width=25, fg="black", bg="white", height=2,
                        font=('times', 15, ' bold'))
        lbl1.place(x=540, y=320)

        message = tk.Label(window, text="", fg="black", bg="white", activeforeground="green", width=35, height=7,
                           font=('times', 15, ' bold '))
        message.place(x=470, y=400)

        def trackImages():
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("DataSet\Trainner.yml")
            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath)
            df = pd.read_csv("StudentRecord.csv")

            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ['Id', 'Name', 'Date', 'Time']
            attendance = pd.DataFrame(columns=col_names)
            while True:
                ret, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                    Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                    if (conf < 50):
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        aa = df.loc[df['Id'] == Id]['Name'].values
                        tt = str(Id) + "-" + aa
                        attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

                    else:
                        Id = 'Unknown'
                        tt = str(Id)
                    if (conf > 75):
                        noOfFile = len(os.listdir("UnknownImages")) + 1
                        cv2.imwrite("UnknownImages\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                    cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
                attendance = attendance.drop_duplicates(subset=['Id'], keep='first')

                cv2.imshow('Face Recognizing', im)
                pass

                if cv2.waitKey(10000):
                    break

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour, Minute, Second = timeStamp.split(":")

            # fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
            fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + ".csv"
            attendance.to_csv(fileName, index=False)

            # jay = storage.child().get_url(blob['downloadTokens'])

            cam.release()
            cv2.destroyAllWindows()

            res = attendance
            message.configure(text=res)

        trackImg = tk.Button(window, text="Track Image", command=trackImages, fg="black", bg="white", width=20,
                             height=3,
                             activebackground="Yellow", font=('times', 15, ' bold '))
        trackImg.place(x=400, y=200)

        quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black", bg="white", width=20, height=3,
                               activebackground="Red", font=('times', 15, ' bold '))
        quitWindow.place(x=700, y=200)

        lbl3 = tk.Label(window, text="DESIGN BY VIT PUNE F.Y B.TECH, GROUP : G4", width=80, fg="white", bg="black",
                        font=('times', 15, ' bold'))
        lbl3.place(x=200, y=620)

        window.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
