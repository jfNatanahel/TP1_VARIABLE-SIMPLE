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