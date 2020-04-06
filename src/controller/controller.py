import re
import datetime

import tkinter as tk

from model.model import Model
from view.view import *
from view.paciente import *


class Controller(tk.Tk):
    def __init__(self, model):
        self.model = model

        tk.Tk.__init__(self)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Paciente, CadastrarPaciente):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.start_page = StartPage
        self.show_frame(StartPage)

    def run(self):
        self.title("Pronon DB test")
        self.geometry("800x600")
        self.deiconify()
        self.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_startpage(self):
        return self.start_page;

    def send_query(self, table, columns, query_values):
        message = 'INSERT into `' + table + '` ' + str(columns) + ' VALUES '
        nr_values = tuple(['%s' for s in query_values])
        message = message + str(nr_values)
        message = message.replace("'", "")

        return self.model.insert(message, query_values)

    def check_date(self, date):
        time_format = re.compile('^\d{2}.\d{2}.\d{4}$')
        date_okay = None
        if (date) and (time_format.match(date)):
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
            try:
                datetime.datetime(year, month, day)
                date_okay = True
            except:
                date_okay = False

        return date_okay
