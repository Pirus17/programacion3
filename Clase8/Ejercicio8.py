# loteria.py

import random

def crearDiccionario():
    loteria = {}
    while True:
        try:
            numero = int(input("Ingrese el número de boleto (o -1 para finalizar): "))
            if numero == -1:
                break
            nombre = input("Ingrese el nombre de la persona: ")
            if numero in loteria:
                print("Este número de boleto ya ha sido comprado. Intente con otro número.")
            else:
                loteria[numero] = nombre
        except ValueError:
            print("Error: Debes introducir un número válido.")
    return loteria

def seleccionar_ganadores(loteria):
    premios = [
        "Un viaje a Turquía con todo pago",
        "Un auto",
        "Una motocicleta",
        "Una notebook",
        "Una bicicleta"
    ]
    
    if len(loteria) < 5:
        print("No hay suficientes participantes para entregar todos los premios.")
        return None

    numeros_ganadores = random.sample(list(loteria.keys()), 5)
    ganadores = {numeros_ganadores[i]: premios[i] for i in range(5)}
    
    return ganadores

def principal():
    print("Bienvenido al sistema de lotería.")
    loteria = crearDiccionario()
    if len(loteria) < 5:
        print("No hay suficientes participantes para realizar la lotería.")
        return
    
    ganadores = seleccionar_ganadores(loteria)
    if ganadores:
        print("\nGanadores de la lotería:")
        for numero, premio in ganadores.items():
            print(f"Número de boleto: {numero}, Ganador: {loteria[numero]}, Premio: {premio}")

principal()
