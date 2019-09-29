import pygame


class cajita_xd:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.ancho = 50
        self.alto = 100
        self.color = (255, 255, 255)
        self.velocidad = 5
        self.puntaje = 0

    def mover_arriba(self):
        self.pos_y -= self.velocidad

    def mover_abajo(self):
        self.pos_y += self.velocidad

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.pos_x,
                                               self.pos_y,
                                               self.ancho,
                                               self.alto))

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.ancho, self.alto)


class pelota(cajita_xd):
    def __init__(self):
        cajita_xd.__init__(self, 250, 250)
        self.alto = 10
        self.ancho = 10
        self.velocidad = [-5, -5]

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, (self.pos_x, self.pos_y), 10)

    def reiniciar(self):
        self.pos_x = 250
        self.pos_y = 250
        self.velocidad[0] *= -1
        self.velocidad[1] *= -1
