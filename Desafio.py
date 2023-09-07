A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))

combinaciones = []

a = A

while a <= C:
    b = B
    while b <= C:
        c = B
        while c <= C:
            if a != b and a != c and b != c:
                combinacion = a * 100 + b * 10 + c
                combinaciones.append(combinacion)
            c += 1
        b += 1
    a += 1

print("Combinaciones posibles:")
for combinacion in combinaciones:
    print(combinacion)