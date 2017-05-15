# -*- coding: utf-8 -*-
from tkinter import *
from GUI.default import DefaultInterface
from Deal.DealershipDAO import Dealership_object


class Reader(DefaultInterface):

    def __init__(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Read only")
        self.root.minsize(100, 300)
        self.root.resizable(width=False, height=True)
        self.root.geometry('780x200+100+110')
        self.output = Text(self.root, bg="white", width=70, height=15, bd=3)
        self.output.grid(row=1, column=2, rowspan=7, padx=(4, 0))
        self.src = Scrollbar(self.root, command=self.output.yview)
        self.output.configure(yscrollcommand=self.src.set)
        self.src.grid(row=1, column=6, sticky=NS)

    def gui(self):
        btn_print_models = Button(self.root, text="Models list", width=18,  font="Comic",
                                  command=self.print_models_btn)
        btn_print_models.grid(row=1, column=1)
        Button(self.root, text="Makers list", width=18, font="Comic", command=self.print_makers_btn).\
            grid(row=2, column=1)
        Button(self.root, text="Cars list", width=18, font="Comic", command=self.print_car_btn).\
            grid(row=3, column=1)

        Button(self.root, text="Search model", bg="light blue", font="Comic", width=18,
               command=self.search_model_btn).grid(row=4, column=1)
        Button(self.root, text="Search maker", bg="light blue", font="Comic", width=18,
               command=self.search_maker_btn).grid(row=5, column=1)
        Button(self.root, text="Not available cars", font="Comic", bg="light blue", width=18,
               command=self.print_not_available_car_btn).grid(row=6, column=1)

        menubar = Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Print all cars", command=self.print_car_btn)
        filemenu.add_command(label="Export to file", command=self.export_notavailable_btn)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

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
        Dealership_object.close_connection()
