#Dada una lista de numeros naturales, determinar si esta ordenada en forma ascendente o descendente.
#De lo contrario informar que no se encuentra ordendada.
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar el primer numero de la lista: "))
ascendente=x
descendente=x
bandera=0
i=1
while i<n and bandera==0:
    x1=int(input("Ingresar numero de la lista: "))
    if ascendente<x1 or descendente<x1:
        bandera=1
    if ascendente<x1:
        ascendente=x1
    if descendente>x1:
        descendente=x1
    
    i=i+1
if ascendente>x:
    print("La lista esta ordenada ascendente")
if descendente<x:
    print("La lista esta ordenada descendente")
if bandera==1:
    print("La lista esta desordenada")
