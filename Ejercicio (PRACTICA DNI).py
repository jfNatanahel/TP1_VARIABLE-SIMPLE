"""
Ingersar un numero de dni y sexo y obtener el cuit.
a)Validar y mostrar el numero. Es correcto (longitud=8)
b)Si la validacion es correcta, generar y mostrar el cuit.
____FORMULA
a) si el dni es par, sumar al ultimo digito el valor "2".
b) si el dni es impar, sumar al ultimo digito el valor "1".
c) si en cualquier caso el resultado es >=10, sumar sus digitos.
"""

#<>
c_numeros=0
m=0
f=0
s=0
dni=int(input("Ingresar el numero de dni: "))
#sexo=input("Ingresar el sexo: ")
aux1=dni
aux=dni
while dni >0:
    r=dni % 10
    dni=dni//10
    c_numeros=c_numeros+1
if c_numeros>8:
    print("DNI ES INCORRECTO")
else:
    p=dni %2
    if p==0:
        aux=aux+2
    else:
        aux=aux+1
        if aux>=10:
            while aux<0:
                r=aux %10
                s=s+r
                aux=aux//10

    print("Su dni y cuit es:",aux1,"-",aux)  

#if sexo==f:
#    f=27
#    print("Su dni y cuit es:",f,"-",aux1,"-",aux)
#if sexo==m:
#    m=20
#    print("Su dni y cuit es:",m,"-",aux1,"-",aux)


            

