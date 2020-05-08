import tkinter.messagebox as messagebox
import tkinter as tk

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from functools import partial
from datetime import datetime

from ..templates import *


class Exportar(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.selected_boxes = []
        self.init_ui()

    def init_ui(self):
        label = ttk.Label(self, text="Selecione as tabelas a serem exportadas: ", font=('Arial', 12))
        label.pack()

        row1 = ttk.Frame(self, width=60)
        row1.pack(side=tk.TOP, padx=5, pady=5)

        paciente_var = tk.IntVar()
        paciente_var.set(0)
        paciente_button = ttk.Checkbutton(self, text="Paciente",
                                          variable=paciente_var)
        paciente_button.pack(in_=row1, side='left')
        self.selected_boxes.append(('Paciente', paciente_var))

        coleta_var = tk.IntVar()
        coleta_var.set(0)
        coleta_button = ttk.Checkbutton(self, text="Coleta",
                                          variable=coleta_var)
        coleta_button.pack(in_=row1, side='left')
        self.selected_boxes.append(('Coleta', coleta_var))

        diagnostico_var = tk.IntVar()
        diagnostico_var.set(0)
        diagnostico_button = ttk.Checkbutton(self, text="Diagnostico",
                                          variable=diagnostico_var)
        diagnostico_button.pack(in_=row1, side='left')
        self.selected_boxes.append(('Diagnostico', diagnostico_var))

        row2 = ttk.Frame(self, width=20)
        row2.pack(side=tk.TOP, padx=5, pady=5)

        amostrarna_var = tk.IntVar()
        amostrarna_var.set(0)
        amostrarna_button = ttk.Checkbutton(self, text="AmostraRNA",
                                          variable=amostrarna_var)
        amostrarna_button.pack(in_=row2, side='left')
        self.selected_boxes.append(('AmostraRNA', amostrarna_var))

        teste_var = tk.IntVar()
        teste_var.set(0)
        teste_button = ttk.Checkbutton(self, text="Teste",
                                          variable=teste_var)
        teste_button.pack(in_=row2, side='left')
        self.selected_boxes.append(('Teste', teste_var))

        rnaseq_var = tk.IntVar()
        rnaseq_var.set(0)
        rnaseq_button = ttk.Checkbutton(self, text="RNASeq",
                                          variable=rnaseq_var)
        rnaseq_button.pack(in_=row2, side='left')
        self.selected_boxes.append(('RNASeq', rnaseq_var))

        row3 = ttk.Frame(self, width=20)
        row3.pack(side=tk.TOP, padx=5, pady=5)

        internamento_var = tk.IntVar()
        internamento_var.set(0)
        internamento_button = ttk.Checkbutton(self, text="Internamento",
                                          variable=internamento_var)
        internamento_button.pack(in_=row3, side='left')
        self.selected_boxes.append(('Internamento', internamento_var))

        infoclinica_var = tk.IntVar()
        infoclinica_var.set(0)
        infoclinica_button = ttk.Checkbutton(self, text="Infos. Clínicas",
                                          variable=infoclinica_var)
        infoclinica_button.pack(in_=row3, side='left')
        self.selected_boxes.append(('InfoClinica', infoclinica_var))

        infomicrobio_var = tk.IntVar()
        infomicrobio_var.set(0)
        infomicrobio_button = ttk.Checkbutton(self, text="Infos. Micro Biologica",
                                          variable=infomicrobio_var)
        infomicrobio_button.pack(in_=row3, side='left')
        self.selected_boxes.append(('InfoMicroBiologica', infomicrobio_var))

        row4 = ttk.Frame(self, width=20)
        row4.pack(side=tk.TOP, padx=5, pady=5)

        obito_var = tk.IntVar()
        obito_var.set(0)
        obito_button = ttk.Checkbutton(self, text="Obito",
                                       variable=obito_var)
        obito_button.pack(in_=row4, side='left')
        self.selected_boxes.append(('Obito', obito_var))

        medicamento_var = tk.IntVar()
        medicamento_var.set(0)
        medicamento_button = ttk.Checkbutton(self, text="Medicamento",
                                       variable=medicamento_var)
        medicamento_button.pack(in_=row4, side='left')
        self.selected_boxes.append(('Medicamento', medicamento_var))

        export_button = ttk.Button(self, text="Exportar",
                                   command=self.export_data)
        export_button.pack(padx=5, pady=15)

    def export_data(self):
        for var in self.selected_boxes:
            if var[1].get()==1:
                self.controller.export_data(var[0])
