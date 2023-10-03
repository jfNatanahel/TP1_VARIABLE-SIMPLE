"""
Se debe realizar un algoritmo para el calculo de cuotas de una persona cuando desea pedir un préstamo y con pagos del sistema alemán. Los datos a ingresar son: el monto solicitado y la cantidad de cuotas.
El monto solicitado debe ser mayor a 1000 (si se ingresa un valor menor, mostrar error) y los posibles valores para la cantidad de cuotas son 6, 12, 24 (si se ingresa otro valor mostrar error)
La tasa de interes a cobrar depende de la cantidad de cuota seleccionada:
-	Si la cantidad de cuota es de 6, la tasa de interés es de 10%
-	Si la cantidad de cuota es de 12, la tasa de interés es de 15%
-	Si la cantidad de cuota es de 24. La tasa de interés es de 20%
"""
monto=int(input("Ingresar monto: "))
cantidad_cuotas=int(input("Ingresar cuota: "))
aux_6monto=monto
aux_12monto=monto
aux_24monto=monto
i=1
j=1
k=1
if monto<1000:
    print("Error")
if cantidad_cuotas!=6 and cantidad_cuotas!=12 and cantidad_cuotas!=24:
    print("Error")
if cantidad_cuotas==6:
    while i<=6:
        amortizacion= monto/6
        capital=aux_6monto-amortizacion
        interes=(aux_6monto*10)/100
        valor_cuota=amortizacion+interes
        aux_6monto=capital
        print("El valor de la cuota es:",valor_cuota)
        i=i+1
if cantidad_cuotas==12:
    while j<=12:
        amortizacion=monto//12
        capital=aux_12monto-amortizacion
        aux_12monto=capital
        interes=(aux_12monto*12)//100
        valor_cuota=amortizacion+interes
        print("Tasa de interes 15 %")
        print("El valor de la cuota es:",valor_cuota)
        j=j+1
if cantidad_cuotas==24:
    while k<=12:
        amortizacion=monto//24
        capital=aux_24monto-amortizacion
        aux_24monto=capital
        interes=(aux_24monto*15)//100
        valor_cuota=amortizacion+interes
        print("Tasa de interes 24%")
        print("El valor de la cuota es:",valor_cuota)
