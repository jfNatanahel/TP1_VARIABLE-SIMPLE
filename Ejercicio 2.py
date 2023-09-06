#De una lista de N números determinar el promedio de los positivos y el de los negativos.
n=int(input("Ingresar el tamaño de la lista: "))
c_positivos= 0
s_positivos=0
c_negativos=0
s_negativos=0
i=1
while i<=n:
    x=int(input("Ingresar un numero de la lista: "))
    if x<0:
        c_negativos=c_negativos+1
        s_negativos=s_negativos+x
        
    else:
        c_positivos=c_positivos+1
        s_positivos=s_positivos+x
    i=i+1
promedio_positivos=s_positivos//c_positivos
promedio_negativos=s_negativos//c_negativos
print("El promedio de los positivos es: ",promedio_positivos,"El promedio de los negativos es: ",promedio_negativos)