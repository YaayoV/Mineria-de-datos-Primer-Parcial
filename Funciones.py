import math

def area_circulo(radio):
    return math.pi * radio**2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

print("Área del círculo:", area_circulo(9))
print("Volumen del cilindro:", volumen_cilindro(5, 10))