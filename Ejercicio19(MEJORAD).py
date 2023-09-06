Monto1 = 0
Monto2 = 0
Monto3 = 0
Monto4 = 0
Monto5 = 0
total_seguros = 0
c = 1

while c <= 5:
    print("Vendedores: 1=Maria , 2=Juan , 3=Pedro, 4=Julieta y 5=Rosa")
    Monto = float(input("Ingresar Monto: "))
    código_vendedor = int(input("Ingresar código_vendedor: "))

    if código_vendedor == 1:
        Monto1 = Monto
    if código_vendedor == 2:
        Monto2 = Monto
    if código_vendedor == 3:
        Monto3 = Monto
    if código_vendedor == 4:
        Monto4 = Monto
    if código_vendedor == 5:
        Monto5 = Monto

    c += 1

# a) Total de seguros vendidos
total_seguros = Monto1 + Monto2 + Monto3 + Monto4 + Monto5

# b) Promedio de ventas que debería haber vendido cada vendedor.
Promedio_ventas = total_seguros / 5

# c) Vendedor que más vendió
Vendedor_mas_vendio = ""
Max_vendedor = 0

if Max_vendedor < Monto1:
    Max_vendedor = Monto1
    Vendedor_mas_vendio = "1: María"
if Max_vendedor < Monto2:
    Max_vendedor = Monto2
    Vendedor_mas_vendio = "2: Juan"
if Max_vendedor < Monto3:
    Max_vendedor = Monto3
    Vendedor_mas_vendio = "3: Pedro"
if Max_vendedor < Monto4:
    Max_vendedor = Monto4
    Vendedor_mas_vendio = "4: Julieta"
if Max_vendedor < Monto5:
    Max_vendedor = Monto5
    Vendedor_mas_vendio = "5: Rosa"

# d) Vendedor que menos vendió
Vendedor_menos_vendio = ""
Min_vendedor = 10000000

if Min_vendedor > Monto1:
    Min_vendedor = Monto1
    Vendedor_menos_vendio = "1: María"
if Min_vendedor > Monto2:
    Min_vendedor = Monto2
    Vendedor_menos_vendio = "2: Juan"
if Min_vendedor > Monto3:
    Min_vendedor = Monto3
    Vendedor_menos_vendio = "3: Pedro"
if Min_vendedor > Monto4:
    Min_vendedor = Monto4
    Vendedor_menos_vendio = "4: Julieta"
if Min_vendedor > Monto5:
    Min_vendedor = Monto5
    Vendedor_menos_vendio = "5: Rosa"

# e) Vendedores que están por debajo del promedio
Debajo_promedio = ""
Encima_promedio = ""

if Monto1 < Promedio_ventas:
    Debajo_promedio = Debajo_promedio + "1: María"
else:
    Encima_promedio = Encima_promedio + "1: María"

if Monto2 < Promedio_ventas:
    Debajo_promedio = Debajo_promedio + "2: Juan"
else:
    Encima_promedio = Encima_promedio + "2: Juan"

if Monto3 < Promedio_ventas:
    Debajo_promedio = Debajo_promedio + "3: Pedro"
else:
    Encima_promedio = Encima_promedio + "3: Pedro"

if Monto4 < Promedio_ventas:
    Debajo_promedio = Debajo_promedio + "4: Julieta"
else:
    Encima_promedio = Encima_promedio + "4: Julieta"

if Monto5 < Promedio_ventas:
    Debajo_promedio = Debajo_promedio + "5: Rosa"
else:
    Encima_promedio = Encima_promedio + "5: Rosa"

print("a) Total de seguros vendidos:", total_seguros)
print("b) Promedio de ventas que debería haber vendido cada vendedor:", Promedio_ventas)
print("c) Vendedor que más vendió:", Vendedor_mas_vendio)
print("d) Vendedor que menos vendió:", Vendedor_menos_vendio)
print("e) Vendedores que están por debajo del promedio:", Debajo_promedio)
print("f) Vendedores que están por encima del promedio:", Encima_promedio)