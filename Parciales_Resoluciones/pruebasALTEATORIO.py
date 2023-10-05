dni=int(input("dni:"))
i=0
divisor=1000000000000000
while i<2:
    cociente=dni // divisor
    r=dni%10
    divisor=divisor//10
    i=i+1
print("cociente es",cociente)
