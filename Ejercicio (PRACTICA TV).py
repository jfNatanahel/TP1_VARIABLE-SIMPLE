bandera=0

productor_desea_terminar=""
while bandera==0:
    c_karolG=0
    c_BaddBunny=0
    c_NatanahelCano=0
    c_Rosalia=0
    c_SebastianYatra=0
    print("CANTANTES MAS VOTADOS")
    print("1=Karol G")
    print("2=Bad Buny")
    print("3=Natanahel Cano")
    print("4=Rosalia")
    print("5=Sebastian Yatra")
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
mas_votados=""
if c_karolG>c_BaddBunny and c_karolG>c_NatanahelCano and c_karolG>c_Rosalia and c_karolG>c_SebastianYatra:
    mas_votados=mas_votados+"Karol G"
if c_BaddBunny>c_karolG and c_BaddBunny>c_NatanahelCano and c_BaddBunny>c_Rosalia and c_BaddBunny>c_SebastianYatra:
    mas_votados=mas_votados+"Badd Bunny"
if c_NatanahelCano>c_karolG and c_NatanahelCano>c_BaddBunny and c_NatanahelCano>c_Rosalia and c_NatanahelCano>c_SebastianYatra:
    mas_votados=mas_votados+"Natanahel Cano"
if c_Rosalia>c_karolG and c_Rosalia>c_BaddBunny and c_Rosalia>c_NatanahelCano and c_Rosalia>c_SebastianYatra:
    mas_votados=mas_votados+"Karol G"
if c_SebastianYatra>c_karolG and c_SebastianYatra>c_BaddBunny and c_SebastianYatra>c_NatanahelCano and c_SebastianYatra>c_Rosalia:
    mas_votados=mas_votados+"Sebastian Yatra"
print("Los mas votados son: ",mas_votados)
#<>

