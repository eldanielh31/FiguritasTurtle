import tkinter as tk

from turtle import *
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono

class Menu:
    def __init__(self):

        self.mainVentana = tk.Tk()
        self.mainVentana.title("Menu Principal")
        self.mainVentana.geometry("500x300")
        self.mainVentana.config(bg='black')
        
        self.botones()

    def start(self):
        self.mainVentana.mainloop()

    def botones(self):
        self.mainVentana.columnconfigure(0, weight=1)
        self.mainVentana.columnconfigure(1, weight=1)
        self.mainVentana.columnconfigure(2, weight=1)
        self.mainVentana.rowconfigure(0, weight=1)
        self.mainVentana.rowconfigure(1, weight=1)
        self.mainVentana.rowconfigure(2, weight=1)

        self.circulo = tk.Button(self.mainVentana, text = "Circulo")
        self.circulo.grid(row=0, column=0)
        
        self.cuadrado = tk.Button(self.mainVentana, text="Cuadrado")
        self.cuadrado.grid(row=0, column=1)
        
        self.triangulo = tk.Button(self.mainVentana, text="Triangulo")
        self.triangulo.grid(row=0, column=2)

        self.hexagono = tk.Button(self.mainVentana, text = "Hexagono")
        self.hexagono.grid(row=1, column=0)
        
        self.pentagono = tk.Button(self.mainVentana, text="Pentagono")
        self.pentagono.grid(row=1, column=1)
        
        self.rombo = tk.Button(self.mainVentana, text="Rombo")
        self.rombo.grid(row=1, column=2)

Menu().start()
