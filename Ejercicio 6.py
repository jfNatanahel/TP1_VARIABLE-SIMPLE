"""
A una fiesta asistieron personas de diferentes edades y sexos. Construir un
algoritmos dadas las edades y sexos de las personas. Calcular :
- Cantidad de personas que asistieron a la fiesta
- Cantidad de hombres y mujeres
- Promedio de edades por sexo
- La edad de la persona más joven que asistió
Ingresar datos hasta una edad sea cero.
"""
band = 0
i = 0
contador_hombres = 0
suma_edades_hombres = 0
contador_mujeres = 0
suma_edades_mujeres = 0
joven = None

while band == 0:
    edades = int(input("Ingresar edades (ingrese 0 para terminar): "))
    
    if edades == 0:
        band = 1
    else:
        if joven is None or edades < joven:
            joven = edades
        
        sexo = int(input("Ingresar sexo (0 = hombre, 1 = mujer): "))
        
        i = i + 1
        
        if sexo == 0:
            contador_hombres += 1
            suma_edades_hombres += edades
        if sexo == 1:
            contador_mujeres += 1
            suma_edades_mujeres += edades

if contador_hombres == 0:
    p_hombres = 0
else:
    p_hombres = suma_edades_hombres // contador_hombres

if contador_mujeres == 0:
    p_mujeres = 0
else:
    p_mujeres = suma_edades_mujeres // contador_mujeres

print("Cantidad de personas que asistieron a la fiesta:", i)
print("Cantidad de hombres que asistieron:", contador_hombres)
print("Cantidad de mujeres que asistieron:", contador_mujeres)
print("Promedio de edades de hombres:", p_hombres)
print("Promedio de edades de mujeres:", p_mujeres)
print("La edad de la persona más joven que asistió:", joven)