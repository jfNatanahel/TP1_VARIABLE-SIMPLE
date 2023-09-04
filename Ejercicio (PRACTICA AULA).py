#<>
"""
Ingersar un numero de dni y sexo y obtener el cuit.
a)Validar y mostrar el numero. Es correcto (longitud=8)
b)Si la validacion es correcta, generar y mostrar el cuit.
____FORMULA
a) si el dni es par, sumar al ultimo digito el valor "2".
b) si el dni es impar, sumar al ultimo digito el valor "1".
c) si en cualquier caso el resultado es >=10, sumar sus digitos.
"""
dni=int(input("Ingresar el numero de dni: "))
sexo=int(input("Ingresar el sexo 0=femenino/1=masculino: "))
longitud=0
s=0
dni_aux=dni
ultimo_digito=dni%10
while dni>0:
    r=dni %10
    dni=dni //10
    longitud= longitud+1
if longitud>8:
    print("EL DNI SUPERA LOS 8 DIGITOS")
else:
    if dni_aux % 2 ==0:
        ultimo_digito=ultimo_digito+2
    else:
        ultimo_digito=ultimo_digito+1
    if ultimo_digito>=10:
        while ultimo_digito>0:
            r1=ultimo_digito%10
            s=s+r1
            ultimo_digito=ultimo_digito//10
        ultimo_digito=s
    if sexo==0:
        f_dni_nuevo=27
        dividendo=10000000
        while dni_aux>0:
            cociente=dni_aux // dividendo
            dni_aux=dni_aux%dividendo
            dividendo=dividendo//10
            f_dni_nuevo=f_dni_nuevo*10+cociente
        print("Cuit es:",f_dni_nuevo*10+ultimo_digito)
    if sexo==1:
        m_dni_nuevo=20
        dividendo=10000000
        while dni_aux>0:
            cociente=dni_aux // dividendo
            dni_aux=dni_aux%dividendo
            dividendo=dividendo//10
            m_dni_nuevo=m_dni_nuevo*10+cociente
        print("Cuit es:",m_dni_nuevo*10+ultimo_digito)

    
