class Guerrero:
    nombre: str
    _poder: int
    
    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self._poder = poder

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Poder: {self._poder}")

goku = Guerrero("Goku", 9000)
vegeta = Guerrero("Vegeta", 6000)
piccolo = Guerrero("Piccolo", 1000)
danny = Guerrero("Danny", 5000)

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
danny.mostrar_info()

print(goku.nombre)
print(goku._poder)
print(vegeta.nombre)
print(vegeta._poder)