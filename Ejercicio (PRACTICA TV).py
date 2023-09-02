bandera=0
c_karolG=0
c_BaddBunny=0
c_NatanahelCano=0
c_Rosalia=0
c_SebastianYatra=0
productor_desea_terminar=""
print("CANTANTES MAS VOTADOS")
print("1=Karol G")
print("2=Bad Buny")
print("3=Natanahel Cano")
print("4=Rosalia")
print("5=Sebastian Yatra")
while bandera==0:
    voto=int(input("Ingresar su voto: "))
    if voto==1:
        c_karolG=c_karolG+1
    if voto==2:
        c_BaddBunny=c_BaddBunny+1
    if voto==3:
        c_NatanahelCano=c_NatanahelCano+1
    if voto==4:
        c_Rosalia=c_Rosalia+1
    if voto==5:
        c_SebastianYatra=c_SebastianYatra+1
    productor_desea_terminar=int(input("USTED PRODUCTOR DESEA TERMINAR? 0=no , -1=si"))
    #print("Productor_desea_terminar? 0=n0 , -1=si")
    if productor_desea_terminar==-1:
        bandera=1
#PRIMER MAS VOTADO
primer_mas_votado=""
if c_karolG>c_BaddBunny and c_karolG>c_NatanahelCano and c_karolG>c_Rosalia and c_karolG>c_SebastianYatra:
    primer_mas_votado=primer_mas_votado+"Karol G"
if c_BaddBunny>c_karolG and c_BaddBunny>c_NatanahelCano and c_BaddBunny>c_Rosalia and c_BaddBunny>c_SebastianYatra:
    primer_mas_votado=primer_mas_votado+"Badd Bunny"
if c_NatanahelCano>c_karolG and c_NatanahelCano>c_BaddBunny and c_NatanahelCano>c_Rosalia and c_NatanahelCano>c_SebastianYatra:
    primer_mas_votados=primer_mas_votado+"Natanahel Cano"
if c_Rosalia>c_karolG and c_Rosalia>c_BaddBunny and c_Rosalia>c_NatanahelCano and c_Rosalia>c_SebastianYatra:
    primer_mas_votado=primer_mas_votado+"Karol G"
if c_SebastianYatra>c_karolG and c_SebastianYatra>c_BaddBunny and c_SebastianYatra>c_NatanahelCano and c_SebastianYatra>c_Rosalia:
    primer_mas_votado=primer_mas_votado+"Sebastian Yatra"
#SEGUNDO MAS VOTADO
segundo_mas_votado=""
if c_karolG < c_BaddBunny and c_karolG < c_NatanahelCano and c_karolG < c_Rosalia and c_karolG < c_SebastianYatra:
    segundo_mas_votado = "Karol G"
if c_BaddBunny < c_karolG and c_BaddBunny < c_NatanahelCano and c_BaddBunny < c_Rosalia and c_BaddBunny < c_SebastianYatra:
    segundo_mas_votado = "Bad Bunny"
if c_NatanahelCano < c_karolG and c_NatanahelCano < c_BaddBunny and c_NatanahelCano < c_Rosalia and c_NatanahelCano < c_SebastianYatra:
    segundo_mas_votado = "Natanahel Cano"
if c_Rosalia < c_karolG and c_Rosalia < c_BaddBunny and c_Rosalia < c_NatanahelCano and c_Rosalia < c_SebastianYatra:
    segundo_mas_votado = "Rosalia"
if c_SebastianYatra < c_karolG and c_SebastianYatra < c_BaddBunny and c_SebastianYatra < c_NatanahelCano and c_SebastianYatra < c_Rosalia:
    segundo_mas_votado = "Sebastian Yatra"

print("Los dos cantantes más votados son:", primer_mas_votado, "y", segundo_mas_votado)
print("Los mas votados son: ",primer_mas_votado,segundo_mas_votado)
print("Votos de Karol G;",c_karolG,"Votos de BaddBunny:",c_BaddBunny,"Votos de Natanahel Cano:",c_NatanahelCano,"Votos de rosalia",c_Rosalia,"Votos Sebastian YatrA:",c_SebastianYatra)
#<>
"""
# Encontrar los dos más votados
primer_mas_votado = ""
segundo_mas_votado = ""
votos_maximos_1 = -1
votos_maximos_2 = -1

if c_karolG >= votos_maximos_1:
    votos_maximos_2 = votos_maximos_1
    votos_maximos_1 = c_karolG
    primer_mas_votado = "Karol G"
elif c_karolG > votos_maximos_2:
    votos_maximos_2 = c_karolG
    primer_mas_votado = "Karol G"

if c_BaddBunny >= votos_maximos_1:
    votos_maximos_2 = votos_maximos_1
    votos_maximos_1 = c_BaddBunny
    primer_mas_votado = "Bad Bunny"
elif c_BaddBunny > votos_maximos_2:
    votos_maximos_2 = c_BaddBunny
    primer_mas_votado = "Bad Bunny"

if c_NatanahelCano >= votos_maximos_1:
    votos_maximos_2 = votos_maximos_1
    votos_maximos_1 = c_NatanahelCano
    primer_mas_votado = "Natanahel Cano"
elif c_NatanahelCano > votos_maximos_2:
    votos_maximos_2 = c_NatanahelCano
    primer_mas_votado = "Natanahel Cano"

if c_Rosalia >= votos_maximos_1:
    votos_maximos_2 = votos_maximos_1
    votos_maximos_1 = c_Rosalia
    primer_mas_votado = "Rosalia"
elif c_Rosalia > votos_maximos_2:
    votos_maximos_2 = c_Rosalia
    primer_mas_votado = "Rosalia"

if c_SebastianYatra >= votos_maximos_1:
    votos_maximos_2 = votos_maximos_1
    votos_maximos_1 = c_SebastianYatra
    primer_mas_votado = "Sebastian Yatra"
elif c_SebastianYatra > votos_maximos_2:
    votos_maximos_2 = c_SebastianYatra
    primer_mas_votado = "Sebastian Yatra"

# Encuentra el segundo más votado
if c_karolG == votos_maximos_2:
    segundo_mas_votado = "Karol G"
elif c_BaddBunny == votos_maximos_2:
    segundo_mas_votado = "Bad Bunny"
elif c_NatanahelCano == votos_maximos_2:
    segundo_mas_votado = "Natanahel Cano"
elif c_Rosalia == votos_maximos_2:
    segundo_mas_votado = "Rosalia"
elif c_SebastianYatra == votos_maximos_2:
    segundo_mas_votado = "Sebastian Yatra"

print("Los dos cantantes más votados son:", primer_mas_votado, "y", segundo_mas_votado)
"""