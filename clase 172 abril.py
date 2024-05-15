
lista=["Ana","Boris","Carlos","Dory","Emma"]
edad=[24,50,80,28,21]
print(lista)
print(edad)


def buscar (nombre):
    for indice,valor in enumerate(lista):
        if nombre==valor:
            return(indice)

x=buscar("Carlos")
print(lista[x])

