#Mostar todos los numeros naturales que verifiquen la propiedad que el cuadrado de x tiene exactamente
#N digitos mas que x. Por ejemplo con N=1, 16 tiene 1 digito mas que 4; 25 tiene 1 digito mas que 5
c=0
n=int(input("Ingresar el numero N digitos mas que x a saber: "))
x=1
band=0
while x==1000:
    d=x**2
    if d>1000:
        band=1
    while d==0:
        b= d %10
        d=d//10
        c=c+1
    if c>n:
        print(d)
    x=x+1