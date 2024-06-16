import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if ini <= numero <= fin:
                return numero
            else:
                print(f"Error: El número debe estar entre {ini} y {fin}.")
        except ValueError:
            print("Error: Debes introducir un número válido.")

def generador():
    numeros = leer_numero(1, 20, "¿Cuántos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    lista_numeros = [random.uniform(0, 100) for _ in range(numeros)]
    lista_redondeados = []

    for numero in lista_numeros:
        if modo == 1:
            redondeado = math.ceil(numero)
        elif modo == 2:
            redondeado = math.floor(numero)
        else:
            redondeado = round(numero)
        print(f"Número original: {numero:.2f} -> Redondeado: {redondeado}")
        lista_redondeados.append(redondeado)

    return lista_redondeados

lista_final = generador()
print(f"Lista final de números redondeados: {lista_final}")
