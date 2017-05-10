# -*- coding: utf-8 -*-
import hashlib
from tkinter import *
from tkinter.ttk import Combobox as Combobox
from GUI.validator import validator
from Deal.Dealership import Dealership1


def admin():
    roota = Tk()
    roota.title("Administration")
    roota.minsize(100, 200)
    roota.geometry('670x350+100+110')
    roota.resizable(width=False, height=True)

    def add_car_btn():
        # Окно для добавления авто
        root1 = Toplevel(roota)
        root1.title("Add new car")
        root1.geometry('250x200+200+200')
        root1.resizable(width=False, height=False)
        # make root1 modal
        root1.grab_set()
        # поля ввода для добавления записи в бд
        car_model = Entry(root1, width=20)
        car_model.grid(row=2, column=2)
        Label(root1, text="Название модели").grid(row=2, column=1)
        maker = Entry(root1, width=20)
        maker.grid(row=3, column=2)
        Label(root1, text="Производитель").grid(row=3, column=1)
        year_production = Entry(root1, width=20)
        year_production.grid(row=4, column=2)
        Label(root1, text="Год выпуска").grid(row=4, column=1)
        car_engine = Entry(root1, width=20)
        car_engine.grid(row=5, column=2)
        Label(root1, text="Объем двигателя").grid(row=5, column=1)
        cost = Entry(root1, width=20)
        cost.grid(row=6, column=2)
        Label(root1, text="Стоимость").grid(row=6, column=1)

        def ok_btn():
            if year_production.get().isdigit() and cost.get().isdigit() and maker.get().isalpha():
                t = Dealership1.add_car(car_model.get().capitalize(), maker.get().upper(), year_production.get(),
                                        car_engine.get(), cost.get())
                output.insert("0.0", str(t) + "\n")
                root1.destroy()
            else:

                if not year_production.get().isdigit():
                    validator(year_production)

                if not cost.get().isdigit():
                    validator(cost)

                if not maker.get().isalpha():
                    validator(maker)

                info = "WARNING: Поля цена, год выпуска должны сожержать цифры; производитель - только буквы\n"
                print(info)
                output.insert(END, info)
        Button(root1, text="Добавить", width=10, height=1, command=ok_btn).grid(row=8, column=1)
        Button(root1, text="Отмена", width=10, height=1, command=root1.destroy).grid(row=8, column=2)
        root1.mainloop()

    def add_lorry_btn():
        root2 = Toplevel(roota)
        root2.title("Add new Lorry")
        root2.geometry('250x200+200+200')
        root2.resizable(width=False, height=False)
        root2.grab_set()
        car_model = Entry(root2, width=20)
        car_model.grid(row=2, column=2)
        Label(root2, text="Модель").grid(row=2, column=1)
        maker = Entry(root2, width=20)
        maker.grid(row=3, column=2)
        Label(root2, text="Производитель").grid(row=3, column=1)
        year_production = Entry(root2, width=20)
        year_production.grid(row=4, column=2)
        Label(root2, text="Год выпуска").grid(row=4, column=1)
        car_engine = Entry(root2, width=20)
        car_engine.grid(row=5, column=2)
        Label(root2, text="Объем двигателя").grid(row=5, column=1)
        cost = Entry(root2, width=20)
        cost.grid(row=6, column=2)
        Label(root2, text="Стоимость").grid(row=6, column=1)
        weight_limit = Entry(root2, width=20)
        weight_limit.grid(row=7, column=2)
        Label(root2, text="Грузовой лимит").grid(row=7, column=1)

        def ok_btn():
            if year_production.get().isdigit() and cost.get().isdigit() and \
                    weight_limit.get().isdigit():
                t = Dealership1.add_lorry(car_model.get().capitalize(), maker.get().upper(), year_production.get(),
                                          car_engine.get(), cost.get(), weight_limit.get())
                output.insert("0.0", str(t) + "\n")
                root2.destroy()
            else:
                if not year_production.get().isdigit():
                    validator(year_production)
                if not cost.get().isdigir():
                    validator(cost)
                if not weight_limit.get().isdigit():
                    validator(weight_limit)

                info = "WARNING: Поля id, цена, год выпуска и весовые ограничения должны сожержать цифры\n"
                print(info)
                output.insert(END, info)
        Button(root2, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root2, text="Отмена", width=10, height=1, command=root2.destroy).grid(row=9, column=2)
        root2.mainloop()

    def add_car_to_ds_btn():
        # Окно для добавления авто дилерцентру
        root3 = Toplevel(roota)
        root3.title("Add new car to dealership")
        root3.geometry('250x100+200+200')
        root3.resizable(width=False, height=False)
        root3.grab_set()
        # поля ввода для добавления записи в бд
        id_car = Entry(root3, width=20)
        id_car.grid(row=1, column=2)
        Label(root3, text="Идентификатор").grid(row=1, column=1)
        amount = Entry(root3, width=20)
        amount.grid(row=2, column=2)
        Label(root3, text="Количество").grid(row=2, column=1)

        def ok_btn():
            if amount.get().isdigit() and id_car.get().isdigit():
                t = Dealership1.add_car_to_dealership(id_car.get(), amount.get())
                output.insert("0.0", str(t) + "\n")
                root3.destroy()
            else:
                if not amount.get().isdigit():
                    validator(amount)
                if not id_car.get().isdigit():
                    validator(id_car)
                info = "WARNING: Поля должны содержать только цифры\n"
                print(info)
                output.insert(END, info)
        Button(root3, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root3, text="Отмена", width=10, height=1, command=root3.destroy).grid(row=9, column=2)
        root3.mainloop()

    def update_amount_btn():
        # Окно для изменения кол-ва
        root4 = Toplevel(roota)
        root4.title("Change cars amount")
        root4.resizable(width=False, height=False)
        root4.geometry('250x100+200+200')
        root4.grab_set()
        options = Dealership1.return_dict()
        # поля ввода для добавления записи в бд
        Label(root4, text="Идентификатор").grid(row=1, column=1)
        amount = Entry(root4, width=20)
        amount.grid(row=2, column=2)
        Label(root4, text="Количество").grid(row=2, column=1)
        ids = Combobox(root4, value=list(options.values()))
        ids.grid(row=1, column=2)

        def ok_btn():
            t = Dealership1.update_amount(ids.get(), amount.get())
            output.insert("0.0", str(t) + "\n")
            root4.destroy()

        Button(root4, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root4, text="Отмена", width=10, height=1, command=root4.destroy).grid(row=9, column=2)
        root4.mainloop()

    def del_car_from_ds_btn():
        # Окно для ввода id записи для удаления
        root5 = Toplevel(roota)
        root5.title("Delete car from dealership")
        root5.geometry('300x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        options = Dealership1.return_dict()
        # поля ввода для удаления записи из бд
        Label(root5, text="Идентификатор").grid(row=1, column=1)
        ids = Combobox(root5, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.delete_car_from_dealership(id_car)
            output.insert("0.0", str(t) + "\n")
            root5.destroy()
        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def update_car_cost_btn():
        root5 = Toplevel(roota)
        root5.title("Change cost")
        root5.geometry('250x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        options = Dealership1.retrive_from_one_db('cars', 'id_car', 'car_model')
        Label(root5, text="Идентификатор").grid(row=1, column=1)
        cost = Entry(root5, width=20)
        cost.grid(row=2, column=2)
        Label(root5, text="Цена").grid(row=2, column=1)
        ids = Combobox(root5, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            if cost.get().isdigit():
                t = Dealership1.update_car(ids.get(), cost.get())
                output.insert("0.0", str(t) + "\n")
                root5.destroy()
            else:
                if not cost.get().isdigit():
                    validator(cost)
                info = "WARNING: Некорректные параметры запроса, поле должны содержать только цифры\n"
                print(info)
                output.insert(END, info)
        Button(root5, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def update_lorry_limits_btn():
        # Окно для изменения грузоподъемность
        root6 = Toplevel(roota)
        root6.title("Change weight limit")
        root6.geometry('250x100+200+200')
        root6.resizable(width=False, height=False)
        root6.grab_set()
        # поля ввода для добавления записи в бд
        id_lorry = Entry(root6, width=20)
        id_lorry.grid(row=1, column=2)
        Label(root6, text="Идентификатор").grid(row=1, column=1)
        weight_limit = Entry(root6, width=20)
        weight_limit.grid(row=2, column=2)
        Label(root6, text="Грузоперевозка").grid(row=2, column=1)

        def ok_btn():
            if weight_limit.get().isdigit():
                t = Dealership1.update_lorry(id_lorry.get(), weight_limit.get())
                output.insert("0.0", str(t) + "\n")
                root6.destroy()
            else:
                validator(weight_limit)
                info = "WARNING: Поле 'Грузоперевозка' может содержать только цифры\n"
                print(info)
                output.insert(END, info)
        Button(root6, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root6, text="Отмена", width=10, height=1, command=root6.destroy).grid(row=9, column=2)
        root6.mainloop()

    def del_car_btn():
        # Окно для ввода id записи для удаления
        root5 = Toplevel(roota)
        root5.title("Delete car")
        # задаем координаты и размеры для вывода окна
        root5.geometry('250x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        options = Dealership1.retrive_from_one_db('cars', 'id_car', 'car_model')
        # поля ввода для удаления записи из бд
        Label(root5, text="Идентификатор").grid(row=1, column=1)
        ids = Combobox(root5, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.delete_car(id_car)
            output.insert("0.0", str(t) + "\n")
            root5.destroy()

        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def del_lorry_btn():
        # Окно для ввода id записи для удаления
        root5 = Toplevel(roota)
        root5.title("Delete Lorry")
        root5.geometry('250x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        # поля ввода для удаления записи из бд
        options = Dealership1.retrive_from_2_tables()
        ids = Combobox(root5, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)
        Label(root5, text="Идентификатор").grid(row=1, column=1)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.delete_lorry(id_car)
            output.insert("0.0", str(t) + "\n")
            root5.destroy()
        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def adminka():
        root5 = Toplevel(roota)
        root5.title("User manager")
        root5.geometry('300x100+200+200')
        root5.resizable(width=True, height=False)
        root5.grab_set()
        log = Entry(root5, width=20)
        log.grid(row=1, column=2)
        Label(root5, text="login").grid(row=1, column=1)
        pwd = Entry(root5, width=20)
        pwd.grid(row=2, column=2)
        Label(root5, text='password').grid(row=2, column=1)
        role = Entry(root5, width=20)
        role.grid(row=3, column=2)
        Label(root5, text='role (0-1-2)').grid(row=3, column=1)
        def ok_btn():
            h = pwd.get().encode()
            h = hashlib.md5(h)
            if re.match(r"^[A-Z]\w*[a-z]{1,3}$", pwd.get()) and role.get().isdigit():
                t = Dealership1.create_user(log.get(), h.hexdigest(), role.get())
                output.insert("0.0", str(t) + "\n")
                root5.destroy()
            else:
                info = "WARNING: Пароль может состоять из цифр и букв, но первый символ пароля всегда должен быть " \
                       "заглавной буквой, а последний строчкой буквой. А роль - цифры: 0 - админ, 1 - пользователь с " \
                       "правами на редактирование, 2 - пользователь с правами на просмотр \n"
                output.insert(END, info)
        Button(root5, text="Create", width=10, height=1, command=ok_btn).grid(row=4, column=2)
        print_users_btn()
        root5.mainloop()

    def del_user():
        root5 = Toplevel(roota)
        root5.title("Delete user")
        root5.minsize(300, 30)
        root5.geometry('300x60+200+200')
        root5.resizable(width=True, height=False)
        root5.grab_set()
        id_user = Entry(root5, width=10)
        id_user.grid(row=1, column=2)
        Label(root5, text="ID").grid(row=1, column=1)

        def ok_btn():

            if id_user.get().isdigit():
                t = Dealership1.del_user(id_user.get())
                output.insert("0.0", str(t) + "\n")
                root5.destroy()
            else:
                info = "WARNING: ID - только цифры \n"
                output.insert(END, info)
        Button(root5, text="Remove", width=10, height=1, command=ok_btn).grid(row=4, column=2)
        print_users_btn()
        root5.mainloop()

    def print_users_btn():
        # очистить окно вывода
        output.delete('1.0', END)
        texts = Dealership1.printer_users()
        output.insert('1.0', " {:<3} {:<10} {:<35} {:<10}".format("ID", "Login", "Password", "Role\n"))
        roles = {0: 'admin', 1: 'manager', 2: 'for read'}
        for line in texts:
            output.insert(END, "\n {:<3} {:<10} {:<35} {:<10}".format(str(line[0]), str(line[1]), str(line[2]), roles[int(line[3])]))
        output.insert(END, "\n\n Total amount of users:{}\n".format(len(texts)))

    Button(roota, text="Add car to cars list", font="Comic", width=25, command=add_car_btn).grid(row=5, column=2)
    Button(roota, text="Add car to dealership", font="Comic", width=25, command=add_car_to_ds_btn).grid(row=6, column=2)
    Button(roota, text="Add lorry", width=25, font="Comic", command=add_lorry_btn).grid(row=7, column=2)

    # Группа кнопок для изменения данных в базе
    Button(roota, text="Change amount", bg="yellow", font="Comic", width=22, command=update_amount_btn).\
        grid(row=5, column=4)
    Button(roota, text="Change cost", bg="yellow", font="Comic", width=22, command=update_car_cost_btn).\
        grid(row=6, column=4)
    Button(roota, text="Change weight limit", font="Comic", bg="yellow", width=22, command=update_lorry_limits_btn).\
        grid(row=7, column=4)

    # Группа кнопок для удаления данных из базы
    Button(roota, text="Del car from dealership", font="Comic", bg="light blue", width=21, command=del_car_from_ds_btn).\
        grid(row=5, column=3)
    Button(roota, text="Del car from list", bg="light blue", width=21, font="Comic", command=del_car_btn).\
        grid(row=6, column=3)
    Button(roota, text="Del lorry", bg="light blue", width=21, font="Comic", command=del_lorry_btn).\
        grid(row=7, column=3)

    # Отрисовка меню бар
    menubar = Menu(roota)
    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add car - CTRL+C", command=add_car_btn)
    filemenu.add_command(label="Add lorry - CTRL+L", command=add_lorry_btn)
    filemenu.add_command(label="Add car to DL - CTRL+D", command=add_car_to_ds_btn)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=roota.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    # # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Delete car", command=del_car_btn)
    editmenu.add_command(label="Delete lorry", command=del_lorry_btn)
    editmenu.add_command(label="Delete car from DL", command=del_car_from_ds_btn)
    editmenu.add_command(label="Edit amount", command=update_amount_btn)
    editmenu.add_command(label="Edit cost", command=update_car_cost_btn)
    editmenu.add_command(label="Edit weight limit", command=update_lorry_limits_btn)
    menubar.add_cascade(label="Edit", menu=editmenu)

    adminmenu = Menu(menubar, tearoff=0)
    adminmenu.add_command(label="Create user", command=adminka)
    adminmenu.add_command(label="Remove user", command=del_user)
    adminmenu.add_command(label="Print users", command=print_users_btn)
    menubar.add_cascade(label="Manage users", menu=adminmenu)

    # display the menu
    roota.config(menu=menubar)

    output = Text(roota, bg="white", width=80, height=15, bd=3)
    output.grid(row=1, column=1, columnspan=4, padx=(4, 0))
    src = Scrollbar(roota, command=output.yview)
    output.configure(yscrollcommand=src.set)
    src.grid(row=1, column=6, sticky=NS)

    roota.mainloop()
    Dealership1.break_connection()
