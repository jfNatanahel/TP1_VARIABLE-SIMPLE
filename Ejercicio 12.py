#Determinar hasta que numero natural consecutivo es necesario sumar para llegar a un valor k (apartir del numero 1)
k=int(input("Ingresar el numero a determinar hasta donde llegar: "))
i=1
s=0

while s<=k and band==0:
    s=s+i
    i=i+1
i=i-1
print("K=",k,"Es necesario sumar hasta el numero natural:",i,)
print(s)