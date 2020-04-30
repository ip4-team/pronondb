import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from ..templates import Menu


class TipoTratamento(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        fields = {
            'Nome':        {'label': 'Nome do tratamento',
                             'entry': ttk.Entry}
        }

        main_page = Menu(self, controller, self.table_name, fields)

