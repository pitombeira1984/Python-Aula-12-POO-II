import math

class FormasGeomtricas():
    def __init__(self, base, altura, raio):
        self.base = base
        self.altura = altura
        self.raio = raio

class Retangulo(FormasGeomtricas):

    def AreaRetangulo(self, base, altura):
        return base * altura
    
    def PerimetroRetangulo(self, base, altura):
        return 2 * (base + altura)

class Circulo(FormasGeomtricas):

    def AreaCirculo(self, raio):
        return math.pi * raio ** 2
    
    def PerimetroCirculo(self, raio):
        return 2 * math.pi * raio

Retangulo = Retangulo(5, 3, 0)
Circulo = Circulo(0, 0, 4)
print("Área do Retângulo:", Retangulo.AreaRetangulo(5, 3))
print("Perímetro do Retângulo:", Retangulo.PerimetroRetangulo(5, 3))
print("Área do Círculo:", Circulo.AreaCirculo(4))
print("Perímetro do Círculo:", Circulo.PerimetroCirculo(4))


