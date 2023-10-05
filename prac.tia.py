#Ejemplo 2: mostrar 3 nombres de microemprendimientos uno al lado del otro.
#print("valentino", "pia", "\nNahiar")
#Ejemplo 1: crear una variable llamada negocio y otra variable llamada préstamo,asignar los siguientes datos respectivamente:
#Fabricación de muebles, 1500000.581


"""Ejemplo 2: Crear 2 variables y asignarles valores enteros. Luego crear una tercera variable que contenga el 
producto de ambos números.
Mostrar el resultado mediante el mensaje: "El producto de ambos números es: "...
c=10
i=1
while c<=i:
    carpinteria=68000
    carniceria=120000
resultado=carpinteria*carniceria
print("El producto de ambos numeros es",resultado)"""

"""Función input()
Ejemplo 1: Solicitar el nombre del cliente, su DNI y el monto de compra.
Mostrar como salida el mensaje "El cliente"...."abonó un total de ".....
nombre_del_cliente=input("como te llamas: ")
dni=int(input("cual es tu dni: "))
monto_de_compra=int(input("cuanto pagaste: "))
print("el cliente",nombre_del_cliente,"abono un total de:",monto_de_compra)"""

"""Ejemplo 2: Solicitar el ingreso del producto, su precio unitario. Calcular el precio de venta teniendo en 
cuenta un incremento por IVA del 18%
Mostrar el resultado mediante el mensaje: "El precio de" ... "con IVA aplicado es:"""
"""
producto=input("nombre el producto: ")
precio_unitario=int(input("ingrese el monto: "))
resultado=precio_unitario+(precio_unitario*0.18)
print("el precio de:",precio_unitario,"con Iva aplicado es:",resultado)"""
#DESAFIO SEMANA 1
"""
Un comercio de la zona se encuentra en mes aniversario, por lo que aplica un descuento del 0.1 
al precio de los nuevos productos ingresados en la semana.
Realizar un código que permita la entrada del nombre del producto, la cantidad de stock del mismo y 
el precio unitario. Luego realizar el descuento indicado.
Finalmente mostrar el mensaje: El precio unitario del producto______ ha sido modificado quedando en: _____ .
Nota: el precio modificado debe mostrarse sólo con 2 posiciones decimales."""
nombre_del_producto=input("mencione el producto: ")
cantidad_stock=int(input("cuantos hay: "))
precio_unitario=int(input("ingrese el monto: "))
precio_unitario=precio_unitario*0.1
print(precio_unitario)
#precio_con_descuento=precio_unitario-descuento
#print("el precio unitario del producto",precio_unitario, "ha sido modificado quedando en:", precio_con_descuento)

