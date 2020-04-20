import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from .templates import *


class Amostra(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = 'Amostra'

        paciente_values = self.get_rows('Paciente')
        coleta_values = self.get_rows('Coleta')

        fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'idColeta': {'label': 'Coleta',
                         'entry': ttk.Combobox,
                         'value': coleta_values},
            'DataExtracao':     {'label': 'Data de Extração (dd/mm/aaaa)',
                                'entry': DateEntry},
            'Caixa':            {'label': 'Caixa',
                                 'entry': ttk.Entry},
            'PosicaoCaixa':     {'label': 'Posicao da caixa',
                                'entry': ttk.Entry},
            'Freezer':          {'label': 'Freezer',
                                 'entry': ttk.Entry},
            'ConcentracaoNanovue':          {'label': 'Concentração aferida no nanovue',
                                             'entry': ttk.Entry},
            'DataNanovue':      {'label': 'Data de medida da concentração de nanovue',
                                 'entry': DateEntry},
            'ConcentracaoQubit':{'label': 'Concentração aferida no qubit',
                                 'entry': ttk.Entry},
            'DataQubit':        {'label': 'Data de medida da concentração de qubit',
                                 'entry': DateEntry},
        }

        main_page = Menu(self, controller, self.table_name, fields)
        #  main_page.pack(fill=tk.BOTH, expand=True)

    def get_rows(self, table):
        table_values = self.controller.send_query('SELECT',
                                                  table,
                                                  '*')
        ids = [x['id'+table] for x in table_values[2]]

        return ids
