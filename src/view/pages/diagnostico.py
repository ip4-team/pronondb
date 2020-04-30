import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial

from ..templates import *


class Diagnostico(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        paciente_values = controller.get_rows_ids('Paciente')

        fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': paciente_values},
            'TipoLeucemia': {'label': 'Tipo de Leucemia',
                             'entry': ttk.Entry},
            'Data':         {'label': 'Data da coleta (dd/mm/aaaa)',
                             'entry': DateEntry}
        }

        main_page = Menu(self, controller, self.table_name, fields)
