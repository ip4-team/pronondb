import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

from tkinter import LEFT, TOP, X, FLAT, RAISED
from functools import partial

from .pages import *


class Dialog:
    def __init__(self, parent):
        self.parent = parent

        x = parent.winfo_x()
        y = parent.winfo_y()

        self.top = tk.Toplevel(parent)
        self.top.title("MySQL")
        self.top.geometry('+%d+%d' % (x + 200, y + 200))
        self.top.transient(parent)
        self.top.grab_set()
        self.top.deiconify()

        self.user_var = tk.StringVar(value='')
        user_label = ttk.Label(self.top, text="Usuário: ").pack()
        user_entry = tk.Entry(self.top, textvariable=self.user_var)
        user_entry.pack(padx=5)

        self.pswd_var = tk.StringVar(value='')
        pswd_label = ttk.Label(self.top, text="Senha: ").pack()
        pswd = tk.Entry(self.top, textvariable=self.pswd_var)
        pswd.pack(padx=5)

        enviar_button = ttk.Button(self.top, text="Enviar", command=self.top.destroy)
        enviar_button.pack(pady=5, padx=5)

    def show(self):
        self.top.focus_force()
        self.parent.wait_window(self.top)
        return self.user_var.get(), self.pswd_var.get()


class Main(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.user = ''
        self.pswd = ''
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Page", font=('Arial', 12))
        label.pack()

        self.hide_menubar()

        parent.focus_set()
        parent.bind('<Alt_L>', self.toggle_menubar)

    def show_about(self):
        pass

    def toggle_menubar(self, e):
        if self.menubar_isopen:
            self.hide_menubar()
        else:
            self.show_menubar()

    def hide_menubar(self):
        self.menubar_isopen = False

        menubar = tk.Menu(self.controller)
        self.controller.config(menu=menubar)

    def show_menubar(self):
        self.menubar_isopen = True

        menubar = tk.Menu(self.controller)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=self.controller.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Sobre", command=self.show_about)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)

        self.controller.config(menu=menubar)


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

        amostrarna_button = ttk.Button(self, text="AmostraRNA",
                           command=lambda: controller.show_frame('AmostraRNA'))
        amostrarna_button.pack(fill='x')

        teste_button = ttk.Button(self, text="Teste",
                           command=lambda: controller.show_frame('Teste'))
        teste_button.pack(fill='x')

        rnaseq_button = ttk.Button(self, text="RNASeq",
                           command=lambda: controller.show_frame('RNASeq'))
        rnaseq_button.pack(fill='x')

        internamento_button = ttk.Button(self, text="Internamento",
                           command=lambda: controller.show_frame('Internamento'))
        internamento_button.pack(fill='x')

        infoclinica_button = ttk.Button(self, text="Infos. Clínicas",
                           command=lambda: controller.show_frame('InfoClinica'))
        infoclinica_button.pack(fill='x')

        infomicrobio_button = ttk.Button(self, text="Infos. Micro Biologica",
                           command=lambda: controller.show_frame('InfoMicroBiologica'))
        infomicrobio_button.pack(fill='x')

        obito_button = ttk.Button(self, text="Obito",
                           command=lambda: controller.show_frame('Obito'))
        obito_button.pack(fill='x')

        medicamento_button = ttk.Button(self, text="Medicamento",
                           command=lambda: controller.show_frame('Medicamento'))
        medicamento_button.pack(fill='x')

        tipotratamento_button = ttk.Button(self, text="Tipo Tratamento",
                           command=lambda: controller.show_frame('TipoTratamento'))
        tipotratamento_button.pack(fill='x')


class Toolbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent, relief=tk.RIDGE, borderwidth=3)
        label = ttk.Label(self, text="PRONON DB", font=('Arial', 12))
        label.pack()
