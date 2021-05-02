from turtle import *

class Rombo:
    def __init__(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self, nuevoLado):
        self.lado = nuevoLado

    def construir(self, tortuga):
        tortuga.pencolor("pink")
        tortuga.left(135)
        tortuga.forward(self.lado)
        for _ in range(3):
            tortuga.right(90)
            tortuga.forward(self.lado)
        tortuga.right(225)
        
        