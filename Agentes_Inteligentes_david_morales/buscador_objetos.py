import random
import time

def mostrar_cuadricula(cuadricula, agente_pos):
    # Mostrar la cuadrícula con el agente y el objeto
    for i in range(5):
        fila = ""
        for j in range(5):
            if (i, j) == agente_pos:
                fila += "A "  # A representa al Agente
            elif cuadricula[i][j] == 1:
                fila += "O "  # O representa el Objeto
            else:
                fila += ". "  # . representa un espacio vacío
        print(fila)
    print("\n")

def mover_agente(agente_pos, objeto_pos):
    # Mover al agente hacia el objeto (sin inteligencia avanzada)
    x, y = agente_pos
    obj_x, obj_y = objeto_pos

    if x < obj_x:
        x += 1
    elif x > obj_x:
        x -= 1
    elif y < obj_y:
        y += 1
    elif y > obj_y:
        y -= 1

    return (x, y)

def buscar_objeto():
    # Inicializar cuadrícula
    cuadricula = [[0 for _ in range(5)] for _ in range(5)]

    # Colocar el objeto en una posición aleatoria
    objeto_pos = (random.randint(0, 4), random.randint(0, 4))
    cuadricula[objeto_pos[0]][objeto_pos[1]] = 1

    # Colocar al agente en la esquina superior izquierda
    agente_pos = (0, 0)

    while agente_pos != objeto_pos:
        # Mostrar la cuadrícula
        mostrar_cuadricula(cuadricula, agente_pos)
        
        # Mover al agente
        agente_pos = mover_agente(agente_pos, objeto_pos)

        # Esperar un momento para simular el movimiento
        time.sleep(0.5)

    print("¡El agente ha encontrado el objeto!")

# Ejecutar el agente buscador
if __name__ == "__main__":
    buscar_objeto()
