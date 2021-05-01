from turtle import *

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self, nuevoLado):
        self.lado = nuevoLado

    def construir(self, tortuga):
        tortuga.forward(self.lado) 
        tortuga.left(90) 
    
        tortuga.forward(self.lado) 
        tortuga.left(90)

        tortuga.forward(self.lado) 
        tortuga.left(90)   

        tortuga.forward(self.lado) 
        tortuga.left(90) 