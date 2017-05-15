# -*- coding: utf-8 -*-
from tkinter import *
import datetime
from GUI.Admin import Admin
from GUI.Reader import Reader
from GUI.Regular import Manager
from GUI.validator import validator
from Deal.DealershipDAO import Dealership_object


TIMESTAMP = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
ADMIN_ROLE = 'ADMIN'
MANAGER_ROLE = 'MANAGER'
USER_ROLE = 'READER'
CORRECT_FIELD = 'white'


def error_window():
    err_window = Tk()
    err_window.title("ERROR")
    err_window.minsize(250, 50)
    err_window.geometry('550x70+350+200')
    out = Text(err_window, font="Arial 12", width=150, height=10)
    out.grid(row=1, column=1, padx=(1, 1))
    out.insert("0.0", TIMESTAMP + " ERROR: Вы ввели не верный логин или "
                                  "пароль,\n либо Вы не зарегистрированны.")
    err_window.mainloop()


def draw_gui(role):
    root.withdraw()
    if role == ADMIN_ROLE:
        interface = Admin()
    elif role == MANAGER_ROLE:
        interface = Manager()
    elif role == USER_ROLE:
        interface = Reader()
    interface.gui()


def authorization():
    login = login_field.get()
    password = passwd.get()
    if login.isalnum() and password.isalnum():
        text = Dealership_object.authorization(login, password)
        if text[0] == ADMIN_ROLE:
            print(TIMESTAMP + " INFO: Login & password are correct. Welcome for " + ADMIN_ROLE)
            draw_gui(ADMIN_ROLE)
        elif text[0] == MANAGER_ROLE:
            print(TIMESTAMP + " INFO: Login/password are correct. Welcome for " + MANAGER_ROLE)
            draw_gui(MANAGER_ROLE)
        elif text[0] == USER_ROLE:
            print(TIMESTAMP + " INFO: Read only access")
            draw_gui(USER_ROLE)
        else:
            error_window()
    else:
        if not login.isalnum() and password.isalnum():
            validator(login_field)
            passwd["bg"] = CORRECT_FIELD
        elif not password.isalnum() and login.isalnum():
            validator(passwd)
            login_field['bg'] = CORRECT_FIELD
        else:
            validator(login_field)
            validator(passwd)
        error_window()


def auth_window():
    global root
    root = Tk()
    root.title("Authorization")
    root.geometry('250x70+350+275')
    root.resizable(width=False, height=False)
    global login_field
    login_field = Entry(root, width=20)
    login_field.grid(row=1, column=2, padx=(1, 1))
    Label(root, text="Login", width=15).grid(row=1, column=1)
    global passwd
    passwd = Entry(root, width=20, show='*')
    passwd.grid(row=2, column=2, padx=(1, 1))
    Label(root, text="Password").grid(row=2, column=1)

    Button(root, text="LogIn", width=10, height=1, command=authorization).grid(row=3, column=1, padx=(1, 1))
    Button(root, text="Cancel", width=10, height=1, command=root.destroy).grid(row=3, column=2, padx=(1, 1))
    root.mainloop()


auth_window()
