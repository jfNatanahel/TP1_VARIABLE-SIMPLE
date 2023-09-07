bandera=0
mi=0
no=0
av=0
su=0
#p_mi=2000
#p_no=3000
#p_av=5000
#p_su=5000

while bandera==0:
    codigo_socio=int(input("Ingresar el codigo: "))

    categoria=input("Ingresar categoria: ")
    if categoria!="mi" and categoria!="no" and categoria!="av" and categoria!="su":
        bandera=1
    if categoria=="mi":
        mi+=1 #2
    if categoria=="no":
        no+=1 #2
    if categoria=="av":
        av+=1 #2
    if categoria=="su":
        su+=1
#1. Cuantos socios tiene el gym
total_socios=mi+no+av+su 

mi_recaudado=2000*mi #3
print("mi",mi_recaudado)
no_recaudado=3000*no #3
print("no",no_recaudado)
av_recaudado=5000*av #3
print("av",av_recaudado)
su_recaudado=5000*su #3
print("su",su_recaudado)

#4.La primera y segunda mas categoria que facturo.
primera_categoria=""
segunda_categoria=""

if mi_recaudado>no_recaudado and mi_recaudado>av_recaudado and mi_recaudado>su_recaudado:
    primera_categoria="mi"
    if no_recaudado>=av_recaudado and no_recaudado>=su_recaudado:
        segunda_categoria="no"
    if av_recaudado>=no_recaudado and av_recaudado>=su_recaudado:
        segunda_categoria="av"
    else:
        segunda_categoria="su"
if no_recaudado>mi_recaudado and no_recaudado>av_recaudado and no_recaudado>su_recaudado:
    primera_categoria="no"
    if mi_recaudado>av_recaudado and mi_recaudado>su_recaudado:
        segunda_categoria="mi"
    if av_recaudado>mi_recaudado and av_recaudado>su_recaudado:
        segunda_categoria="av"
    else:
        segunda_categoria="su"
if av_recaudado>mi_recaudado and av_recaudado>no_recaudado and av_recaudado>su_recaudado:
    primera_categoria="av"
    if mi_recaudado>su_recaudado and mi_recaudado>no_recaudado:
        segunda_categoria="mi"
    if no_recaudado>mi_recaudado and no_recaudado>su_recaudado:
        segunda_categoria="no"
    else:
        segunda_categoria="su"
if su_recaudado>mi_recaudado and su_recaudado>no_recaudado and su_recaudado>av_recaudado:
    primera_categoria="su"
    if mi_recaudado>no_recaudado and mi_recaudado>av_recaudado:
        segunda_categoria="mi"
    if no_recaudado>mi_recaudado and no_recaudado>av_recaudado:
        segunda_categoria="no"
    else:
        segunda_categoria="av"



#<>
#5.Categorias que estan por debajo del promedio
promedio=(no_recaudado+av_recaudado+su_recaudado+mi_recaudado)//total_socios
debajo_promedio=""
if promedio>mi_recaudado:
    debajo_promedio+="mi"
if promedio>no_recaudado:
    debajo_promedio+="no"
if promedio>av_recaudado:
    debajo_promedio+="av"
if promedio>su_recaudado:
    debajo_promedio+="su"

#<>
print("1.",total_socios)
print("2.",mi,no,av,su)
print("3.Total recaudado por categoria")
print("MI:",mi_recaudado)
print("NO:",no_recaudado)
print("AV:",av_recaudado)
print("SU:",su_recaudado)
print("4.")
print("El promedio es:",promedio)
print("Primer categoria mas facturo:",primera_categoria)
print("Segunda categoria que mas facturo:",segunda_categoria)
print("5.Categorias estan por debajo del promedio:",debajo_promedio)
