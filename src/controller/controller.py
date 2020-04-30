import re
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar

from model.model import Model
from view.view import *


class Controller(tk.Tk):
    def __init__(self, ip, db):
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

        # TODO:  <30-04-20, make inputs for user and pswd> #
        self.model = Model(ip, user, pswd, db)
        self.run()

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

    def send_query(self, command, table, columns, query_values=None, where=None, where_values=None):
        return_value = 3, '?', 'MySQL command not found'

        if command == 'INSERT':
            message = 'INSERT into `' + table + \
                '` ' + str(columns) + ' VALUES '
            nr_values = tuple(['%s' for s in query_values])
            message = message + str(nr_values)
            message = message.replace("'", "")
            return_value = self.model.insert(message, query_values)

        if command == 'SELECT':
            where_stat = ''
            if where:
                nr_values = tuple(['%s' for s in where])
                where_stat = ' WHERE ' + str(where) + '=' + where_values
            message = 'SELECT ' + str(columns) + ' FROM ' + table + where_stat
            return_value = self.model.select(message)

        if command == 'UPDATE':
            set_stat = ''
            for column in columns:
                set_stat = set_stat + column+'=%s, '
            set_stat = set_stat[:-2]

            where_stat = ' WHERE ' + str(where) + '=' + where_values
            message = 'UPDATE ' + table + ' SET ' + set_stat + where_stat

            return_value = self.model.update(message, query_values)

        if command == 'DELETE':
            where_stat = ' WHERE ' + str(where) + '=' + where_values
            message = 'DELETE from ' + table + where_stat

            return_value = self.model.delete(message)

        return return_value

    def handler(self, error_type, code, message):
        if error_type == 1:
            tk.messagebox.showwarning(
                title="Mysql Aviso", message=str(code)+': '+message)

        if error_type == 2:
            tk.messagebox.showerror(
                title="Mysql Erro", message=str(code)+': '+message)

    def get_rows_ids(self, table):
        table_values = self.send_query('SELECT',
                                                  table,
                                                  '*')
        ids = [x['id'+table] for x in table_values[2]]

        return ids

