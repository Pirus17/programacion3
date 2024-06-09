class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def verInformacion(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Disponibilidad: {self.disponibilidad}"

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, disponibilidad, garantia):
        super().__init__(nombre, precio, disponibilidad)
        self.garantia = garantia  # en meses

    def verInformacion(self):
        informacionBase = super().verInformacion()
        return f"{informacionBase}, Garantía: {self.garantia} meses"

class Ropa(Producto):
    def __init__(self, nombre, precio, disponibilidad, talla, material):
        super().__init__(nombre, precio, disponibilidad)
        self.talla = talla
        self.material = material

    def verinformacion(self):
        informacionBase = super().verInformacion()
        return f"{informacionBase}, Talla: {self.talla}, Material: {self.material}"

class Juguete(Producto):
    def __init__(self, nombre, precio, disponibilidad, edadRecomendada):
        super().__init__(nombre, precio, disponibilidad)
        self.edadRecomendada = edadRecomendada  

    def verInformacion(self):
        informacionBase = super().verInformacion()
        return f"{informacionBase}, Edad Recomendada: {self.edadRecomendada} años"


electrodomestico = Electrodomestico("Horno Microonda", 350000, True, 8)
ropa = Ropa("Pantalon", 40000, True, "XL", "Jean")
juguete = Juguete("Avion", 2500, True, 15)

print(electrodomestico.verInformacion())
print(ropa.verInformacion())
print(juguete.verInformacion())
