#Ejercicio 7: Dados N numeros, contar la cantidad de positivos pares multiplos de x.
"""
DE):N=6=(-2,3,10,6,-4,15)
DE) X= 3
DS): Cantidad positivos pares multiplos de x=3: 3x2=6"Multiplo" 6%2=0 es par.
DS) La cantidad de positivos pares multiplos de x=3: son 6 y 15
¿Como saber si es multiplo?
multiplos de 3: 3x1=3 , 3x2=6 , 3x3=9 , 3x4=12 , 3x5=15



"""
#Ejercicio 7: Dados N numeros, contar la cantidad de positivos pares multiplos de x.
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar el numero a saber sus pares multiplos: "))
i=1
cp=0
while i<=n:
    numero=int(input("Ingresar los numeros de la lista: "))
    if numero>0 and numero % x==0 and numero % 2==0:    
        cp=cp+1
    i=i+1
print("La cantidad de positivos pares multiplos es: ",cp)

