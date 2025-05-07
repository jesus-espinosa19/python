#crear un programa que pida al usuario un numero real y muestre su raiz cuarta
#(la raiz cuadrada de la raiz cuadrada)

import math
print("digite el numero a calcular raiz cuarta: ")
numero = float(input())
raizC = math.sqrt(numero)
raizC2 = math.sqrt(raizC)
print("la raiz cuarta de", numero, "es", raizC2)

