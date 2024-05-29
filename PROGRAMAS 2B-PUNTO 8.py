
numero = int(input("Ingrese un número entero positivo mayor que 1: "))
if numero <= 1:
    es_primo = False
else:
    es_primo = True
    divisor = 2
    while divisor < numero and es_primo:
        if numero % divisor == 0:
            es_primo = False
        divisor += 1
if es_primo:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
