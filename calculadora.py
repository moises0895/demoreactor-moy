num1 = 5
num2 = -2

def suma(numero1, numero2):
    total = numero1 * numero2
    return total

def resta(numero1, numero2):
    total = numero1 - numero2
    return total 

def multiplicacion(numero1, numero2):
    total = numero1 * numero2
    return total

resultado = suma(num1, num2)
resultado2 = resta(num1, num2)
resultado3 = multiplicacion(num1, num2)

print('El resultado es: ',resultado)
print('El resultado de la resta es: ', resultado2)
print('El resultado de la multiplicación es: ', resultado3)