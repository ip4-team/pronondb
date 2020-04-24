import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from .templates import *


class Teste(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = 'Teste'

        paciente_values = controller.get_rows_ids('Paciente')
        amostra_values = controller.get_rows_ids('Amostra')

        fields = {
            'idPaciente':   {'label': 'Pacientes',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'idAmostra':    {'label': 'Amostras',
                             'entry': ttk.Combobox,
                             'value': amostra_values},
            'TesteRealizado': {'label': 'Teste realizado',
                             'entry': ttk.Entry},
            'Data':         {'label': 'Data do teste (dd/mm/aaaa)',
                             'entry': DateEntry}
        }

        main_page = Menu(self, controller, self.table_name, fields)

