def diagnostico():
    sintomas = input("Ingrese síntomas separados por comas: ").lower().split(",")
    
    # Eliminar espacios adicionales
    sintomas = [sintoma.strip() for sintoma in sintomas]
    
    # Reglas para diagnósticos
    if "fiebre" in sintomas and "tos" in sintomas:
        print("Posible diagnóstico: Gripe")
    elif "dolor de cabeza" in sintomas and "náuseas" in sintomas:
        print("Posible diagnóstico: Migraña")
    elif "dolor de garganta" in sintomas and "dificultad para tragar" in sintomas:
        print("Posible diagnóstico: Amigdalitis")
    elif "fiebre" in sintomas and "dolor de garganta" in sintomas:
        print("Posible diagnóstico: Faringitis")
    else:
        print("No se encontró un diagnóstico preciso.")

if __name__ == "__main__":
    diagnostico()
