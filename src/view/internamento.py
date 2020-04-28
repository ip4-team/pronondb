import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from .templates import *


class Internamento(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = 'Internamento'

        paciente_values = controller.get_rows_ids('Paciente')

        fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'DataEntrada':  {'label': 'Data de Entrada (dd/mm/aaaa)',
                             'entry': DateEntry},
            'DiaAlta':      {'label': 'Data de Alta',
                             'entry': DateEntry},
            'Motivo':       {'label': 'Motivo',
                             'entry': ttk.Entry},
        }

        main_page = Menu(self, controller, self.table_name, fields)
