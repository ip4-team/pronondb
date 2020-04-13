import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

from tkinter import LEFT, TOP, X, FLAT, RAISED
from functools import partial
from .paciente import *


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=('Verdana', 12))
        label.pack(side='top', fill=tk.X, pady=10)

        #  button.focus_set()

        button2 = tk.Button(self, text="Cadastrar Paciente",
                            command=lambda: controller.show_frame('CadastrarPaciente'))
        button2.pack()


        button = tk.Button(self, text="Cadastrar Amostra",
                           command=lambda: controller.show_frame('CadastrarAmostra'))
        button.pack()
