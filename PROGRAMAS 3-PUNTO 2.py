
numeros = [89, 33, 44, 9, 13, 1]
menor_numero = numeros[0]
posicion_menor = 0
for i in range(1, len(numeros)):
    if numeros[i] < menor_numero:
        menor_numero = numeros[i]
        posicion_menor = i
if numeros:
    print("El número menor en la lista es:", menor_numero)
    print("Su posición en la lista es:", posicion_menor)
else:
    print("La lista no tiene elementos.")
