class SolicitudConsular:
    def __init__(self, nombre: str, tramite: str):
        self.nombre = nombre
        self.tramite = tramite

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Tramite:", self.tramite)

    def mostrar_estado(self):
        print("El estado de la solicitud es:", "Pendiente")


class SolicitudAprobada(SolicitudConsular):
    def __init__(self, nombre: str, tramite: str):
        super().__init__(nombre, tramite)

    def mostrar_info(self):
        print("Solicitud aprobada")
        print("Nombre:", self.nombre)
        print("Tramite:", self.tramite)

    def mostrar_estado(self):
        print("El estado de la solicitud es:", "Aprobada")


carlos = SolicitudAprobada("Carlos Perez", "Visa B1/B2")
maria = SolicitudConsular("Maria Lopez", "Pasaporte Americano")

carlos.mostrar_info()
carlos.mostrar_estado()
maria.mostrar_info()
maria.mostrar_estado()
