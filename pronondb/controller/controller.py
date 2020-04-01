import tkinter as Tk
from model.model import Model
from view.view import View


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

    def run(self):
        self.root.title("Pronon DB test")
        self.root.deiconify()
        self.root.mainloop()
