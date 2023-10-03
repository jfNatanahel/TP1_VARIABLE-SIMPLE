dni=int(input("Ingresar Dni: "))
dni=dni%10
if dni % 2==0:
    num1=dni-1
    num2=dni-2
    if num1<=-1:
        num1=num1+10
    if num2<=-1:
        num2=num2+10
    num3=dni
    num4=dni+1
    num5=dni+2
    if num4>=10:
        num4=num4-10
    if num5>=10:
        num5=num5-10
    password=((((num1*10+num2)*10+num3)*10+num4)*10+num5)
    print("Su nueva contraseña es: ",password)
    comprobar=int(input("Elegir un numero, ¿Coincide con el ultimo digito dni?: "))
    if comprobar!=dni:
        print("Error")
    else:
        print("Ok")
if dni % 2 !=0:
    num1=dni
    num2=dni-1
    num3=dni-2
    if num1<=-1:
        num1=num1+10
    if num2<=-1:
        num2=num2+10
    num4=dni+1
    num5=dni+2
    if num4>=10:
        num4=num4-10
    if num5>=10:
        num5=num5-10
    password=((((num1*10+num2)*10+num3)*10+num4)*10+num5)
    print("Su nueva contraseña es: ",password)
    comprobar=int(input("Elegir un numero, ¿Coincide con el ultimo digito dni?: "))
    if comprobar!=dni:
        print("Error")
    else:
        print("Ok")
if dni==0:
    num1=dni-1
    num2=dni-2
    if num1<=-1:
        num1=num1+10
    if num2<=-1:
        num2=num2+10
    num3=dni+1
    num4=dni+2
    if num3>=10:
        num3=num3-10
    if num4>10:
        num4=num4-10
    num5=dni
    password=((((num1*10+num2)*10+num3)*10+num4)*10+num5)
    print("Su nueva contraseña es: ",password)
    comprobar=int(input("Elegir un numero, ¿Coincide con el ultimo digito dni?: "))
    if comprobar!=dni:
        print("Error")
    else:
        print("Ok")

    