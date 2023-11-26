#1)Mostrar el segundo menor y el segundo mayor, numero de la lista.
#2)Mostrar los numeros que contengan al digito D
#)3Buscar y mostrar el numero que contenga mas veces al digito D (se supone uno solo)
n=int(input("Ingersar el tamaño de la lista: "))
x=int(input("Ingresar el primer numero de la lista: "))
d=int(input("Ingresar el numero D:"))
primer_mayor=x
segundo_menor=0
segundo_mayor=0
primer_menor=x
i=1
bandera1=0
contador_d1=0
while i<n:
    while x>0 and bandera1==0:
        resto=x%10
        if resto==d:
            print("El digito x contiene a D:",x)
            contador_d1+=1
            bandera1=1
        x=x//10
    x1=int(input("Ingresar x1: "))
    if primer_mayor<x1:
        segundo_mayor=primer_mayor
        primer_mayor=x1    
    else:
        if primer_menor>x1:
            segundo_menor=primer_menor
            primer_menor=x1
    bandera=0
    contador_d=0
    while x1>0 and bandera==0:
        r=x1 % 10
        if r==d:
            print("El numero x1 contiene a D:",x1)
            contador_d=contador_d+1
            bandera=1
                  
        x1= x1//10
    
    i=i+1

print("El segundo mayor es:",segundo_mayor)
print("El esgundo menor es:",segundo_menor)
#print(primer_mayor)
#print(primer_menor)