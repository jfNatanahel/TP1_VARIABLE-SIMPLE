h=int(input("Ingresar la cantidad de numeros primos a generar: "))

numero=1

fin=0
while fin<h:
    div=1
    p=0
    while div<=numero:
        if numero % div==0:
            p=p+1
        div=div+1
    
    if p==2:
        fin=fin+1
        print(numero)
    numero=numero+1