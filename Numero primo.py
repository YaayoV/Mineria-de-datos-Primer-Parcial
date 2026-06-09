numero = int(input("Escribe un número entero: "))
if numero <= 1:
    print("No es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")