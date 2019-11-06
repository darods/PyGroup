class Personaje:
    Vida = 0
    Sprites = []
    Pos_x = 40
    Pos_y = 0
    Velocidad = 0

    def __init__(self, vida, sprites, posx, posy, velocidad):
        self.Vida = vida
        self.Sprites = sprites
        self.Pos_x = posx
        self.Pos_y = posy
        self.Velocidad = velocidad

    def quitarVida(self, puntos):
        self.vida = self.vida - puntos

    def morir(self):
        pass

    def disparar(self):
        pass

    def chocar(self):
        pass

    def mover_izq(self):
        self.Pos_x -= self.Velocidad

    def mover_der(self):
        self.Pos_x += self.Velocidad

    def dibujar(self, ventana):
        pass
