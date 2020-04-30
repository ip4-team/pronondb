import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from ..templates import *


class Coleta(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        paciente_values = controller.get_rows_ids('Paciente')

        fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'Data':         {'label': 'Data da coleta (dd/mm/aaaa)',
                             'entry': DateEntry},
            'DiaTratamento':{'label': 'Dia do tratamento',
                             'entry': DateEntry},
            'MaterialColetado': {'label': 'Material coletado',
                             'entry': ttk.Entry}
        }

        main_page = Menu(self, controller, self.table_name, fields)
