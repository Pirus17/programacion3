class Personaje:
    def __init__(self, nombre, puntosVida, puntosAtaque, puntosDefensa):
        self.nombre = nombre
        self.puntosVida = puntosVida
        self.puntosAtaque = puntosAtaque
        self.puntosDefensa = puntosDefensa

    def atacar(self, enemigo):
        dano = self.puntosAtaque - enemigo.puntosDefensa
        enemigo.puntosVida -= dano
        return f"{self.nombre} ataca a {enemigo.nombre} y causa {dano} puntos de daño."

    def verEstado(self):
        return f"{self.nombre}: Vida={self.puntosVida}, Ataque={self.puntosAtaque}, Defensa={self.puntosDefensa}"

class Guerrero(Personaje):
    def __init__(self, nombre, puntosVida, puntosAtaque, puntosDefensa):
        super().__init__(nombre, puntosVida, puntosAtaque, puntosDefensa)
        self.fuerzaExtra = 5

    def ataqueEspecial(self, enemigo):
        dano = (self.puntosAtaque + self.fuerzaExtra) - enemigo.puntosDefensa
        enemigo.puntosVida -= dano
        return f"{self.nombre} usa ataque especial contra {enemigo.nombre} y causa {dano} puntos de daño."

class Mago(Personaje):
    def __init__(self, nombre, puntosVida, puntosAtaque, puntosDefensa, puntosMagia):
        super().__init__(nombre, puntosVida, puntosAtaque, puntosDefensa)
        self.puntosMagia = puntosMagia

    def tirarHechizo(self, enemigo):
        if self.puntosMagia >= 10:
            dano = self.puntosAtaque * 2 - enemigo.puntosDefensa
            enemigo.puntosVida -= dano
            self.puntosMagia -= 10
            return f"{self.nombre} lanza un hechizo a {enemigo.nombre} y causa {dano} puntos de daño."
        else:
            return f"{self.nombre} no tiene suficiente magia para lanzar un hechizo."

class Arquero(Personaje):
    def __init__(self, nombre, puntosVida, puntosAtaque, puntosDefensa, flechas):
        super().__init__(nombre, puntosVida, puntosAtaque, puntosDefensa)
        self.flechas = flechas

    def tirarFlecha(self, enemigo):
        if self.flechas > 0:
            dano = self.puntosAtaque - enemigo.puntosDefensa
            enemigo.puntosVida -= dano
            self.flechas -= 1
            return f"{self.nombre} dispara una flecha a {enemigo.nombre} y causa {dano} puntos de daño. Flechas restantes: {self.flechas}."
        else:
            return f"{self.nombre} no tiene flechas para disparar."


guerrero = Guerrero("Thor", 100, 40, 30)
mago = Mago("Dr Strange", 100, 25, 20, 40)
arquero = Arquero("Hawkeye", 100, 20, 20, 15)

print(guerrero.verEstado())
print(mago.verEstado)
print(arquero.verEstado())

print(guerrero.atacar(mago))
print(mago.tirarHechizo(guerrero))
print(arquero.tirarFlecha(guerrero))
print(guerrero.ataqueEspecial(arquero))
