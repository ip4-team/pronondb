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

        self.table_name = 'Paciente'

        self.initUI()

    def initUI(self):
        self.buttonframe.lift()
        register_button = ttk.Button(self.buttonframe, text="Cadastrar " + self.table_name,
                                     command=self.register.lift)
        register_button.pack()

        update_button = ttk.Button(self.buttonframe, text="Atualizar " + self.table_name,
                                   command=partial(self.select_id, self.update))
        update_button.pack()

        remove_button = ttk.Button(self.buttonframe, text="Remover " + self.table_name,
                                   command=self.initUI)
        remove_button.pack()

    def select_id(self, slave):
        table_values = self.controller.send_query('SELECT',
                                                  self.table_name,
                                                  '*')

        self.ids = [x['idPaciente'] for x in table_values[2]]

        self.modal = tk.Toplevel(self)
        self.modal.minsize(300, 100)
        self.modal.grab_set()

        modal_label = ttk.Label(
            self.modal, text="Selecione o " + self.table_name)
        modal_label.pack(side=tk.TOP)

        self.modal_entry = ttk.Combobox(
            self.modal, state='readonly', values=self.ids)
        self.modal_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, padx=15)

        exit_button = ttk.Button(
            self.modal, text="Fechar", command=self.modal.destroy)
        exit_button.pack(side=tk.LEFT, padx=5, pady=5)

        send_button = ttk.Button(
            self.modal, text="Enviar", command=partial(self.raise_slave, slave))
        send_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def raise_slave(self, slave):
        slave.set_id(self.modal_entry.get())
        self.modal.destroy()
        slave.lift()

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
        self.entries = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=self.exit)
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=self.callback)
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

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, text=v[0], value=v[1], variable=ent_var)
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='readonly',
                            values=self.fields[key]['value'], variable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy',
                            textvariable=ent_var)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, textvariable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        return entries

    def callback(self):
        query_values = []
        column_names = []
        for entry in self.entries:
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
            self.exit()

    def exit(self):
        self.refresh()
        self.parent.raise_parent()

    def refresh(self):
        for entry in self.entries:
            entry[1].set('')


class AtualizarPaciente(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.selected_id = ''

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
        self.entries = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=self.exit)
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=self.callback)
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

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, text=v[0], value=v[1], variable=ent_var)
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='readonly',
                            values=self.fields[key]['value'], variable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy',
                            textvariable=ent_var)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, textvariable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        return entries

    def update_form(self):
        row_values = list(self.row.values())[1:]
        entry_objs = [x[1] for x in self.entries]
        zipped_entries = zip(self.entries, row_values)

        for entry, value in zipped_entries:
            if entry[2] == DateEntry:
                raw_date = value.strftime('%Y/%m/%d')
                date = raw_date.split('/')
                date_fix = date[2] + '/' + date[1] + '/' + date[0]
                entry[1].set(date_fix)
                continue

            entry[1].set(value)

    def callback(self):
        old_values = []
        query_values = []
        column_names = []
        row_values = list(self.row.values())[1:]
        zipped_entries = zip(self.entries, row_values)

        for entry, value in zipped_entries:
            key = entry[0]
            entry_type = entry[2]
            text = entry[1].get()

            if entry_type == DateEntry:
                value = value.strftime('%Y/%m/%d')
                date = text.split('/')
                text = date[2] + '/' + date[1] + '/' + date[0]

            if text == '':
                text = None

            if text != str(value):
                old_values.append(str(value)) 
                query_values.append(str(text))
                column_names.append(key)

        if len(old_values) == 0:
            tk.messagebox.showwarning(message="Nenhuma mudança encontrada em " + self.parent.table_name + "!")
            return
        
        confirm_message = "Os seguintes valores serão atualizados: "
        for key,old,new in zip(column_names, old_values, query_values):
            if len(old.split('/')) == 3 and len(new.split('/')) == 3:
                old_splitted = old.split('/')
                old = old_splitted[2] + '/' + old_splitted[1] + '/' + old_splitted[2]
                new_splitted = new.split('/')
                new = new_splitted[2] + '/' + new_splitted[1] + '/' + new_splitted[2]

            confirm_message = confirm_message + "\n\n" + key + " de: " + old + " para: " + new 
        confirm_message = confirm_message + "\n\n Deseja continuar?"
        confirm_response = tk.messagebox.askyesno(message=confirm_message)

        if not confirm_response:
            return

        result = self.controller.send_query('UPDATE',
                                            self.parent.table_name,
                                            column_names,
                                            query_values=query_values,
                                            where='idPaciente',
                                            where_values=self.selected_id
                                            )
        if result[0]:
            self.controller.handler(*result)

        if not result[0]:
            tk.messagebox.showinfo(message="Paciente atualizado com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.parent.raise_parent()

    def refresh(self):
        for entry in self.entries:
            entry[1].set('')

    def set_id(self, input_id):
        self.selected_id = input_id

        code, message, selected_row = self.controller.send_query('SELECT',
                                                                 self.parent.table_name,
                                                                 '*',
                                                                 where='idPaciente',
                                                                 where_values=self.selected_id)

        self.row = selected_row[0]
        self.update_form()
