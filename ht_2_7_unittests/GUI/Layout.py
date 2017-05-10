# -*- coding: utf-8 -*-
import threading
from tkinter import *
from Deal.Dealership import Dealership1
from GUI.validator import validator


def markup():
    # Draw a window
    root = Tk()
    root.title("Просмотр базы данных дилерского центра")
    root.minsize(50, 90)
    root.resizable(width=False, height=True)
    output = Text(root, bg="white", width=80, height=15, bd=3)
    output.grid(row=1, column=2, rowspan=8, padx=(4, 0))
    src = Scrollbar(root, command=output.yview)
    output.configure(yscrollcommand=src.set)
    src.grid(row=1, column=6, sticky=NS)

    def print_models_btn():
        # очистить окно вывода
        output.delete('1.0', END)
        texts = Dealership1.printer_models()
        output.insert("1.0", "{:<3} {:<10}".format(" №", "Model name\n"))
        n = 0
        for line in texts:
            n += 1
            output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_makers_btn():
        output.delete('1.0', END)
        makers = Dealership1.printer_makers()
        output.insert("1.0", "{:<3} {:<10}".format(" №", "Maker name\n"))
        n = 0
        for line in makers:
            n += 1
            output.insert(END, " {:<3} {:<10}".format(n, str(line[0]))+"\n")
        output.insert(END, "\n Total amount:{}\n".format(len(makers)))

    def print_car_btn():
        output.delete('1.0', END)
        texts = Dealership1.printer_car_dealership()
        output.insert("1.0", " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
        for i in texts:
            output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
        output.insert(END, "\n Total amount:{}\n".format(len(texts)))

    def print_not_available_car_btn():
        output.delete('1.0', END)
        cars = Dealership1.printer_not_available_car()
        output.insert("1.0", " {:<3}{:<18}{:<12}{:<10}\n".format("№", "Model", "Maker", "Engine"))
        n = 0
        for i in cars:
            n += 1
            output.insert(END, " {:<3}{:<18}{:<12}{:<10}".format(n, i[0], i[1], i[2], i[3])+"\n")
        output.insert(END, "\n Total amount:{}\n".format(len(cars)))

    def export_notavailable_btn():
        root1 = Toplevel(root)
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
            file = filename.get()
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

    def search_model_btn():
        # Окно для ввода модели для поиска
        root5 = Toplevel(root)
        root5.title("Search model")
        root5.minsize(250, 100)
        root5.resizable(width=False, height=False)
        root5.geometry('250x100+200+200')
        root5.grab_set()
        # поля ввода для удаления записи из бд
        model = Entry(root5, width=20)
        model.grid(row=1, column=2)
        Label(root5, text="Модель").grid(row=1, column=1)

        def ok_btn():
            output.delete('1.0', END)
            output.insert("1.0", "Результаты поиска\n")
            texts = Dealership1.search_car_model(model.get())
            if texts:
                output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                for i in texts:
                    output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                root5.destroy()
            else:
                info = "WARNING: По запросу '%s' ничего не найдено\n" % model.get()
                print(info)
                output.insert(END, info)
        Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def search_maker_btn():
        # Окно для ввода производителя для поиска
        root5 = Toplevel()
        root5.title("Search maker")
        root5.minsize(250, 100)
        root5.resizable(width=False, height=False)
        root5.grab_set()
        root5.geometry('250x100+200+200')
        # поля ввода для удаления записи из бд
        maker = Entry(root5, width=20)
        maker.grid(row=1, column=2)
        Label(root5, text="Производитель").grid(row=1, column=1)

        def ok_btn():
            if maker.get().isalpha():
                output.delete('1.0', END)
                output.insert("1.0", "Результаты поиска\n")
                texts = Dealership1.search_car_maker(maker.get())
                if texts:
                    output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}\n".format("ID", "Model", "Maker", "Engine", "Cost", "Amount"))
                    for i in texts:
                        output.insert(END, " {:<3}{:<18}{:<10}{:<8}{:<8}{:<3}".format(i[0], i[1], i[2], i[3], i[4], i[5])+"\n")
                        root5.destroy()
                    output.insert(END, "\n Total amount:{}\n".format(len(texts)))
                else:
                    output.insert(END, "По запросу '{}' ничего не найдено.\n".format(maker.get()))
            else:
                info = "WARNING: Некорректный запрос в поле 'Производитель'\n"
                print(info)
                output.insert(END, info)

        Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
        Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
        root5.mainloop()

    def about():
        root5 = Toplevel(root)
        root5.title("About program")
        root5.minsize(300, 30)
        root5.resizable(width=True, height=False)
        text = Text(root5, height=15, width=70)
        root5.geometry('650x300+200+200')
        root5.grab_set()
        text.insert(INSERT, "Задание:\nПредметная область – автосалон. \nРазработать класс Car_dealership, описывающий работу "
                            "автосалона.\nРазработать класс Car, автомобиль описывается следующими параметрами:\nуникальный"
                            "идентификатор,\nмарка автомобиля, \nстрана-производитель, \nгод выпуска, \nобъём двигателя,\n"
                            "стоимость.\nРазработать класс Lorry на базе класс Car, грузовик характеризуется: \nвесовым "
                            "ограничение перевозки\n\nВыполнил: Чернышова Анастасия")
        text.grid(row=1, column=1)
        Button(root5, text="Понятно", width=10, height=1, command=root5.destroy).grid(row=2, column=2)
        root.mainloop()

    # Группа кнопок для вывода информации на экран
    btn_print_models = Button(root, text="Models list", width=18,  font="Comic", command=print_models_btn)
    btn_print_models.grid(row=1, column=1)
    Button(root, text="Makers list", width=18, font="Comic", command=print_makers_btn).\
        grid(row=2, column=1)
    Button(root, text="Cars list", width=18, font="Comic", command=print_car_btn).\
        grid(row=3, column=1)

    # Остальные команды - поиск и вывод не доступных в автосалоне машин
    Button(root, text="Search model", bg="light blue", font="Comic", width=18, command=search_model_btn).\
        grid(row=4, column=1)
    Button(root, text="Search maker", bg="light blue", font="Comic", width=18, command=search_maker_btn).\
        grid(row=5, column=1)
    Button(root, text="Not available cars", font="Comic", bg="light blue", width=18, command=print_not_available_car_btn)\
        .grid(row=6, column=1)

    # Отрисовка меню бар
    menubar = Menu(root)
    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Print all cars", command=print_car_btn)
    filemenu.add_command(label="Export to file", command=export_notavailable_btn)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    # search
    searchmenu = Menu(menubar, tearoff=0)
    searchmenu.add_command(label="Search model", command=search_model_btn)
    searchmenu.add_command(label="Search maker", command=search_maker_btn)
    menubar.add_cascade(label="Search", menu=searchmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About  - F1", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)
    root.mainloop()
    Dealership1.break_connection()
