#sumar n numeros mayores a un numero x
n=int(input("Ingresar el tamaño de la lista: "))
x=int(input("Ingresar un numero: "))
i=1
s=0
while i<=n:
    n1=int(input("Ingresar un numero de la lista: "))
    i=i+1
    if n1 > x:
        s=s+n1
print (s)

