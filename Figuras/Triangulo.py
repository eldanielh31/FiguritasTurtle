from turtle import *

class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self, nuevoLado):
        self.lado = nuevoLado

    def construir(self, tortuga):
        for i in range(3):
            tortuga.pencolor("green")
            tortuga.forward(self.lado)
            tortuga.left(120)