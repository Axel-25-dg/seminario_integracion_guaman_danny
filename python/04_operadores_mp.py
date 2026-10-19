print("OPERADORES")
print("Operadores Aritmeticos")
print("+ Suma de documentos:", 5, "+", 3, "=", 5 + 3)
print("- Resta de documentos:", 5, "-", 3, "=", 5 - 3)
print("* Multiplicacion de formularios:", 5, "*", 3, "=", 5 * 3)
print("/ Division de turnos:", 15, "/", 3, "=", 15 / 3)
print("// Turnos completos:", 10, "//", 3, "=", 10 // 3)
print("% Turnos restantes:", 10, "%", 3, "=", 10 % 3)
print("** Potencia de ejemplo:", 2, "**", 3, "=", 2 ** 3)

print ("Tabla de cupos de atencion del 5")
print(5, "*", 1, "=", 5 * 1)
print(5, "*", 2, "=", 5 * 2)
print(5, "*", 3, "=", 5 * 3)
print(5, "*", 4, "=", 5 * 4)
print(5, "*", 5, "=", 5 * 5)
print(5, "*", 6, "=", 5 * 6)
print(5, "*", 7, "=", 5 * 7)
print(5, "*", 8, "=", 5 * 8)
print(5, "*", 9, "=", 5 * 9)
print(5, "*", 10, "=", 5 * 10)


print ("OPERADORES DE COMPARACION")
print("== Mismo numero de documentos: ", 5, "==", 5, "=", 5 == 5)
print("== Diferente numero de documentos: ", 5, "==", 4, "=", 5 == 4)
print("!= Cantidades distintas: ", 5, "!=", 5, "=", 5 != 5)
print("> Mas citas: ", 10, ">", 8, "=", 10 > 8)
print("> Mas citas: ", 10, ">", 18, "=", 10 > 18)
print("< Menos citas: ", 10, "<", 18, "=", 10 < 18)
print("< Menos citas: ", 10, "<", 8, "=", 10 < 8)
print(">= Cupos disponibles: ", 10, ">=", 18, "=", 10 >= 18)
print(">= Cupos disponibles: ", 10, ">=", 8, "=", 10 >= 8)
print("<= Documentos permitidos: ", 10, "<=", 18, "=", 10 <= 18)
print("<= Documentos permitidos: ", 10, "<=", 8, " =", 10 <= 8)

print("OPERADORES LOGICOS")
print("Operador and: (5==5) and (4>3)", (5==5) and (4>3))
print("Operador and: (5==5) and (4>8)", (5==5) and (4>8))
print("Operador or: (5==5) or (4>8)", (5==5) or (4>8))
print("Operador or: (5==6) or (4>8)", (5==6) or (4>8))
print("Operador not: not (5==6)", not (5==6))
print("Operador not: not (5==5)", not (5==5))

tiene_documentos = True
oficina_abierta = False
puede_realizar_tramite = tiene_documentos and oficina_abierta
print("¿Puede realizar el tramite?", puede_realizar_tramite)

tiene_cita = True
tiene_documentos = False
puede_ingresar = tiene_cita or tiene_documentos
print("¿Puede ingresar?", puede_ingresar)