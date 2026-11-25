class Personaje:
    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Raza:", self.raza)

    def muestra_nombre(self):
        print("El nombre es:", self.nombre)

class Saiyajin(Personaje):
    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre, raza)

    def mostrar_info(self):
        print("Nombre del Super Saiyajin:", self.nombre)
        print("Raza:", self.raza)

goku = Saiyajin("Goku", 'Saiyajin')
vegeta = Saiyajin("Vegeta", 'Saiyajin')
goku.mostrar_info()
vegeta.mostrar_info()
goku.muestra_nombre()
vegeta.muestra_nombre()