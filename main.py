
from Figuras.Triangulo import Triangulo
from Figuras.Cuadrado import Cuadrado
from Figuras.Circulo import Circulo
from Figuras.Pentagono import Pentagono
from Figuras.Hexagono import Hexagono


tortuga = Turtle()

screen = Screen()
screen.setup(width=750, height=500)

triangulo = Triangulo(500)
cuadrado = Cuadrado(100)
circulo = Circulo(100)
pentagono = Pentagono(100)
hexagono = Hexagono(100)

#hexagono.construir(tortuga)
#pentagono.construir(tortuga)
#circulo.construir(tortuga)
#triangulo.construir(tortuga)
#cuadrado.construir(tortuga)



done()