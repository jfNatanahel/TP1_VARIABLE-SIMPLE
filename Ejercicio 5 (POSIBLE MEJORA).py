N = int(input("Ingrese la cantidad de alumnos:"))

while N > 0:
    C = 1
    X = int(input("Ingrese el valor de la primer nota:"))
    P1 = X
    P2 = X
    N = N - 1
    
    while C < 5:
        X1 = int(input("Ingrese el valor de la nota:"))
        X2 = int(input("Ingrese el valor de la nota:"))
        
        if X1 > P1 and X1 > X2:
            P1 = P1
            P2 = X2
        if X1 > P1 and X1 < X2:
            P1 = P1
            P2 = X1
        if X1 < P1 and X2 < P2:
            if X2 > X1:
                P1 = X1
                P2 = P1
            else:
                P1 = X1
                P2 = X2
        if X1 < P1 and X2 > P2:
            if X2 > X1:
                P1 = X1
                P2 = P2
            else:
                P1 = X1
                P2 = X2
        
        C = C + 2
    
    print("Las peores notas son:")
    print(P1)
    print(P2)
