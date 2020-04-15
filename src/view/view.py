import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

from tkinter import LEFT, TOP, X, FLAT, RAISED
from functools import partial
from .paciente import *
from .amostra import *


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Page", font=('Arial', 12))
        label.pack()


class Navbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, relief=tk.RIDGE, borderwidth=3)

        button2 = ttk.Button(self, text="Paciente",
                            command=lambda: controller.show_frame('Paciente'))
        button2.pack(fill='x')

        button = ttk.Button(self, text="Amostra",
                           command=lambda: controller.show_frame('CadastrarAmostra'))
        button.pack(fill='x')


class Toolbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent, relief=tk.RIDGE, borderwidth=3)
        label = ttk.Label(self, text="PRONON DB", font=('Arial', 12))
        label.pack()
