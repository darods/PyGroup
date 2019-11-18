import pygame as pg
from configuracion import *
vector = pg.math.Vector2  # sirve para manejar el movimiento en 2D


class Jugador(pg.sprite.Sprite):
    def __init__(self, juego):
        pg.sprite.Sprite.__init__(self)
        self.juego = juego  # Hacemos una referencia al juego
        self.image = pg.Surface((ANCHO_JUGADOR, ALTO_JUGADOR))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO / 2)
        self.pos = vector(ANCHO / 2, ALTO / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

    def jump(self):
        # salta solo si está en una plataforma
        self.rect.y += 1  # corre en 1 pixel a ver si colisiona
        colision = pg.sprite.spritecollide(
            self, self.juego.platafaformas, False)
        self.rect.y -= 1
        if colision:
            self.vel.y = -20

    def update(self):  # importante que se llame update, no valen traducciones
        self.acc = vector(0, GRAVEDAD)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -ACC_JUGADOR

        if keys[pg.K_RIGHT]:
            self.acc.x = ACC_JUGADOR

        self.acc.x += self.vel.x * FRICCCION
        self.vel += self.acc  # equación de la velocidad
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc  # equación de la posición

        # vuelve a aparecer en el otro lado de la pantalla
        if self.pos.x > ANCHO:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = ANCHO
        self.rect.midbottom = self.pos  # actualizamos su posición


class Plataforma(pg.sprite.Sprite):
    # w y h hacen referencia a ancho y alto (en ingles)
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
