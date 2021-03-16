# import modules

from os import name
from tkinter import *
from functools import partial
import os
import _sqlite3
import sqlite3
from datetime import date
from datetime import time
from datetime import datetime

# Designing window for registration
global a, b


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    main_screen.destroy()
    global login_screen

    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)

    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    frame1 = Tk()
    frame1.title("Admin Section")
    frame1.geometry("500x500")
    frame1.configure(background="gray")

    def ad1():
        def call_result():
            global conn, cursor

            username_info = name.get()
            password_info = id.get()

            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS student ( username TEXT, password TEXT)")
            cursor.execute("INSERT INTO student (username,password) VALUES(?,?)", (username_info, password_info))
            # cursor.execute("SELECT * FROM `member` WHERE  `username` = ''")
            print("abc")
            conn.commit()
            # Result.config(text="Result = %d")
            return

        global addstud_screen
        addstud_screen = Tk()
        addstud_screen.title("ADD A STUDENT")
        addstud_screen.geometry("500x550")

        global name
        global id
        global dat
        global name_entry
        global ID_entry
        global date_entry
        global today
        global endday
        name = StringVar()
        id = StringVar()
        dat = StringVar()

        Label(addstud_screen, text="Please enter details below", bg="blue").pack()
        Label(addstud_screen, text="").pack()
        username_lable = Label(addstud_screen, text="Name of student* ")
        username_lable.pack()
        name_entry = Entry(addstud_screen, textvariable=name)
        name_entry.pack()

        password_lable = Label(addstud_screen, text="USER ID * ")
        password_lable.pack()
        ID_entry = Entry(addstud_screen, textvariable=id)
        ID_entry.pack()

        today = date.today()
        endday = str(today.day - today.month + 1 - today.year)
        print(endday)
        dat_lable = Label(addstud_screen, text="Date of Join * ")
        dat_lable.pack()

        dat_lable = Label(addstud_screen, text=today)
        dat_lable.pack()

        Label(addstud_screen, text="").pack()

        Label(addstud_screen, text="").pack()
        Button(addstud_screen, text="Register", width=10, height=1, bg="red", command=call_result()).pack()
        Button(addstud_screen, text="Register", width=10, height=1, bg="red", command=student_user()).pack()

    def student_user():
        username_info = name.get()
        password_info = id.get()
        dat_info = today

        file = open("guru99.txt", "a+")
        file.write(username_info + "\t")
        file.write(password_info + "\t")
        file.write(str(dat_info) + "\t")
        file.write(str(endday) + "\n")
        file.close()

        name_entry.delete(0, END)
        ID_entry.delete(0, END)

        Label(addstud_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    def disp1():
        print("abc")

    def grc1():
        print("abc")

    Add = Label(frame1, text="Add New Student: ").place(x=30, y=50)
    Addb = Button(frame1, text="Add", command=ad1).place(x=170, y=50)

    Disp = Label(frame1, text="Show List of Sudents: ").place(x=30, y=90)
    Dispb = Button(frame1, text="Show", command=disp1).place(x=170, y=90)

    Grc = Label(frame1, text="Grocery Section").place(x=30, y=130)
    Grcb = Button(frame1, text="Grocery", command=grc1).place(x=170, y=130)


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login for admin", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Change Password", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()


label1 =  Label(showstud_screen, text=at[0]+"\t"+str(at[1])+"\t"+str(at[2])+"\t"+at[3]+"\t"+str(at[4])+"\t"+str(at[5])+"\n",font=("calibri", 20)).pack()

for i in range(1, scr):
    cursor.execute("SELECT * FROM `student` " )
    pint = cursor.fetchall()
    print(pint)
    at = pint[0]
    bt = at[0]
    Label(showstud_screen, text="NAME \t ID  \t DATE \t ADDRESS \t\t MOBILE NUMBER  NO. OF DAYS", bg="red",
          font=("bold, 20")).pack()
    label1 = Label(showstud_screen,
                   text=at[0] + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + at[3] + "\t" + str(at[4]) + "\t" + str(
                       at[5]) + "\n", font=("calibri", 20)).pack()
    i = i + 1

 for i in range(1,100):
            l1 = Label(showstud_screen, text=records[0]).grid(row=1, column=1, sticky=W, pady=2)
            l2 = Label(showstud_screen, text=records[1]+"\n").grid(row=2, column=2, sticky=W, pady=2)
            l3 = Label(showstud_screen, text=records[2]).grid(row=3, column=3, sticky=W, pady=2)
            l4 = Label(showstud_screen, text=records[3]).grid(row=4, column=4, sticky=W, pady=2)
            l5 = Label(showstud_screen, text=records[4]).grid(row=5, column=5, sticky=W, pady=2)
            l6 = Label(showstud_screen, text=records[5]).grid(row=6, column=6, sticky=W, pady=2)



conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM student")
        counter = cursor.fetchall()
        print(counter)

        count = counter[0]
        scr = count[0]
        print(scr)

file = open("guru99.txt", "r")
if file.mode == 'r':
    contents = file.read()
# or, readlines reads the individual line into a list
fl = file.readlines()

# Label(showstud_screen, text=result_,font=("calibri", 20)).pack()\


file.close()

try:
    sqliteConnection = sqlite3.connect("pythontut.db")
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from student"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")

