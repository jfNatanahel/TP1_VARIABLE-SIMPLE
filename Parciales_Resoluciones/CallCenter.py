
llamadas_total=0
requerimiento_total=0
cant_fs=0
cant_fh=0
cant_fc=0
cant_c=0
cant_i=0
cant_capital=0
cant_interior=0
bandera=0
i=1
while bandera==1: 
    hora=int(input("Ingresar hora: "))
    minuto=int(input("Ingresar minuto: "))
    # Verificar si la hora está dentro del rango laboral
    if (hora == 8 and minuto >= 30) or (hora > 8 and hora < 20) or (hora == 20 and minuto == 0):
        bandera = 0  # Estamos dentro del rango laboral
    else:
        bandera = 1  # Estamos fuera del rango laboral
    llamados_capital=input("Ingresar llamados capital (I)Interior (C)capital: ")
    llamadas_total+=1
    tipo_requerimiento=input("Ingresar tipo de requerimiento FS-FH-FC: ")
    requerimiento_total+=1
    if tipo_requerimiento=="FS":
        cant_fs+=1
    if tipo_requerimiento=="FH":
        cant_fh+=1
    if tipo_requerimiento=="FC":
        cant_fc+=1
    if llamados_capital=="C":
        cant_c+=1
    if llamados_capital=="I":
        cant_i+=1
total_requerimientos=cant_fc+cant_fh+cant_fs
promedio_FS=(cant_fs/total_requerimientos)*100
promedio_FH=(cant_fh/total_requerimientos)*100
promedio_FC=(cant_fc/total_requerimientos)*100
#Ranking de llamadas por nombres de tipo de falla (mostrar de mayor a menor)
p_mayor=-1
mayor=""
medio=""
menor=""
if cant_fc>cant_fh and cant_fc>cant_fs: #FS=5 , FH=2 , FC=3
    mayor="FC"
    if cant_fh<cant_fs:
        medio="FS"
        menor="FH"
    else:
        medio="FH"
        menor="FS"
if cant_fs>cant_fc and cant_fs>cant_fh: #FS=5 , FH=2 , FC=3
    mayor="FS"
    if cant_fc<cant_fh:
        medio="FH"
        menor="FC"
    else:
        medio="FC"
        menor="FH"
if cant_fh>cant_fc and cant_fh>cant_fs: #FS=5 , FH=2 , FC=3
    mayor="FH"
    if cant_fc<cant_fs:
        medio="FC"
        menor="FS"
    else:
        medio="FS"
        menor="FC"

porcentaje_capital=(cant_c/10)*100
porcentaje_interior=(cant_i/10)*100
print("1",llamadas_total)
print("2.Cantidad de reclamos","FS",cant_fs,"-","FH",cant_fh,"-","FC",cant_fc)
print("3.Promedio expresado en porcentaje de reclamos","FS",promedio_FS,"-","FH",promedio_FH,"-","FC",promedio_FC)
print("4.Cantidad total de llamadas recibidas por capital e interior","C:",cant_c,"-","I",cant_i)
print("5.Ranking de llamads por nombre de tipo de falla(de mayor a menor)",mayor,medio,menor)
print("6.Porcentaje de llamads de C e I",porcentaje_capital,porcentaje_interior)
