# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import *
import datetime
from GUI.Admin import Admin
from GUI.Reader import Reader
from GUI.Regular import Manager
from GUI.validator import validator
from Deal.Dealership import Dealership1


root = Tk()
root.title("Authorization")
root.geometry('250x70+350+275')
root.resizable(width=False, height=False)
log = Entry(root, width=20)
log.grid(row=1, column=2, padx=(1, 1))
Label(root, text="Login", width=15).grid(row=1, column=1)
passwd = Entry(root, width=20, show='*')
passwd.grid(row=2, column=2, padx=(1, 1))
Label(root, text="Password").grid(row=2, column=1)


def authorization():
    login = log.get()
    password = passwd.get()

    if login.isalnum() and password.isalnum():
        text = Dealership1.authorization(login, password)
        # отображение интерфейса администратора
        if str(text[0]) == '1':
            print(str(datetime.datetime.today())[:19] + " INFO: Login & password "
                                                        "are correct. Welcome for ADMIN")
            root.withdraw()
            interface = Admin()
            interface.gui()
        # отображение интерфейса обычного пользователя
        elif str(text[0]) == '0':
            print(str(datetime.datetime.today())[:19] + " INFO: Login & password "
                                                        "are correct. Welcome for USER")
            root.withdraw()
            interface = Manager()
            interface.gui()
        elif str(text[0]) == '2':
            print(str(datetime.datetime.today())[:19] + " INFO: Получен доступ "
                                                        "только на просмотр данных")
            root.withdraw()
            interface = Reader()
            interface.gui()
        # окно с ошибкой
        else:
            rooter = Tk()
            rooter.title("ERROR")
            root.minsize(30, 50)
            out = Text(rooter, bg="white", font="Arial 12", width=50, height=10)
            out.grid(row=1, column=1, padx=(1, 1))
            out.insert("0.0", str(datetime.datetime.today())[:19] + " ERROR: Вы ввели не "
                                                                    "верный логин или пароль, "
                                                                    "либо Вы не зарегистрированны.")
            rooter.mainloop()
    else:
        if not login.isalnum() and password.isalnum():
            validator(log)
            passwd["bg"] = 'white'
        elif not password.isalnum() and login.isalnum():
            validator(passwd)
            log['bg'] = 'white'
        else:
            validator(log)
            validator(passwd)
        rooter = Tk()
        rooter.title("ERROR")
        root.minsize(50, 50)
        out = Text(rooter, bg="white", font="Arial 12", width=50, height=10)
        out.grid(row=1, column=1, padx=(1, 1))
        out.insert("0.0", str(datetime.datetime.today())[:19] + " ERROR: Вы "
                                                                "ввели не верные данные.")
        rooter.mainloop()

Button(root, text="LogIn", width=10, height=1, command=authorization).grid(row=3, column=1, padx=(1, 1))
Button(root, text="Cancel", width=10, height=1, command=root.destroy).grid(row=3, column=2, padx=(1, 1))
root.mainloop()
Dealership1.break_connection()
