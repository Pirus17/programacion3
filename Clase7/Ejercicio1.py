class Vuelo:
    def __init__(self, numeroVuelo, origen, destino, duracion):
        self.numeroVuelo = numeroVuelo
        self.origen = origen
        self.destino = destino
        self.duracion = duracion

    def mostrarInformacion(self):
        return f"Vuelo {self.numeroVuelo} desde {self.origen} hasta {self.destino}, Duración: {self.duracion} horas"

class VueloNacional(Vuelo):
    def __init__(self, numeroVuelo, origen, destino, duracion, tarifaBase):
        super().__init__(numeroVuelo, origen, destino, duracion)
        self.tarifaBase = tarifaBase

    def calcularPrecio(self):
        return self.tarifaBase

    def mostrarInformacion(self):
        informacionBase = super().mostrarInformacion()
        return f"{informacionBase}, Precio: ${self.calcularPrecio()} (Vuelo Nacional)"

class VueloInternacional(Vuelo):
    def __init__(self, numeroVuelo, origen, destino, duracion, tarifaBase, tasaInternacional):
        super().__init__(numeroVuelo, origen, destino, duracion)
        self.tarifaBase = tarifaBase
        self.tasaInternacional = tasaInternacional

    def verificarRequisitosPasaporte(self, pasaporteValido):
        return pasaporteValido

    def calcularPrecio(self):
        return self.tarifaBase + self.tasaInternacional

    def mostrarInformacion(self):
        informacionBase = super().mostrarInformacion()
        return f"{informacionBase}, Precio: ${self.calcularPrecio()} (Vuelo Internacional)"


vueloNacional = VueloNacional("12345", "Santiago del Estero", "BuenosAires", 2, 38000)
vueloInternacional = VueloInternacional("678910", "Buenos Aires", "Colombia", 5, 150000, 25000)

print(vueloNacional.mostrarInformacion())
print(vueloInternacional.mostrarInformacion())
if (vueloInternacional.verificarRequisitosPasaporte(True)):
    print("Pasaporte valido")
else:
    print("Pasaporte invalido")