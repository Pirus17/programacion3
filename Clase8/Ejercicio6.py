import datetime
import time

def Reloj():
    try:
        while True:
            tiempoActual = datetime.datetime.now()
            mostrarTiempo = tiempoActual.strftime("%H:%M:%S")
            
            print(f"Hora actual: {mostrarTiempo}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReloj detenido.")

Reloj()
    