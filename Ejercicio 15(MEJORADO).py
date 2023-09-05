N = float(input("Ingresar un número decimal: "))
X = N * 10
E = int(X / 100)
D = round((N - E), 4) * 10000

Entero = 0
while E > 0:
    Entero += 1
    E = E // 10

Decimal = 0
Resto = 0
while Resto == 0:
    if D % 10 == 0:
        D = D // 10
    else:
        Resto = 1

while D > 0:
    Decimal += 1
    D = D // 10

print("Cantidad de dígitos enteros:", Entero)
print("Cantidad de dígitos decimales:", Decimal)
"""
El usuario ingresa un número decimal N.

1.El programa multiplica N por 10 y lo almacena en X. Esto es para mover el punto decimal un lugar hacia la derecha, convirtiendo así el número decimal en un número entero.

A partir de X, se calcula E como el cociente de la división entera de X entre 100. Esto se hace para obtener la parte entera del número original.

Luego, D se calcula de la siguiente manera: primero, se resta E a N para obtener la parte decimal original, luego se redondea a 4 decimales, y finalmente se multiplica por 10,000 para convertirlo en un número entero. Esto se hace para aislar la parte decimal en un número entero.

Se inicializan dos contadores: "Entero" y "Decimal" en 0, que se utilizarán para contar los dígitos enteros y decimales, respectivamente.

En un bucle, se cuenta la cantidad de dígitos enteros en E. Esto se hace dividiendo E sucesivamente por 10 hasta que E sea igual a 0, y cada vez que se divide, se incrementa el contador "Entero".

En el siguiente bucle, se busca el primer dígito no nulo en la parte decimal. Esto se hace dividiendo D sucesivamente por 10 hasta que se encuentre un dígito diferente de 0, y se marca "Resto" como 1. Esto garantiza que el programa comience a contar los dígitos decimales después de cualquier 0 a la izquierda.

Finalmente, se cuenta la cantidad de dígitos decimales en D. Esto se hace de manera similar a como se contaron los dígitos enteros, dividiendo D por 10 sucesivamente y aumentando el contador "Decimal".

El programa muestra la cantidad de dígitos enteros y decimales.

"""

