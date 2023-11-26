bandera=0
op1_mr=0
op1_rg=0
viernes1=0
sabado1=0
domingo1=0
op2_mr=0
op2_rg=0
viernes2=0
sabado2=0
domingo2=0
op3_mr=0
op3_rg=0
viernes3=0
sabado3=0
domingo3=0
while bandera==0:
    dia=input("Ingresar el dia: ")
    if dia !="viernes" and dia !="sabado" and dia!="domingo":
        print("Se trabaja solo los dias vienres/sabados/domingos")
        bandera=1
    else: 
        bandera=0
    operario=input("Ingresar OP1 - OP2 - OP3: ")
    atraccion_falla=input("Ingresar Falla -> Montaña Rusa o Ruega gigante:: ")
    if operario=="op1":
        if dia=="viernes":
            viernes1+=1
        if dia=="sabado":
            sabado1+=1
        if dia=="domingo":
            domingo1+=1
        if atraccion_falla=="montaña rusa":
            op1_mr+=1
        if atraccion_falla=="rueda gigante":
            op1_rg+=1
    if operario=="op2":
        if dia=="viernes":
            viernes2+=1
        if dia=="sabado":
            sabado2+=1
        if dia=="domingo":
            domingo2+=1
        if atraccion_falla=="montaña rusa":
            op2_mr+=1
        if atraccion_falla=="rueda gigante":
            op2_rg+=1
    if operario=="op3":
        if dia=="viernes":
            viernes3+=1
        if dia=="sabado":
            sabado3+=1
        if dia=="domingo":
            domingo3+=1
        if atraccion_falla=="montaña rusa":
            op3_mr+=1
        if atraccion_falla=="rueda gigante":
            op3_rg+=1
#1
cantidad_total_avisos=(op1_rg+op1_mr)+(op2_mr+op2_rg)+(op3_mr+op3_rg)

#2
porcentaje_MontañaRusa=(op1_mr+op2_mr+op3_mr)/cantidad_total_avisos*100
porcentaje_RuedaGigante=(op1_rg+op2_rg+op3_rg)/cantidad_total_avisos*100

#3
primero=""
segundo=""
op1_fallas=op1_rg+op1_mr
op2_fallas=op2_mr+op2_rg
op3_fallas=op3_mr+op3_rg
if op1_fallas>op2_fallas and op1_fallas>op3_fallas:
    primero="OP1"
    if op2_fallas>op3_fallas:
        segundo="OP2"
    else:
        segundo="OP3"
if op2_fallas>op1_fallas and op2_fallas>op3_fallas:
    primero="OP2"
    if op1_fallas>op3_fallas:
        segundo="OP1"
    else:
        segundo="OP3"
if op3_fallas>op1_fallas and op3_fallas>op2_fallas:
    primero="OP3"
    if op1_fallas>op2_fallas:
        segundo="OP1"
    else:
        segundo="OP2"
#4
menor_fallo=""
total_sabados=sabado1+sabado2+sabado3
total_domingo=domingo1+domingo2+domingo3
total_viernes=viernes1+viernes2+viernes3
if total_sabados<total_domingo and total_sabados<total_viernes:
    menor_fallo="Sabado"
if total_domingo<total_sabados and total_domingo<total_viernes:
    menor_fallo="Domingo"
if total_viernes<total_domingo and total_viernes<total_sabados:
    menor_fallo="Viernes"
print("1.Cantidad total de avisos de fallas recibidas por CRA:",cantidad_total_avisos)
print("2.Promedio expresado en porcentaje de los avisos de fallas de cada atraccion:","/nMontaña Rusa:",porcentaje_MontañaRusa,"/nRueda Gigante",porcentaje_RuedaGigante)
print("3.El primero y segundo operador que mas avisos recibio","primero:",primero,"segundo:",segundo)
print("4. El dia que hubo menos fallos:",menor_fallo)