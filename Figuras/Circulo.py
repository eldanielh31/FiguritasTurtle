from turtle import *

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def getLado(self):
        return self.radio

    def setLado(self, nuevoRadio):
        self.radio = nuevoRadio

    def construir(self, tortuga):
        tortuga.circle(self.radio)

    def irCentro(self):
        print("hola")