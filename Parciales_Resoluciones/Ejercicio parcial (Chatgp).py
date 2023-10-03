
#amortizacion=monto solicitado / Cantidad de cuota (valor fijo)
#Capital= capital de la cuota anterior - amortizacion
#Interes=(Capital * tasa de interes)//100
#Valor de la cuota= capital + interes 
monto = int(input("Ingresar monto: "))
cantidad_cuotas = int(input("Ingresar cuota: "))

if monto < 1000:
    print("Error: El monto debe ser igual o mayor a 1000.")
elif cantidad_cuotas not in [6, 12, 24]:
    print("Error: La cantidad de cuotas debe ser 6, 12 o 24.")
else:
    aux_6monto = monto
    aux_12monto = monto
    aux_24monto = monto
    i = 1
    j = 1
    k = 1

    if cantidad_cuotas == 6:
        while i <= 6:
            amortizacion = monto / 6
            capital = aux_6monto - amortizacion
            aux_6monto = capital
            interes = (aux_6monto * 10) / 100
            valor_cuota = amortizacion + interes
            print("El valor de la cuota es:", valor_cuota)
            i = i + 1

    if cantidad_cuotas == 12:
        while j <= 12:
            amortizacion = monto / 12
            capital = aux_12monto - amortizacion
            aux_12monto = capital
            interes = (aux_12monto * 15) / 100
            valor_cuota = amortizacion + interes
            print("El valor de la cuota es:", valor_cuota)
            j = j + 1

    if cantidad_cuotas == 24:
        while k <= 24:
            amortizacion = monto / 24
            capital = aux_24monto - amortizacion
            aux_24monto = capital
            interes = (aux_24monto * 20) / 100
            valor_cuota = amortizacion + interes
            print("El valor de la cuota es:", valor_cuota)
            k = k + 1