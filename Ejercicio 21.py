#Dada una lista de numeros naturales, determinar si esta ordenada en forma ascendente o descendente.
#De lo contrario informar que no se encuentra ordendada.
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar el primer numero de la lista: "))
ascendente=0
descendente=0
#bandera=0
comparar=x
i=1
while i<n: #and bandera==0:
    x1=int(input("Ingresar numero de la lista: "))
    
    if comparar<=x1:
        ascendente=1
    if comparar>=x1:
        descendente=1
    #elif ascendente<= x1 or descendente>=x1:
     #   bandera=1
    comparar=x1
    i=i+1
if ascendente == 1 and descendente==1:
    print("La lista esta desordenada")
elif ascendente==1:
    print("La lista es ascendente")
elif descendente==1:
    print("La lista es descendente")
