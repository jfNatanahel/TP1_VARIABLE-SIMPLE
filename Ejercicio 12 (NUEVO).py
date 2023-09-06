# Ingresar el valor de k
k = int(input("Ingrese el valor de k: "))

# Inicializar variables
acumulador = 0
contador = 0
i = 1

# Repetir mientras el acumulador sea menor que k
while acumulador < k:
    contador = contador + 1
    acumulador = acumulador + contador
    print(contador)

# Mostrar el resultado final
print(f"Se necesitaron {contador} números naturales consecutivos para llegar a {k}")