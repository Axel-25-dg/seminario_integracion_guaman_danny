print("FUNCIONES")
print("Embajada de Estados Unidos en Ecuador")

def revisar_documentos():
    print("El oficial consular revisa los documentos")
    print("Documentacion verificada")

revisar_documentos()
revisar_documentos()
revisar_documentos()
revisar_documentos()
revisar_documentos()

def atender_solicitante(solicitante):
    print(solicitante, "realiza un tramite consular")

atender_solicitante("Carlos")
atender_solicitante("Maria")
atender_solicitante("Juan")
atender_solicitante("Danny Guaman")

def calcular_costo(costo_tramite, cantidad):
    total = costo_tramite * cantidad
    return total

resultado = calcular_costo(4, 26)
print("El costo total del tramite es :", resultado)

resultado = calcular_costo(10, 5000)
print("El costo total de las solicitudes es :", resultado)


def verificar_requisitos(requisitos, nombre):
    if requisitos >= 9000:
        print(f"Documentacion de {nombre} verificada exitosamente")
    else:
        print(f"{nombre} necesita completar sus documentos")

verificar_requisitos(10000, "Carlos")
verificar_requisitos(5000, "Maria")
verificar_requisitos(50, "Danny Guaman")


nombre_solicitante: str = "Carlos"
edad: int = 33
altura: float = 1.75
tramite_activo: bool = True

def calcular_tiempo_revision(documentos: float, dias: int) -> float:
    return documentos * dias

tiempo: float = calcular_tiempo_revision(15.5, 2)
print("Tiempo calculado de revision: ", tiempo)
