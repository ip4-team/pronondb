import re
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar

from model.model import Model
from view.view import *


class Controller(tk.Tk):
    def __init__(self, ip, db):
        self.ip = ip
        self.db = db
        tk.Tk.__init__(self)

        self.title("Pronon DB test")
        self.geometry('800x600')
        style = ttk.Style(self)
        style.theme_use('clam')

        self.make_layout()

        self.check_credentials()

        self.mainloop()

    def check_credentials(self):
        # TODO:  <04-05-20> Change this when deploy! #
        #  credentials_modal = Dialog(self)
        #  user, pswd = credentials_modal.show()
        user = 'gabriel'
        pswd = 'olescki'

        if user == '' and pswd == '':
            self.handler(2, 1, "Erro: Usuário e senha não podem ser vazios")
            self.destroy()
            return

        self.model = Model(self.ip, user, pswd, self.db)
        result, code, message = self.model.con_check()
        if result:
            self.handler(result, code, message)
            self.destroy()
            return
        else:
            tk.messagebox.showinfo("Sucesso!", "Conexão com o banco de dados foi um sucesso!")

        self.user = user
        self.pswd = pswd

    def make_layout(self):
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

        if command != 'SELECT':
            self.insert_log(command, message, query_values, table)

        return return_value

    def insert_log(self, command, query, query_values, table):
        query = query.replace('%s, ', '')
        splitted_query = query.split(' ')
        splitted_query[-1] = query_values
        final_query = str(splitted_query)

        time = datetime.datetime.now()
        time_str = time.strftime('%Y-%d-%m %H:%M:%S')

        message = 'INSERT into LogPreenchimento (Comando, Query, Tabela, Data, Nome) VALUES (%s, %s, %s, %s, %s)'
        log_values = (command, final_query, table, time_str, self.user)
        print(log_values)
        return_value = self.model.insert(message, log_values)
        print(return_value)

    def handler(self, error_type, code, message):
        if error_type == 1:
            tk.messagebox.showwarning(
                title="Mysql Aviso", message=str(code)+': '+message)

        if error_type == 2:
            tk.messagebox.showerror(
                title="Mysql Erro", message=str(code)+': '+message)

    def get_rows_ids(self, table):
        table_values = self.send_query('SELECT', table, '*')
        ids = [x['id'+table] for x in table_values[2]]

        return ids

