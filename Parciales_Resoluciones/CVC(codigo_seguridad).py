#DNI=
#TARJETA DE CREDITO=4348577015644895
bandera=0
while bandera==0:
    dni=int(input("Ingresar el dni: "))
    tarjeta_credito=int(input("Ingresar tarjeta de credito: "))
    dni_digitos=0
    tarjeta_digito=0
    aux_dni=dni
    aux2_dni=dni
    aux_tarjeta=tarjeta_credito
    aux2_tarjeta=tarjeta_credito
    while dni>0:
        r1=dni %10
        dni_digitos+=1
        dni=dni //10
    while tarjeta_credito>0:
        r2=tarjeta_credito%10
        tarjeta_digito+=1
        tarjeta_credito=tarjeta_credito//10
    if dni_digitos== 8 and tarjeta_digito==16:
        print("Ambos numeros son validos")
        bandera=1
    else: 
        print("Algunos de los numeros ingresados es invalido. Intente de nuevo")
        bandera=0
#3)a. Se suman todos los digitos del DNI
suma_dni=0
while aux_dni>0:
    r3= aux_dni % 10
    suma_dni=suma_dni+r3
    aux_dni=aux_dni//10
#print("a",suma_dni)
#3)b. Sumar los digitos posiciones impares desde la 3 posicion.
i=17
suma_tarjeta=0
while i>=3:
    r4=aux_tarjeta%10
    aux_tarjeta=aux_tarjeta//10
    i=i-1
    if i %2!=0:
        suma_tarjeta=suma_tarjeta+r4
#print("b",suma_tarjeta)
#3)c. El CVC se calcula en combinacion de tres variables (UD,SS Y T)
ud=aux2_dni %10
ss=suma_dni//16
t=suma_tarjeta//16
cvc=((ud*10+ss)*10+t)
print("El CVC es:",cvc)
#4) Determinar de acuerdo a los dos primeros digitos de la tarjeta cual es la entidad emisora
j=0
divisor=1000000000000000
primeros_digitos=0
while j<2:
    cociente=aux2_tarjeta // divisor
    r=dni%10
    divisor=divisor//10
    j=j+1
if cociente==34 or cociente==37:
    print("American Express")
if cociente==51 or cociente==55:
    print("Mastercard")
if cociente==43:
    print("VISA")