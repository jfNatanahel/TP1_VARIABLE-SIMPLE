#Calcular cuantos segundos tiene una hora dada.
print("CALCULAR CUANTOS SEGUNDOS TIENE UNA HORA DADA")
horas=int(input("Ingresar hora: "))
c_horas=3600
minutos=int(input("Ingresar minutos: "))
c_minutos=60
segundos=int(input("Ingresar segundos: "))
c_segundos=0
if horas <24 and minutos <60 and segundos <90:
    c_horas=c_horas*horas
    c_minutos=c_minutos*minutos
    c_segundos=c_segundos+segundos
calculo_final=c_horas+c_minutos+c_segundos
print("La hora dada",horas,":",minutos,":",segundos,"- Tiene tantos segundos: ",calculo_final)
