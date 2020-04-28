import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import ScrolledText
from functools import partial

from .templates import *


class InfoMicroBiologica(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        coleta_values = controller.get_rows_ids('Coleta')

        fields = {
            'idPaciente':   {'label': 'Coleta',
                             'entry': ttk.Combobox,
                             'value': coleta_values},
            'DataCultura': {'label': 'Data da cultura',
                                'entry': DateEntry},
            'Microrganismo': {'label': 'Microorganismo identificado',
                                'entry': ttk.Entry},
            'FonteAmostra': {'label': 'Fonte da amostra',
                                        'entry': ttk.Combobox,
                                        'value':['Sangue',
                                                 'Veia periferica',
                                                 'Cateter central',
                                                 'DTTP > 2h', 'DTTP < 2h',
                                                 'DTTP desconhecido',
                                                 'Ponta de cateter',
                                                 'Líquido perineural',
                                                 'Outro líquido estéril',
                                                 'Líquor',
                                                 'Escarro',
                                                 'Aspirado traqueal',
                                                 'Outro aspirado',
                                                 'BAL',
                                                 'Outro lavado',
                                                 'Urina',
                                                 'Biópsia',
                                                 'Outro']}
        }

        main_page = Menu(self, controller, self.table_name, fields)
