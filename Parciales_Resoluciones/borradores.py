bandera = 0
monto = int(input("Ingresar el monto: "))
cuota = int(input("Ingresar las cuotas (6, 12 o 24): "))
i = 1
tasa6 = 0.1
tasa12 = 0.15
tasa24 = 0.2

if monto < 1000:
    print("Error: El monto debe ser al menos 1000.")
    bandera = 1
elif cuota not in [6, 12, 24]:
    print("Error: Cuota no identificada. Debe ser 6, 12 o 24.")
    bandera = 1

while bandera == 0 and i <= cuota:
    if cuota == 6:
        tasa = tasa6
    elif cuota == 12:
        tasa = tasa12
    elif cuota == 24:
        tasa = tasa24

    amortizacion = monto / cuota
    interes = monto * tasa
    valor_cuota = amortizacion + interes
    monto -= amortizacion
    i += 1

    print(f"(Tasa {tasa * 100}%)\nCuota {i - 1}:")
    print(f"Amortización: {amortizacion}")
    print(f"Interés: {interes}")
    print(f"Valor de la cuota: {valor_cuota}")