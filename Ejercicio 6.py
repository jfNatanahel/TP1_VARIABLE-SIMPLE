"""
A una fiesta asistieron personas de diferentes edades y sexos. Construir un
algoritmos dadas las edades y sexos de las personas. Calcular :
- Cantidad de personas que asistieron a la fiesta
- Cantidad de hombres y mujeres
- Promedio de edades por sexo
- La edad de la persona más joven que asistió
Ingresar datos hasta una edad sea cero.
"""
band=0
i=0
ch=0
sh=0
cm=0
sm=0
while band==0:
    edades=int(input("Ingresar edades: "))
    joven=edades
    if joven>edades:
        joven=edades
    sexo=int(input("Ingresar sexo: 0=hombre y 1=mujer : "))
    if edades==0:
        band=1
    i=i+1
    if sexo==0:
        ch=ch+1
        sh=sh+edades
    else:
        cm=cm+1
        sm=sm+edades
p_hombres= sh//ch
p_mujeres=sm//cm
print("La cantidad de personas asistieron",i,"- Cantidad de hombres que asistieron",ch,"- Cantidad de mujeres que asisteron",cm)
print("Promedio de hombres",p_hombres,"- Promedio de mujeres",p_mujeres)
print("La edad de la persona mas joven",joven)