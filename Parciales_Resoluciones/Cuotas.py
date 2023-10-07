bandera = 0
monto = int(input("Ingresar el monto: "))

if monto < 1000:
    print("Error: El monto debe ser al menos 1000.")
    bandera = 1
else:
    cuota = int(input("Ingresar las cuotas (6, 12 o 24): "))
    
    if cuota not in [6, 12, 24]:
        bandera = 1
        print("Error: Valor de la cuota incorrecto.")
i=1
tasa6=0.1
tasa12=0.15
tasa20=0.2
while bandera == 0 and i<=cuota:
    if cuota==6:
        tasa=tasa6
    if cuota==12:
        tasa=tasa12
    if cuota==20:
        tasa=tasa20
    amortizacion=monto//cuota
    capital=monto-amortizacion
    interes=(monto*tasa)
    valor_cuota=amortizacion+interes
    monto=capital
    i=i+1
    print("Capital es:",capital)
    print("Amortizacion",amortizacion)
    print("Interes",interes)
    print(i,"Valor cuota:",valor_cuota)
    
            # Aquí puedes continuar con el cálculo de los pagos, ya que el monto y la cuota son válidos.
            # ... (resto del código para calcular los pagos)

