n=int(input("Ingresar el tamaño de la lista: "))
i=1
while i<=n:
    x=int(input("Ingresar numero de la lista: "))
    x1=x
    y=0
    while x1<0:
        d=x1 % 10
        y=y*10+d
        x1=x1//10
    if x!=y:
        print("El numero que no es capicua es:")
    else:
        print("El numero es capicua")
    i=i+1