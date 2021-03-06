from turtle import Turtle

class Hexagono:
    def __init__(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self, nuevoLado):
        self.lado = nuevoLado

    def construir(self, tortuga):
        for _ in range(6):
            tortuga.pencolor("blue")
            tortuga.forward(self.lado)
            tortuga.left(360 / 6)