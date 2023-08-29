"""
un cajero automatico necesita entregar dinero con la menor c antidad de billetes posibles. Realizar un 
algoritmo de tal manera entregar al usuario de acuerdo al monto de la extraccion la menor cantidad de 
billetes. (Considerar billetes de $100,$50,$20,$10,$5)
Ej: Monto: $1155
B100:11
B50:1
B20:0
B10:0
B5:1
"""
max_interaciones = int(input("Ingresar máximo de iteraciones: "))
iteraciones = 0
monto = int(input("Ingresar monto: "))

b_100 = 0
b_50 = 0
b_20 = 0
b_10 = 0
b_5 = 0

while iteraciones <= max_interaciones:
    if monto >= 100:
        b_100 = monto // 100
        monto = monto - (100 * b_100)
        
        while monto > 0:
            if monto >= 50:
                b_50 = b_50 + 1
                monto = monto - 50
            elif monto >= 20:
                b_20 = b_20 + 1
                monto = monto - 20
            elif monto >= 10:
                b_10 = b_10 + 1
                monto = monto - 10
            elif monto >= 5:
                b_5 = b_5 + 1
                monto = monto - 5
            else:
                break

    iteraciones = iteraciones + 1

print("B100:", b_100)
print("B50:", b_50)
print("B20:", b_20)
print("B10:", b_10)
print("B5:", b_5)
"""

"""