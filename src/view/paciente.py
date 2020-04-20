import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial
from datetime import datetime

from .templates import *


class Paciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = 'Paciente'
        fields = {
            'HospitalOrigem':   {'label': 'Hospital de Origem',
                                 'entry': ttk.Entry},
            'ProntuarioOrigem': {'label': 'Prontuario de Origem',
                                 'entry': ttk.Entry},
            'Sexo':             {'label': 'Sexo',
                                 'entry': ttk.Radiobutton,
                                 'value': [('Feminino', 'feminino'),
                                           ('Masculino', 'masculino')]},
            'DataNascimento':   {'label': 'Data de Nascimento (dd/mm/aaaa)',
                                 'entry': DateEntry},
            'Pais':             {'label': 'Pais',
                                 'entry': ttk.Entry},
            'Estado':           {'label': 'Estado',
                                 'entry': ttk.Entry},
            'Municipio':        {'label': 'Municipio',
                                 'entry': ttk.Entry},
            'TipoAtendimento':  {'label': 'Tipo de Atendimento',
                                 'entry': ttk.Entry},
            'TipoParto':        {'label': 'Tipo de Parto',
                                 'entry': ttk.Entry},
            'Lactante':         {'label': 'Lactante',
                                 'entry': ttk.Radiobutton,
                                 'value': [('Sim', 1),
                                           ('Não', 2)]},
            'Etnia':            {'label': 'Etnia',
                                 'entry': ttk.Entry}
        }

        main_page = Menu(self, controller, self.table_name, fields)
        #  main_page.pack(fill=tk.BOTH, expand=True)
