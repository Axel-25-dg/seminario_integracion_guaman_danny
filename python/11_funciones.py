print ("FuNCIONES")
print("Autor: Danny Guaman")

def Kamekameha():
    print("Goku concentra su energia")
    print ("!Kamehameha!")

Kamekameha()
Kamekameha()
Kamekameha()
Kamekameha()
Kamekameha()

def atacar(guerrero):
    print (guerrero, "realiza un ataque")

atacar("GOku")
atacar("Vegeta")
atacar("Piccolo")
atacar("Danny Guaman")

def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(4, 26)
print("El poder de Danny Guaman es :", resultado)

resultado = calcular_poder(10, 5000)
print("El poder de Goku es :", resultado)


def transformar_sayajin(poder, nombre):
    if poder >= 9000:
        print(f"Transformacion de  {nombre} a super sayajin exitosa")
    else:
        print(f"{nombre} necesita aumentar su poder")

transformar_sayajin(10000, "Goku")
transformar_sayajin(5000, "Vegeta")
transformar_sayajin(50, "Danny Guaman")


nombre_personaje:str = "goku"
edad: int = 33
altura: float = 1.75
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int ) -> float:
    return entrenamiento * edad

poder: float = multiplicador_poder(15.5,2)
print("Poder calculado: ",poder)