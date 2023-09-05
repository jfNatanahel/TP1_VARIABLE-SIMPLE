#Ejercicio 8: Determinar si un numero x es perfecto, un numero es perfecto si la suma de sus divisores es el mismo 
#numero. Ej. El 6 es perfecto ya que 1+2+3=6
x=int(input("Ingresar un numero: "))
i=1
x1=x
s=0
while i<x:
    if x % i==0:
        s=s+i
    i=i+1
if s==x1:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")