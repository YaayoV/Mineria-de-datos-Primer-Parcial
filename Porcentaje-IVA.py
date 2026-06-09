def calcular_total(cantidad, iva):
    return cantidad + (cantidad * iva / 100)

print(calcular_total(100, 21))
print(calcular_total(100, 16))