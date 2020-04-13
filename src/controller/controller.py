import re
import datetime

import tkinter as tk
from tkinter import ttk
#  import tkinter. as messagebox

from model.model import Model
from view.view import *
from view.paciente import *


class Controller(tk.Tk):
    def __init__(self, model):
        self.model = model

        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Paciente, CadastrarPaciente):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.start_page = 'StartPage'
        self.show_frame('StartPage')

    def run(self):
        self.title("Pronon DB test")
        self.geometry('800x600')
        style = ttk.Style(self)
        style.theme_use('clam')
        self.deiconify()
        self.mainloop()

    def show_frame(self, page_name):
        #  for frame in self.frames.values():
        #      frame.grid_remove()
        frame = self.frames[page_name]
        frame.tkraise()

    def get_startpage(self):
        return self.start_page

    def send_query(self, table, columns, query_values):
        message = 'INSERT into `' + table + '` ' + str(columns) + ' VALUES '
        nr_values = tuple(['%s' for s in query_values])
        message = message + str(nr_values)
        message = message.replace("'", "")

        return self.model.insert(message, query_values)

    def handler(self, error_type, code, message):
        if error_type == 1:
            tk.messagebox.showwarning(title="Mysql Aviso", message=str(code)+': '+message)

        if error_type == 2:
            tk.messagebox.showerror(title="Mysql Erro", message=str(code)+': '+message)
