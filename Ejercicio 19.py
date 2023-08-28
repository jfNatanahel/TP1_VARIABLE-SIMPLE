i=1
codigo1=maria
codigo2=juan
codigo3=pedro
codigo4=julieta
codigo5=rosa
while i>=5:
    monto=int(input("Ingresar monto: "))
    codigo=int(input("Ingresar codigo: "))
    if codigo==1:
        monto1=monto
    if codigo==2:
        monto2=monto
    if codigo==3:
        monto3=monto
    if codigo==4:
        monto4=monto
    if codigo==5:
        monto5=monto
#a)Total de seguros vendidos
total_seguros_vendidos=monto1+monto2+monto3+monto4+monto5
#b)Promedio de ventas 
promedio_ventas=total_seguros_vendidos//5
#c)Vendedor mas vendio
if monto1>monto2 and monto1>monto3 and monto1>monto5 and monto1>monto4:
    vendedor_menos_vendio=monto1
if monto2>monto1 and monto2>monto3 and monto2>monto4 and monto2>monto5:
    vendedor_menos_vendio=monto2
if monto3>monto1 and monto3>monto2 and monto3>monto4 and monto3>monto5:
    vendedor_menos_vendio=monto3
if monto4>monto1 and monto4>monto2 and monto4>monto3 and monto4>monto5:
    vendedor_menos_vendio=monto4
if monto5>monto1 and monto5>monto2 and monto5>monto3 and monto5>monto4:
    vendedor_menos_vendio=monto5
#d)Vendedor menos vendio
if monto1<monto2 and monto1<monto3 and monto1<monto5 and monto1<monto4:
    vendedor_mas_vendio=monto1
if monto2<monto1 and monto2<monto3 and monto2<monto4 and monto2<monto5:
    vendedor_mas_vendio=monto2
if monto3<monto1 and monto3<monto2 and monto3<monto4 and monto3<monto5:
    vendedor_mas_vendio=monto3
if monto4<monto1 and monto4<monto2 and monto4<monto3 and monto4<monto5:
    vendedor_mas_vendio=monto4
if monto5<monto1 and monto5<monto2 and monto5<monto3 and monto5<monto4:
    vendedor_mas_vendio=monto5
# MOSTRAR RESULTADOS
print(total_seguros_vendidos)
print(promedio_ventas)
print(vendedor_menos_vendio)
print(vendedor_mas_vendio)