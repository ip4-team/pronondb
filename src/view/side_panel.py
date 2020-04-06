import tkinter as Tk
from PIL import Image, ImageTk


class SidePanel():
    def __init__(self, master):
        self.master = master
        self.master.title("Toolbar")

        menubar = Tk.Menu(self.master)
        self.fileMenu = Tk.Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = Tk.Frame(self.master, bd=1, relief=RAISED)

        exitButton = Tk.Button(toolbar, text="Sair", relief=FLAT,
                            command=self.onExit)
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)

    def onExit(self):
        self.quit()
