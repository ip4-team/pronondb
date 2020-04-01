import tkinter as Tk


class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.plotBut = Tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side='top', fill=Tk.BOTH)

        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side='top', fill=Tk.BOTH)

