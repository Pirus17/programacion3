from collections import Counter
import re

def contarPalabras(texto):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    contador = Counter(palabras)
    palabras_frecuentes = contador.most_common(10)
    return palabras_frecuentes

def principal():
    print("Por favor, ingrese un texto de al menos diez líneas. Presione Enter dos veces para finalizar la entrada:")
    lineas = []
    while True:
        linea = input()
        if linea == '':
            break
        lineas.append(linea)
    
    texto = "\n".join(lineas)
    
    if len(lineas) < 10:
        print("El texto debe contener al menos diez líneas.")
        return
    
    palabras_frecuentes = contarPalabras(texto)
    print("\nLas 10 palabras más frecuentes son:")
    for palabra, frecuencia in palabras_frecuentes:
        print(f"{palabra}: {frecuencia}")

principal()
