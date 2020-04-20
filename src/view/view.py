import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

from tkinter import LEFT, TOP, X, FLAT, RAISED
from functools import partial
from .paciente import Paciente
from .amostra import Amostra
from .coleta import Coleta


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

        amostra_button = ttk.Button(self, text="Amostra",
                           command=lambda: controller.show_frame('Amostra'))
        amostra_button.pack(fill='x')


class Toolbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent, relief=tk.RIDGE, borderwidth=3)
        label = ttk.Label(self, text="PRONON DB", font=('Arial', 12))
        label.pack()
