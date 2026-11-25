class SolicitudConsular:
    nombre: str
    tramite: str

    def __init__(self, nombre: str, tramite: str):
        self.nombre = nombre
        self.tramite = tramite

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Tramite:", self.tramite)


class SolicitudUrgente(SolicitudConsular):
    def __init__(self, nombre: str, tramite: str, prioridad: str):
        super().__init__(nombre, tramite)
        self.prioridad = prioridad

    def mostrar_prioridad(self):
        print("Prioridad:", self.prioridad)


carlos = SolicitudUrgente("Carlos Perez", "Visa B1/B2", "Alta")
maria = SolicitudUrgente("Maria Lopez", "Pasaporte Americano", "Media")

carlos.mostrar_info()
carlos.mostrar_prioridad()
maria.mostrar_info()
maria.mostrar_prioridad()
