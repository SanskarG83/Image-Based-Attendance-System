from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("Image Based Attendance System")

        # ========= variables ========
        self.var_branch = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Adding 1st image -->
        img = Image.open(r"C:\Users\user\Pictures\CP2 images\download.jpg")
        img = img.resize((510, 170), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)

        # Adding 2nd image -->
        img2 = Image.open(r"C:\Users\user\Pictures\CP2 images\image_based_attendance.jpg")
        img2 = img2.resize((510, 170), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Adding 3nd image -->
        img4 = Image.open(r"C:\Users\user\Pictures\CP2 images\pexels-max-fischer-5212345.jpg")
        img4 = img4.resize((510, 170), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(self.root, image=self.photoimg4)
        f_lbl.place(x=1020, y=0, width=510, height=130)

        # Background image -->
        img3 = Image.open(r"C:\Users\user\Pictures\CP2 images\pexels-aleksandar-pasaric-2603464 (1).jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title -->
        title_lbl = Label(bg_img, text="Student Portal", font=("times new roman", 35, "bold"), bg="white", fg="purple")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=12, y=60, width=1500, height=620)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=12, y=10, width=750, height=600)

        img_left = Image.open(r"C:\Users\user\Pictures\CP2 images\Student_details.jpg")
        img_left = img_left.resize((300, 150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=730, height=120)

        # Currnet Course
        Current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=135, width=730, height=150)

        # Branch
        branch_label = Label(Current_course_frame, text="Branch", font=("times new roman", 12, "bold"))
        branch_label.grid(row=0, column=0, padx=10, sticky=W)

        branch_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_branch,
                                    font=("times new roman", 12, "bold"), width=25, state="readonly")
        branch_combo["values"] = (
            "Select Branch", "Computer", "IT", "Artificial Intelligence & Data Science", "Mechanical",
            "Electronics & Tele-Communication", "Instrumental & Control")
        branch_combo.current(0)
        branch_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=13, sticky=W)

        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), width=25, state="readonly")
        course_combo["values"] = ("Select Course", "FY", "SY", "TY", "B.TECH (LAST YR)")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(Current_course_frame, text="Academic Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=13, sticky=W)

        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=25, state="readonly")
        year_combo["values"] = (
            "Select Academic Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        sem_label = Label(Current_course_frame, text="Select Semester", font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=13, sticky=W)

        sem_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester,
                                 font=("times new roman", 12, "bold"), width=25, state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester - 1", "Semester - 2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Details
        Class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Details",
                                         font=("times new roman", 12, "bold"))
        Class_student_frame.place(x=5, y=260, width=730, height=300)

        # Student ID
        StudentID_label = Label(Class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"))
        StudentID_label.grid(row=0, column=0, padx=13, sticky=W)

        StudentID_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_ID,
                                    font=("times new roman", 12, "bold"))
        StudentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student Name
        Student_name_label = Label(Class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        Student_name_label.grid(row=0, column=2, padx=13, sticky=W)

        Student_name_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_name,
                                       font=("times new roman", 12, "bold"))
        Student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Division
        Div_label = Label(Class_student_frame, text="Division:", font=("times new roman", 12, "bold"))
        Div_label.grid(row=1, column=0, padx=13, sticky=W)

        div_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"),
                                 width=18, state="readonly")
        div_combo["values"] = (
        "Select Division", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
        "R", "S", "T")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=3, sticky=W)

        # Roll
        roll_no_label = Label(Class_student_frame, text="Roll:", font=("times new roman", 12, "bold"))
        roll_no_label.grid(row=1, column=2, padx=13, sticky=W)

        roll_no_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_roll,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender
        Gender_label = Label(Class_student_frame, text="Gender:", font=("times new roman", 12, "bold"))
        Gender_label.grid(row=2, column=0, padx=13, sticky=W)

        gender_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=3, sticky=W)

        # DOB
        dob_label = Label(Class_student_frame, text="Date Of Birth:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=13, sticky=W)

        dob_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_dob,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Email
        email_label = Label(Class_student_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=13, sticky=W)

        email_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_email,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Phone
        phone_label = Label(Class_student_frame, text="Phone NO:", font=("times new roman", 12, "bold"))
        phone_label.grid(row=3, column=2, padx=13, sticky=W)

        phone_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_phone,
                                font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address
        Student_name_label = Label(Class_student_frame, text="Address:", font=("times new roman", 12, "bold"))
        Student_name_label.grid(row=4, column=0, padx=13, sticky=W)

        Student_name_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_address,
                                       font=("times new roman", 12, "bold"))
        Student_name_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Techer name
        Student_name_label = Label(Class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"))
        Student_name_label.grid(row=4, column=2, padx=13, sticky=W)

        Student_name_entry = ttk.Entry(Class_student_frame, width=20, textvariable=self.var_teacher,
                                       font=("times new roman", 12, "bold"))
        Student_name_entry.grid(row=4, column=3, padx=10, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(Class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame 1
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=160, width=720, height=35)

        save_btn = Button(btn_frame, text="Save", width=17, command=self.add_data, font=("times new roman", 13, "bold"),
                          bg="purple", fg="white")
        save_btn.grid(row=0, column=0)

        updt_btn = Button(btn_frame, text="Update", width=17, command=self.upd_data,
                          font=("times new roman", 13, "bold"), bg="purple",
                          fg="white")
        updt_btn.grid(row=0, column=1)

        dlt_btn = Button(btn_frame, text="Delete", width=17, command=self.dlt_data,
                         font=("times new roman", 13, "bold"), bg="purple",
                         fg="white")
        dlt_btn.grid(row=0, column=2)

        rst_btn = Button(btn_frame, text="Reset", width=17, command=self.rst, font=("times new roman", 13, "bold"),
                         bg="purple",
                         fg="white")
        rst_btn.grid(row=0, column=3)

        # button frame 2
        btn_frame2 = Frame(Class_student_frame, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=195, width=720, height=35)

        take_photo_btn = Button(btn_frame2, command=self.gent_dataset, text="Take a photo sample", width=36,
                                font=("times new roman", 13, "bold"),
                                bg="purple", fg="white")
        take_photo_btn.grid(row=0, column=2)

        updt_photo_btn = Button(btn_frame2, text="Update a photo sample", width=36,
                                font=("times new roman", 13, "bold"), bg="purple", fg="white")
        updt_photo_btn.grid(row=0, column=3)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=600)

        img_right = Image.open(r"C:\Users\user\Pictures\CP2 images\kids_class_1400.jpg")
        img_right = img_right.resize((550, 150), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=730, height=120)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=730, height=70)

        search_label = Label(search_frame, text="Search by", font=("times new roman", 14, "bold"), bg="grey")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=25, state="readonly")
        search_combo["values"] = ("Select", "PRN No", "Name", "Roll")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(search_frame, width=14, font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=11, font=("times new roman", 11, "bold"), bg="purple",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, text="Show All", width=11, font=("times new roman", 11, "bold"), bg="purple",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=2)

        # ========== Table frame ==========

        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=705, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "Branch", "Course", "Year", "Semester", "ID", "Name", "Div", "Roll", "Gender", "DOB", "Email",
            "Phone No",
            "Address", "Teacher", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Branch", text="Branch")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("ID", text="Student ID (PRN)")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div", text="Divison")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone No", text="Phone No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Branch", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone No", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ========== Function declaration ==========

    def add_data(self):
        if self.var_branch.get() == "select Branch" or self.var_name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sg@83192003",
                                               database="sys")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_branch.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_ID.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success!", "Student details has been successfully added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error,", f"Due to:{str(es)}", parent=self.root)

    # ======= Fetching data from database =======
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sg@83192003", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
        conn.close()

    # ======= Get cursor functn ====
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_branch.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ==== Update ====
    def upd_data(self):
        if self.var_branch.get() == "select Branch" or self.var_name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Warning!", "All fields are required!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update!", "Do you want to update your details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sg@83192003",
                                                   database="sys")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Branch=%s,Course=%s,Year=%s,Semester=%s,`Name`=%s,`Div`=%s,`Roll`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`Photosample`=%s where `ID`=%s",
                        (
                            self.var_branch.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_ID.get(),
                        ))
                    conn.commit()
                    conn.close()


                else:
                    if not update:
                        return
                messagebox.showinfo("success!", "Student details successfullt updated!", parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # ==== delete functn ====
    def dlt_data(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error!", "Student ID must be required", parent=self.root)
        else:
            try:
                dlt = messagebox.askyesno("Delete Page", "Do you want to delete details of this student?",
                                          parent=self.root)
                if dlt > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sg@83192003",
                                                   database="sys")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID= %s"
                    val = (self.var_ID.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()


                else:
                    if not delete:
                        return

                self.fetch_data()
                messagebox.showinfo("Delete", "Student details Successfully deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # ===== Reset function =====
    def rst(self):
        self.var_branch.set("Select Branch"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_ID.set(""),
        self.var_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

        # ========= Generate data set and take photo samples =========

    def gent_dataset(self):
        if self.var_branch.get() == "select Branch" or self.var_name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sg@83192003",
                                               database="sys")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set Branch=%s,Course=%s,Year=%s,Semester=%s,`Name`=%s,`Div`=%s,`Roll`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`Photosample`=%s where `ID`=%s",
                    (
                        self.var_branch.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_ID.get() == id + 1,
                    ))
                conn.commit()
                self.fetch_data()
                self.rst()
                conn.close()

                # ===== load predefined data on face from opencv =====

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scalling factor = 1.3
                    # Minimum neighbour = 5

                    for (x, y, w, h) in faces:
                        face_crop = img[y:y + h, x:x + w]
                        return face_crop

                cap = cv2.VideoCapture(0)  # for other camera(ext) type (1)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_crop(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_crop(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
                        file_name_path = "img data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, img=face, params=None)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data-set of images completed successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()