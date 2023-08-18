n=int(input("Ingresar el tamaño de la lista: "))
c=1
while c<=n:
    factorial=1
    i=2
    x=int(input("Ingresar un numero: "))
    if x==1 or x==0:
        print("El factorial de",x,"Es 1")
    else:
        while i<=x:
            factorial=factorial*i
            i=i+1
        print("El factor del numero",x,"Es igual a:",factorial)
    c=c+1
