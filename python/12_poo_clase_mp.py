class SolicitudConsular:
    nombre: str
    tramite: str

    def __init__(self, nombre: str, tramite: str):
        self.nombre = nombre
        self.tramite = tramite

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tramite: {self.tramite}")

carlos = SolicitudConsular("Carlos", "Visa B1/B2")
maria = SolicitudConsular("Maria", "Pasaporte Americano")
juan = SolicitudConsular("Juan", "Servicio Notarial")
danny = SolicitudConsular("Danny", "Visa de estudiante")

carlos.mostrar_info()
maria.mostrar_info()
juan.mostrar_info()
danny.mostrar_info()
