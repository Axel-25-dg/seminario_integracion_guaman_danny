poder = 2000
while poder < 10000:
    print("Vegeta esta entrenando")
    poder += 2000
print("Vegeta alcanzo su objetivo")

while poder > 0:
    print("Majin Buu tiene", poder, "de poder")
    poder -= 500  
print("Majin Buu ha sido derrotado")

print("--- Continue y Break ---")
dia = 0
while dia < 0:
    dia += 1
    if dia == 4:
        print("Dia 4: Gohan estudia")
        continue
    print("Dia", dia, ": Entrena Goten")
    if dia == 8:
        print("Fin del sistema de entrenamiento")
        break