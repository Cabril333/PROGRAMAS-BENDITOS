
lista_num = [10, 5, 8, 3, 12, 7]
suma = 0
for n in lista_num:
    suma += n
media = suma / len(lista_num)


suma = 0
for nm in lista_num:
    suma += (nm - media) ** 2
varianza = suma / len(lista_num)
print("La varianza de la lista es:", varianza)
