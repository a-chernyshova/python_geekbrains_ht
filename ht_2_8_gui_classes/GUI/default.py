# -*- coding: utf-8 -*-
import threading
import hashlib
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox as Combobox
from GUI.validator import validator
from Deal.DealershipDAO import Dealership_object


class DefaultInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Car dealership")
        self.root.minsize(100, 300)
        self.root.resizable(width=False, height=True)
        self.root.geometry('910x350+100+110')
        self.output = Text(self.root, bg="white", width=110, height=15, bd=3)
        self.output.grid(row=1, column=1, columnspan=5, padx=(4, 0))
        self.src = Scrollbar(self.root, command=self.output.yview)
        self.output.configure(yscrollcommand=self.src.set)
        self.src.grid(row=1, column=6, sticky=NS)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            Dealership_object.close_connection()

    def manage_buttons(self, window, command, name1, row1, row2, column1, column2):
        Button(window, text=name1, width=10, height=1, command=command).grid(row=row1, column=column1)
        Button(window, text='Cancel', width=10, height=1, command=window.destroy).grid(row=row2, column=column2)

    def params_modal_window(self, window, name, width, height):
        window.title(name)
        window.resizable(width=False, height=False)
        window.geometry('{}x{}+200+200'.format(width, height))
        window.grab_set()

    def print_models_btn(self):
        # clear output before show new information
        self.output.delete('0.0', END)
        texts = Dealership_object.printer_models()
        self.output.insert("1.0", "{:<3} {:<10}".format(" №", "Model name\n"))
        n = 0
        for line in texts:
            n += 1
            self.output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_makers_btn(self):
        self.output.delete('1.0', END)
        makers = Dealership_object.printer_makers()
        self.output.insert("1.0", "{:<3} {:<10}".format(" №", "Maker name\n"))
        n = 0
        for line in makers:
            n += 1
            self.output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(makers)))

    def print_car_btn(self):
        self.output.delete('1.0', END)
        texts = Dealership_object.printer_car_dealership()
        self.output.insert("1.0", " {:<3}{:<18}{:<15}{:<8}{:<8}{:<3}\n".
                           format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
        for i in texts:
            self.output.insert(END, " {:<3}{:<18}{:<15}{:<8}{:<8}{:<3}".
                               format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_not_available_car_btn(self):
        self.output.delete('1.0', END)
        cars = Dealership_object.printer_not_available_car()
        self.output.insert("1.0", " {:<3}{:<18}{:<12}{:<10}\n".
                           format("№", "Model", "Maker", "Engine"))
        n = 0
        for i in cars:
            n += 1
            self.output.insert(END, " {:<3}{:<18}{:<12}{:<10}".
                               format(n, i[0], i[1], i[2], i[3])+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(cars)))

    def about(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "About program", 650, 300)
        text = Text(modal_window, height=15, width=70)

        text.insert(INSERT, "Задание:\nПредметная область – автосалон. "
                            "\nРазработать класс Car_dealership, описывающий работу автосалона."
                            "\nРазработать класс Car, автомобиль описывается следующими параметрами:"
                            "\nуникальный идентификатор,"
                            "\nмарка автомобиля, "
                            "\nстрана-производитель, "
                            "\nгод выпуска, "
                            "\nобъём двигателя,"
                            "\nстоимость."
                            "\nРазработать класс Lorry на базе класс Car, грузовик характеризуется: "
                            "\nвесовым ограничение перевозки\n"
                            "\nВыполнил: Чернышова Анастасия")
        text.grid(row=1, column=1)
        Button(modal_window, text="Got it", width=10, height=1, command=modal_window.destroy).grid(row=2, column=2)
        self.root.mainloop()

    def export_notavailable_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Export to file", 250, 70)

        filename = Entry(modal_window, width=20)
        filename.grid(row=1, column=2)
        Label(modal_window, text="File name (name.txt)").grid(row=1, column=1)

        cars = Dealership_object.printer_not_available_car()
        models = Dealership_object.printer_models()
        makers = Dealership_object.printer_makers()

        def ok_btn():
            file = filename.get()+'.txt'
            if file:
                f = open(file, 'a+')
                thread1 = threading.Thread(target=Dealership_object.export_to_file, args=('Thread1', f, cars))
                thread2 = threading.Thread(target=Dealership_object.export_to_file, args=('Thread2', f, models))
                thread3 = threading.Thread(target=Dealership_object.export_to_file, args=('Thread3', f, makers))
                thread1.start()
                thread2.start()
                thread3.start()
                thread1.join()
                thread2.join()
                thread3.join()
                f.close()
                modal_window.destroy()
            else:
                validator(filename)
        self.manage_buttons(modal_window, ok_btn, 'Export', 8, 8, 1, 2)
        modal_window.mainloop()

    def add_car_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Add new car", 250, 160)

        car_model = Entry(modal_window, width=20)
        car_model.grid(row=2, column=2)

        Label(modal_window, text="Название модели").grid(row=2, column=1)
        maker = Entry(modal_window, width=20)
        maker.grid(row=3, column=2)

        Label(modal_window, text="Производитель").grid(row=3, column=1)
        year_production = Entry(modal_window, width=20)
        year_production.grid(row=4, column=2)
        Label(modal_window, text="Год выпуска").grid(row=4, column=1)
        car_engine = Entry(modal_window, width=20)
        car_engine.grid(row=5, column=2)
        Label(modal_window, text="Объем двигателя").grid(row=5, column=1)
        cost = Entry(modal_window, width=20)
        cost.grid(row=6, column=2)
        Label(modal_window, text="Стоимость").grid(row=6, column=1)

        def ok_btn():
            if year_production.get().isdigit() and cost.get().isdigit() and maker.get().isalpha():
                t = Dealership_object.add_car(car_model.get().capitalize(), maker.get().upper(),
                                              year_production.get(), car_engine.get(), cost.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                if not year_production.get().isdigit():
                    validator(year_production)

                if not cost.get().isdigit():
                    validator(cost)

                if not maker.get().isalpha():
                    validator(maker)

                info = "WARNING: Поля цена, год выпуска должны сожержать цифры; " \
                       "производитель - только буквы\n"
                print(info)
                self.output.insert(END, info)
        self.manage_buttons(modal_window, ok_btn, 'Add', 8, 8, 1, 2)
        modal_window.mainloop()

    def add_lorry_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Add new Lorry", 250, 200)

        car_model = Entry(modal_window, width=20)
        car_model.grid(row=2, column=2)
        Label(modal_window, text="Model").grid(row=2, column=1)
        maker = Entry(modal_window, width=20)
        maker.grid(row=3, column=2)
        Label(modal_window, text="Maker").grid(row=3, column=1)
        year_production = Entry(modal_window, width=20)
        year_production.grid(row=4, column=2)
        Label(modal_window, text="Год выпуска").grid(row=4, column=1)
        car_engine = Entry(modal_window, width=20)
        car_engine.grid(row=5, column=2)
        Label(modal_window, text="Объем двигателя").grid(row=5, column=1)
        cost = Entry(modal_window, width=20)
        cost.grid(row=6, column=2)
        Label(modal_window, text="Cost").grid(row=6, column=1)
        weight_limit = Entry(modal_window, width=20)
        weight_limit.grid(row=7, column=2)
        Label(modal_window, text="Грузовой лимит").grid(row=7, column=1)

        def ok_btn():
            if year_production.get().isdigit() and cost.get().isdigit() and \
                    weight_limit.get().isdigit():
                t = Dealership_object.add_lorry(car_model.get().capitalize(), maker.get().upper(),
                                          year_production.get(), car_engine.get(), cost.get(), weight_limit.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                if not year_production.get().isdigit():
                    validator(year_production)
                if not cost.get().isdigit():
                    validator(cost)
                if not weight_limit.get().isdigit():
                    validator(weight_limit)

                info = "WARNING: Поля id, цена, год выпуска и весовые ограничения должны сожержать цифры\n"
                print(info)
                self.output.insert(END, info)

        self.manage_buttons(modal_window, ok_btn, 'Add', 9, 9, 1, 2)
        modal_window.mainloop()

    def add_car_to_ds_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Add new car to dealership", 250, 100)

        id_car = Entry(modal_window, width=20)
        id_car.grid(row=1, column=2)
        Label(modal_window, text="ID").grid(row=1, column=1)
        amount = Entry(modal_window, width=20)
        amount.grid(row=2, column=2)
        Label(modal_window, text="Amount").grid(row=2, column=1)

        def ok_btn():
            if amount.get().isdigit() and id_car.get().isdigit():
                t = Dealership_object.add_car_to_dealership(id_car.get(), amount.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                if not amount.get().isdigit():
                    validator(amount)
                if not id_car.get().isdigit():
                    validator(id_car)
                info = "WARNING: Поля должны содержать только цифры\n"
                print(info)
                self.output.insert(END, info)
        self.manage_buttons(modal_window, ok_btn, 'Add', 9, 9, 1, 2)
        modal_window.mainloop()

    def update_amount_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Change cars amount", 250, 100)

        Label(modal_window, text="ID").grid(row=1, column=1)
        amount = Entry(modal_window, width=20)
        amount.grid(row=2, column=2)
        Label(modal_window, text="Amount").grid(row=2, column=1)
        options = Dealership_object.return_dict()
        ids = Combobox(modal_window, value=list(options.values()))
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership_object.update_amount(id_car, amount.get())
            self.output.insert("0.0", str(t) + "\n")
            modal_window.destroy()

        self.manage_buttons(modal_window, ok_btn, 'Save', 9, 9, 1, 2)
        modal_window.mainloop()

    def del_car_from_ds_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Delete car from dealership", 250, 50)

        options = Dealership_object.return_dict()
        Label(modal_window, text="ID", width=15).grid(row=1, column=1)
        ids = Combobox(modal_window, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership_object.delete_car_from_dealership(id_car)
            self.output.insert("0.0", str(t) + "\n")
            modal_window.destroy()

        self.manage_buttons(modal_window, ok_btn, 'Delete', 9, 9, 1, 2)
        modal_window.mainloop()

    def update_car_cost_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Change cost", 250, 100)

        options = Dealership_object.retrive_from_one_db('cars', 'id_car', 'car_model')
        Label(modal_window, text="ID").grid(row=1, column=1)
        cost = Entry(modal_window, width=20)
        cost.grid(row=2, column=2)
        Label(modal_window, text="Cost").grid(row=2, column=1)
        ids = Combobox(modal_window, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership_object.update_car(id_car, cost.get())
            self.output.insert("0.0", str(t) + "\n")
            modal_window.destroy()
        self.manage_buttons(modal_window, ok_btn, 'Save', 9, 9, 1, 2)
        modal_window.mainloop()

    def update_lorry_limits_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Change weight limit", 250, 100)

        options = Dealership_object.retrive_from_2_tables()
        id_lorry = Combobox(modal_window, value=list(options.values()), width=17)
        id_lorry.grid(row=1, column=2)
        Label(modal_window, text="ID", width=15).grid(row=1, column=1)

        weight_limit = Entry(modal_window, width=20)
        weight_limit.grid(row=2, column=2)
        Label(modal_window, text="Weight limits").grid(row=2, column=1)

        def ok_btn():
            if weight_limit.get().isdigit():
                t = Dealership_object.update_lorry(id_lorry.get(), weight_limit.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                validator(weight_limit)
                info = "WARNING: Поле 'Weight limits' может содержать только цифры\n"
                print(info)
                self.output.insert(END, info)
        self.manage_buttons(modal_window, ok_btn, 'Save', 9, 9, 1, 2)
        modal_window.mainloop()

    # can choose car which is not in dealership table
    def del_car_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Delete car", 250, 50)
        options = Dealership_object.retrive_cars_only()
        Label(modal_window, text="ID", width=15).grid(row=1, column=1)
        ids = Combobox(modal_window, value=list(options.values()), width=17)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership_object.delete_car(id_car)
            self.output.insert("0.0", str(t) + "\n")
            modal_window.destroy()
        self.manage_buttons(modal_window, ok_btn, 'Delete', 9, 9, 1, 2)
        modal_window.mainloop()

    def del_lorry_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Delete Lorry", 250, 50)

        options = Dealership_object.retrive_from_2_tables()
        ids = Combobox(modal_window, value=list(options.values()), width=17)
        ids.grid(row=1, column=2)
        Label(modal_window, text="ID", width=15).grid(row=1, column=1)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership_object.delete_lorry(id_car)
            self.output.insert("0.0", str(t) + "\n")
            modal_window.destroy()

        self.manage_buttons(modal_window, ok_btn, 'Delete', 9, 9, 1, 2)
        modal_window.mainloop()

    def search_model_btn(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, 'Search model', 250, 100)

        model = Entry(modal_window, width=20)
        model.grid(row=1, column=2)
        Label(modal_window, text="Модель").grid(row=1, column=1)

        def ok_btn():
            self.output.delete('1.0', END)
            self.output.insert('1.0', "Search results\n")
            texts = Dealership_object.search_car_model(model.get())
            if texts:
                self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}"
                                   "\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                for i in texts:
                    self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}"
                                       "{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                modal_window.destroy()
            else:
                info = "WARNING: По запросу '%s' ничего не найдено\n" % model.get()
                print(info)
                self.output.insert(END, info)

        self.manage_buttons(modal_window, ok_btn, 'Search', 9, 9, 1, 2)
        modal_window.mainloop()

    def search_maker_btn(self):
        modal_window = Toplevel()
        self.params_modal_window(modal_window, "Search maker", 250, 100)

        maker = Entry(modal_window, width=20)
        maker.grid(row=1, column=2)
        Label(modal_window, text="Производитель").grid(row=1, column=1)

        def ok_btn():
            if maker.get().isalpha():
                self.output.delete('1.0', END)
                self.output.insert("1.0", "Результаты поиска\n")
                texts = Dealership_object.search_car_maker(maker.get())
                if texts:
                    self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}"
                                       "\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                    for i in texts:
                        self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}"
                                           "{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                        modal_window.destroy()
                    self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                else:
                    self.output.insert(END, "По запросу '{}' ничего не найдено.\n".format(maker.get()))
            else:
                info = "WARNING: Некорректный запрос в поле 'Производитель'\n"
                print(info)
                self.output.insert(END, info)

        self.manage_buttons(modal_window, ok_btn, "Search", 9, 9, 1, 2)
        modal_window.mainloop()

    def adminka(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, 'Users manager', 300, 100)

        login = Entry(modal_window, width=20)
        login.grid(row=1, column=2)
        Label(modal_window, width=15, text="Login").grid(row=1, column=1)
        pwd = Entry(modal_window, width=20)
        pwd.grid(row=2, column=2)
        Label(modal_window, text='Password').grid(row=2, column=1)
        options = ['ADMIN', 'MANAGER', 'READER']
        role = Combobox(modal_window, width=17, value=list(options))
        role.grid(row=3, column=2)
        Label(modal_window, text='Role').grid(row=3, column=1)

        def ok_btn():
            h = pwd.get().encode()
            h = hashlib.md5(h)
            if re.match(r"^[A-Z]\w*[a-z]{1,2}$", pwd.get()):
                t = Dealership_object.create_user(login.get(), h.hexdigest(), role.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                info = "WARNING: Пароль может состоять из цифр и букв, но первый символ " \
                       "пароля всегда должен быть заглавной буквой, а последний строчкой буквой.\n"
                self.output.insert(END, info)

        self.manage_buttons(modal_window, ok_btn, 'Create', 4, 4, 1, 2)
        self.print_users_btn()
        modal_window.mainloop()

    def del_user(self):
        modal_window = Toplevel(self.root)
        self.params_modal_window(modal_window, "Delete user", 250, 50)

        id_user = Entry(modal_window, width=10)
        id_user.grid(row=1, column=2)
        Label(modal_window, width=15, text="ID").grid(row=1, column=1)

        def ok_btn():

            if id_user.get().isdigit():
                t = Dealership_object.del_user(id_user.get())
                self.output.insert("0.0", str(t) + "\n")
                modal_window.destroy()
            else:
                info = "WARNING: ID - только цифры \n"
                self.output.insert(END, info)
        self.manage_buttons(modal_window, ok_btn, 'Remove', 4, 4, 1, 2)
        self.print_users_btn()
        modal_window.mainloop()

    def print_users_btn(self):
        self.output.delete('1.0', END)
        texts = Dealership_object.printer_users()
        self.output.insert('1.0', " {:<3} {:<10} {:<35} {:<10}".format("ID", "Login", "Password", "Role\n"))
        for line in texts:
            self.output.insert(END, "\n {:<3} {:<10} {:<35} "
                               "{:<10}".format(str(line[0]), str(line[1]), str(line[2]), str(line[3])))
        self.output.insert(END, "\n\n Total amount of users:{}\n".format(len(texts)))

    def gui(self):
        # Группа кнопок для вывода информации на экран
        btn_print_models = Button(self.root, text="Models list", width=10,  font="Comic", command=self.print_models_btn)
        btn_print_models.grid(row=5, column=1)
        Button(self.root, text="Makers list", width=10, font="Comic", command=self.print_makers_btn).\
            grid(row=6, column=1)
        Button(self.root, text="Cars list", width=10, font="Comic", command=self.print_car_btn).\
            grid(row=7, column=1)

        # Группа кнопок для добавления данных в базу
        Button(self.root, text="Add car to cars list", bg="grey", font="Comic", width=18, command=self.add_car_btn).\
            grid(row=5, column=2)
        Button(self.root, text="Add car to dealership", font="Comic", bg="grey", width=18,
               command=self.add_car_to_ds_btn).grid(row=6, column=2)
        Button(self.root, text="Add lorry", bg="grey", width=18, font="Comic", command=self.add_lorry_btn).\
            grid(row=7, column=2)

        # Группа кнопок для изменения данных в базе
        Button(self.root, text="Change amount", bg="yellow", font="Comic", width=18,
               command=self.update_amount_btn).grid(row=5, column=4)
        Button(self.root, text="Change cost", bg="yellow", font="Comic",
               width=18, command=self.update_car_cost_btn).grid(row=6, column=4)
        Button(self.root, text="Change weight limit", font="Comic", bg="yellow", width=18,
               command=self.update_lorry_limits_btn).grid(row=7, column=4)

        # Группа кнопок для удаления данных из базы
        Button(self.root, text="Del car from dealership", font="Comic", bg="red", width=18,
               command=self.del_car_from_ds_btn).grid(row=5, column=3)
        Button(self.root, text="Del car from list", bg="red", width=18, font="Comic", command=self.del_car_btn).\
            grid(row=6, column=3)
        Button(self.root, text="Del lorry", bg="red", width=18, font="Comic", command=self.del_lorry_btn).\
            grid(row=7, column=3)

        # Остальные команды - поиск и вывод не доступных в автосалоне машин
        Button(self.root, text="Search model", bg="light blue", font="Comic",
               width=18, command=self.search_model_btn).grid(row=5, column=5)
        Button(self.root, text="Search maker", bg="light blue", font="Comic",
               width=18, command=self.search_maker_btn).grid(row=6, column=5)
        Button(self.root, text="Not available cars", font="Comic", bg="light blue", width=18,
               command=self.print_not_available_car_btn).grid(row=7, column=5)

        menubar = Menu(self.root)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About  - F1", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        adminmenu = Menu(menubar, tearoff=0)
        adminmenu.add_command(label="Create user", command=self.adminka)
        adminmenu.add_command(label="Remove user", command=self.del_user)
        adminmenu.add_command(label="Print users", command=self.print_users_btn)
        menubar.add_cascade(label="Manage users", menu=adminmenu)

        self.root.config(menu=menubar)
        self.root.mainloop()
        Dealership_object.close_connection()
