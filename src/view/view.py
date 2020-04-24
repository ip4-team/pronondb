import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

from tkinter import LEFT, TOP, X, FLAT, RAISED
from functools import partial
from .paciente import Paciente
from .coleta import Coleta
from .diagnostico import Diagnostico
from .amostra import Amostra
from .teste import Teste
from .infoclinica import InfoClinica


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Page", font=('Arial', 12))
        label.pack()


class Navbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, relief=tk.RIDGE, borderwidth=3)

        paciente_button = ttk.Button(self, text="Paciente",
                            command=lambda: controller.show_frame('Paciente'))
        paciente_button.pack(fill='x')

        coleta_button = ttk.Button(self, text="Coleta",
                           command=lambda: controller.show_frame('Coleta'))
        coleta_button.pack(fill='x')

        diagnostico_button = ttk.Button(self, text="Diagnostico",
                           command=lambda: controller.show_frame('Diagnostico'))
        diagnostico_button.pack(fill='x')

        amostra_button = ttk.Button(self, text="Amostra",
                           command=lambda: controller.show_frame('Amostra'))
        amostra_button.pack(fill='x')

        teste_button = ttk.Button(self, text="Teste",
                           command=lambda: controller.show_frame('Teste'))
        teste_button.pack(fill='x')

        infoclinica_button = ttk.Button(self, text="Infos. Clínicas",
                           command=lambda: controller.show_frame('InfoClinica'))
        infoclinica_button.pack(fill='x')


class Toolbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent, relief=tk.RIDGE, borderwidth=3)
        label = ttk.Label(self, text="PRONON DB", font=('Arial', 12))
        label.pack()
