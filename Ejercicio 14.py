x=int(input("Ingresar un numero: "))
c=0
while x!=0:
    if x<0:
        x=x*-1
    #c=0
    x=x//10
    c=c+1
print("Tiene:",c,"Digitos")