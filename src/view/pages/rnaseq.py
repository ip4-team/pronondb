import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from ..templates import *


class RNASeq(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        paciente_values = controller.get_rows_ids('Paciente')
        amostra_values = controller.get_rows_ids('AmostraRNA')

        fields = {
            'idPaciente':   {'label': 'Pacientes',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'idAmostraRNA':    {'label': 'Amostras',
                             'entry': ttk.Combobox,
                             'value': amostra_values},
            'Metodo':       {'label': 'Metodo utilizado',
                            'entry': ttk.Combobox,
                            'value':['Transcriptoma total',
                                     'Ampliseq',
                                     'SMART3seq']},
            'DataPreparo':  {'label': 'Data de preparo (dd/mm/aaaa)',
                             'entry': DateEntry},
            'DataCorrida':  {'label': 'Data da corrida',
                             'entry': DateEntry},
            'Barcode':      {'label': 'Barcode',
                             'entry': ttk.Entry},
            'NomeRegistroIon': {'label': 'Nome registrado no Ion',
                                'entry': ttk.Entry},
            'Qualidade':    {'label': 'Qualidade do sequenciamento *TODO',
                             'entry': ttk.Entry}
        }

        main_page = Menu(self, controller, self.table_name, fields)

