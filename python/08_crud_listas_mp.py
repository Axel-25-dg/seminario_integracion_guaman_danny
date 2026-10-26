print('CRUD DE LISTAS EN PYTHON')

solicitudes = [
    {'id': 1, 'Nombre': 'Carlos Perez', 'tramite': 'Visa B1/B2', 'estado': 'Aprobado'},
    {'id': 2, 'Nombre': 'Maria Lopez', 'tramite': 'Pasaporte Americano', 'estado': 'En Revision'},
    {'id': 3, 'Nombre': 'Juan Andrade', 'tramite': 'Servicio Notarial', 'estado': 'Pendiente'}
]

id_publico = 4

def create():
    global id_publico
    print('\n--- Registrar Solicitud Consular ---')
    nombre = input('Nombre del solicitante: ')
    tramite = input('Tipo de tramite (ej. Visa B1/B2, Pasaporte, Notaria): ')
    estado = input('Estado (Aprobado, En Revision, Pendiente): ')
    
    nueva_solicitud = {
        'id': id_publico,
        'Nombre': nombre,
        'tramite': tramite,
        'estado': estado
    }
    solicitudes.append(nueva_solicitud)
    id_publico += 1
    print("Solicitud consular agregada exitosamente.")

def read():
    print('\n--- Lista de Solicitudes Consulares ---')
    for solicitud in solicitudes:
        print(f"ID: {solicitud['id']} | Nombre: {solicitud['Nombre']} | Tramite: {solicitud['tramite']} | Estado: {solicitud['estado']}")

def update():
    print('\n--- Actualizar Solicitud Consular ---')
    id_update = int(input('ID a modificar: '))
    encontrado = False
    for solicitud in solicitudes:
        if solicitud['id'] == id_update:
            solicitud['Nombre'] = input('Nuevo nombre del solicitante: ')
            solicitud['tramite'] = input('Nuevo tramite: ')
            solicitud['estado'] = input('Nuevo estado: ')
            print('Solicitud consular actualizada exitosamente.')
            encontrado = True
            break
    if not encontrado:
        print('No se encontro una solicitud consular con ese ID.')

def delete():
    print('\n--- Eliminar Solicitud Consular ---')
    id_delete = int(input('ID a borrar: '))
    encontrado = False
    for solicitud in solicitudes:
        if solicitud['id'] == id_delete:
            solicitudes.remove(solicitud)
            print('Solicitud consular eliminada exitosamente.')
            encontrado = True
            break
    if not encontrado:
        print('No se encontro una solicitud consular con ese ID.')

def menu():
    while True:
        print('\n--- Menú Embajada de Estados Unidos en Ecuador ---')
        print('1. Crear')
        print('2. Leer')
        print('3. Actualizar')
        print('4. Eliminar')
        print('5. Salir')
        
        opcion = input('Seleccione del 1 al 5: ')
        
        if opcion == '1':
            create()
        elif opcion == '2':
            read()
        elif opcion == '3':
            update()
        elif opcion == '4':
            delete()
        elif opcion == '5':
            print('Gracias por usar el programa.')
            break
        else:
            print('Opcion invalida. Intente de nuevo.')

if __name__ == '__main__':
    menu()
