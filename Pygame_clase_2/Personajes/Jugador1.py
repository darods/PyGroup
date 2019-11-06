from .Personaje import Personaje
from Controles import Controles


class Jugador1(Personaje):

    def __init__(self, control):
        controles = Controles()
        Personaje.__init__(
            self, 50, None, controles.teclasMovimiento, 500, 500)
        # self.sprites = None

    def morir(self):
        self.vida = 50
