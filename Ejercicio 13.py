"""
Se necesita diseñar un programa para realizar una encuesta entre los alumnos integrantes de la facultad.
La encuesta debe arrojar como resultado el total de alumnos, la cantidad de la ciudad de Salta, del
Interior y de otras provincias, las edades comprendidas entre >25, 25-21,18-21<18. En el caso de personas
mayores a 21 se le debera preguntar y contar cuanto de ellos tienen trabajo.
Nota: Cuando el alumno sea vacia debe salir del programa y mostrar los resultados.
"""
c_alumnos=0
c_salta=0
c_interior=0
t_t=0
c_otro=0
e_cu=0
e_m25=0
#band=0
while True:
    alumnos = input("Ingresar alumno (dejar vacío para salir): ")
    if alumnos == "":
        break
    ciudad=int(input("Si pone 1=salta - 2=interior - 3= otras provincias"))
    edad=int(input("Ingresar su edad: "))
    if edad >= 21 and edad <= 25:
        e_cu=e_cu+1
        if edad>21:
            tiene_trabajo=int(input("Tiene trabajo? 1=si - 0=no"))
            if tiene_trabajo ==1:
                t_t=t_t+1
    c_alumnos=c_alumnos+1
    if ciudad==1:
        c_salta=c_salta+1
    if ciudad==2:
        c_interior=c_interior+1
    if ciudad==3:
        c_otro=c_otro+1
    if edad>25:
        e_m25=e_m25+1
    
print("Total de alumnos: ", c_alumnos)
print("Cantidad de alumnos de Salta: ", c_salta)
print("Cantidad de alumnos del Interior: ", c_interior)
print("Cantidad de alumnos de otras provincias: ", c_otro)
print("Cantidad de alumnos con edades entre 21 y 25: ", e_cu)
print("Cantidad de alumnos mayores a 25: ", e_m25)
print("Cantidad de alumnos mayores a 21 con trabajo: ", t_t)

#Codigo mejorado CHATGTP
