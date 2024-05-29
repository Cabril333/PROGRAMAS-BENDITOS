import math

# Pedir al usuario que ingrese las coordenadas de los dos puntos
x1 = float(input("Digite la coordenada  exacta x del primer punto: "))
y1 = float(input("Digie la coordenada  exacta y del primer punto: "))
x2 = float(input("Digite la coordenada exacta  x del segundo punto: "))
y2 = float(input("Digite la coordenada  exacta y del segundo punto: "))

# Calculamos la distancia utilizando la fórmula D = √((x2 − x1)^2 + (y2 − y1)^2)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los puntos", (x1, y1), "y", (x2, y2), "es:", distancia)
