import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
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
        self.fields = {
            'HospitalOrigem':   {'label': 'Hospital de Origem',
                                 'entry': ttk.Entry},
            'ProntuarioOrigem': {'label': 'Prontuario de Origem',
                                 'entry': ttk.Entry},
            'Sexo':             {'label': 'Sexo',
                                 'entry': ttk.Combobox,
                                 'value': ['Feminino', 'Masculino']},
                                 #  'value': [('Feminino', 'feminino'),
                                 #            ('Masculino', 'masculino')]},
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
                ent = entry(row, state='readonly', values=self.fields[key]['value'])
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

        result = self.controller.send_query('Paciente',
                                            tuple(column_names),
                                            tuple(query_values)
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