for row in records:
    i = 1

    l1 = Label(showstud_screen, text=row[0]).l1.grid(row=1, column=1, sticky=W, pady=2)
    l2 = Label(showstud_screen, text=row[1]).l2.grid(row=1, column=2, sticky=W, pady=2)
    l3 = Label(showstud_screen, text=row[2]).l3.grid(row=1, column=3, sticky=W, pady=2)
    l4 = Label(showstud_screen, text=row[3]).l4.grid(row=1, column=4, sticky=W, pady=2)
    l5 = Label(showstud_screen, text=row[4]).l5.grid(row=1, column=5, sticky=W, pady=2)
    l6 = Label(showstud_screen, text=row[5]).l6.grid(row=1, column=6, sticky=W, pady=2)

    i = i + 1
cursor.close()

except sqlite3.Error as error:
print("Failed to read data from sqlite table", error)
finally:
if (sqliteConnection):
    sqliteConnection.close()
    print("The SQLite connection is closed")

    l1.delete(0, END)
    l2.delete(0, END)
    l3.delete(0, END)
    l4.delete(0, END)
    l5.delete(0, END)
    l6.delete(0, END)
    l7.delete(0, END)
    l8.delete(0, END)
    l9.delete(0, END)
    l10.delete(0, END)
    l11.delete(0, END)
    l12.delete(0, END)
    l13.delete(0, END)
    l14.delete(0, END)

    if scr > 1:
        for i in range(0, 1):
            at = pint[i]

            Label(showstud_screen, text="NAME \t ID  DATE \t ADDRESS \t\t MOBILE NUMBER  NO. OF DAYS", bg="red",
                  font=("bold, 20")).pack()
            label1 = Label(showstud_screen,
                           text=at[0] + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + at[3] + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 2:
        for i in range(0, 2):
            at = pint[i]

            label2 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 3:
        for i in range(0, 3):
            at = pint[i]

            label3 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 4:
        for i in range(0, 4):
            at = pint[i]

            label4 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 5:
        for i in range(0, 5):
            at = pint[i]

            label5 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()
            print("hello")

    if scr > 6:
        for i in range(0, 6):
            at = pint[i]

            label6 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 7:
        for i in range(0, 7):
            at = pint[i]

            label7 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 8:
        for i in range(0, 8):
            at = pint[i]

            label8 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 9:
        for i in range(0, 9):
            at = pint[i]

            label9 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

    if scr > 9:
        for i in range(0, 9):
            at = pint[i]

            label10 = Label(showstud_screen,
                            text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                                at[4]) + "\t" + str(
                                at[5]) + "\n", font=("calibri", 20)).pack()

