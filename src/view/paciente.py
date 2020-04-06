import tkinter as tk
import tkinter.messagebox as messagebox

from functools import partial
from tkcalendar import Calendar, DateEntry


class Paciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)


class CadastrarPaciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        fields = {
                  'HospitalOrigem':   {'label': 'Hospital de Origem',
                                       'entry': tk.Entry},
                  'ProntuarioOrigem': {'label': 'Prontuario de Origem',
                                       'entry': tk.Entry},
                  'Sexo':             {'label': 'Sexo',
                                       'entry': tk.Entry},
                  'DataNascimento':   {'label': 'Data de Nascimento',
                                       'entry': DateEntry},
                  'Pais':             {'label': 'Pais',
                                       'entry': tk.Entry},
                  'Estado':           {'label': 'Estado',
                                       'entry': tk.Entry},
                  'Municipio':        {'label': 'Municipio',
                                       'entry': tk.Entry},
                  'TipoAtendimento':  {'label': 'Tipo de Atendimento',
                                       'entry': tk.Entry},
                  'TipoParto':        {'label': 'Tipo de Parto',
                                       'entry': tk.Entry},
                  'Lactante':         {'label': 'Lactante',
                                       'entry': tk.Entry},
                  'Etnia':            {'label': 'Etnia',
                                       'entry': tk.Entry}
                 }

        #  inputs = (tk.Entry, tk.Entry, (), DateEntry, tk.Entry, tk.Entry,
        #            tk.Entry, tk.Entry, tk.Entry, tk.Entry, tk.Entry,)
        ents = self.make_form(fields)

        # Send Query button
        back_button = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(
            self.controller.get_startpage()))
        back_button.pack(side=tk.LEFT)

        query_button = tk.Button(self, text="Salvar",
                                 command=partial(self.callback, ents))
        query_button.pack(side=tk.RIGHT, padx=5)

    def make_form(self, fields):
        entries = []
        for key in fields:
            label_text = fields[key]['label']
            entry = fields[key]['entry']

            row = tk.Frame(self)
            lab = tk.Label(row, width=25, text=label_text, anchor='w')
            ent = entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT, padx=15)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            entries.append((key, ent))
        return entries

    def callback(self, entries):
        query_values = []
        column_names = []
        for entry in entries:
            key = entry[0]
            column_names.append(key)
            text = entry[1].get()
            query_values.append(text)

        state = self.controller.send_query('Paciente',
                                           tuple(column_names),
                                           tuple(query_values)
                                           )
