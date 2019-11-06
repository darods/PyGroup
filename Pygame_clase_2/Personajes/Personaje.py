class Personaje:
    vida = 0
    sprites = []
    pos_x = 0
    pos_y = 0
    control = []

    def __init__(self, vida, sprites, control, posx, posy):
        self.vida = vida
        self.sprites = sprites
        self.control = control
        self.pos_x = posx
        self.pos_y = posy

    def quitarVida(self, puntos):
        self.vida = self.vida - puntos

    def morir(self):
        pass

    def disparar(self):
        pass

    def chocar(self):
        pass

    def getTeclasMovimiento(self, indice):
        return self.control[indice]
