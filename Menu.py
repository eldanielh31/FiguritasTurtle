import tkinter as tk

from turtle import *
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono
from Dibujos import Dibujos

class Menu:
    def __init__(self):

        self.mainVentana = tk.Tk()
        self.mainVentana.title("Menu Principal")
        self.mainVentana.geometry("500x300")
        self.mainVentana.config(bg='black')
        self.primeraFigura = True

        self.texto = tk.Label(self.mainVentana, text = "ELIJA PRIMERA FIGURA")
        self.texto.config(fg = "green",
                        bg = "black",
                        font=("Verdana",24))
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

        self.circulo = tk.Button(self.mainVentana, text = "Circulo", command = self.popupCirculo)
        self.circulo.grid(row=1, column=0)
        
        self.cuadrado = tk.Button(self.mainVentana, text="Cuadrado", command = self.popupCuadrado)
        self.cuadrado.grid(row=1, column=1)
        
        self.triangulo = tk.Button(self.mainVentana, text="Triangulo", command = self.popupTriangulo)
        self.triangulo.grid(row=1, column=2)

        self.hexagono = tk.Button(self.mainVentana, text = "Hexagono", command = self.popupHexagono)
        self.hexagono.grid(row=2, column=0)
        
        self.pentagono = tk.Button(self.mainVentana, text="Pentagono", command = self.popupPentagono)
        self.pentagono.grid(row=2, column=1)
        
        self.rombo = tk.Button(self.mainVentana, text="Rombo", command = self.popupRombo)
        self.rombo.grid(row=2, column=2)

    def popupCirculo(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese radio de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarCirculo(self.w.value)
            self.primeraFigura = False
            self.texto.config(text="ELIJA SEGUNDA FIGURA")
            
        else:
            self.primeraFigura = True     

    def popupCuadrado(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarCuadrado(self.w.value)
            self.primeraFigura = False

        else:
            self.primeraFigura = True

    def popupTriangulo(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarTriangulo(self.w.value)
            self.primeraFigura = False

        else:
            self.primeraFigura = True
    
    def popupHexagono(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarHexagono(self.w.value)
            self.primeraFigura = False

        else:
            self.primeraFigura = True

    def popupPentagono(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarPentagono(self.w.value)
            self.primeraFigura = False

        else:
            self.primeraFigura = True

    def popupRombo(self):
        if (self.primeraFigura):
            self.w=infoVentana(self.mainVentana, "Ingrese lado de la figura:")
            self.deshabilitarBotones()
            self.mainVentana.wait_window(self.w.top)
            self.habilitarBotones()

            self.dibujos.dibujarRombo(self.w.value)
            self.primeraFigura = False

        else:
            self.primeraFigura = True

class infoVentana:
    def __init__(self,master, texto):
        top=self.top = tk.Toplevel(master)
        top.geometry("200x75")
        top.resizable(False, False)
        self.l=tk.Label(self.top,text=texto)
        self.l.pack()
        self.e=tk.Entry(top)
        self.e.pack()
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        if((self.isInt(self.value))):
            if(int(self.value) > 0):
                self.value = int(self.value)
                self.top.destroy()
        else:
            tk.messagebox.showerror(title= "Error", message= "El valor introducido no puede ser procesado.")
            
    
    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

Menu().start()
