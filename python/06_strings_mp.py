"""
Manejo de cadena Caracteres
"""
oficial1 = "Arthur Brown"
print(f"Oficial Consular 1: {oficial1}")
print(f"Tipo de datos: {type(oficial1)}")
oficial2 = "Sarah Jenkins"
print(f"Oficial Consular 2: {oficial2}")
print(f"Tipo de datos: {type(oficial2)}")

### Funciones comunes de las variables String

print("\nFunciones comunes de texto")
solicitante_1 = "Carlos Perez"
solicitante_2 = "Maria Lopez"
longitud_solicitante_1 = len(solicitante_1)
longitud_solicitante_2 = len(solicitante_2)
print(f"Nombre del solicitante 1: {solicitante_1}")
print(f"Longitud del solicitante 1: {longitud_solicitante_1}")
print(f"Nombre del solicitante 2: {solicitante_2}")
print(f"Longitud del solicitante 2: {longitud_solicitante_2}")

print("\nConvertir a mayúsculas y minúsculas")
mensaje = "La Embajada de Estados Unidos atiende en Quito y Guayaquil"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("Mensaje Original: ", mensaje)
print("Mensaje en mayúsculas: ", mensaje_mayusculas)
print("Mensaje en minúsculas: ", mensaje_minusculas)

print("\nReemplazo de substrings")
mensaje = "La cita consular será en Guayaquil"
nuevo_mensaje = mensaje.replace("Guayaquil", "Quito")
print("Mensaje con reemplazo: ", nuevo_mensaje)

sedes = "Quito, Guayaquil, Washington"
print("Sedes consulares: ", sedes)
lista_sedes = sedes.split(", ")
print("Lista de sedes: ", lista_sedes)
print("Primera sede: ", lista_sedes[0])

print("\nExtraer subcadenas")
mensaje = "Tramite consular aprobado con exito"
tipo_tramite = mensaje[8:16]  
resultado = mensaje[17:25]    
print("Tipo de tramite es: ", tipo_tramite)
print("Resultado es: ", resultado)

print("\nComprobaciones útiles")
codigo = "B1B2"
numero = "2026"          
nombre = "EmbajadaEEUU"  
identificador = "VENTANILLA1"

print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())
