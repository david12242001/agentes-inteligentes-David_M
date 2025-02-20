import time
import random

def simular_semaforo_inteligente():
    estados_semaforo = ["Verde", "Amarillo", "Rojo"]
    while True:  # Ciclo infinito
        vehiculos = random.randint(0, 20)  # Detección de vehículos

        if vehiculos > 10:
            tiempo_verde = 14
        elif vehiculos > 5:
            tiempo_verde = 7
        else:
            tiempo_verde = 4

        print(f"🔵 Vehículos detectados: {vehiculos}")
        print(f"🟢 Semáforo: {estados_semaforo[0]} ({tiempo_verde} segundos)")
        time.sleep(tiempo_verde)

        print(f"🟡 Semáforo: {estados_semaforo[1]} (3 segundos)")
        time.sleep(3)

        print(f"🔴 Semáforo: {estados_semaforo[2]} (5 segundos)")
        time.sleep(5)

        print("\n" + "-"*30 + "\n")

        if random.random() < 0.1:
            print("🛑 Pausa temporal por mantenimiento...")
            time.sleep(random.randint(5, 10))

# Ejecutar el semáforo inteligente
if __name__ == "__main__":
    try:
        simular_semaforo_inteligente()
    except KeyboardInterrupt:
        print("\n🚦 Simulación detenida por el usuario.")
