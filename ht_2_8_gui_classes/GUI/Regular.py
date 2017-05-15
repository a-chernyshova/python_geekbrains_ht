# -*- coding: utf-8 -*-
from tkinter import *
from GUI.default import DefaultInterface
from Deal.Dealership import Dealership_object


class Manager(DefaultInterface):

    def __init__(self):
        self.root = Tk()
        self.root.title("Access for manager")
        self.root.minsize(100, 300)
        self.root.resizable(width=False, height=True)
        self.root.geometry('850x350+100+110')
        self.output = Text(self.root, bg="white", width=100, height=15, bd=3)
        self.output.grid(row=1, column=1, columnspan=5, padx=(4, 0))
        self.src = Scrollbar(self.root, command=self.output.yview)
        self.output.configure(yscrollcommand=self.src.set)
        self.src.grid(row=1, column=6, sticky=NS)

    def gui(self):
        # Группа кнопок для вывода информации на экран
        btn_print_models = Button(self.root, text="Models list", width=10,  font="Comic", command=self.print_models_btn)
        btn_print_models.grid(row=5, column=1)
        Button(self.root, text="Makers list", width=10, font="Comic", command=self.print_makers_btn).\
            grid(row=6, column=1)
        Button(self.root, text="Cars list", width=10, font="Comic", command=self.print_car_btn).\
            grid(row=7, column=1)

        # Группа кнопок для добавления данных в базу
        Button(self.root, text="Add car to cars list", bg="grey", font="Comic", width=18,
               command=self.add_car_btn).grid(row=5, column=2)
        Button(self.root, text="Add car to dealership", font="Comic", bg="grey", width=18,
               command=self.add_car_to_ds_btn).grid(row=6, column=2)
        Button(self.root, text="Add lorry", bg="grey", width=18, font="Comic",
               command=self.add_lorry_btn).grid(row=7, column=2)

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
        Button(self.root, text="Del car from list", bg="red", width=18, font="Comic",
               command=self.del_car_btn).grid(row=6, column=3)
        Button(self.root, text="Del lorry", bg="red", width=18, font="Comic",
               command=self.del_lorry_btn).grid(row=7, column=3)

        # Остальные команды - поиск и вывод не доступных в автосалоне машин
        Button(self.root, text="Search model", bg="light blue", font="Comic",
               width=18, command=self.search_model_btn).grid(row=5, column=5)
        Button(self.root, text="Search maker", bg="light blue", font="Comic",
               width=18, command=self.search_maker_btn).grid(row=6, column=5)
        Button(self.root, text="Not available cars", font="Comic", bg="light blue", width=18,
               command=self.print_not_available_car_btn).grid(row=7, column=5)

        # Отрисовка меню бар
        menubar = Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add car - CTRL+C", command=self.add_car_btn)
        filemenu.add_command(label="Add lorry - CTRL+L", command=self.add_lorry_btn)
        filemenu.add_command(label="Add car to DL - CTRL+D", command=self.add_car_to_ds_btn)
        filemenu.add_command(label="Export to file", command=self.export_notavailable_btn)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        # # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Delete car", command=self.del_car_btn)
        editmenu.add_command(label="Delete lorry", command=self.del_lorry_btn)
        editmenu.add_command(label="Delete car from DL", command=self.del_car_from_ds_btn)
        editmenu.add_command(label="Edit amount", command=self.update_amount_btn)
        editmenu.add_command(label="Edit cost", command=self.update_car_cost_btn)
        editmenu.add_command(label="Edit weight limit", command=self.update_lorry_limits_btn)
        menubar.add_cascade(label="Edit", menu=editmenu)

        # search
        searchmenu = Menu(menubar, tearoff=0)
        searchmenu.add_command(label="Search model", command=self.search_model_btn)
        searchmenu.add_command(label="Search maker", command=self.search_maker_btn)
        menubar.add_cascade(label="Search", menu=searchmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About  - F1", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.root.config(menu=menubar)
        self.root.mainloop()
        Dealership_object.break_connection()
