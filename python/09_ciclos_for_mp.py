for solicitud in range(1, 6):
    print("Se revisa la solicitud consular", solicitud)

for numero in range(1, 11):
    print("Tramite", 5, "*", numero, "=", 5 * numero)

for numero in range(1, 11, 3):
    print("Tramite", 5, "*", numero, "=", 5 * numero)

solicitudes = [
    {'id': 1, 'Nombre': 'Carlos Perez', 'tramite': 'Visa B1/B2', 'estado': 'En Revision'},
    {'id': 2, 'Nombre': 'Maria Lopez', 'tramite': 'Pasaporte Americano', 'estado': 'Aprobado'},
    {'id': 3, 'Nombre': 'Juan Andrade', 'tramite': 'Servicio Notarial', 'estado': 'Pendiente'}
]

print("====== LISTA DE SOLICITUDES CONSULARES =====")
for solicitud in solicitudes:
    print(f"ID: {solicitud['id']} - Nombre: {solicitud['Nombre']} ({solicitud['tramite']})")

nombres = ["Carlos", "Maria", "Juan"]
for nombre in nombres:
    print("Solicitante actual: ", nombre)

tramites = {
    "Visa B1/B2": 9500,
    "Pasaporte Americano": 6000,
    "Servicio Notarial": 6000,
    "Visa de Estudiante": 4500
}

for nombre, prioridad in tramites.items():
    if prioridad >= 9000:
        print(nombre, "Puede pasar a revision prioritaria")
    else:
        print(nombre, "Debe esperar su turno")


print("====== CICLOS ANIDADOS ======")

solicitantes = ["Carlos", "Maria", "Juan", "Ana", "Pedro", "Lucia"]
for solicitante in solicitantes:
    print("Turno de: ", solicitante)
    for ventanilla in range(1, 4):
        print("Ventanilla: ", ventanilla)


print("======== BREAK Y CONTINUE =========")
for solicitante in solicitantes:
    if solicitante == "Lucia":
        break
    if solicitante == "Maria":
        continue
    print("Solicitante: ", solicitante)
