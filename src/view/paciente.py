import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from functools import partial
from tkcalendar import Calendar, DateEntry

from datetime import datetime


class Paciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.register = CadastrarPaciente(self, controller)
        self.update = AtualizarPaciente(self, controller)
        #  self.delete = RemoverPaciente(self, controller)

        self.buttonframe = tk.Frame(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.buttonframe.place(in_=container, x=0, y=0,
                               relwidth=1, relheight=1)

        self.register.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.update.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.initUI()

    def initUI(self):
        self.buttonframe.lift()
        register_button = ttk.Button(self.buttonframe, text="Cadastrar Paciente",
                                     command=self.register.lift)
        register_button.pack()

        update_button = ttk.Button(self.buttonframe, text="Atualizar dados do Paciente",
                                   command=self.update.lift)
        update_button.pack()

        remove_button = ttk.Button(self.buttonframe, text="Remover Paciente",
                                   command=self.initUI)
        remove_button.pack()

    def raise_parent(self):
        self.buttonframe.lift()


class CadastrarPaciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.table_name = 'Paciente'
        self.fields = {
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

            if entry_type == DateEntry and text != None:
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
            self.exit(entries)

    def exit(self, entries):
        self.refresh(entries)
        self.parent.raise_parent()

    def refresh(self, entries):
        for entry in entries:
            if entry[2] == ttk.Radiobutton or entry[2] == ttk.Combobox:
                entry[1].set('')
            else:
                entry[1].delete(0, 'end')


class AtualizarPaciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.table_name = 'Paciente'

        table_values = self.controller.send_query('SELECT',
                                                  self.table_name,
                                                  '*')

        ids = [x['idPaciente'] for x in table_values[2]]
        for row in ids:
            print(row)

        #  selected_id = self.get_id(ids)

        self.fields = {
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
        ents = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=partial(self.exit, ents))
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=partial(self.callback, ents))
        query_button.pack(side=tk.RIGHT, padx=5)

    def get_id(self, ids):
        #  self.parent.wm_attributes('-disabled', True)

        self.toplevel_dialog = tk.Toplevel(self)
        self.toplevel_dialog.minsize(300, 100)

        self.toplevel_dialog.transient(self)

        self.toplevel_dialog.protocol('WM_DELETE_WINDOW', self.close_toplevel)

        self.toplevel_dialog_label = ttk.Label(
            self.toplevel_dialog, text="Do you want to enable my parent window again?")
        self.toplevel_dialog_label.pack(side='top')

        self.toplevel_dialog_yes_button = ttk.Button(
            self.toplevel_dialog, text='Yes', command=self.close_toplevel)
        self.toplevel_dialog_yes_button.pack(side='left', fill='x', expand=True)

        self.toplevel_dialog_no_button = ttk.Button(
            self.toplevel_dialog, text='No')
        self.toplevel_dialog_no_button.pack(side='right', fill='x', expand=True)

    def close_toplevel(self):
        #  self.parent.wm_attributes('-disabled', False)
        self.toplevel_dialog.destroy()
        #  self.deiconify()

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

            if entry_type == DateEntry and text != None:
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
            self.exit(entries)

    def exit(self, entries):
        self.refresh(entries)
        self.parent.raise_parent()

    def refresh(self, entries):
        for entry in entries:
            if entry[2] == ttk.Radiobutton or entry[2] == ttk.Combobox:
                entry[1].set('')
            else:
                entry[1].delete(0, 'end')
