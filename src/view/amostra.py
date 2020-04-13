import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from functools import partial
from tkcalendar import Calendar, DateEntry


class CadastrarAmostra(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.table_name = 'Amostra'
        self.fields = {
            'idPaciente':   {'label': 'Paciente',
                             'entry': ttk.Combobox,
                             'value': ['1']},
            'idColeta': {'label': 'Coleta',
                         'entry': ttk.Combobox,
                         'value': ['1']},
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
        ents = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=partial(self.exit, ents))
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=partial(self.callback, ents))
        query_button.pack(side=tk.RIGHT, padx=5)

    def make_form(self):
        entries = []
        for key in self.fields:
            label_text = self.fields[key]['label']
            entry = self.fields[key]['entry']

            row = tk.Frame(self)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            lab = ttk.Label(row, width=35, text=label_text, anchor='w')
            lab.pack(side=tk.LEFT, padx=15)

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                ent = tk.StringVar()
                ent.set('')
                for v in self.fields[key]['value']:
                    _ent = entry(row, text=v[0], value=v[1], variable=ent)
                    _ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='readonly',
                            values=self.fields[key]['value'])
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy')
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent, entry))
        return entries

    def callback(self, entries):
        query_values = []
        column_names = []
        for entry in entries:
            key = entry[0]
            text = entry[1].get()
            entry_type = entry[2]

            if text == '':
                text = None

            if entry_type == DateEntry:
                date = text.split('/')
                text = date[2] + '/' + date[1] + '/' + date[0]

            column_names.append(key)
            query_values.append(text)

        result = self.controller.send_query('INSERT',
                                            self.table_name,
                                            tuple(column_names),
                                            query_values=tuple(query_values)
                                            )
        if result[0]:
            self.controller.handler(*result)

        if not result[0]:
            tk.messagebox.showinfo(message="Paciente cadastrado com sucesso!")
            self.refresh(entries)
            self.controller.show_frame(self.controller.get_startpage())

    def exit(self, entries):
        self.refresh(entries)
        self.controller.show_frame(self.controller.get_startpage())

    def refresh(self, entries):
        for entry in entries:
            if entry[2] == ttk.Radiobutton or entry[2] == ttk.Combobox:
                entry[1].set('')
            else:
                entry[1].delete(0, 'end')
