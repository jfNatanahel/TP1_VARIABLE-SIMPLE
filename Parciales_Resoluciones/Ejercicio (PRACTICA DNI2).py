"""
Dada el nombre de usuario y DNI de la presona, generar su clave provisoria para ingresar a un sistema. 
La misma se forma atraves del siguiente criterio:
-Contar el total de numeros primos que tiene ese dni. Ese total sera la primera parte de la clave
-A la clave anterior ubicar, como segunda parte de la clave, un numero compuesto por los digitos de las 
posciones impares (tomar de derecha a izquierda) del Dni.
"""

usuario=input("Ingresar usuario: ")
dni=int(input("Ingresar dni: "))
aux_dni=dni
primera_parte=0
while dni>0:
    div=1
    contador=0
    r=dni % 10
    while div<=r:
        if r % div==0:
            contador=contador+1
        div=div+1
    if contador==2:
        primera_parte+=1
    dni=dni//10

password=primera_parte
i=-1
while aux_dni>0:
    digito=aux_dni %10
    i=i+1
    if i % 2!=0:
        password=password*10+digito
    aux_dni=aux_dni//10
print("Su nuevo contraseña es:",password)

#<>