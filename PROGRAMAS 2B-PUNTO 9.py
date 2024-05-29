
def esprimo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
print("numeros primos hasta 10:")
for n in range(2, 11):
    if esprimo(n):
        print(n)
