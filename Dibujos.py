from turtle import *
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono

class Dibujos:
    def __init__(self):
        self.pantalla = Screen()
        self.pantalla.setup(width=750, height=500)

        self.tortuga1 = Turtle()
        self.tortuga2 = Turtle()

        

    def dibujarTriangulo(self, lado):
        self.triangulo = Triangulo(lado)
        self.triangulo.construir(self.tortuga1)
    

    def dibujarCuadrado(self, lado):
        self.cuadrado = Cuadrado(lado)
        self.cuadrado.construir(self.tortuga1)
        

    
dibujos = Dibujos()
dibujos.dibujarTriangulo(100)
dibujos.dibujarCuadrado(200)