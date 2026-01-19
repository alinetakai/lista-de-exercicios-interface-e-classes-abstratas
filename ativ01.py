from abc import ABC, abstractmethod
# ABC significa Abstract Base Class
import math

class Forma(ABC): # classe abstrata

    @abstractmethod # Obriga todas as classes filhas a implementarem esse método. Se não implementar → erro
    def calcular_area(self):
        pass # pass → Placeholder (o método ainda não faz nada)

class Quadrado(Forma): # Quadrado herda de Forma, é obrigada a implementar calcular_area
    def __init__(self, lado):
        self.lado = lado # Armazena o valor do lado do quadrado

    def calcular_area(self):
        return self.lado ** 2 # Calcula a área do quadrado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

#testes
q = Quadrado(4)
print(q.calcular_area())

c = Circulo(3)
print(c.calcular_area())
