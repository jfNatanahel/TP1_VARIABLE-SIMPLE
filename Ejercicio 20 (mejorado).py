monto = int(input("Ingrese el monto: "))

b_100 = monto // 100
resto = monto % 100

b_50 = resto // 50
resto = resto % 50

b_20 = resto // 20
resto = resto % 20

b_10 = resto // 10
resto = resto % 10

b_5 = resto // 5

print("B100:", b_100)
print("B50:", b_50)
print("B20:", b_20)
print("B10:", b_10)
print("B5:", b_5)