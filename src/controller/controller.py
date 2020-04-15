import re
import datetime

import tkinter as tk
from tkinter import ttk

from model.model import Model
from view.view import *
#  from view.paciente import *
#  from view.amostra import *


class Controller(tk.Tk):
    def __init__(self, model):
        self.model = model

        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.container.pack(side='top', fill='both', expand=True)
        #  self.statusbar = Statusbar(container, self)
        self.toolbar = Toolbar(self.container, self)
        self.navbar = Navbar(self.container, self)
        self.main = Main(self.container, self)

        #  self.statusbar.pack(side='bottom', fill='x')
        self.toolbar.pack(side='top', fill='x')
        self.navbar.pack(side='left', fill='y')

        self.main.pack(side='right', fill='both', expand=True)
        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)


    def run(self):
        self.title("Pronon DB test")
        self.geometry('800x600')
        style = ttk.Style(self)
        style.theme_use('clam')
        self.deiconify()
        self.mainloop()

    def show_frame(self, page_name):
        self.main.destroy()

        # create the new page and pack it in the container
        cls = globals()[page_name]
        self.main = cls(self.container, self)
        self.main.pack(fill="both", expand=True)

    def send_query(self, command, table, columns, query_values=None):
        if command == 'INSERT':
            message = 'INSERT into `' + table + \
                '` ' + str(columns) + ' VALUES '
            nr_values = tuple(['%s' for s in query_values])
            message = message + str(nr_values)
            message = message.replace("'", "")
            return_value = self.model.insert(message, query_values)

        if command == 'SELECT':
            #  if query_values:
                # TODO: Make queries with WHERE statment
            message = 'SELECT ' + str(columns) + ' FROM ' + table
            #  message = message.replace("'", "")
            return_value = self.model.select(message)

        return return_value

    def handler(self, error_type, code, message):
        if error_type == 1:
            tk.messagebox.showwarning(
                title="Mysql Aviso", message=str(code)+': '+message)

        if error_type == 2:
            tk.messagebox.showerror(
                title="Mysql Erro", message=str(code)+': '+message)
