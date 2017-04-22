# -*- coding: utf-8 -*-
import Deal.Dealership as Deal
import tkinter
from tkinter import *


Dealership1 = Deal.Dealership('localhost', 'dealership', 'root', 'password')
# Draw a window
root = Tk()
root.title("Car dealership")
root.minsize(100, 300)
root.resizable(width=False, height=True)


# Форматировать вывод
def print_models_btn():
    # очистить окно вывода
    output.delete('1.0', END)
    texts = Dealership1.printer_models()
    for line in texts:
        output.insert("0.0", str(line)+"\n")


def print_makers_btn():
    output.delete('1.0', END)
    makers = Dealership1.printer_makers()
    for line in makers:
        output.insert("0.0", str(line)+"\n")


def print_car_btn():
    output.delete('1.0', END)
    texts = Dealership1.printer_car_dealership()
    for line in texts:
        output.insert("0.0", str(line)+"\n")


def print_not_available_car_btn():
    cars = Dealership1.printer_not_available_car()
    for line in cars:
        output.insert("0.0", str(line)+"\n")


# закрывать окно после добавления
# дизэйблить родительское окно
def add_car_btn():
    # Окно для добавления авто
    root1 = Tk()
    root1.title("Add new car")
    root1.minsize(250, 200)
    root1.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_car = Entry(root1, width=20)
    id_car.grid(row=1, column=2)
    Label(root1, text="Идентификатор").grid(row=1, column=1)
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
        t = Dealership1.add_car(id_car.get(), car_model.get(), maker.get(), year_production.get(), car_engine.get(),
                                cost.get())
        output.insert("0.0", str(t) + "\n")

    Button(root1, text="Добавить", width=10, height=1, command=ok_btn).grid(row=8, column=1)
    Button(root1, text="Отмена", width=10, height=1, command=root1.destroy).grid(row=8, column=2)
    root1.mainloop()


def add_lorry_btn():
    # Окно для добавления лорри
    root2 = Tk()
    root2.title("Add new Lorry")
    root2.minsize(250, 200)
    root2.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_car = Entry(root2, width=20)
    id_car.grid(row=1, column=2)
    Label(root2, text="Идентификатор").grid(row=1, column=1)
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
        t = Dealership1.add_lorry(id_car.get(), car_model.get(), maker.get(), year_production.get(), car_engine.get(),
                                cost.get(), weight_limit.get())
        output.insert("0.0", str(t) + "\n")

    Button(root2, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root2, text="Отмена", width=10, height=1, command=root2.destroy).grid(row=9, column=2)
    root2.mainloop()


