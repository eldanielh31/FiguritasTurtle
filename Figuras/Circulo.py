from turtle import *

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def getLado(self):
        return self.radio

    def setLado(self, nuevoRadio):
        self.radio = nuevoRadio

    def construir(self, tortuga):
        tortuga.pencolor("red")
        tortuga.circle(self.radio)

    def irCentro(self, tortuga):
        tortuga.penup()
        tortuga.left(90)
        tortuga.forward(self.radio)
        tortuga.left(180)
        tortuga.pendown()
        