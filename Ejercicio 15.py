x=input("Ingresar un numero decimal: ")
c_digitoseneteros=0
c_digitosdecimales=0
bandera=0
for punto in(x):
    if punto==".":
        bandera=1
    else:
        if bandera==0:
            c_digitoseneteros=c_digitoseneteros+1
        else:
            c_digitosdecimales=c_digitosdecimales+1
print(c_digitosdecimales)
print(c_digitoseneteros)