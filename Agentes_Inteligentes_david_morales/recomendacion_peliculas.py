import random

def recomendar_pelicula():
    peliculas = {
        "acción": ["Mad Max", "John Wick", "Die Hard"],
        "comedia": ["Superbad", "Ted", "The Hangover"],
        "drama": ["Forrest Gump", "El Padrino", "La Lista de Schindler"]
    }

    recomendaciones_previas = []  # Memoria del agente

    while True:
        genero = input("Ingrese su género favorito (acción, comedia, drama): ").lower()

        if genero in peliculas:
            pelicula_recomendada = random.choice([p for p in peliculas[genero] if p not in recomendaciones_previas])
            recomendaciones_previas.append(pelicula_recomendada)
            print(f"Te recomendamos: {pelicula_recomendada}")
        else:
            print("Género no encontrado. Por favor ingrese 'acción', 'comedia' o 'drama'.")
            continue

        respuesta = input("¿Te parece bien esta película? (sí/no): ").lower()

        if respuesta == "sí":
            print("¡Genial! ¡Disfruta la película!")
            break
        else:
            print("¡Vamos a probar otra recomendación!")

if __name__ == "__main__":
    recomendar_pelicula()
