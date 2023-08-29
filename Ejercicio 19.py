"""
Un empresa que vende seguros tiene 5 vendedores (Maria, Juan , Pedro , Julieta y Rosa). Mes a mes se desea saber
los resultados de las ventas y el desempeño de los vendedores. La empresa cuenta a fin de mes con un lista con
la siguiente informacion: codigo del vendedor (1:Maria , 2:Juan, 3:Pedro, 4:Julieta, 5:Rosa) y monto de la venta
se desea obtener:
a)total de seguros vendidos
b)promedio de ventas que deberia haber vendido c/vendedor
c)Vendedor que mas vendio
d) Vendedor que menos vendio.
e) Vendedores que estan por debajo del promedio.
f) Vendores que estan por encima del promedio.
Ejemplo:
Codigo 1 - Monto=2000 , Nombre= Maria
Codigo 2 - Monto=1200 , Nombre= Juan
Codigo 3 - Monto= 3000 , Nombre= Pedro
Codigo 4 - Monto= 1500 , Nombre= Julieta
Codigo 5 - Monto=3200 , Nombre= Rosa
"""
i=1
monto1=0
monto2=0
monto3=0
monto4=0
monto5=0
vendedor_mas_vendio=0
vendedor_menos_vendio=0
#codigo1=maria
#codigo2=juan
#codigo3=pedro
#codigo4=julieta
#codigo5=rosa
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