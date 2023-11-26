#DNI=22555444
#TARJETA CREDITO= 4348577015644896
bandera=0

while bandera==0:
    contador_dni=0
    contador_tarjeta=0
    dni=int(input("Ingresar su dni: "))
    aux_dni=dni
    tarjeta_credito=int(input("Ingresar su numero de tarjeta de credito: "))
    while dni>0:
        r1=dni %10
        contador_dni+=1
        dni=dni//10
    while tarjeta_credito>0:
        r2=tarjeta_credito%10
        contador_tarjeta+=1
        tarjeta_credito=tarjeta_credito//10
    
    if contador_dni != 8 and contador_tarjeta !=16:
        validacion=input("DNI o Tarjeta de credito es incorrecto ¡INTENTAR DE NUEVO! apretar S mayuscula: ")
        if validacion=="S":
            bandera=0
    else:
            bandera=1
    
suma_a=0
ud=dni%10
while dni>0:
    r=dni %10
    suma_b=suma_b+r
    dni=dni//10
i=17
suma_b=0
while i<=3:
    r=tarjeta_credito % 10
    i=i-1
    if i % 2 != 0:
        suma_b=suma_b+r
    tarjeta_credito=tarjeta_credito//10
ss=suma_a//16
t=suma_b//16
cvc=((ud*10+ss)*10+t)
j=0
divisor=1000000000000000
while j<=2:
    r=aux_dni % divisor
    c=aux_dni // divisor
    j=j+1
    divisor=divisor//10
if c==34 or c==37:
    print("AMERICAN EXPRESS")
if c==51 or c==55:
    print("MASTERCAD")
if c==43:
    print("VISA")
    
print("Su codigo de seguridad es:",cvc)#<>


#DNI=22555444
#TARJETA CREDITO= 4348577015644896

