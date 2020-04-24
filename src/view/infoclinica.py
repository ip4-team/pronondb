import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import ScrolledText
from functools import partial

from .templates import *


class InfoClinica(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = self.__class__.__name__

        coleta_values = self.get_rows('Coleta')

        fields = {
            'idColeta':     {'label': 'Coleta',
                             'entry': ttk.Combobox,
                             'value': coleta_values},
            'DataDiagnostico': {'label': 'Data do diagnostico da infecção',
                                'entry': DateEntry},
            'Febre38':         {'label': 'Febre >= 38º',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'Hipotensao':      {'label': 'Hipotensão',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'Hipotermia':      {'label': 'Hipotermia',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'PerfusaoPeriferica':{'label': 'Perfusão periférica rui',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'DistensaoAbdominal':{'label': 'Distensao abdominal',
                                  'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'Letargia':         {'label': 'Letargia',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'Sepse':            {'label': 'Sepse',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'SepseSevera':      {'label': 'SepseSevera',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0),
                                          ('Desconhecido', 2)]},
            'OutrosSinaisClinicos': {'label': 'Outros sinais clínicos',
                                    'entry': ScrolledText},
            'ProvavelSitioInfeccioso': {'label': 'Provavel sítio infeccioso',
                                        'entry': ttk.Combobox,
                                        'value':['ICS',
                                                 'pneumonia',
                                                 'meningite',
                                                 'peritonite',
                                                 'osteomielite',
                                                 'gastroenterite',
                                                 'celulite',
                                                 'miosite',
                                                 'mucosite',
                                                 'outra']},
            'CateterPeriferico':{'label': 'Apenas catéter periférico IV',
                                'entry': ttk.Radiobutton,
                                'value': [('Sim', 1),
                                          ('Não', 0)]},
            'CVCPermanente':   {'label': 'CVC permanente',
                                'entry': ttk.Entry},
            'CVCTemporario':   {'label': 'CVC temporário',
                                'entry': ttk.Entry},
            'CateterFlebotomia':{'label': 'Cateter flebotomia',
                                'entry': ttk.Entry},
            'CateterArterial':{'label': 'Cateter arterial',
                                'entry': ttk.Entry},
            'CateterEstado':    {'label': 'Estado do cateter',
                                 'entry': ttk.Combobox,
                                 'value':['Removido e não recolocado',
                                          'Removido e recolocado em outro sítio',
                                          'Removido e recolocado por cateter guia',
                                          'Paciente sem cateter',
                                          'Não',
                                          'Desconhecido']},
            'InfeccaoTipo':       {'label': 'Tipo de infecção',
                                   'entry': ttk.Combobox,
                                   'value': ['Comunitária',
                                             'Nosocomial',
                                             'Colonização']},
            'InfeccaoNosocomial': {'label': 'Infecção nosocomial',
                                   'entry': ttk.Combobox,
                                   'value': ['Intra-hospitalar',
                                             'Ambulatorial',
                                             'Home-care',
                                             'Não']},
            'InfeccaoOrigem': {'label': 'Origem da infecção',
                                   'entry': ttk.Combobox,
                                   'value': ['Endógena',
                                             'Exógena',
                                             'Desconhecida']}
        }

        main_page = Menu(self, controller, self.table_name, fields)

    def get_rows(self, table):
        table_values = self.controller.send_query('SELECT',
                                                  table,
                                                  '*')
        ids = [x['id'+table] for x in table_values[2]]

        return ids

