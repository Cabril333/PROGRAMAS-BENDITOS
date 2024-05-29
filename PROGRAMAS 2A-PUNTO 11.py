
numeromes = int(input("Ingrese el número del mes (1-12): "))

if numeromes < 1 or numeromes > 12:
    print("Número de mes inválido. Debe ser un número entre 1 y 12.")
else:
   
    diaspormes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
   
    numdias = diaspormes[numeromes - 1]
    
    # Mostrar el resultado
    print("El mes", numeromes, "tiene", numdias, "días.")
