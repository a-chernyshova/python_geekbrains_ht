# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import threading
import hashlib
from tkinter import *
from tkinter.ttk import Combobox as Combobox
from GUI.validator import validator
from Deal.Dealership import Dealership1


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

    def print_models_btn(self):
        # очистить окно вывода
        self.output.delete('1.0', END)
        texts = Dealership1.printer_models()
        self.output.insert("1.0", "{:<3} {:<10}".format(" №", "Model name\n"))
        n = 0
        for line in texts:
            n += 1
            self.output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_makers_btn(self):
        self.output.delete('1.0', END)
        makers = Dealership1.printer_makers()
        self.output.insert("1.0", "{:<3} {:<10}".format(" №", "Maker name\n"))
        n = 0
        for line in makers:
            n += 1
            self.output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(makers)))

    def print_car_btn(self):
        self.output.delete('1.0', END)
        texts = Dealership1.printer_car_dealership()
        self.output.insert("1.0", " {:<3}{:<18}{:<15}{:<8}{:<8}{:<3}\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
        for i in texts:
            self.output.insert(END, " {:<3}{:<18}{:<15}{:<8}{:<8}{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_not_available_car_btn(self):
        self.output.delete('1.0', END)
        cars = Dealership1.printer_not_available_car()
        self.output.insert("1.0", " {:<3}{:<18}{:<12}{:<10}\n".format("№", "Model", "Maker", "Engine"))
        n = 0
        for i in cars:
            n += 1
            self.output.insert(END, " {:<3}{:<18}{:<12}{:<10}".format(n, i[0], i[1], i[2], i[3])+"\n")
        self.output.insert(END, "\n Total amount:{}\n".format(len(cars)))

    def about(self):
        root5 = Toplevel(self.root)
        root5.title("About program")
        root5.minsize(300, 30)
        root5.resizable(width=True, height=False)
        text = Text(root5, height=15, width=70)
        root5.geometry('650x300+200+200')
        root5.grab_set()
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
        Button(root5, text="Понятно", width=10, height=1, command=root5.destroy).grid(row=2, column=2)
        self.root.mainloop()

    def export_notavailable_btn(self):
        root1 = Toplevel(self.root)
        root1.title("Export to file")
        root1.minsize(200, 70)
        root1.resizable(width=False, height=False)
        root1.geometry('250x70+200+200')
        root1.grab_set()
        filename = Entry(root1, width=20)
        filename.grid(row=1, column=2)
        Label(root1, text="File name (name.txt)").grid(row=1, column=1)
        cars = Dealership1.printer_not_available_car()
        models = Dealership1.printer_models()
        makers = Dealership1.printer_makers()

        def ok_btn():
            file = filename.get()+'.txt'
            if file:
                f = open(file, 'a+')
                thread1 = threading.Thread(target=Dealership1.export_to_file, args=('Thread1', f, cars))
                thread2 = threading.Thread(target=Dealership1.export_to_file, args=('Thread2', f, models))
                thread3 = threading.Thread(target=Dealership1.export_to_file, args=('Thread3', f, makers))
                thread1.start()
                thread2.start()
                thread3.start()
                thread1.join()
                thread2.join()
                thread3.join()
                f.close()
                root1.destroy()
            else:
                validator(filename)
        Button(root1, text="Экспортировать", width=15, height=1, command=ok_btn).grid(row=8, column=1)
        Button(root1, text="Отмена", width=15, height=1, command=root1.destroy).grid(row=8, column=2)
        root1.mainloop()

    def add_car_btn(self):
        root1 = Toplevel(self.root)
        root1.title("Add new car")
        root1.minsize(250, 200)
        root1.resizable(width=False, height=False)
        root1.geometry('250x110+200+200')
        root1.grab_set()
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
                t = Dealership1.add_car(car_model.get().capitalize(), maker.get().upper(),
                                        year_production.get(), car_engine.get(), cost.get())
                self.output.insert("0.0", str(t) + "\n")
                root1.destroy()
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
        Button(root1, text="Добавить", width=10, height=1, command=ok_btn).grid(row=8, column=1)
        Button(root1, text="Отмена", width=10, height=1, command=root1.destroy).grid(row=8, column=2)
        root1.mainloop()

    def add_lorry_btn(self):
        root2 = Toplevel(self.root)
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
                t = Dealership1.add_lorry(car_model.get().capitalize(), maker.get().upper(),
                                          year_production.get(), car_engine.get(), cost.get(), weight_limit.get())
                self.output.insert("0.0", str(t) + "\n")
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
                self.output.insert(END, info)
        Button(root2, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root2, text="Отмена", width=10, height=1, command=root2.destroy).grid(row=9, column=2)
        root2.mainloop()

    def add_car_to_ds_btn(self):
        root3 = Toplevel(self.root)
        root3.title("Add new car to dealership")
        root3.geometry('250x100+200+200')
        root3.resizable(width=False, height=False)
        root3.grab_set()
        id_car = Entry(root3, width=20)
        id_car.grid(row=1, column=2)
        Label(root3, text="Идентификатор").grid(row=1, column=1)
        amount = Entry(root3, width=20)
        amount.grid(row=2, column=2)
        Label(root3, text="Количество").grid(row=2, column=1)

        def ok_btn():
            if amount.get().isdigit() and id_car.get().isdigit():
                t = Dealership1.add_car_to_dealership(id_car.get(), amount.get())
                self.output.insert("0.0", str(t) + "\n")
                root3.destroy()
            else:
                if not amount.get().isdigit():
                    validator(amount)
                if not id_car.get().isdigit():
                    validator(id_car)
                info = "WARNING: Поля должны содержать только цифры\n"
                print(info)
                self.output.insert(END, info)
        Button(root3, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root3, text="Отмена", width=10, height=1, command=root3.destroy).grid(row=9, column=2)
        root3.mainloop()

    def update_amount_btn(self):
        root4 = Toplevel(self.root)
        root4.title("Change cars amount")
        root4.resizable(width=False, height=False)
        root4.geometry('250x100+200+200')
        root4.grab_set()
        options = Dealership1.return_dict()
        Label(root4, text="Идентификатор").grid(row=1, column=1)
        amount = Entry(root4, width=20)
        amount.grid(row=2, column=2)
        Label(root4, text="Количество").grid(row=2, column=1)
        ids = Combobox(root4, value=list(options.values()))
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.update_amount(id_car, amount.get())
            self.output.insert("0.0", str(t) + "\n")
            root4.destroy()

        Button(root4, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root4, text="Отмена", width=10, height=1, command=root4.destroy).grid(row=9, column=2)
        root4.mainloop()

    def del_car_from_ds_btn(self):
        root5 = Toplevel(self.root)
        root5.title("Delete car from dealership")
        root5.geometry('300x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        options = Dealership1.return_dict()
        Label(root5, text="Идентификатор").grid(row=1, column=1)
        ids = Combobox(root5, value=list(options.values()), width=18)
        ids.grid(row=1, column=2)

        def ok_btn():
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.delete_car_from_dealership(id_car)
            self.output.insert("0.0", str(t) + "\n")
            root5.destroy()
        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def update_car_cost_btn(self):
        root5 = Toplevel(self.root)
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
            x = ids.get()
            for key, value in options.items():
                if value == x:
                    id_car = key
            t = Dealership1.update_car(id_car, cost.get())
            self.output.insert("0.0", str(t) + "\n")
            root5.destroy()
        Button(root5, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def update_lorry_limits_btn(self):
        root6 = Toplevel(self.root)
        root6.title("Change weight limit")
        root6.geometry('250x100+200+200')
        root6.resizable(width=False, height=False)
        root6.grab_set()
        id_lorry = Entry(root6, width=20)
        id_lorry.grid(row=1, column=2)
        Label(root6, text="Идентификатор").grid(row=1, column=1)
        weight_limit = Entry(root6, width=20)
        weight_limit.grid(row=2, column=2)
        Label(root6, text="Грузоперевозка").grid(row=2, column=1)

        def ok_btn():
            if weight_limit.get().isdigit():
                t = Dealership1.update_lorry(id_lorry.get(), weight_limit.get())
                self.output.insert("0.0", str(t) + "\n")
                root6.destroy()
            else:
                validator(weight_limit)
                info = "WARNING: Поле 'Грузоперевозка' может содержать только цифры\n"
                print(info)
                self.output.insert(END, info)
        Button(root6, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root6, text="Отмена", width=10, height=1, command=root6.destroy).grid(row=9, column=2)
        root6.mainloop()

    def del_car_btn(self):
        root5 = Toplevel(self.root)
        root5.title("Delete car")
        root5.geometry('250x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
        dict1 = Dealership1.retrive_from_one_db('cars', 'id_car', 'car_model')
        dict2 = Dealership1.retrive_from_2_tables()
        for key, value in dict2.items():
            dict1.pop(key)
        options = dict1
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
            self.output.insert("0.0", str(t) + "\n")
            root5.destroy()

        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def del_lorry_btn(self):
        root5 = Toplevel(self.root)
        root5.title("Delete Lorry")
        root5.geometry('250x100+200+200')
        root5.resizable(width=False, height=False)
        root5.grab_set()
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
            self.output.insert("0.0", str(t) + "\n")
            root5.destroy()
        Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def search_model_btn(self):
        root5 = Toplevel(self.root)
        root5.title("Search model")
        root5.minsize(250, 100)
        root5.resizable(width=False, height=False)
        root5.geometry('250x100+200+200')
        root5.grab_set()
        model = Entry(root5, width=20)
        model.grid(row=1, column=2)
        Label(root5, text="Модель").grid(row=1, column=1)

        def ok_btn():
            self.output.delete('1.0', END)
            self.output.insert("1.0", "Результаты поиска\n")
            texts = Dealership1.search_car_model(model.get())
            if texts:
                self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}"
                                   "\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                for i in texts:
                    self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}"
                                       "{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                root5.destroy()
            else:
                info = "WARNING: По запросу '%s' ничего не найдено\n" % model.get()
                print(info)
                self.output.insert(END, info)
        Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def search_maker_btn(self):
        root5 = Toplevel()
        root5.title("Search maker")
        root5.minsize(250, 100)
        root5.resizable(width=False, height=False)
        root5.grab_set()
        root5.geometry('250x100+200+200')
        maker = Entry(root5, width=20)
        maker.grid(row=1, column=2)
        Label(root5, text="Производитель").grid(row=1, column=1)

        def ok_btn():
            if maker.get().isalpha():
                self.output.delete('1.0', END)
                self.output.insert("1.0", "Результаты поиска\n")
                texts = Dealership1.search_car_maker(maker.get())
                if texts:
                    self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}"
                                       "\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                    for i in texts:
                        self.output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}"
                                           "{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                        root5.destroy()
                    self.output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                else:
                    self.output.insert(END, "По запросу '{}' ничего не найдено.\n".format(maker.get()))
            else:
                info = "WARNING: Некорректный запрос в поле 'Производитель'\n"
                print(info)
                self.output.insert(END, info)

        Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def adminka(self):
        root5 = Toplevel(self.root)
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
                self.output.insert("0.0", str(t) + "\n")
                root5.destroy()
            else:
                info = "WARNING: Пароль может состоять из цифр и букв, но первый символ " \
                       "пароля всегда должен быть заглавной буквой, а последний строчкой буквой. " \
                       "А роль - цифры: 0 - админ, 1 - пользователь с " \
                       "правами на редактирование, 2 - пользователь с правами на просмотр \n"
                self.output.insert(END, info)
        Button(root5, text="Create", width=10, height=1, command=ok_btn).grid(row=4, column=2)
        self.print_users_btn()
        root5.mainloop()

    def del_user(self):
        root5 = Toplevel(self.root)
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
                self.output.insert("0.0", str(t) + "\n")
                root5.destroy()
            else:
                info = "WARNING: ID - только цифры \n"
                self.output.insert(END, info)
        Button(root5, text="Remove", width=10, height=1, command=ok_btn).grid(row=4, column=2)
        self.print_users_btn()
        root5.mainloop()

    def print_users_btn(self):
        self.output.delete('1.0', END)
        texts = Dealership1.printer_users()
        self.output.insert('1.0', " {:<3} {:<10} {:<35} {:<10}".format("ID", "Login", "Password", "Role\n"))
        roles = {0: 'admin', 1: 'manager', 2: 'for read'}
        for line in texts:
            self.output.insert(END, "\n {:<3} {:<10} {:<35} "
                               "{:<10}".format(str(line[0]), str(line[1]), str(line[2]), roles[int(line[3])]))
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
        Dealership1.break_connection()