def add_car_to_ds_btn():
    # Окно для добавления авто дилерцентру
    root3 = Tk()
    root3.title("Add new car to dealership")
    root3.minsize(250, 100)
    root3.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_car = Entry(root3, width=20)
    id_car.grid(row=1, column=2)
    Label(root3, text="Идентификатор").grid(row=1, column=1)
    amount = Entry(root3, width=20)
    amount.grid(row=2, column=2)
    Label(root3, text="Количество").grid(row=2, column=1)

    def ok_btn():
        t = Dealership1.add_car_to_dealership(id_car.get(), amount.get())
        output.insert("0.0", str(t) + "\n")

    Button(root3, text="Добавить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root3, text="Отмена", width=10, height=1, command=root3.destroy).grid(row=9, column=2)
    root3.mainloop()


def update_amount_btn():
    # Окно для изменения кол-ва
    root4 = Tk()
    root4.title("Change cars amount")
    root4.minsize(250, 100)
    root4.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_row = Entry(root4, width=20)
    id_row.grid(row=1, column=2)
    Label(root4, text="Идентификатор").grid(row=1, column=1)
    amount = Entry(root4, width=20)
    amount.grid(row=2, column=2)
    Label(root4, text="Количество").grid(row=2, column=1)

    def ok_btn():
        t = Dealership1.update_amount(id_row.get(), amount.get())
        output.insert("0.0", str(t) + "\n")

    Button(root4, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root4, text="Отмена", width=10, height=1, command=root4.destroy).grid(row=9, column=2)
    root4.mainloop()


def del_car_from_ds_btn():
    # Окно для ввода id записи для удаления
    root5 = Tk()
    root5.title("Delete car from dealership")
    root5.minsize(300, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для удаления записи из бд
    id_row = Entry(root5, width=20)
    id_row.grid(row=1, column=2)
    Label(root5, text="Идентификатор").grid(row=1, column=1)

    def ok_btn():
        t = Dealership1.delete_car_from_dealership(id_row.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def update_car_cost_btn():
    # Окно для изменения цены авто
    root5 = Tk()
    root5.title("Change cost")
    root5.minsize(250, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_car = Entry(root5, width=20)
    id_car.grid(row=1, column=2)
    Label(root5, text="Идентификатор").grid(row=1, column=1)
    cost = Entry(root5, width=20)
    cost.grid(row=2, column=2)
    Label(root5, text="Цена").grid(row=2, column=1)

    def ok_btn():
        t = Dealership1.update_car(id_car.get(), cost.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def update_lorry_limits_btn():
    # Окно для изменения грузоподъемность
    root6 = Tk()
    root6.title("Change weight limit")
    root6.minsize(250, 100)
    root6.resizable(width=False, height=False)
    # поля ввода для добавления записи в бд
    id_lorry = Entry(root6, width=20)
    id_lorry.grid(row=1, column=2)
    Label(root6, text="Идентификатор").grid(row=1, column=1)
    weight_limit = Entry(root6, width=20)
    weight_limit.grid(row=2, column=2)
    Label(root6, text="Цена").grid(row=2, column=1)

    def ok_btn():
        t = Dealership1.update_lorry(id_lorry.get(), weight_limit.get())
        output.insert("0.0", str(t) + "\n")

    Button(root6, text="Сохранить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root6, text="Отмена", width=10, height=1, command=root6.destroy).grid(row=9, column=2)
    root6.mainloop()


def del_car_btn():
    # Окно для ввода id записи для удаления
    root5 = Tk()
    root5.title("Delete car")
    root5.minsize(250, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для удаления записи из бд
    id_car = Entry(root5, width=20)
    id_car.grid(row=1, column=2)
    Label(root5, text="Идентификатор").grid(row=1, column=1)

    def ok_btn():
        t = Dealership1.delete_car(id_car.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def del_lorry_btn():
    # Окно для ввода id записи для удаления
    root5 = Tk()
    root5.title("Delete Lorry")
    root5.minsize(250, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для удаления записи из бд
    id_car = Entry(root5, width=20)
    id_car.grid(row=1, column=2)
    Label(root5, text="Идентификатор").grid(row=1, column=1)

    def ok_btn():
        t = Dealership1.delete_lorry(id_car.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Удалить", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def search_model_btn():
    # Окно для ввода модели для поиска
    root5 = Tk()
    root5.title("Search model")
    root5.minsize(250, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для удаления записи из бд
    model = Entry(root5, width=20)
    model.grid(row=1, column=2)
    Label(root5, text="Модель").grid(row=1, column=1)

    def ok_btn():
        t = Dealership1.search_car_model(model.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def search_maker_btn():
    # Окно для ввода производителя для поиска
    root5 = Tk()
    root5.title("Search maker")
    root5.minsize(250, 100)
    root5.resizable(width=False, height=False)
    # поля ввода для удаления записи из бд
    maker = Entry(root5, width=20)
    maker.grid(row=1, column=2)
    Label(root5, text="Производитель").grid(row=1, column=1)

    def ok_btn():
        t = Dealership1.search_car_maker(maker.get())
        output.insert("0.0", str(t) + "\n")

    Button(root5, text="Поиск", width=10, height=1, command=ok_btn).grid(row=9, column=1)
    Button(root5, text="Отмена", width=10, height=1, command=root5.destroy).grid(row=9, column=2)
    root5.mainloop()


def about():
    root5 = Tk()
    root5.title("About program")
    root5.minsize(300, 30)
    root5.resizable(width=True, height=False)
    text = Text(root5, height=15, width=70)
    text.insert(INSERT, "Задание:\nПредметная область – автосалон. \nРазработать класс Car_dealership, описывающий работу "
                        "автосалона.\nРазработать класс Car, автомобиль описывается следующими параметрами:\nуникальный"
                        "идентификатор,\nмарка автомобиля, \nстрана-производитель, \nгод выпуска, \nобъём двигателя,\n"
                        "стоимость.\nРазработать класс Lorry на базе класс Car, грузовик характеризуется: \nвесовым "
                        "ограничение перевозки\n\nВыполнил: Чернышова Анастасия")
    text.grid(row=1, column=1)
    Button(root5, text="Понятно", width=10, height=1, command=root5.destroy).grid(row=2, column=2)
    root.mainloop()


# Группа кнопок для вывода информации на экран
btn_print_models = Button(root, text="Models list", width=10,  font="Comic", command=print_models_btn)
btn_print_models.grid(row=5, column=1)
btn_print_makers = Button(root, text="Makers list", width=10, font="Comic", command=print_makers_btn).\
    grid(row=6, column=1)
btn_show_all = Button(root, text="Cars list", width=10, font="Comic", command=print_car_btn).\
    grid(row=7, column=1)

# Группа кнопок для добавления данных в базу
btn_add_car = Button(root, text="Add car to cars list", bg="grey", font="Comic", width=18, command=add_car_btn).\
    grid(row=5, column=2)
btn_add_to_dealership = Button(root, text="Add car to dealership", font="Comic", bg="grey", width=18,
                               command=add_car_to_ds_btn).grid(row=6, column=2)
btn_add_lorry = Button(root, text="Add lorry", bg="grey", width=18, font="Comic", command=add_lorry_btn).\
    grid(row=7, column=2)

# Группа кнопок для изменения данных в базе
btn_update_amount = Button(root, text="Change amount", bg="yellow", font="Comic", width=18, command=update_amount_btn).\
    grid(row=5, column=4)
btn_update_cost = Button(root, text="Change cost", bg="yellow", font="Comic", width=18, command=update_car_cost_btn).\
    grid(row=6, column=4)
btn_update_lorry_limits = Button(root, text="Change weight limit", font="Comic", bg="yellow", width=18,
                                 command=update_lorry_limits_btn).grid(row=7, column=4)

# Группа кнопок для удаления данных из базы
btn_delete_car_from_ds = Button(root, text="Del car from dealership", font="Comic", bg="red", width=18,
                                command=del_car_from_ds_btn).grid(row=5, column=3)
btn_delete_car = Button(root, text="Del car from list", bg="red", width=18, font="Comic", command=del_car_btn).\
    grid(row=6, column=3)
btn_delete_lorry = Button(root, text="Del lorry", bg="red", width=18, font="Comic", command=del_lorry_btn).\
    grid(row=7, column=3)

# Остальные команды - поиск и вывод не доступных в автосалоне машин
btn_search_model = Button(root, text="Search model", bg="light blue", font="Comic", width=18, command=search_model_btn).\
    grid(row=5, column=5)
btn_search_maker = Button(root, text="Search maker", bg="light blue", font="Comic", width=18, command=search_maker_btn).\
    grid(row=6, column=5)
btn_show_unavailable = Button(root, text="Not available cars", font="Comic", bg="light blue", width=18,
                              command=print_not_available_car_btn).grid(row=7, column=5)

# Добавлены чек-боксы - просто для примера
checkbox1 = IntVar()
checkbox2 = IntVar()
che1 = Checkbutton(root, text="Первая не используемая опция", variable=checkbox1, onvalue=1, offvalue=0).\
    grid(row=13, column=2)
che2 = Checkbutton(root, text="Вторая не используемая опция", variable=checkbox2, onvalue=2, offvalue=0).\
    grid(row=13, column=4)

# Отрисовка меню бар
menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Add car - CTRL+C", command=add_car_btn)
filemenu.add_command(label="Add lorry - CTRL+L", command=add_lorry_btn)
filemenu.add_command(label="Add car to DL - CTRL+D", command=add_car_to_ds_btn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
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

output = Text(root, bg="white", width=110, height=15, bd=3)
output.grid(row=1, column=1, columnspan=5, padx=(4, 0))
src = Scrollbar(root, command=output.yview)
output.configure(yscrollcommand=src.set)
src.grid(row=1, column=6, sticky=NS)
# не работает вызов
root.bind("F1", about)

root.mainloop()
Dealership1.break_connection()

# При закрытии на крестик - не закрывает модальные окна
# bind hot keys
