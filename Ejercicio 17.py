#Mostar todos los numeros naturales que verifiquen la propiedad que el cuadrado de x tiene exactamente
#N digitos mas que x. Por ejemplo con N=1, 16 tiene 1 digito mas que 4; 25 tiene 1 digito mas que 5
#c=0
n = int(input("Ingresar el número N para la propiedad: "))
max_iteraciones = int(input("Ingresar el número máximo de iteraciones: "))
i = 1
iteraciones = 0

while iteraciones < max_iteraciones:
    x = i
    c = 0
    x1 = x
    x = x ** 2
    
    while x != 0:
        x = x // 10
        c = c + 1
        #print(x)
    if c >n :
        print(x1,x1**2)
        
    i = i+ 1
    iteraciones += 1