from tkinter import *

import math
from turtle import *
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono
from Dibujos import Dibujos

class Menu:
    def __init__(self):

        self.mainVentana = Tk()
        self.mainVentana.title("Menu Principal")
        self.mainVentana.geometry("500x300")
        self.primeraFigura = True
        self.nombreFigura = ""

        self.texto = Label(self.mainVentana, text = "Elija primera figura")
        self.texto.config(font=("Century" , 24))
        self.texto.grid(row = 0, column = 1)

        self.dibujos = Dibujos()
        
        self.botones()

    def start(self):
        self.mainVentana.mainloop()

    def deshabilitarBotones(self):
        self.triangulo["state"] = "disabled" 
        self.circulo["state"] = "disabled" 
        self.cuadrado["state"] = "disabled" 
        self.pentagono["state"] = "disabled" 
        self.hexagono["state"] = "disabled" 
        self.rombo["state"] = "disabled" 

    def habilitarBotones(self):
        self.triangulo["state"] = "normal" 
        self.circulo["state"] = "normal" 
        self.cuadrado["state"] = "normal" 
        self.pentagono["state"] = "normal" 
        self.hexagono["state"] = "normal" 
        self.rombo["state"] = "normal" 

    def botones(self):
        self.mainVentana.columnconfigure(0, weight=1)
        self.mainVentana.columnconfigure(1, weight=1)
        self.mainVentana.columnconfigure(2, weight=1)
        self.mainVentana.rowconfigure(1, weight=1)
        self.mainVentana.rowconfigure(2, weight=1)
        self.mainVentana.rowconfigure(3, weight=1)

        self.circulo = Button(self.mainVentana, text = "🟣", width = 10, height = 2, command = self.popupCirculo)
        self.circulo.grid(row=1, column=0)
        
        self.cuadrado = Button(self.mainVentana, text="🟪", width = 10, height = 2, command = self.popupCuadrado)
        self.cuadrado.grid(row=1, column=1)
        
        self.triangulo = Button(self.mainVentana, text="🔺", width = 10, height = 2, command = self.popupTriangulo)
        self.triangulo.grid(row=1, column=2)

        self.hexagono = Button(self.mainVentana, text = "Hexagono", width = 10, height = 2, command = self.popupHexagono)
        self.hexagono.grid(row=2, column=0)
        
        self.pentagono = Button(self.mainVentana, text="Pentagono", width = 10, height = 2, command = self.popupPentagono)
        self.pentagono.grid(row=2, column=1)
        
        self.rombo = Button(self.mainVentana, text="🔷", width = 10, height = 2, command = self.popupRombo)
        self.rombo.grid(row=2, column=2)

    def popupCirculo(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese radio de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarCirculo(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "circulo"
            self.primeraFigura = False
            
        else:
            self.texto.config(text="Elija primera figura")
            self.primeraFigura = True

            if(self.nombreFigura == "triangulo"):
                self.dibujos.tortuga1.forward(self.w.value / 2)
                self.dibujos.dibujarCirculo(self.w.value/3.5)
            
            elif(self.nombreFigura == "cuadrado"):
                self.dibujos.tortuga1.forward(self.w.value / 2)
                self.dibujos.dibujarCirculo(self.w.value/2)

            elif(self.nombreFigura == "rombo"):
                self.dibujos.tortuga1.left(45)
                self.dibujos.tortuga1.forward(self.w.value / 2)
                self.dibujos.dibujarCirculo(self.w.value/2)

            elif(self.nombreFigura == "pentagono"):
                self.dibujos.tortuga1.forward(self.w.value)
                self.dibujos.tortuga1.left(72)
                self.dibujos.tortuga1.forward(self.w.value / 2)
                self.dibujos.dibujarCirculo(self.w.value / 1.45)

            elif(self.nombreFigura == "hexagono"):
                self.dibujos.tortuga1.forward(self.w.value / 2)
                self.dibujos.dibujarCirculo(self.w.value/1.16)
            
            else:
                self.dibujos.dibujarCirculo(self.w.value/2)

            
    def popupCuadrado(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarCuadrado(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "cuadrado"
            self.primeraFigura = False

        else:
            self.texto.config(text="Elija primera figura")
            self.dibujos.dibujarCuadrado(self.w.value)
            self.primeraFigura = True

    def popupTriangulo(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarTriangulo(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "triangulo"
            self.primeraFigura = False

        else:
            self.texto.config(text="Elija primera figura")
            self.dibujos.dibujarTriangulo(self.w.value)
            self.primeraFigura = True
    
    def popupHexagono(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarHexagono(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "hexagono"
            self.primeraFigura = False

        else:
            self.texto.config(text="Elija primera figura")
            self.dibujos.dibujarHexagono(self.w.value)
            self.primeraFigura = True

    def popupPentagono(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarPentagono(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "pentagono"
            self.primeraFigura = False

        else:
            self.texto.config(text="Elija primera figura")
            self.dibujos.dibujarPentagono(self.w.value)
            self.primeraFigura = True

    def popupRombo(self):
        if (self.primeraFigura):
            self.dibujos.pantalla.clear()
            self.dibujos.tortuga1 = Turtle()
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarRombo(self.w.value)
            self.texto.config(text="Elija segunda figura")
            self.nombreFigura = "rombo"
            self.primeraFigura = False

        else:
            self.texto.config(text="Elija primera figura")
            self.primeraFigura = True
            
            if(self.nombreFigura == "circulo"):
                self.dibujos.dibujarRombo(self.w.value * 1.4)

            else:
                self.dibujos.dibujarRombo(self.w.value)
            

class infoVentana:
    def __init__(self,master, texto):
        top=self.top = Toplevel(master)
        top.geometry("200x75")
        top.resizable(False, False)
        self.l=Label(self.top,text=texto)
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        
    def cleanup(self):
        self.value=self.e.get()
        if((self.isInt(self.value))):
            if(int(self.value) > 0):
                self.value = int(self.value)
                self.top.destroy()
            else:
                messagebox.showerror(title= "Error", message= "El valor introducido debe ser positivo.")

        else:
            messagebox.showerror(title= "Error", message= "El valor introducido no puede ser procesado.")
            
    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    Menu().start()
