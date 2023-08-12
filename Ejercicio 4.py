#4.Dada una lista de n numeros naturales, calcular el menor y el mayor de la lista.
#DE) Ln=(4,7,2,3,5) , DS) Menor= 2 y el mayor = 7
#Buscar el menor , ir comparando menor=x, mayor= x {4<7 -> si 4<2 -> si 4=2 m=x ENCONTRE EL MENOR=2}
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar un numero: "))
i=1
menor=x
mayor=x
while i<n:
    x1=int(input("Ingresar un numero: "))
    if menor>x1: #and mayor<x1:
        menor=x1 #Encontramos el menor
        
    if mayor<x1:
        mayor=x1
    i=i+1
    #if menor 
print(menor)
print(mayor)
