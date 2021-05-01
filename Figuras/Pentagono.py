from turtle import Turtle

class Pentagono:
    def __init__(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self, nuevoLado):
        self.lado = nuevoLado

    def construir(self, tortuga):
        for _ in range(5):
            tortuga.forward(self.lado)
            tortuga.left(72)
  

   