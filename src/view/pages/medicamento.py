import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from ..templates import *


class Medicamento(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        paciente_values = controller.get_rows_ids('Paciente')
        tipotratamento_values = controller.get_rows_ids('TipoTratamento')

        fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'TipoTratamento':   {'label': 'Tipo de Tratamento',
                                   'entry': ttk.Entry},
            'Nome':        {'label': 'Nome do medicamento',
                             'entry': ttk.Entry},
            'DataInicio':   {'label': 'Data de inicio (dd/mm/aaaa)',
                             'entry': DateEntry},
            'DataTermino':  {'label': 'Data de termino',
                             'entry': DateEntry},
        }

        main_page = Menu(self, controller, self.table_name, fields)
