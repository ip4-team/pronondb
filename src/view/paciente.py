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

        self.register = Register(self, controller, fields)
        self.update = Update(self, controller, fields)
        self.delete = Delete(self, controller, fields)

        self.buttonframe = tk.Frame(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.buttonframe.place(in_=container, x=0, y=0,
                               relwidth=1, relheight=1)

        self.register.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.update.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.delete.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

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
                                   command=partial(self.select_id, self.delete))
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
