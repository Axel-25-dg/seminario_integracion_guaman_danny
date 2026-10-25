print("CONDICIONALES IF")
print("Condicional Simple")
documentos_completos = 10
if documentos_completos >= 5:
    print("El visitante puede continuar con su tramite en la Embajada")
    
print("Programa Finalizo")


print("Condicional If - Else")
print("Condicional dos caminos")
pago_arancel = float(input("Cantidad de pago de arancel disponible: "))
costo_visa = float(input("Costo del tramite de visa: "))
if (pago_arancel >= costo_visa):
    print("Pago autorizado para tramite consular")
else:
    print("Fondos insuficientes para el arancel")
    print("Acercarse a ventanilla de recaudacion de la Embajada")
    

    
print("Condicional If - Elif - Else")
print("Condicional Anidadas")
requisitos = float(input("Porcentaje de requisitos verificados del solicitante: "))

if (requisitos >= 75):
    print("Optimo - Documentacion completa")
elif (requisitos >= 50):
    print("Suficiente - Revision preliminar aceptada")
elif (requisitos >= 20):
    print("Bajo - Faltan documentos de respaldo")
else:
    print("Critico - Documentacion incompleta")
    print("Consulte en ventanilla de informacion consular")
    

solicitante = input("Nombre del solicitante: ")
cita_confirmada = input("¿Cita confirmada en el sistema? (si/no): ")
requisitos_verificados = float(input("Porcentaje de documentos presentados: "))

if (cita_confirmada == "si"):
    print("Cita consular verificada")
    if requisitos_verificados >= 50:
        print("Documentacion verificada")
        print("Ingreso a la Embajada autorizado")
    else:
        print("Debe completar los documentos requeridos")
else:
    print("No puede ingresar a la Embajada")
    print("Debe agendar una cita previa en el portal consular")