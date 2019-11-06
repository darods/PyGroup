from .Personaje import Personaje

Sprites = ["Imagenes/Sprites/LanceWalkingL.gif"]


class Jugador1(Personaje):

    def __init__(self):
        Personaje.__init__(self, 50, Sprites, 50, 50, 10)

    def morir(self):
        self.vida = 50
