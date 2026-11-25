class SolicitudConsular:
    nombre: str
    _estado: int

    def __init__(self, nombre: str, estado: int):
        self.nombre = nombre
        self._estado = estado

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Estado: {self._estado}")

carlos = SolicitudConsular("Carlos", 9000)
maria = SolicitudConsular("Maria", 6000)
juan = SolicitudConsular("Juan", 1000)
danny = SolicitudConsular("Danny", 5000)

carlos.mostrar_info()
maria.mostrar_info()
juan.mostrar_info()
danny.mostrar_info()

print(carlos.nombre)
print(carlos._estado)
print(maria.nombre)
print(maria._estado)
