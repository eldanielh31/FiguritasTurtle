from turtle import *
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono

class Dibujos:
    def __init__(self):
        self.pantalla = Screen()
        self.pantalla.screensize(2000, 2000)
        self.pantalla.setup(width=750, height=500)

        self.tortuga1 = Turtle()
    
    def dibujarTriangulo(self, lado):
        self.triangulo = Triangulo(lado)
        self.triangulo.construir(self.tortuga1)
    

    def dibujarCirculo(self, radio):
        self.circulo = Circulo(radio)
        self.circulo.construir(self.tortuga1)
        self.circulo.irCentro(self.tortuga1)

    def dibujarCuadrado(self, lado):
        self.cuadrado = Cuadrado(lado)
        self.cuadrado.construir(self.tortuga1)

    def dibujarHexagono(self, lado):
        self.hexagono = Hexagono(lado)
        self.hexagono.construir(self.tortuga1)

    def dibujarPentagono(self, lado):
        self.pentagono = Pentagono(lado)
        self.pentagono.construir(self.tortuga1)

    def dibujarRombo(self, lado):
        self.rombo = Cuadrado(lado)
        self.rombo.construir(self.tortuga1)

    def exitOnClick(self):
        self.pantalla.exitonclick()