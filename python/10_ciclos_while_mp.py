solicitudes_pendientes = 2000
while solicitudes_pendientes < 10000:
    print("La Embajada esta revisando solicitudes")
    solicitudes_pendientes += 2000
print("La Embajada alcanzo su objetivo de revision")

while solicitudes_pendientes > 0:
    print("Quedan", solicitudes_pendientes, "solicitudes por revisar")
    solicitudes_pendientes -= 500
print("Todas las solicitudes han sido revisadas")

print("--- Continue y Break ---")
dia = 0
while dia < 0:
    dia += 1
    if dia == 4:
        print("Dia 4: Se revisan los documentos consulares")
        continue
    print("Dia", dia, ": Se atiende a los solicitantes")
    if dia == 8:
        print("Fin de la jornada de atencion consular")
        break
