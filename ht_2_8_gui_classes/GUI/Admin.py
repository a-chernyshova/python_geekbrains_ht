# -*- coding: utf-8 -*-
from tkinter import *
from GUI.default import DefaultInterface
from Deal.DealershipDAO import Dealership_object


class Admin(DefaultInterface):

    def __init__(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Adminka")
        self.root.minsize(100, 300)
        self.root.resizable(width=False, height=True)
        self.root.geometry('680x350+100+110')
        self.output = Text(self.root, bg="white", width=80, height=15, bd=3)
        self.output.grid(row=1, column=1, columnspan=3, padx=(4, 0))
        self.src = Scrollbar(self.root, command=self.output.yview)
        self.output.configure(yscrollcommand=self.src.set)
        self.src.grid(row=1, column=6, sticky=NS)

    # CR: Move all subsets of commands to separate, self-explainable functions
    def gui(self):
        Button(self.root, text="Add car to cars list", bg="light blue", font="Comic", width=20,
               command=self.add_car_btn).grid(row=5, column=1)
        Button(self.root, text="Add car to dealership", font="Comic", bg="light blue", width=20,
               command=self.add_car_to_ds_btn).grid(row=6, column=1)
        Button(self.root, text="Add lorry", bg="light blue", width=20, font="Comic", command=self.add_lorry_btn).\
            grid(row=7, column=1)

        # Button set to change data in db
        Button(self.root, text="Change amount", bg="yellow", font="Comic", width=20,
               command=self.update_amount_btn).grid(row=5, column=2)
        Button(self.root, text="Change cost", bg="yellow", font="Comic",
               width=20, command=self.update_car_cost_btn).grid(row=6, column=2)
        Button(self.root, text="Change weight limit", font="Comic", bg="yellow", width=20,
               command=self.update_lorry_limits_btn).grid(row=7, column=2)

        # Buttons set to remove data from db
        Button(self.root, text="Del car from dealership", font="Comic", bg="red", width=20,
               command=self.del_car_from_ds_btn).grid(row=5, column=3)
        Button(self.root, text="Del car from list", bg="red", width=20, font="Comic", command=self.del_car_btn).\
            grid(row=6, column=3)
        Button(self.root, text="Del lorry", bg="red", width=20, font="Comic", command=self.del_lorry_btn).\
            grid(row=7, column=3)

        # Show menu bar
        menubar = Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add car - CTRL+C", command=self.add_car_btn)
        filemenu.add_command(label="Add lorry - CTRL+L", command=self.add_lorry_btn)
        filemenu.add_command(label="Add car to DL - CTRL+D", command=self.add_car_to_ds_btn)
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

        adminmenu = Menu(menubar, tearoff=0)
        adminmenu.add_command(label="Create user", command=self.adminka)
        adminmenu.add_command(label="Remove user", command=self.del_user)
        adminmenu.add_command(label="Print users", command=self.print_users_btn)
        menubar.add_cascade(label="Manage users", menu=adminmenu)

        # display the menu
        self.root.config(menu=menubar)
        self.root.mainloop()
        Dealership_object.close_connection()
