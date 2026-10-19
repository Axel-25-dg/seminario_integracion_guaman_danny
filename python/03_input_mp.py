print("Incluir datos con Input")
nombre=input("¿Cual es el nombre del visitante?")
print("!Hola", nombre, "!")
print("Bienvenido a la Embajada de Estados Unidos en Ecuador")
print("Hasta luego " +nombre)

cantidad = int(input("¿Cuantos documentos lleva?"))
total = cantidad + 2
print ("Documentos en total: ", total)

print(" Conversiones")
print("====Atencion al visitante====")
nombre_cliente = input("Nombre del visitante: ")
precio = float(input("Costo de ejemplo por servicio: "))
cantidad = int(input("Cantidad de servicios: "))
total = precio * cantidad
print("Total de ejemplo:", total)
print("Total de ejemplo (round):", round(total, 2))
print(f"Total de ejemplo (f): {total:.2f}")