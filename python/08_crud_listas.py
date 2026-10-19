print('CRUD DE LISTAS EN PYTHON')

avengers = [
    {'id': 1, 'Nombre': 'Tony Stark', 'Heroe': 'Iron Man', 'estado': 'Activo'},
    {'id': 2, 'Nombre': 'Steve Rogers', 'Heroe': 'Captain America', 'estado': 'Activo'},
    {'id': 3, 'Nombre': 'Thor Odinson', 'Heroe': 'Thor', 'estado': 'Activo'}
]

id_publico = 4

def create():
    global id_publico
    print('\n--- Reclutar Avenger ---')
    nombre = input('Nombre real: ')
    heroe = input('Héroe: ')
    estado = input('Estado (Activo, Retirado, Desaparecido): ')
    
    nuevo_advenger = {
        'id': id_publico,
        'Nombre': nombre,
        'Heroe': heroe,
        'estado': estado
    }
    avengers.append(nuevo_advenger)
    id_publico += 1
    print("Avenger agregado exitosamente.")

def read():
    print('\n--- Lista de Avengers ---')
    for avenger in avengers:
        print(f"ID: {avenger['id']} | Nombre: {avenger['Nombre']} | Héroe: {avenger['Heroe']} | Estado: {avenger['estado']}")

def update():
    print('\n--- Actualizar Avenger ---')
    id_update = int(input('ID a modificar: '))
    encontrado = False
    for avenger in avengers:
        if avenger['id'] == id_update:
            avenger['Nombre'] = input('Nuevo nombre: ')
            avenger['Heroe'] = input('Nuevo héroe: ')
            avenger['estado'] = input('Nuevo estado: ')
            print('Avenger actualizado exitosamente.')
            encontrado = True
            break
    if not encontrado:
        print('No se encontró un Avenger con ese ID.')

def delete():
    print('\n--- Eliminar Avenger ---')
    id_delete = int(input('ID a borrar: '))
    encontrado = False
    for avenger in avengers:
        if avenger['id'] == id_delete:
            avengers.remove(avenger)
            print('Avenger eliminado exitosamente.')
            encontrado = True
            break
    if not encontrado:
        print('No se encontró un Avenger con ese ID.')

def menu():
    while True:
        print('\n--- Menú Avengers ---')
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
            print('Opción inválida. Intente de nuevo.')

if __name__ == '__main__':
    menu()