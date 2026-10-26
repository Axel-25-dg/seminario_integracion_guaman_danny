for flexion in range(1, 6):
    print("Goku hace la flexion", flexion)

for numero in range(1, 11):
    print("Multiplicacion", 5, "*", numero, "=", 5 * numero)

for numero in range(1, 11, 3):
    print("Multiplicacion", 5, "*", numero, "=", 5 * numero)

avengers = [
    {'id': 1, 'Nombre': 'Tony Stark', 'Heroe': 'Iron Man', 'estado': 'Activo'},
    {'id': 2, 'Nombre': 'Steve Rogers', 'Heroe': 'Captain America', 'estado': 'Activo'},
    {'id': 3, 'Nombre': 'Thor Odinson', 'Heroe': 'Thor', 'estado': 'Activo'}
]

print("====== LISTA AVENGERS =====")
for avenger in avengers:
    print(f"ID: {avenger['id']} - Nombre: {avenger['Nombre']} ({avenger['Heroe']})")

nombres = ["Pedro", "Pablo", "Juan"]
for nombre in nombres:
    print("Nombre actual: ", nombre)

guerreros = {
    "Goku": 9500,
    "Vegeta": 6000,
    "Gohan": 6000,
    "Piccolo": 4500
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(nombre, "Puede enfrentar a Freezer")
    else:
        print(nombre, "Necesita entrenar mas")


print("======CICLOS ANIDADOS======")  

guerreros = ["Goku","Vegeta","Gohan","Trunks","Piccolo", "Majinbu"]
for guerrero in guerreros:
    print("Turno de: ", guerrero)
    for ronda in range(1,4):
        print("Ronda: ", ronda)


print("======== BREACK Y CONTINUE =========")
for guerrero in guerreros:
    if guerrero == "Piccolo":
        break
    if guerrero == "Vegeta":
        continue
    print("Guerrero: ", guerrero)



    
    