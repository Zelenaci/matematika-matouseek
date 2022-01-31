#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random

# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "matematikovací věda"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.frame = tk.Frame(self, highlightbackground="#000000")
        self.frame.pack(padx=50, pady=25)
        self.lbl = tk.Label(self.frame, text="Ahoj kamosu")
        self.lbl.pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.btn2 = tk.Button(self, text="Pokracovat", command=self.generovani)
        self.btn2.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()


    def plus(self):
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text=f'{self.cisloA} + {self.cisloB} = ')

    def minus(self):
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        self.lbl.config(text=f'{self.cisloA} - {self.cisloB} = ')

    def krat(self):
        self.cisloA = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text=f'{self.cisloA} * {self.cisloB} = ')

    def deleno(self):
        self.vysledek = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl.config(text=f'{self.cisloA} / {self.cisloB} = ')

    def generovani(self):
        priklad = random.choice([self.plus, self.minus, self.krat, self.deleno])
        priklad()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
