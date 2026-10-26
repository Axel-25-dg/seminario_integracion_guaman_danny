class Guerrero:
    nombre: str
    raza: str
    
    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")

goku = Guerrero("Goku", "Sayajin")
vegeta = Guerrero("Vegeta", "Sayajin")
piccolo = Guerrero("Piccolo", "Namekiano")
danny = Guerrero("Danny", "Humano")

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
danny.mostrar_info()