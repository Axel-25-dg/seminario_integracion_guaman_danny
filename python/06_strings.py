"""
Manejo de cadena Caracteres
"""
nombre1 = "Qui-Gon Jinn"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2 = "Obi-Wan Kenobi"
print(f"Jedi 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

### Funciones comunes de las variables String

print("\nFunciones comunes de texto")
droide_1 = "R2-D2"
droide_2 = "C-3PO"
longitud_droide_1 = len(droide_1)
longitud_droide_2 = len(droide_2)
print(f"Nombre del droide 1: {droide_1}")
print(f"Longitud del droide 1: {longitud_droide_1}")
print(f"Nombre del droide 2: {droide_2}")
print(f"Longitud del droide 2: {longitud_droide_2}")

print("\nConvertir a mayúsculas y minúsculas")
mensaje = "La federación invade el planeta Naboo"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("Mensaje Original: ", mensaje)
print("Mensaje en mayúsculas: ", mensaje_mayusculas)
print("Mensaje en minúsculas: ", mensaje_minusculas)

print("\nReemplazo de substrings")
mensaje = "La nave viajará a Tatooine"
nuevo_mensaje = mensaje.replace("Tatooine", "Coruscant")
print("Mensaje con reemplazo: ", nuevo_mensaje)

planetas = "Naboo, Tatooine, Kamino"
print("Planetas: ", planetas)
lista_planetas = planetas.split(", ")
print("Lista de planetas: ", lista_planetas)
print("Primer planeta: ", lista_planetas[0])

print("\nExtraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:13]  
verbo = mensaje[17:25]    
print("Adjetivo es: ", adjetivo)
print("Verbo es: ", verbo)

print("\nComprobaciones útiles")
codigo = "R2D2"
numero = "2026"          
nombre = "UniversidadUTE"  
identificador = "DROIDE1"

print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())