print("CONDICIONALES IF")
print("Condicional Simple")
dinero=10
if dinero>=5:
    print("Homero puede comprar rosquillas")
    
print("Programa Finalizo")


print("Conddicionalk If - Else")
print("Codicional dos camninos")
credito = float(input("Cantidad de credito disponibles"))
precio_repuesto = float(input("Precio del repuesto"))
if (credito >= precio_repuesto):
    print("Compra autorizada")
else:
    print("Creditos insuficientes")
    print("Buscar solucion o Trueque")
    

    
print("Conddicionalk If - Elif - Else")
print("Codicional Anidadas")
combustible  = float(input("combustible de la nave"))

if (combustible >= 75):
    print("Optimo")
elif (combustible >= 50):
    print("Suficiente")
elif (combustible >= 20):
    print("Bajo")
else:
    print("critico")
    print("Localiza Base mas cercana")
    

piloto = input("Nombre del piloto")
motor_funciona = input("Motor funciona? (si/no)")
cobustible = input("Combustible disponible? ")

if (motor_funciona == "si"):
    print("Motor verificado")
    if combustible>= 50:
        print("Combustible verificado")
        print("Participacion autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede partcipar")
    print("El motor necesista reparacion")